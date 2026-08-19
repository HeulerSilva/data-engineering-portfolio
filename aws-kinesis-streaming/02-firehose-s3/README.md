# Kinesis Firehose — Delivery to S3

## Overview

This project demonstrates automated data delivery using **Amazon Kinesis Data Firehose**: a Python producer sends records to a Firehose delivery stream, which automatically batches and delivers the data to an **Amazon S3** bucket — no consumer code required.

*Status: 🔄 In progress — documentation will be expanded as the pipeline is built.*

## Architecture

```
Producer (Python)
        │
        │  boto3 — put_record()
        ▼
Kinesis Data Firehose
        │
        │  automatic batching & delivery
        ▼
Amazon S3 (destination bucket)
```

## Technical Stack

- **Language:** Python
- **AWS SDK:** boto3
- **Service:** Amazon Kinesis Data Firehose → S3

## Project Structure

```
02-firehose-s3/
├── producer.py
├── .env.example
└── README.md
```

## Cost Awareness

Unlike Kinesis Data Streams, Firehose does not charge a per-hour "active stream" fee — cost is driven purely by data volume ingested (~$0.029/GB), making it a lower-risk option to leave configured between sessions. Still deleted after use as a general cost-hygiene practice.

---

**Author:** Heuler Ferreira Silva
