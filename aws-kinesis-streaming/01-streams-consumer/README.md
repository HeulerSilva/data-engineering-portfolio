# Kinesis Data Streams — Producer & Consumer

## Overview

This project demonstrates a real-time data streaming pattern using **Amazon Kinesis Data Streams**: a Python producer sends records to a Kinesis stream, and a Python consumer reads and processes those records in near real-time.

*Status: 🔄 In progress — documentation will be expanded as the pipeline is built.*

## Architecture

```
Producer (Python)
        │
        │  boto3 — put_record()
        ▼
Kinesis Data Stream
        │
        │  boto3 — get_records()
        ▼
Consumer (Python)
```

## Technical Stack

- **Language:** Python
- **AWS SDK:** boto3
- **Service:** Amazon Kinesis Data Streams (On-Demand mode)

## Project Structure

```
01-streams-consumer/
├── producer.py
├── consumer.py
├── .env.example
└── README.md
```

## Cost Awareness

Kinesis Data Streams has **no free tier** and charges per stream-hour (~$0.04/hour) regardless of usage. The stream created for this project is deleted immediately after each study session to avoid unnecessary cost accumulation.

---

**Author:** Heuler Ferreira Silva
