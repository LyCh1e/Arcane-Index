---
type: learning
status: established
title: "INF2003 Database Systems — Exam Study Notes"
domain: database-systems
source: "[[sources/INF2003-database-systems|INF2003 Source]]"
complexity: high
updated: 2026-05-14
tags: [learning, database-systems, exam-prep, sql, normalisation, transactions, indexing, acid]
---

# INF2003 Database Systems — Exam Study Notes

Dense Q&A and definition cards for exam preparation. Covers relational fundamentals, SQL, normalisation, indexing, and transactions.

---

## 1. Foundations

> [!question]- State the ACID properties and define each.
> | Property | Guarantee | Responsibility |
> |----------|-----------|----------------|
> | **Atomicity** | The entire transaction executes or none of it does — no partial commits | DBMS transaction manager |
> | **Consistency** | The database moves from one consistent state to another; all integrity constraints hold | Application programmer |
> | **Isolation** | Concurrent transactions appear to execute serially — no interference | DBMS concurrency control |
> | **Durability** | Once committed, changes survive system crashes | DBMS recovery manager |
> Note: ACID consistency guarantees integrity constraints are satisfied, not that business logic is correct.

> [!question]- State the six stages of database design in order.
> | # | Stage | Activity |
> |---|-------|---------|
> | S1 | **Requirement Analysis** | Gather what data, applications, and operations are needed |
> | S2 | **Conceptual Design** | Build an ER diagram — implementation-independent |
> | S3 | **Logical Design** | Translate ER diagram to relational schemas (tables, keys) |
> | S4 | **Schema Refinement** | Normalise schemas — eliminate redundancy and anomalies |
> | S5 | **Physical Design** | Optimise for hardware: indexes, clustering, partitioning |
> | S6 | **Application & Security Design** | Access control, encryption, backup, authorisation |

> [!question]- What is NULL semantics? Why must you use IS NULL?
> NULL means "unknown" or "inapplicable". Key rules:
> - Any comparison with NULL evaluates to **NULL**, not TRUE or FALSE: `NULL = 5` → NULL; `NULL > 100` → NULL
> - Test for null with `IS NULL` / `IS NOT NULL` — never with `= NULL` (which is always NULL, never TRUE)
> - Aggregation functions (`SUM`, `AVG`, `MIN`, `MAX`, `COUNT(col)`) **ignore** NULLs; `COUNT(*)` counts all rows including those with NULLs

---

## 2. Relational Algebra

> [!question]- Name the six fundamental RA operators, their symbols, and SQL equivalents.
> | Operator | Symbol | Description | SQL Equivalent |
> |----------|--------|-------------|----------------|
> | **Select** | σ_P(r) | Filter tuples where predicate P is true | `WHERE P` |
> | **Project** | π_{a,b}(r) | Return only specified columns; duplicates eliminated | `SELECT DISTINCT a, b` |
> | **Union** | r ∪ s | All tuples from both relations; no duplicates | `UNION` |
> | **Set difference** | r − s | Tuples in r not in s | `EXCEPT` |
> | **Cartesian product** | r × s | All combinations of tuples from r and s | `FROM r, s` (implicit cross join) |
> | **Rename** | ρ_x(E) | Rename relation E as x (and optionally rename attributes) | `AS x` alias |
> Union and set difference require **the same schema** (same attributes, types, order). Cartesian product does not.

> [!question]- What is the key efficiency rule when composing RA queries?
> Push **selections (σ) and projections (π) before joins** to reduce tuple counts early.
> Joining large relations then filtering is far more expensive than filtering first and joining smaller results.

---

## 3. SQL — Full SELECT Syntax and Clause Order

