# AWS S3 → RDS PostgreSQL Ingestion Pipeline

## Overview

This project implements a simple but complete data ingestion pipeline: reading image files stored in an **Amazon S3** bucket and loading their metadata into an **Amazon RDS PostgreSQL** database, using Python (`boto3` and `psycopg2`).

While technically straightforward, this project demonstrates practical integration across two core AWS services — object storage and a managed relational database — along with secure credential handling and safe SQL practices, following the same principles applied throughout this portfolio.

## Architecture

```
Amazon S3 (image bucket)
        │
        │  boto3 — list & filter objects (.jpg, .jpeg, .png)
        ▼
Python Script (local / VS Code)
        │
        │  psycopg2 — parameterized INSERT
        ▼
Amazon RDS (PostgreSQL)
        │
        └── database: inventory
                └── table: files (idfiles, filename)
```

## Technical Stack

- **Language:** Python
- **AWS SDK:** boto3 (S3 access)
- **Database Driver:** psycopg2 (PostgreSQL connectivity)
- **Database:** Amazon RDS for PostgreSQL (not Aurora — see note below)
- **Environment Management:** python-dotenv
- **Version Control:** GitHub

## Project Structure

```
aws-s3-rds-ingestion/
├── main.ipynb          # Full pipeline: DB/table creation, S3 read, RDS insert
├── .env.example         # Required environment variables (no real values)
└── README.md
```

## How It Works

### 1. Database & Table Setup
Connects to the RDS PostgreSQL instance and creates the `inventory` database and a `files` table (`idfiles`, `filename`) to store ingested image metadata.

### 2. S3 Read & Filter
Uses `boto3.resource('s3')` to list all objects under a given prefix in the target bucket, filtering only image files (`.jpg`, `.jpeg`, `.png`, case-insensitive).

### 3. RDS Insert
For each matching image, extracts the filename and inserts a record into the `files` table, using a **parameterized query** (`%s` placeholders) — never string concatenation — to prevent SQL injection.

### 4. Validation
Queries the `files` table to confirm all records were inserted correctly.

## Security Practices

This project follows the same security discipline applied across the portfolio:

- **No hardcoded credentials** — all AWS and RDS credentials are loaded from environment variables via `python-dotenv`, never committed to version control (`.env` is git-ignored; only `.env.example` is versioned as a template)
- **Parameterized SQL queries** — inserts use `psycopg2`'s parameter substitution (`%s`) instead of string concatenation, eliminating SQL injection risk
- **Restricted network access** — the RDS Security Group inbound rule is scoped to a specific IP, not open to `0.0.0.0/0`
- **Explicit resource cleanup** — connections and cursors are explicitly closed after use; the RDS instance is stopped when not actively in use to avoid unnecessary free-tier consumption

## A Note on RDS vs. Aurora

AWS recently expanded free-tier access to Aurora PostgreSQL, which now appears alongside standard RDS in the console. This project intentionally uses **RDS for PostgreSQL** (not Aurora) — a more predictable, straightforward managed database service, better suited for this scope and for understanding core relational database fundamentals before exploring Aurora's more complex, cloud-native architecture.

## Environment Variables

See `.env.example` for the full list of required variables:

```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=sa-east-1
S3_BUCKET_NAME=

RDS_HOST=
RDS_PORT=5432
RDS_DATABASE=inventory
RDS_USER=
RDS_PASSWORD=
```

## Key Takeaways

- Integrating two distinct AWS services (S3 and RDS) through a single Python pipeline
- Applying secure credential management and SQL injection prevention as standard practice, not an afterthought
- Understanding PostgreSQL's default lowercase identifier behavior and its practical implications
- Managing cloud cost awareness by explicitly stopping compute resources when not in use

## References

- [Boto3 S3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
- [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/)

---

**Author:** Heuler Ferreira Silva
**Repository:** https://github.com/HeulerSilva/data-engineering-portfolio/tree/main/aws-s3-rds-ingestion
