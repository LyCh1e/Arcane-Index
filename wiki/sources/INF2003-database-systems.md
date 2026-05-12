---
type: source
title: "INF2003 Database Systems"
domain: database-systems
course: INF2003
tags: [database, sql, relational-algebra, normalisation, er-diagram, indexing, transactions, nosql, data-warehouse, acid]
ingested: 2026-05-12
raw: "raw/INF2003 Database Systems Notes.md"
---

# Source: INF2003 — Database Systems

**Institution:** Singapore Institute of Technology (SIT)  
**Academic Year:** AY2025/26 Trimester 1  
**Lecturers:** Dr. Tong Rong (Lectures 1–5), Zhang Wei (Lectures 6–10)

---

## Coverage Summary

Full lecture notes from a two-part module: the first half covers classical relational database theory; the second half covers physical storage, transactions, and modern database paradigms.

| Lecture | Topic | Key Content |
|---------|-------|-------------|
| 1 | DB Introduction | DBMS advantages, 3-level data abstraction, data independence, ACID overview, 6 stages of DB design, relational model, keys |
| 2 | Relational Algebra & SQL Pt 1 | 6 fundamental RA operators, extended operators (join, division), ICs, SQL DDL, basic DML |
| 3 | SQL Part 2 | INSERT/UPDATE/DELETE/SELECT (advanced), UNION/INTERSECT/EXCEPT, nested queries, aggregates, GROUP BY/HAVING, set comparisons, ORDER BY, query optimisation |
| 4 | Database Refinement | Anomalies, functional dependencies, Armstrong's axioms, attribute closure, 1NF/BCNF, decomposition properties |
| 5 | ER Diagrams | ER model notation, entity/attribute/relationship types, participation constraints, cardinality, weak entities, ISA, ER→relational schema conversion |
| 6 | Indexing | File organisation (heap/sorted/indexed), hash index, B+ tree (search/insert/delete) |
| 7 | Transactions | ACID deep-dive, serial vs serializable schedules, interleaving, SQL TCL (COMMIT/ROLLBACK/SAVEPOINT), locking, deadlock, optimistic 3-phase concurrency |
| 8 | NoSQL | Key-value (Redis), document (MongoDB), columnar (Cassandra), graph (Neo4j); SQL→NoSQL migration; when to use NoSQL |
| 9 | Blockchain | Hash chains, blocks, mining, proof-of-work, longest-chain rule, tamper-resistance |
| 10 | Data Warehouse | ETL, star/snowflake schema, OLAP cube, slice/dice/drill-down/roll-up/pivot, OLTP vs OLAP |

---

## Assessment

| Item | Weight |
|------|--------|
| Quiz 1 (Week 6) | ~25% |
| Project (group, 6 students) | ~40% |
| Final Exam | ~35% |

**Project:** Build an application using both relational and non-relational databases; deliverables include proposal, final report, video presentation, and source code.

---

## Key Concepts Generated

- [[concepts/relational-database-fundamentals]] — DB/DBMS basics, data abstraction, ACID, 6 design stages, relational model, keys, integrity constraints
- [[concepts/relational-algebra-and-sql]] — Full RA operator set, SQL DDL/DML, aggregates, set operations, subqueries, optimisation
- [[concepts/database-normalisation]] — FDs, Armstrong's axioms, closure, 1NF/BCNF, lossless and dependency-preserving decomposition
- [[concepts/er-diagrams]] — ER model, entity/attribute/relationship types, ER→schema conversion
- [[concepts/database-indexing-transactions]] — Hash index, B+ tree, ACID transactions, schedules, concurrency control, recovery
- [[concepts/nosql-and-data-warehousing]] — NoSQL types, MongoDB, when to use NoSQL, ETL, star/snowflake schema, OLAP

---

## Tools Used in Module

- MariaDB / MySQL — SQL labs
- SQLite3 via Python — Python-SQL lab
- SQLAlchemy (ORM) — Python ORM lab
- MongoDB — NoSQL lab
- Google Colab / Jupyter Notebook — Python labs
