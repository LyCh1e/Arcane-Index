---
type: concept
title: "NoSQL and Data Warehousing"
domain: database-systems
course: INF2003
complexity: medium
tags: [nosql, mongodb, redis, cassandra, graph-database, data-warehouse, etl, star-schema, snowflake-schema, olap, oltp, blockchain]
updated: 2026-05-12
status: established
created: 2026-05-12
---

# NoSQL and Data Warehousing

This page covers the two major database paradigms that extend beyond classical relational systems: **NoSQL** (for flexible, distributed, large-scale data) and **data warehousing** (for analytical processing of historical data). A brief treatment of **blockchain** as a specialised data structure is also included.

---

## Relational DB Limitations

Classical relational databases (RDBMS) are **centralised** — all data lives on one server.

| Advantage | Limitation |
|-----------|-----------|
| ACID guarantees | Poor horizontal scalability |
| SQL — mature, standardised | Schema rigidity (schema changes are costly) |
| Mature tooling | Geo-distribution is complex |
| Efficient joins | Does not handle heterogeneous/diverse data well |

**When RDBMS struggles:**
- Big data: data too large for one server
- Real-time web applications: burst write load
- Diverse data: e-commerce items with completely different schemas (a book vs a GPU)
- Geo-distribution: data spread across multiple continents

---

## NoSQL Overview

**NoSQL** ("Not Only SQL") simplifies data models to improve generalisability, flexibility, and distribution.

**Four main categories:**

| Category | Data Model | Key Characteristic | Examples |
|----------|-----------|-------------------|----------|
| **Key-value** | Hash table | Simplest; all access via key | Redis, Memcached, DynamoDB |
| **Document** | JSON/BSON/XML documents | Nested, schema-flexible documents | MongoDB, CouchDB |
| **Columnar** | Column families | Column-wise storage; compression | Cassandra, HBase, BigTable |
| **Graph** | Nodes + edges | Traversal; relationship-centric queries | Neo4j |

---

## Key-Value: Redis

The most popular key-value store. Written in C++; open-source; in-memory with optional disk persistence.

**Operations — all O(1):**
```
SET key2003 "DBSys"    → OK
GET key2003            → "DBSys"
DEL key2003            → 1
GET key2003            → (nil)
```

**Rich data structures:** strings, hashes, lists, sets, sorted sets, bitmaps.

**Ideal for:** caching, session storage, real-time leaderboards, pub/sub messaging.

**Limitation:** no complex queries or joins; all querying must happen in application code.

---

## Document Database: MongoDB

A schema-less, document-oriented database. Each record is a **document** (JSON/BSON), and documents within the same collection can have different fields.

**Key mapping — RDBMS → MongoDB:**

| RDBMS | MongoDB |
|-------|---------|
| Database | Database |
| Table / View | Collection |
| Row | Document (BSON) |
| Column | Field |
| Index | Index |
| JOIN | Embedded document / `$lookup` |
| Foreign key | Reference (manual) |
| Partition | Shard |

**CRUD operations:**

```javascript
// Create
db.ppl.insert({ _id: 11, type: "Avengers", name: "Spider Man" })
db.ppl.insert({ type: "Transformers", cat: "Autobot", name: "Optimus Prime" })
// MongoDB auto-generates _id if omitted

// Read
db.ppl.find()                              // all documents
db.ppl.find({ type: "Avengers" })          // filter by field
db.ppl.findOne({ name: "Spider Man" })     // first match

// Update
db.ppl.update({ type: "Avengers" }, { $set: { type: "The Avengers" } })

// Delete
db.ppl.remove({ type: /^A/ })             // remove all where type starts with A
```

**Strengths:** flexible schema, easy horizontal scaling (sharding), fast for simple queries, native JSON integration.

**Weaknesses:** no joins; not suitable for complex ACID transactions.

---

## Columnar Database: Cassandra / HBase

