# Kinesis Data Streams — Producer & Consumer

## Overview

This project demonstrates a real-time data streaming pattern using **Amazon Kinesis Data Streams**: a Python producer sends JSON records to a Kinesis stream, and a Python consumer reads and processes those records in near real-time using shard iterators.

## Architecture

```
Producer (Python)
        │
        │  boto3 — put_record()
        ▼
Kinesis Data Stream (On-Demand)
        │
        │  boto3 — get_shard_iterator() + get_records()
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
├── producer.ipynb
├── consumer.ipynb
├── .env.example
└── README.md
```

## How It Works

### Producer
Connects to Kinesis using credentials loaded from environment variables, and sends a JSON-encoded record to the stream via `put_record()`, using a partition key to determine shard placement.

### Consumer
Retrieves a shard iterator (`ShardIteratorType="LATEST"`) to start reading from the most recent point in the stream, then polls `get_records()` in a loop, printing each record's sequence number, arrival timestamp, partition key, and decoded payload.

**Controlled execution:** rather than running indefinitely (the default behavior for a streaming consumer, which typically runs as a long-lived service in production), this consumer stops automatically after processing a fixed number of records (3) — a deliberate choice for demonstration and testing purposes, avoiding the need to force-interrupt execution.

```python
max_records = 3
count = 0

while shard is not None and count < max_records:
    response = client.get_records(ShardIterator=shard, Limit=10)
    for record in response["Records"]:
        # process record
        count += 1
        if count >= max_records:
            break
    shard = response.get("NextShardIterator")
```

## Security Practices

- All AWS credentials are loaded from environment variables via `python-dotenv`; `.env` is git-ignored, only `.env.example` is versioned as a template
- No hardcoded stream names, shard IDs, or partition keys — all configurable via environment variables

## Cost Awareness

Kinesis Data Streams has **no free tier** and bills per stream-hour (~$0.04/hour) regardless of usage volume. The stream used for this lab was deleted immediately after testing to avoid unnecessary cost accumulation.

## Key Takeaways

- Understanding the shard-based architecture of Kinesis Data Streams
- Implementing both producer (`put_record`) and consumer (`get_shard_iterator` + `get_records`) patterns
- Designing controlled, testable execution for a naturally continuous streaming process
- Applying cost-conscious cloud resource management

---

**Author:** Heuler Ferreira Silva
**Repository:** https://github.com/HeulerSilva/data-engineering-portfolio/tree/main/aws-kinesis-streaming/01-streams-consumer