> [!question]- Write the full SQL SELECT syntax in correct clause order.
> ```sql
> SELECT   col1, col2, ...          -- which columns (π)
> FROM     table1, table2, ...      -- source relations
> WHERE    condition                 -- row filter (σ)
> GROUP BY attributes               -- partition into groups
> HAVING   group_condition          -- filter groups (after grouping)
> ORDER BY attributes [ASC|DESC];   -- sort result
> ```
> **Evaluation order**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
> - `HAVING` filters **groups**; `WHERE` filters **rows** — aggregates cannot appear in `WHERE`
> - `SELECT DISTINCT` eliminates duplicates but is expensive; avoid unless required

> [!question]- HTTP methods safe/idempotent — what about SQL HTTP methods? (SQL idempotency)
> *(See INF1005 notes for HTTP. For SQL:)*
> - `SELECT` — read-only, safe
> - `DELETE WHERE pk = x` — idempotent (second delete finds nothing, same end state)
> - `INSERT` — not idempotent (repeated inserts create duplicate rows unless a unique constraint prevents it)
> - `UPDATE … SET x = 5` — idempotent

> [!question]- When must you use HAVING instead of WHERE?
> Whenever the filter condition involves an **aggregate function** (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`). `WHERE` is evaluated before grouping and cannot reference aggregates.
> ```sql
> -- Correct: groups with more than 1 member
> SELECT rating, AVG(age) FROM Sailors
> GROUP BY rating HAVING COUNT(*) > 1;
> -- Wrong: WHERE COUNT(*) > 1  -- syntax error
> ```

---

## 4. Normalisation

> [!question]- Define a functional dependency. How does it differ from observing data?
> A **functional dependency** X → Y means: for any two tuples in the relation, if they agree on X, they must agree on Y. FDs are **constraints on all possible legal instances**, not just the current data. Observing the current data can show an FD does *not* hold; it cannot prove one *does* hold.

> [!question]- State Armstrong's three axioms.
> | Axiom | Statement |
> |-------|-----------|
> | **Reflexivity** | If Y ⊆ X, then X → Y (a set determines any subset of itself) |
> | **Augmentation** | If X → Y, then XZ → YZ for any attribute set Z |
> | **Transitivity** | If X → Y and Y → Z, then X → Z |
> These three rules are **sound and complete** — all valid FDs can be derived from them.

> [!question]- Describe the attribute closure algorithm (X⁺).
> ```
> Input: attribute set X, FD set F
> 1. Split all FDs so each RHS has one attribute
> 2. Result := X
> 3. Repeat until no change:
>       for each FD B → Y in F:
>           if B ⊆ Result then Result := Result ∪ {Y}
> 4. X⁺ := Result
> ```
> Uses: check whether X → Y follows from F (is Y ⊆ X⁺?); find all candidate keys (find K where K⁺ = all attributes).

> [!question]- Define BCNF. How do you test for a violation?
> **Boyce-Codd Normal Form**: for every **non-trivial** FD X → Y in relation R, X must be a **superkey** of R.
> A trivial FD is one where Y ⊆ X.
> **Test**: for each non-trivial FD X → Y, compute X⁺. If X⁺ ≠ all attributes of R, the FD violates BCNF.
> *Example violation*: `Product(name, price, category, color)` with FD `category → color`.
> `category⁺ = {category, color}` ≠ all attributes → BCNF violation.

> [!question]- State the BCNF decomposition procedure.
> ```
> Normalise(R):
>   Find FD X → A where A ∉ X and X is NOT a superkey (violates BCNF)
>   If none: R is in BCNF — done
>   Else:
>     Y = X⁺ (all attributes determined by X)
>     Z = R − X⁺ (remaining attributes)
>     Decompose into R1(X⁺) and R2(X ∪ Z)
>     Recursively Normalise(R1) and Normalise(R2)
> ```
> BCNF decomposition **guarantees lossless join** (the original relation is perfectly reconstructable via natural join) but does **not guarantee dependency preservation** — some FDs may span decomposed relations.

---

## 5. B+ Tree Indexing

> [!question]- State the key structural properties of a B+ tree.
> - **All data entries reside in leaf nodes** — internal nodes are routing keys only
> - All leaves are at the **same level** — the tree is perfectly balanced
> - Leaves are linked in a **doubly-linked list** — enables efficient range scans
> - Each node (except the root) maintains **minimum 50% occupancy**
> - **High fanout** (typically 100+) → shallow tree → few I/Os per operation
> - All operations (search, insert, delete) are **O(log n)**

> [!question]- Describe B+ tree insertion — when and how does a split occur?
> 1. Locate the target leaf and insert the key
> 2. If the leaf is **full**: split into two leaves; **duplicate** the minimum key of the right leaf up into the parent
> 3. If the parent is also full: split the parent and push the median key up (note: internal node pushes up, leaf duplicates up)
> 4. If the root splits: create a new root — the tree grows taller
> Tree height only increases when the root splits.

> [!question]- Describe B+ tree deletion — when does borrowing vs merging occur?
> 1. Locate the target leaf and remove the key
> 2. If the leaf still meets minimum occupancy: done
> 3. If **under-full**: try **borrowing** from the nearest sibling (left sibling preferred); update the separator key in the parent
> 4. If borrowing is not possible (sibling is also at minimum): **merge** the two siblings and **remove** the separator key from the parent
> 5. Propagate merges upward recursively; if the root becomes empty, the tree shrinks in height

> [!question]- Hash index vs B+ tree index — when to use each?
> | | Hash Index | B+ Tree |
> |-|-----------|---------|
> | Equality search | O(1) average | O(log n) |
> | Range search | **Cannot** (hash destroys order) | O(log n + k) |
> | Use when | Only equality lookups needed | Equality and range queries needed |

---

## 6. Transactions and Concurrency

> [!question]- What are the three concurrency anomalies?
> | Anomaly | Description |
> |---------|-------------|
> | **Dirty read** | T1 reads data written by T2 before T2 commits; T2 then rolls back |
> | **Non-repeatable read** | T1 reads a value twice; T2 modifies it between the reads |
> | **Lost update** | T1 and T2 both read-then-write the same value; one update overwrites the other |

> [!question]- Describe the three phases of optimistic concurrency control.
> Used when write conflicts are rare (lock overhead exceeds its benefit):
> 1. **Read phase**: each transaction reads data and makes modifications in a **private copy** — not yet written to the database
> 2. **Validate phase**: check whether the private updates conflict with any concurrently committed transaction. Pass → proceed. Fail → restart the transaction from scratch
> 3. **Write phase**: commit the validated private copy to the actual database
> Advantage: no lock overhead for read-heavy workloads. Disadvantage: wasted work if validation fails frequently.

> [!question]- What is the write-ahead logging rule and why does it matter?
> The **transaction log** records every write (before and after values) and must be written to disk **before** the corresponding data page is committed. This guarantees that if a crash occurs between writing the log and writing the data, the recovery manager can **redo** committed writes or **undo** uncommitted ones to restore a consistent state.
> The log is stored on a separate device from the database to survive disk failure.

---

## Quick Reference

| Concept | Key Rule |
|---------|---------|
| NULL comparison | Always use `IS NULL`, never `= NULL` |
| Armstrong's axioms | Reflexivity, Augmentation, Transitivity |
| BCNF definition | Every non-trivial FD's LHS must be a superkey |
| BCNF decomposition | Lossless join guaranteed; dependency preservation is NOT |
| B+ tree occupancy | Minimum 50% full (root exempt) |
| B+ tree insert | Split leaf upward; internal node pushes median up |
| B+ tree delete | Borrow from sibling first; merge if borrow impossible |
| Write-ahead logging | Log written to disk before commit |

## See Also

- [[concepts/relational-database-fundamentals|Relational Database Fundamentals]]
- [[concepts/relational-algebra-and-sql|Relational Algebra and SQL]]
- [[concepts/database-normalisation|Database Normalisation]]
- [[concepts/database-indexing-transactions|Database Indexing and Transactions]]
