# AWS Kinesis — Streaming Data Labs

## Overview

This directory contains two hands-on labs exploring real-time data streaming patterns on AWS using **Amazon Kinesis**, each demonstrating a different architecture for moving event data through the cloud.

## Labs

| # | Lab | Pattern | Stack |
|---|-----|---------|-------|
| 01 | [Streams — Producer & Consumer](./01-streams-consumer/README.md) | Direct real-time consumption | Kinesis Data Streams, boto3 |
| 02 | [Firehose — Delivery to S3](./02-firehose-s3/README.md) | Automated batch delivery to storage | Amazon Data Firehose, S3, boto3 |

## Why Two Patterns

These labs intentionally cover two distinct real-world streaming use cases:

- **Data Streams (Lab 01)** — used when an application needs to react to events in near real-time, with full control over how records are read and processed (e.g., triggering alerts, real-time dashboards, custom business logic per event).
- **Firehose (Lab 02)** — used when the goal is reliable, automated delivery of streaming data into a data lake or warehouse for later batch analysis, without managing consumer logic or infrastructure.

Understanding when to use each is a practical architectural decision in real data engineering work — not just a tooling choice. Choosing the wrong one for a given workload means either over-engineering a simple delivery pipeline (using Data Streams when Firehose would suffice) or under-provisioning real-time responsiveness (using Firehose when true low-latency consumption is required).

## Security & Cost Practices

Both labs follow consistent discipline applied throughout this portfolio:

- Credentials managed via environment variables (`.env`, git-ignored), never hardcoded
- Cloud resources (streams, delivery streams) deleted immediately after each study session — Kinesis Data Streams has no free tier and bills per stream-hour regardless of usage
- Screenshots and evidence files reviewed for sensitive account information before publishing

## References

- [Amazon Kinesis Data Streams Documentation](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [Amazon Data Firehose Documentation](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

---

**Author:** Heuler Ferreira Silva
**Repository:** https://github.com/HeulerSilva/data-engineering-portfolio/tree/main/aws-kinesis-streaming