Row-oriented storage (MySQL): all fields of one row stored together.  
**Column-oriented storage**: all values of one column stored together.

```
Row-oriented:    22, Dustin, 1000, 45, 31, Lubber, 1001, 55 …
Column-oriented: 22, 31, 58, 74 | Dustin, Lubber, Rusty, Rusty | 1000, 1001, 1001, …
```

**Benefits:**
- Excellent **data compression** (same-type values compress well)
- Fast **aggregation queries** on a single column (`SUM(sales)`)
- Flexible schema: columns can vary row-to-row
- Self-indexing

**Weaknesses:** poor for frequent inserts/updates (must update all column stores).

**Real-world case:** Facebook migrated 50 GB of data from MySQL to Cassandra:
- Write latency: 300 ms → 0.12 ms
- Read latency: 350 ms → 15 ms

---

## Graph Database: Neo4j

Optimised for data that is inherently graph-structured (social networks, recommendation engines, fraud detection, knowledge graphs).

**Core elements:**
- **Nodes**: entities with properties (key-value pairs) and labels
- **Relationships**: directed, typed edges between nodes; can have properties
- **Properties**: named values attached to nodes or relationships

```
(Tom Hanks :Person) -[:ACTED_IN { roles: ['Forrest'] }]-> (Forrest Gump :Movie)
```

**Key advantage:** graph traversal is efficient because each node knows its adjacent nodes directly — no expensive join-based path finding.

| RDBMS | Graph DB |
|-------|---------|
| Tables | Graphs |
| Rows | Nodes |
| Columns + data | Properties + values |
| Constraints | Relationships |
| JOINs | Traversals |

---

## When to Use NoSQL

Use NoSQL when:
- RDBMS is too restrictive; schema flexibility is needed
- ACID guarantees are not required
- Data volume exceeds single-node capacity
- Data sources are diverse (heterogeneous schema)
- High availability is required (partition tolerance)

**Do not use NoSQL for:** banking/finance systems, systems that require complex multi-table transactions, or any application where ACID correctness is non-negotiable.

---

## SQL → NoSQL Migration Strategies

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **1-to-1 mapping** | Each SQL table → one NoSQL collection | Most common; minimal redesign |
| **Denormalisation** | Reverse BCNF decomposition — merge tables | Moderate changes; read-performance focus |
| **Redesign from scratch** | Ignore the SQL schema; model for NoSQL | Dramatic application change; best long-term |

---

## Data Warehouse

A **data warehouse** is a central repository of integrated data from multiple sources, optimised for **analytical reporting** rather than transaction processing.

| Dimension | Description |
|-----------|-------------|
| **Application** | Data drawn from multiple operational systems (sales, HR, marketing) |
| **Time** | Both historical and current data; enables trend analysis |
| **Objective** | Reporting, data analysis, business intelligence |

**Architecture:**

```
Operational Systems (OLTP)
        │
    ETL Process
        │
    Data Warehouse (OLAP)
        │
    Access Layer (BI tools, dashboards)
```

---

## ETL: Extract, Transform, Load

| Phase | Activity |
|-------|---------|
| **Extract** | Pull raw data from operational systems and external sources |
| **Transform** | Data type conversion, column merging, cleansing, masking, normalisation |
| **Load** | Write transformed data into the data warehouse |

**Challenges:** large data volumes, dirty data, synchronisation across sources, loading spikes.

---

## Star Schema

The simplest and most popular data warehouse schema.

**Structure:**
- One central **fact table** (business events/transactions)
- Multiple surrounding **dimension tables** (descriptive attributes)

**Fact table:** numeric measures + foreign keys to dimension tables  
**Dimension tables:** descriptive attributes (time, geography, product, employee …)

```
         DimTime
            │
DimProduct ─┼─ FactSales ─┼─ DimRegion
            │
         DimEmployee
```

**Benefits:** simple join logic, fast read queries, easy to understand.

