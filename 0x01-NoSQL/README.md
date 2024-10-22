# NoSQL Databases and MongoDB

## Table of Contents
- [What NoSQL Means](#what-nosql-means)
- [Difference Between SQL and NoSQL](#difference-between-sql-and-nosql)
- [What is ACID](#what-is-acid)
- [What is Document Storage](#what-is-document-storage)
- [NoSQL Types](#nosql-types)
- [Benefits of NoSQL Databases](#benefits-of-nosql-databases)


---

### What NoSQL Means
NoSQL refers to "Not Only SQL." It's a broad class of database systems designed for scalability and performance. Unlike traditional SQL databases (which use a structured schema and tables), NoSQL databases can handle unstructured or semi-structured data and are optimized for specific workloads like handling large volumes of data or high traffic.

### Difference Between SQL and NoSQL
| Feature                | SQL (Relational)                       | NoSQL (Non-relational)                       |
|------------------------|----------------------------------------|---------------------------------------------|
| Data Model             | Structured, with predefined schema     | Flexible, schema-less, or dynamic schemas   |
| Storage                | Tables with rows and columns           | Key-Value, Document, Column, or Graph stores|
| Scalability            | Vertical scaling (scaling up)          | Horizontal scaling (scaling out)            |
| Transactions           | ACID-compliant                         | CAP theorem-based (may sacrifice ACID)      |
| Query Language         | SQL                                    | Varies (e.g., JSON queries, key-value lookups)|
| Best For               | Structured data, complex queries       | Unstructured or semi-structured data        |

### What is ACID
ACID stands for Atomicity, Consistency, Isolation, and Durability, which are key properties for reliable database transactions:
- **Atomicity**: Ensures that a transaction is all or nothing. If any part of the transaction fails, the entire transaction fails.
- **Consistency**: Guarantees that a transaction will bring the database from one valid state to another, maintaining database rules.
- **Isolation**: Ensures that concurrent execution of transactions leaves the database in the same state as if the transactions were executed sequentially.
- **Durability**: Ensures that once a transaction is committed, it remains in the system even in the case of a failure.

### What is Document Storage
Document storage refers to a type of NoSQL database that stores, retrieves, and manages data in document format (usually JSON, BSON, or XML). Each document can have a different structure, making it flexible for handling semi-structured data. An example of this is MongoDB.

### NoSQL Types
1. **Document Stores** (e.g., MongoDB, Couchbase): Stores data as documents (e.g., JSON, BSON).
2. **Key-Value Stores** (e.g., Redis, DynamoDB): Stores data as key-value pairs.
3. **Columnar Databases** (e.g., Cassandra, HBase): Uses columns for storage instead of rows like relational databases.
4. **Graph Databases** (e.g., Neo4j, ArangoDB): Stores relationships between data points as graphs.

### Benefits of NoSQL Databases
- **Scalability**: NoSQL databases are designed to scale out by distributing data across multiple servers.
- **Flexible Schema**: NoSQL databases do not require a fixed schema, making it easier to handle changing data models.
- **High Performance**: Optimized for fast read/write operations, even with large datasets.
- **Handling Large Volumes of Data**: Ideal for big data and real-time web applications.
- **Horizontal Scaling**: NoSQL databases scale by adding more servers, making it easy to handle traffic growth.
