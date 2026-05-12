---
type: concept
title: "Database Indexing and Transactions"
domain: database-systems
course: INF2003
complexity: high
tags: [indexing, b-plus-tree, hash-index, transactions, acid, concurrency, locking, deadlock, recovery, serializable, tcl]
updated: 2026-05-12
---

# Database Indexing and Transactions

This page covers the physical layer (Stage S5) and security/recovery layer (Stage S6) of the database design process — specifically: how the DBMS stores and retrieves data efficiently (indexing), and how it maintains correctness under concurrent access and failures (transactions).

---

## File Organisation

A table is stored in a **data file** made up of **pages** (fixed-size chunks). How pages are organised determines query performance.

| Organisation | Description | Best For |
|---|---|---|
| **Heap file** | Pages in arbitrary order; tuples unsorted | Full table scans (`SELECT *`) |
| **Sorted file** | Pages sorted by one or more attributes | Range queries and ORDER BY |
| **Index** | Additional data structure alongside the file | Point queries and range queries on the indexed attribute |

**Creating an index in SQL:**
```sql
CREATE INDEX idx_sid ON Students (sid);
```

**Trade-off:** Indexes speed up reads (`SELECT`) but slow down writes (`INSERT`, `UPDATE`, `DELETE`) because the index must be maintained on every modification. Create indexes strategically on columns used in `WHERE`, `JOIN ON`, and `ORDER BY`.

---

## Index Data Structures

### Hash Index

Uses a **hash function** `h(r)` to map a record's search key to a **bucket** (primary page + optional overflow pages).

```
h(r) = bucket number → scan that bucket for the record
```

**Properties:**
- O(1) average for equality search: `WHERE sid = '2001234'`
- **Cannot** support range queries: `WHERE year BETWEEN 2013 AND 2015` — hash destroys ordering
- One record belongs to exactly one bucket; different records may share a bucket (collision)

**Use when:** You need only equality lookups; key distribution is fairly uniform.

---

### B+ Tree

The most widely used index structure in relational DBMS. Supports both equality and range queries.

**Structure:**
- **Root node** — top of the tree
- **Internal nodes** — routing nodes containing keys and pointers to children
- **Leaf nodes** — all data entries; leaves are linked together in a doubly-linked list

**Key invariants:**
- All data is in the **leaf** nodes (internal nodes only route)
- All leaves are at the **same level** (perfectly balanced)
- Each leaf node contains `k` keys and `k+1` pointers, with **minimum 50% occupancy** (root is exempt)
- **High fanout** (typically 100+): each internal node has many children → shallow tree → few I/Os per search

---

#### B+ Tree: Search — O(log n)

Traverse from root to leaf following key comparisons.

**Range search** `[8, 24]`:
1. Search for lower bound (8) → land on a leaf
2. Follow the linked leaf list until the upper bound (24) is passed

Hash cannot do this; B+ tree can in O(log n + k) where k is the number of results.

---

#### B+ Tree: Insert

1. **Locate** the target leaf
2. **Insert** the key
   - If the leaf has space: done
   - If the leaf is full: **split** the leaf into two; duplicate the minimum key of the second node into the parent
3. **Recursively** propagate splits up the tree if the parent is also full
4. If the root splits, a **new root** is created — the tree grows taller

**Example: insert 8 into a leaf `[2, 3, 5, 7]` (capacity 4)**
1. Leaf is full → split: `[2, 3]` and `[5, 7, 8]`
2. Duplicate `5` into parent → parent may also split → recurse

---

#### B+ Tree: Delete

1. **Locate** the target leaf; remove the key
2. If the leaf still meets minimum occupancy: done
3. If **under-full**:
   - Try **borrowing** from the nearest sibling (left sibling preferred)
   - If borrowing is not possible (sibling is also at minimum): **merge** the two siblings into one node and remove the separator key from the parent
4. **Recursively** propagate merges up the tree
5. If the root becomes empty, the tree shrinks in height

A B+ tree is a **dynamic structure**: it grows and shrinks gracefully without periodic reorganisation.

**Complexity summary:**

| Operation | Time |
|-----------|------|
| Search (point) | O(log n) |
| Search (range) | O(log n + k) |
| Insert | O(log n) |
| Delete | O(log n) |

---

## Transactions

A **transaction (TXN)** is a logical unit of work: a sequence of database reads and writes that must execute as a single, indivisible operation.

**Example — bank transfer:**
1. Read `bal_wei`
2. Write `bal_wei := bal_wei − 100`
3. Read `bal_wayne`
4. Write `bal_wayne := bal_wayne + 100`

If step 2 completes but step 4 fails, the money disappears. Transactions prevent this.

---

## ACID Properties (Deep Dive)

| Property | Guarantee | Who is Responsible |
|----------|-----------|-------------------|
| **Atomicity** | All operations execute, or none do. No partial commits. | DBMS (transaction manager) |
| **Consistency** | Database moves from one consistent state to another. ICs hold before and after. | Application programmer |
| **Isolation** | Concurrently executing transactions appear to each other as if they were serial. | DBMS (concurrency control) |
| **Durability** | Once committed, changes survive system crashes. | DBMS (recovery manager) |