**Drawbacks:** denormalised dimensions; data integrity not enforced at the warehouse level; limited flexibility for complex analytics.

---

## Snowflake Schema

An extension of the star schema where dimension tables are **normalised** into multiple related tables.

**Example:** instead of a flat `DimProduct(product_id, product_name, category_id, category_name)`, the snowflake version has:
- `DimProduct(product_id, product_name, category_id)` 
- `DimCategory(category_id, category_name)`

**Benefit:** reduces storage through normalisation.  
**Drawback:** more complex queries with more joins; slower query performance.

**Rule of thumb:** Star schema for performance-critical analytical queries; Snowflake when storage savings matter and query complexity is acceptable.

---

## OLTP vs. OLAP

| Dimension | OLTP | OLAP |
|-----------|------|------|
| **Purpose** | Run the business (transactions) | Analyse the business (reporting) |
| **Focus** | INSERT, UPDATE, DELETE | SELECT (complex aggregations) |
| **Data** | Current operational data | Historical + current |
| **Query complexity** | Simple, fast | Complex, slow |
| **Normalisation** | Normalised (3NF/BCNF) | Denormalised (star/snowflake) |
| **Users** | Thousands (clerks, apps) | Hundreds (analysts, executives) |
| **Transaction size** | Short | Long |

> **Summary:** DBMS is used to run a business; data warehouse helps optimise the business.

---

## OLAP Cube

The core of OLAP — a **multi-dimensional array** of data (hypercube if > 3 dimensions).

**Dimensions:** product, region, time.  
**Measure:** sales value stored in each cell.

**OLAP Operations:**

| Operation | Description | Example |
|-----------|-------------|---------|
| **Slice** | Fix one dimension; view the remaining 2D cross-section | Apple sales for all regions in 2023 |
| **Dice** | Sub-cube by specifying ranges on multiple dimensions | Asia & Africa, 2021–2023 |
| **Drill Down** | Navigate from summary to detail | Country → City |
| **Roll Up** | Navigate from detail to summary | City → Country (aggregates with SUM, etc.) |
| **Pivot** | Rotate the cube to see a different face | Swap row/column axes |

**SQL for cubes:**
```sql
-- Total sales per product
SELECT SUM(sales) FROM ProductSales GROUP BY product;

-- Total sales per product per day
SELECT SUM(sales) FROM ProductSales GROUP BY product, sday;
```

---

## Blockchain (Brief)

Blockchain is a **distributed, append-only ledger** — not a general-purpose database, but a specialised data structure built on hash chaining.

**Core mechanism:**
- Transactions are grouped into **blocks**
- Each block contains the **SHA-256 hash** of the previous block → forms a chain
- Any tampering with a block changes its hash, breaking the `prev` pointer in the next block — instantly detectable

**Tamper-resistance:** to alter block 2 in a 5-block chain, the attacker must recompute blocks 2–5 faster than the honest network extends the chain — computationally infeasible with Proof-of-Work.

**Proof-of-Work:** finding a nonce such that the block's hash starts with N leading zeros (expected 2^N attempts). Hard to compute; trivial to verify. Secures the chain by making cheating expensive.

**Limitations as a database:**
- Bitcoin: ~400 transactions/minute; Visa: ~102,000 transactions/minute
- No CRUD — append-only
- Not suitable for frequently updated operational data

**Suitable applications:** international currency (no central authority needed), anti-counterfeiting, cross-border document authentication, patent records.

---

## See Also

- [[concepts/relational-database-fundamentals]] — ACID properties that NoSQL relaxes
- [[concepts/database-indexing-transactions]] — Transaction management that NoSQL simplifies or skips
- [[concepts/database-normalisation]] — Normalisation that data warehouses intentionally reverse (denormalise)
- [[concepts/data-structures-fundamentals]] — Hash tables and B-Trees underpin index structures and blockchain hash chains
- [[sources/INF2003-database-systems]] — Source course
