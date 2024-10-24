# Backend Storage Project

## Overview

This repository contains implementations related to backend storage technologies, including advanced SQL features, NoSQL databases like MongoDB, and caching mechanisms using Redis.

## Table of Contents

- [Advanced SQL Features](#advanced-sql-features)
  - [Triggers](#triggers)
  - [Stored Procedures](#stored-procedures)
  - [Views](#views)
  - [Indexing](#indexing)
- [NoSQL with MongoDB](#nosql-with-mongodb)
  - [MongoDB Overview](#mongodb-overview)
  - [MongoDB in Python](#mongodb-in-python)
- [Redis and Redis in Python](#Redis)

## Advanced SQL Features

### Triggers

Triggers are special types of stored procedures that automatically run in response to certain events on a particular table or view in a database. They can be used to enforce business rules, validate data, and maintain audit trails.

### Stored Procedures

Stored procedures are precompiled collections of SQL statements that can be executed as a single call. They help encapsulate business logic, improve performance by reducing the amount of data sent over the network, and enhance security by controlling access to data.

### Views

Views are virtual tables created by querying data from one or more tables. They provide a way to present data in a specific format or to simplify complex queries. Views can help with data abstraction and security by restricting access to certain data.

### Indexing

Indexing is a technique used to speed up the retrieval of rows from a database table. Indexes create a data structure that allows for faster searching, sorting, and filtering of records, improving query performance significantly.

## NoSQL with MongoDB

### MongoDB Overview

MongoDB is a NoSQL database that stores data in flexible, JSON-like documents. It allows for dynamic schemas, making it ideal for handling unstructured data. MongoDB is designed to scale horizontally and is known for its high performance and availability.

### MongoDB in Python

To interact with MongoDB in Python, you can use the `pymongo` library. It provides an easy way to connect to a MongoDB server, perform CRUD operations, and manage data.

```python
# Example of connecting to MongoDB
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Inserting a document
collection.insert_one({"name": "John", "age": 30})

## Redis

Redis is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures, such as strings, hashes, lists, sets, and sorted sets, making it versatile for different use cases.

### Key Features of Redis

- **In-memory storage**: Redis stores data in memory, providing high-speed access and low-latency performance.
- **Persistence**: It offers various persistence options, including snapshots and append-only files (AOF), ensuring data durability.
- **Pub/Sub messaging**: Redis supports publish/subscribe messaging, enabling real-time communication between applications.
- **Atomic operations**: Redis provides atomic operations for its data structures, allowing for reliable updates.

### Using Redis in Python

To use Redis in Python, you typically use the `redis-py` library. Below is a simple example of how to connect to a Redis instance and perform basic operations:

```python
import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('foo', 'bar')

# Get the value by key
value = r.get('foo')

# Print the value
print(value.decode('utf-8'))  # Output: bar