**Consistency nuance:** ACID consistency means ICs are satisfied — not that the *business logic* is correct. If you mistakenly code a 30% interest rate instead of 3%, ACID cannot detect that.

---

## Schedules and Serializability

A **schedule** is an ordered sequence of operations from multiple concurrent transactions.

| Schedule Type | Description | Safety |
|---|---|---|
| **Serial** | All operations of T1 complete before T2 starts; no interleaving | Safe; often poor performance |
| **Equivalent** | Two schedules that produce the same output | — |
| **Serializable** | Equivalent to *some* serial schedule | Safe |

**Goal:** allow interleaved execution (for performance) while guaranteeing serializability (for correctness).

**Interleaving can cause problems:**

| Problem | Description |
|---------|-------------|
| **Dirty read** | T1 reads data written by T2 before T2 commits; T2 then rolls back |
| **Non-repeatable read** | T1 reads a value twice; T2 modifies it between the two reads |
| **Lost update** | T1 and T2 both read and then overwrite the same value; one update is lost |

---

## SQL Transaction Control (TCL)

```sql
-- Mark a savepoint
SAVEPOINT sp1234;

-- Undo all changes since sp1234
ROLLBACK TO SAVEPOINT sp1234;

-- Make all pending changes permanent
COMMIT;

-- Discard all pending changes
ROLLBACK;
```

**A transaction ends with `COMMIT`, `ROLLBACK`, or a DDL/DCL statement.**

```sql
-- Example: safe update with savepoint
UPDATE Students SET grade = 'B' WHERE sid = 200123;
SAVEPOINT sp1234;
INSERT INTO Students VALUES (200999, 'Jon', 'A');
UPDATE Students SET grade = 'A+';   -- oops — updates ALL rows
ROLLBACK TO SAVEPOINT sp1234;       -- undo the bad UPDATE; keep the grade='B' change
COMMIT;                             -- commit the grade='B' UPDATE
```

---

## Concurrency Control

### Locking

The simplest correctness mechanism: before accessing data, a transaction acquires a lock.

**Lock granularity** (from coarsest to finest):

| Level | Scope | Suitability |
|-------|-------|-------------|
| Database | Entire database | Single-user only |
| Table | Entire table | Low concurrency |
| Page | One disk page | Most practical for multi-user |
| Row | One row | High concurrency; many locks |
| Field | One column of one row | Rarely used; impractical overhead |

**Deadlock**: T1 waits for T2 to release a lock; T2 waits for T1. Neither can proceed.  
Prevention: careful lock ordering in code. Detection: timeout; the DBMS kills one transaction and rolls it back.

### Optimistic Concurrency Control (3-Phase Method)

When write conflicts are rare, the cost of locking outweighs its benefit. The optimistic approach assumes bad things won't happen and verifies at the end:

1. **Read phase**: each transaction reads data and makes updates in a *private copy* (not committed to the database)
2. **Validate phase**: check whether the private updates conflict with any other concurrent transaction. If they pass: proceed. If they fail: restart the transaction
3. **Write phase**: commit the validated private copy to the database

Advantage: no lock overhead for read-heavy workloads.  
Disadvantage: wasted work if validation fails frequently.

---

## Recovery

Transactions provide one layer of protection. Additional recovery mechanisms protect against:
- System crash (power failure, OS crash)
- Disk damage
- User mistake
- Cyber attack

**Transaction log:**
- Records every write operation, including before and after values
- Written to disk *before* the commit (write-ahead logging)
- Chained by transaction ID — allows replaying or undoing operations
- Stored on a *separate* device from the database (e.g., backup tape)

**Recovery strategies:**
- **Checkpoint**: periodically record the current committed state to disk; on restart, replay only operations after the last checkpoint
- **Redo/undo**: redo committed but not-yet-persisted writes; undo uncommitted writes

**Rule of thumb:** Prevention is the best medicine — redundant hardware, UPS, RAID, off-site backups, and regular checkpoint intervals reduce recovery time and data loss.

---

## Summary

```
Physical layer (S5):
    Files → pages
    Heap: scan everything
    Sorted: range-friendly
    Index: targeted retrieval
      └── Hash: equality only, O(1)
      └── B+ Tree: equality + range, O(log n), dynamic

Transaction layer (S6):
    ACID: Atomicity + Consistency + Isolation + Durability
    Schedules: serial (safe) → serializable (safe + concurrent)
    Concurrency control:
      ├── Locking (pessimistic): acquires locks; deadlock risk
      └── Optimistic (3-phase): assumes no conflict; validates before commit
    Recovery:
      ├── Transaction log (write-ahead, chained, on separate device)
      └── Checkpoint + redo/undo
```

---

## See Also

- [[concepts/relational-database-fundamentals]] — ACID was introduced here at a high level
- [[concepts/relational-algebra-and-sql]] — SQL TCL commands (COMMIT, ROLLBACK, SAVEPOINT)
- [[concepts/nosql-and-data-warehousing]] — NoSQL trades ACID for availability/scale
- [[concepts/data-structures-fundamentals]] — B-Trees covered from INF1008's algorithmic perspective
- [[sources/INF2003-database-systems]] — Source course
