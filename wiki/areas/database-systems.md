---
type: area
title: "Database Systems"
domain: database-systems
source: [[sources/INF2003-database-systems]]
updated: 2026-05-14
tags: [area, database-systems]
---

# Database Systems

**Source**: INF2003 — Database Systems, SIT.

---

## What I Know

The full relational database stack from the ACID guarantees and relational model through SQL, schema design, normalisation, indexing, transactions, and NoSQL alternatives. INF2003 covers 6 design stages that take a business problem to a deployed, secure database.

---

## Concept Pages

| Page | What It Covers |
|------|---------------|
| [[concepts/relational-database-fundamentals\|Relational DB Fundamentals]] | ACID, 6 design stages, relational model, keys (super/candidate/primary/foreign), integrity |
| [[concepts/relational-algebra-and-sql\|Relational Algebra & SQL]] | 6 fundamental RA operators (σ/π/∪/−/×/ρ), full SQL syntax (SELECT…GROUP BY…HAVING), optimisation |
| [[concepts/database-normalisation\|Database Normalisation]] | FDs, Armstrong's axioms, FD closure, BCNF decomposition (lossless but not always dependency-preserving) |
| [[concepts/er-diagrams\|Entity-Relationship Diagrams]] | ER notation (entity/relationship/attribute), cardinality, participation, weak entity, ISA, ER→schema translation |
| [[concepts/database-indexing-transactions\|Indexing & Transactions]] | Hash index (O(1) equality), B+ tree (O(log n), range queries), ACID transactions, locking, optimistic concurrency, WAL |
| [[concepts/nosql-and-data-warehousing\|NoSQL & Data Warehousing]] | Key-value/document/columnar/graph stores, ETL, star/snowflake schemas, OLAP cube operations |

---

## Key Ideas

- **The 6-stage design pipeline**: Requirements → Conceptual (ER) → Logical (relational schema) → Refinement (BCNF) → Physical (indexes) → Security
- **BCNF**: every non-trivial FD X→Y must have X as a superkey. Decomposition is lossless but may not preserve all FDs
- **B+ tree** is the universal index: all data in leaves (linked list for range scans), internal nodes route; O(log n) for equality and range; min 50% occupancy maintained via split/merge
- **Write-Ahead Logging (WAL)**: log before write. On crash: replay redo log for committed transactions; undo log for uncommitted ones
- **Push σ/π before joins**: the most impactful SQL optimisation is to filter and project early, reducing the rows that joins must process

---

## Cross-Domain Connections

- [[concepts/data-structures-fundamentals|Data Structures]] — B-Trees in INF1008 provide the algorithmic perspective on B+ tree indexes
- [[concepts/server-side-web-development|Server-Side Web Dev]] — PDO/MySQL in INF1005 is the practical application of INF2003's SQL theory
- [[synthesis/maths-to-ml-bridge|Mathematics → ML]] — descriptive statistics underpin CRISP-DM data understanding phase

---

## Study Notes

[[learning/inf2003-database-systems-study-notes|INF2003 Study Notes]] — exam-prep summaries
