---
type: concept
title: "Relational Database Fundamentals"
domain: database-systems
course: INF2003
complexity: medium
tags: [database, dbms, relational-model, acid, keys, integrity-constraints, data-abstraction, data-independence]
updated: 2026-05-12
---

# Relational Database Fundamentals

A **database** is an organised collection of information. A **Database Management System (DBMS)** is the software layer that stores, manages, and provides efficient access to that data — handling integrity, security, concurrency, and crash recovery in ways that flat files cannot.

---

## Why DBMS Over Flat Files?

| Advantage | Description |
|-----------|-------------|
| **Data independence** | Logical and physical structure are separated; applications are insulated from storage changes |
| **Efficient access** | Indexing, query optimisation, and large-file retrieval |
| **Reduced development time** | Query facilities mean less application code for data access |
| **Integrity and security** | Constraint validation and access control |
| **Concurrency control** | Multiple simultaneous users without corrupting data |
| **Crash recovery** | Consistent state can be restored after failure |

---

## Three Levels of Data Abstraction

```
View Level (External)    ← end-users, application developers
Logical Level (Conceptual) ← DB designers, developers
Physical Level (Internal)  ← DB administrators, storage engineers
```

| Level | Who Uses It | What It Describes |
|-------|-------------|-------------------|
| **View** | Users, app code | Subset of data visible to a particular user or application |
| **Logical** | Developers, DBA | Schema: tables, attributes, relationships, constraints |
| **Physical** | DBA, storage | How data is actually stored on disk (files, blocks, compression) |

### Data Independence

**Physical independence**: Change the physical storage (compression, indexing, disk layout) without altering the logical schema or applications.

**Logical independence**: Add, modify, or remove attributes, entities, or relationships without rewriting existing applications. *Harder to achieve* than physical independence, because applications depend on the logical schema.

---

## Relational Data Model

A **relational database** is a collection of **relations** (tables), each with a unique name.

| Term | Meaning |
|------|---------|
| **Relation** | A table with rows and columns |
| **Tuple** | A single row; specifies a relationship among attribute values |
| **Attribute** | A column; has a name and a domain (set of valid values) |
| **Relation schema** | The type information: `STUDENT(sid, sname, saddress)` |
| **Domain** | The set of valid values for an attribute; includes the special value **NULL** |

**Key property**: Relations are *unordered sets* of tuples — no guaranteed row order. Attribute values are *atomic* (indivisible).

### NULL

NULL means "unknown" or "inapplicable". NULL is a member of every domain.  
- `NULL > 100` evaluates to NULL, not TRUE or FALSE  
- Operations with NULL generally propagate NULL  
- Test for NULL with `IS NULL` / `IS NOT NULL`, never `= NULL`  
- Avoid nullable columns where possible; use default values instead

---

## Keys

Keys allow individual tuples to be uniquely identified and referenced.

| Key Type | Definition |
|----------|-----------|
| **Superkey** | Any set of attributes that uniquely identifies a tuple (can be redundant) |
| **Candidate key** | A *minimal* superkey — no proper subset is also a superkey |
| **Primary key** | The candidate key chosen as the main identifier; **underlined** in schema notation |
| **Foreign key** | An attribute (or set) in one relation that references the primary key of another; acts as a logical pointer |

**Example**: `STUDENT(sid, sname, saddress, sphone)`  
- Superkeys: `{sid}`, `{sphone}`, `{sid, sname}`, ...  
- Candidate keys: `{sid}`, `{sphone}` (assuming unique)  
- Primary key: `sid` (chosen as most appropriate)

---

## ACID Properties

The standard guarantee for relational database transactions:

| Property | Guarantee |
|----------|-----------|
| **Atomicity** | The entire transaction happens, or none of it does — no partial commits |
| **Consistency** | The database is in a consistent state before and after every transaction |
| **Isolation** | Concurrent transactions execute as if they were serial — no interference |
| **Durability** | Once committed, changes are permanent even through system crashes |

---

## Six Stages of Database Design

| Stage | Name | Activity |
|-------|------|---------|
| S1 | **Requirement Analysis** | Gather user needs: what data, what applications, what operations |
| S2 | **Conceptual Design** | Build an ER diagram — high-level, implementation-independent |
| S3 | **Logical Design** | Translate ER diagram to relational schemas (tables, columns, keys) |
| S4 | **Schema Refinement** | Normalise the schemas — eliminate redundancy and anomalies |
| S5 | **Physical Design** | Optimise for the target hardware: indexes, clustering, partitioning |
| S6 | **Application & Security Design** | Access control, encryption, backup and recovery, authorisation |

ER diagrams are relevant to stages S1–S3; normalisation is the focus of S4.

---

## Integrity Constraints (ICs)

ICs are rules enforced by the DBMS to maintain the faithfulness of stored data to the real world. They are specified at schema definition time and checked on every modification.

A database **instance** is **legal** if all ICs hold.

### Domain Constraints

Restrict the values an attribute can hold to its declared data type and range.

```sql
gender CHAR(1) CHECK (gender IN ('M', 'F'))
age    INTEGER CHECK (age > 0)
```

### Key Constraints

- **NOT NULL**: primary key attributes cannot be null  
- **UNIQUE**: no two tuples can have identical values for key attributes  
- Only **one primary key** per table; but multiple UNIQUE constraints are allowed  
- UNIQUE does *not* exclude NULL — multiple NULLs are permitted (NULLs are treated as unequal)

### Referential Integrity Constraints

A foreign key value must match an existing primary key value in the referenced relation — or be NULL.

```sql
CREATE TABLE Enrolled (
    sid  CHAR(8),
    mid  CHAR(7),
    grade CHAR(2),
    PRIMARY KEY (sid, mid),
    FOREIGN KEY (sid) REFERENCES Student,
    FOREIGN KEY (mid) REFERENCES Module
);
```

If a referenced row is deleted, dependent rows can be: rejected (`RESTRICT`), cascaded (`ON DELETE CASCADE`), or nullified (`ON DELETE SET NULL`).

---

## DBMS Architecture Tiers

| Architecture | Description |
|---|---|
| **1-tier** | Client and database on the same machine |
| **2-tier** | Client application communicates directly with the database server |
| **3-tier** | Client → Application server → Database server; most common for web apps |

---

## See Also

- [[concepts/relational-algebra-and-sql]] — Querying and manipulating relations
- [[concepts/database-normalisation]] — Formal refinement of schemas (S4)
- [[concepts/er-diagrams]] — Conceptual design tool (S2–S3)
- [[concepts/database-indexing-transactions]] — Physical design and transaction management (S5–S6)
- [[concepts/nosql-and-data-warehousing]] — Beyond relational: NoSQL and analytical systems
- [[sources/INF2003-database-systems]] — Source course
