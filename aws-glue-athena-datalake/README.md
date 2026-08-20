# AWS Glue & Athena — Serverless Data Lake

## Overview

This project builds a serverless Data Lake pipeline using **AWS Glue** (ETL, crawling, cataloging) and **Amazon Athena** (SQL querying), transforming raw sales CSV data into a partitioned, query-ready Parquet dataset.

## Architecture

```
S3 (source CSVs)
        │
        │  Glue Crawler — schema discovery
        ▼
Glue Data Catalog (database: sales)
        │
        │  Glue Job — joins, schema mapping, data quality check
        ▼
S3 (Parquet, partitioned by status)
        │
        │  Glue Crawler — catalog the Data Lake output
        ▼
Glue Data Catalog (database: sales_datalake)
        │
        │  SQL — CTE + window functions
        ▼
Amazon Athena
```

## Technical Stack

- **ETL & Cataloging:** AWS Glue (Crawlers, Data Catalog, Visual ETL Job)
- **Storage:** Amazon S3 (Parquet, Snappy compression, partitioned)
- **Query Engine:** Amazon Athena
- **Language:** PySpark (Glue-generated), SQL

## Project Structure

```
aws-glue-athena-datalake/
├── sample-data/            # Source CSVs (clientes, vendas, produtos, itensvenda, vendedores)
├── glue_job/
│   ├── JobVendas.py         # PySpark ETL script
│   └── JobVendas.json       # Job definition (visual pipeline export)
├── assets/                  # Pipeline evidence screenshots
└── README.md
```

## How It Works

### 1. Ingestion & Cataloging
A Glue Crawler scans 5 source CSV tables in S3 (`clientes`, `vendas`, `itensvenda`, `produtos`, `vendedores`) and populates the Glue Data Catalog (`sales` database) with their schemas.

### 2. Transformation (Glue Job)
A visual ETL job:
- Reads all 5 tables from the Data Catalog
- Applies schema mapping (renaming conflicting keys, e.g. `idcliente` → `idcliente_vendas`)
- Joins all 5 tables into a single denormalized dataset (Vendas → ItensVendas → Clientes → Produtos → Vendedores)
- Runs a basic data quality check (`ColumnCount > 0`)
- Writes the result to S3 as **Parquet**, compressed with **Snappy**, partitioned by `status` (customer tier: Gold/Platinum/Silver)

### 3. Re-cataloging the Data Lake
A second Glue Crawler catalogs the transformed output (`sales_datalake` database), making the partitioned dataset queryable.

### 4. Querying with Athena
The final dataset is queried using standard SQL, including advanced constructs such as CTEs and window functions:

```sql
WITH ranking_clientes AS (
    SELECT distinct(cliente), status, total,
        DENSE_RANK() OVER (PARTITION BY status ORDER BY total DESC) AS dense_rank
    FROM datalake
)
SELECT cliente, status, total, dense_rank
FROM ranking_clientes
WHERE dense_rank <= 3
```
This query ranks the top 3 customers by total spend, within each status tier — demonstrating practical use of `DENSE_RANK()` and `PARTITION BY` on the partitioned Data Lake.

## Security & Cost Practices

- **IAM least privilege awareness:** the initial setup used a broad `AdministratorAccess` role (flagged early as a known simplification for this study project) — the role was deleted after project completion rather than left active
- **Resource cleanup:** both crawlers and both Glue databases were deleted after documentation was complete; only the S3 bucket was retained as historical evidence
- **Cost awareness:** Glue crawlers bill a 10-minute minimum per run regardless of actual duration — runs were planned deliberately to avoid unnecessary repeated executions

## Key Takeaways

- Building a full serverless ETL pipeline: crawl → catalog → transform → re-catalog → query
- Applying schema mapping to resolve column name conflicts across joined tables
- Understanding Glue's per-DPU-hour billing model and its practical cost implications (crawler minimums, DPU sizing)
- Writing optimized Athena queries using CTEs and window functions against partitioned Parquet data

## References

- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [Amazon Athena Documentation](https://docs.aws.amazon.com/athena/)

---

**Author:** Heuler Ferreira Silva
**Repository:** https://github.com/HeulerSilva/data-engineering-portfolio/tree/main/aws-glue-athena-datalake
