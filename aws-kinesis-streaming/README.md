# AWS Kinesis — Streaming Data Labs

## Overview

This directory contains two hands-on labs exploring real-time data streaming patterns on AWS using **Amazon Kinesis**, each demonstrating a different architecture for moving event data through the cloud.

## Labs

| # | Lab | Pattern | Stack |
|---|-----|---------|-------|
| 01 | [Streams — Producer & Consumer](./01-streams-consumer/README.md) | Direct real-time consumption | Kinesis Data Streams, boto3 |
| 02 | [Firehose — Delivery to S3](./02-firehose-s3/README.md) | Automated batch delivery to storage | Kinesis Data Firehose, S3, boto3 |

## Why Two Patterns

These labs intentionally cover two distinct real-world streaming use cases:

- **Data Streams (Lab 01)** — used when an application needs to react to events in near real-time, with full control over how records are read and processed (e.g., triggering alerts, real-time dashboards).
- **Firehose (Lab 02)** — used when the goal is reliable, automated delivery of streaming data into a data lake or warehouse for later batch analysis, without managing consumer logic.

Understanding when to use each is a practical architectural decision in real data engineering work — not just a tooling choice.

## Cost Awareness

Kinesis Data Streams has **no free tier** and bills per stream-hour regardless of usage; Firehose bills purely by data volume. Streams are created only for active study sessions and deleted immediately afterward to avoid unnecessary cost accumulation.

---

**Author:** Heuler Ferreira Silva
**Repository:** https://github.com/HeulerSilva/data-engineering-portfolio/tree/main/aws-kinesis-streaming
