# Redis Overview and Usage in Python

## What is Redis?

**Redis** (Remote Dictionary Server) is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, and geospatial indexes. Redis is known for its high performance, scalability, and flexibility.

### Features of Redis
- **In-memory**: Redis stores data in memory, making it incredibly fast.
- **Persistent**: Redis offers data persistence to disk (RDB and AOF), allowing for data recovery after a crash.
- **Data structures**: Redis supports a rich set of data types like strings, lists, sets, sorted sets, hashes, etc.
- **Pub/Sub**: Redis has support for publish/subscribe messaging.

## Installing Redis in Python

To use Redis in Python, we need to install the `redis` package.

You can install Redis client for Python using pip:
```bash
pip install redis
