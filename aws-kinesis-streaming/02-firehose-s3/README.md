# Kinesis Firehose — Delivery to S3

## Overview

This project demonstrates automated data delivery using **Amazon Data Firehose** (formerly Kinesis Data Firehose, renamed by AWS in February 2024): a Python producer sends records to a Firehose delivery stream, which automatically batches and delivers the data into an **Amazon S3** bucket — no consumer code required.

## Architecture

```
Producer (Python)
        │
        │  boto3 — put_record()
        ▼
Amazon Data Firehose (Delivery Stream)
        │
        │  automatic batching & delivery
        ▼
Amazon S3 (destination bucket)
```

## Technical Stack

- **Language:** Python
- **AWS SDK:** boto3
- **Service:** Amazon Data Firehose → S3

## Project Structure

```
02-firehose-s3/
├── producer.ipynb
├── sample-output/          # Records as delivered to S3 by Firehose
├── assets/                 # Screenshot evidence of successful delivery
├── .env.example
└── README.md
```

## How It Works

The producer sends JSON records to a Firehose delivery stream via `put_record()`. Firehose handles buffering, batching, and delivery to the configured S3 destination automatically — no polling or consumer logic is required, unlike Kinesis Data Streams.

Delivered files land in S3 under an automatically generated, timestamp-based prefix structure (e.g., `_file_2026/08/19/21/`), with filenames following Firehose's default naming convention (delivery stream name + timestamp + UUID). Sample delivered files are included in `sample-output/` as evidence of the end-to-end pipeline working correctly.

## A Note on Naming: Kinesis Data Firehose → Amazon Data Firehose

AWS renamed this service in February 2024. The functionality, APIs, CLI, and IAM policies remain unchanged — only the console name and documentation were updated. This project uses the current name (Amazon Data Firehose) while acknowledging the original name for reference.

## Security Practices

- All AWS credentials are loaded from environment variables via `python-dotenv`; `.env` is git-ignored, only `.env.example` is versioned as a template
- Screenshot evidence in `assets/` has sensitive account information (AWS Account ID) redacted before publishing

## Cost Awareness

Unlike Kinesis Data Streams, Firehose does not charge a per-hour "active stream" fee — cost is driven purely by data volume ingested (~$0.029/GB). The delivery stream used for this lab was deleted after testing as a general cost-hygiene practice.

## Key Takeaways

- Understanding when to use Firehose (automated delivery) vs. Data Streams (custom real-time consumption)
- Implementing a producer that feeds a fully managed delivery pipeline with zero consumer-side code
- Recognizing Firehose's default S3 delivery structure and file naming conventions
- Applying the same security and cost discipline used across this portfolio, even for simple pipelines

---

**Author:** Heuler Ferreira Silva
**Repository:** https://github.com/HeulerSilva/data-engineering-portfolio/tree/main/aws-kinesis-streaming/02-firehose-s3