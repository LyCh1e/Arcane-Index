---
type: concept
title: "Relational Algebra and SQL"
domain: database-systems
course: INF2003
complexity: high
tags: [relational-algebra, sql, ddl, dml, select, join, aggregates, subquery, query-optimisation, group-by]
updated: 2026-05-12
status: established
created: 2026-05-12
---

# Relational Algebra and SQL

**Relational algebra (RA)** is the procedural mathematical foundation for querying relational databases. It defines *how* to retrieve data. **SQL** is the declarative language that sits on top — it defines *what* to retrieve, and the DBMS's query optimiser translates it into an efficient RA execution plan.

> RA is to DBMS what machine code is to a CPU — the internal execution language.

---

## Relational Algebra

### Fundamental Operators (6)

All RA queries can be expressed using these six operators alone.

#### 1. Select — σ (tuple-wise filter)

```
σ_P(r)
```

Returns all tuples in relation `r` where predicate `P` is true.  
Logical operators: `∧` (AND), `∨` (OR), `¬` (NOT).  
Comparison: `=`, `≠`, `<`, `>`, `≤`, `≥`.

```
σ_{location="Winterfell" ∧ YOB>285}(GOT)
```

SQL equivalent: `SELECT * FROM r WHERE P`

#### 2. Project — π (column-wise selection)

```
π_{a,b,...}(r)
```

Returns only the specified columns. Duplicate tuples are **eliminated** (RA operates on sets).

```
π_{Location}(GOT)   -- returns distinct locations
```

SQL equivalent: `SELECT DISTINCT a, b FROM r`

#### 3. Set Union — ∪

```
r ∪ s
```

Returns all tuples from both relations, removing duplicates.  
**Requirement**: `r` and `s` must have the same schema (same attribute names, types, and order).

#### 4. Set Difference — −

```
r − s
```

Returns tuples in `r` that are *not* in `s`. Note: `r − s ≠ s − r`.  
**Requirement**: same schema as union.

#### 5. Cartesian Product — ×

```
r × s
```

Returns all combinations of tuples from `r` and `s` (n_r × n_s tuples).  
If both have attribute `id`, they become `r.id` and `s.id`.  
No schema constraint — unlike union and difference.

#### 6. Rename — ρ

```
ρ_x(E)               -- rename relation E as x
ρ_{x(a1,a2,...)}(E)  -- rename relation and attributes
```

Used to: refer to intermediate results, resolve ambiguities, and self-join (`r × ρ_s(r)`).

---

### Extended Operators

These can be expressed using the fundamental six, but are provided for convenience.

#### Intersection — ∩

```
r ∩ s  ≡  r − (r − s)
```

Returns tuples present in both relations. Same schema requirement as union.

#### Natural Join — ⋈

```
r ⋈ s
```

Joins on *all common attributes* (same name and type), returning one copy of the common columns.

```
r ⋈ s  ≡  π_{S∪T}(σ_{r.A1=s.A1 ∧ … ∧ r.Am=s.Am}(r × s))
```

where `S ∩ T = {A1, …, Am}` are the shared attributes.

#### Outer Joins

Handle "imperfect" matches by padding with NULL instead of discarding non-matching tuples:

| Operator | Symbol | Behaviour |
|----------|--------|-----------|
| **Left outer join** | r ⟕ s | Keep all tuples from `r`; fill missing `s` attributes with NULL |
| **Right outer join** | r ⟖ s | Keep all tuples from `s`; fill missing `r` attributes with NULL |
| **Full outer join** | r ⟗ s | Keep all tuples from both; fill missing values with NULL |

#### Division — ÷

```
r ÷ s
```

Used for "for all" queries. Returns tuples in `r` associated with *every* tuple in `s`.  
Requirement: attributes of `s` are a subset of attributes of `r`.

```
-- Find modules taught in ALL programmes
Modules(module, programme) ÷ AllProgrammes(programme)
```

#### Assignment — ←

Stores an intermediate result in a temporary variable:

```
r1 ← σ_{color='red'}(Parts)
r2 ← r1 ⋈ Catalog
```

Equivalent to SQL CTEs or subqueries. Cuts complex queries into readable steps.

---

### Query Efficiency in RA

**Key principle**: push selections and projections *before* joins to reduce tuple counts early.

```
-- Inefficient: join everything, then filter
π_{name,title}(σ_{dept='ICT'}(instructor ⋈ teaches ⋈ course))

-- Efficient: filter instructor first, then join smaller set
π_{name,title}(σ_{dept='ICT'}(instructor) ⋈ teaches ⋈ π_{course_id,title}(course))
```

---

## SQL

SQL is the universal declarative query language for relational databases. Standardised in 1986 (ANSI), revised through SQL:2019.

### SQL Sublanguages

| Sublanguage | Commands | Purpose |
|-------------|----------|---------|
| **DDL** (Data Definition) | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Define and modify schema |
| **DML** (Data Manipulation) | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Manipulate data |
| **DCL** (Data Control) | `GRANT`, `REVOKE` | Access control |
| **TCL** (Transaction Control) | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Transaction management |

---

### DDL: Defining Schema

```sql
CREATE TABLE Sailors (
    sid     INTEGER,
    name    CHAR(10),
    rating  INTEGER,
    age     INTEGER,
    PRIMARY KEY (sid),
    CHECK (rating >= 1 AND rating <= 10)
);

-- Modify table structure
ALTER TABLE Sailors ADD COLUMN email VARCHAR(100);
ALTER TABLE Sailors DROP COLUMN email;

-- Remove table
DROP TABLE Sailors;
```

**Common data types:**

| Type | Description |
|------|-------------|
| `INT` / `SMALLINT` | Integer values |
| `NUMERIC(p,d)` | Fixed-point: p total digits, d after decimal |
| `REAL` / `DOUBLE PRECISION` | Floating-point |
| `CHAR(n)` | Fixed-length string of n characters |
| `VARCHAR(n)` | Variable-length string, max n characters |
| `DATE` / `TIME` / `TIMESTAMP` | Temporal values |

---

### DML: Manipulating Data

#### INSERT

```sql
-- Full row (column order must match schema)
INSERT INTO Sailors VALUES (74, 'Rusty', 7.5, 35);

-- Partial row (specify columns explicitly)
INSERT INTO Sailors (sid, name, rating) VALUES (75, 'Sandy', 8);
```

#### UPDATE

```sql
UPDATE Sailors
SET rating = 9.5
WHERE sid = 22;
```

#### DELETE

```sql
DELETE FROM Sailors
WHERE sid = 74;
```

#### SELECT

The most important SQL statement. General form:

```sql
SELECT   col1, col2, ...       -- π (project): which columns
FROM     table1, table2, ...   -- relations (implicit cross product)
WHERE    condition              -- σ (select): filter tuples
GROUP BY attributes            -- partition into groups
HAVING   group_condition       -- filter groups
ORDER BY attributes [ASC|DESC];-- sort result
```

- `SELECT *` returns all columns  
- `SELECT DISTINCT` removes duplicates (costly; avoid unless needed)  
- SQL operates on **multi-sets** (bags); RA operates on sets — duplicates are retained unless `DISTINCT` is used

**Arithmetic and aliases:**

```sql
SELECT sid, name, rating / 2 AS new_rating, age
FROM Sailors;
```

**Multi-table queries (implicit join via WHERE):**

```sql
-- Find names of sailors who reserved a red boat
SELECT S.name
FROM Sailors S, Reserves R, Boats B
WHERE S.sid = R.sid
  AND R.bid = B.bid
  AND B.color = 'red';
```

**Explicit JOIN syntax:**

```sql
SELECT S.name, B.color
FROM Sailors S
INNER JOIN Reserves R ON S.sid = R.sid
INNER JOIN Boats B    ON R.bid = B.bid
WHERE B.color = 'red';

-- Left outer join (keep unmatched left rows)
SELECT S.name, R.bid
FROM Sailors S
LEFT JOIN Reserves R ON S.sid = R.sid;
```

---

### Set Operations

```sql
-- UNION (removes duplicates by default)
SELECT name FROM Sailors WHERE rating = 10
UNION
SELECT name FROM Sailors WHERE age < 20;

-- UNION ALL (retains duplicates; faster)
SELECT Name FROM Finance
UNION ALL
SELECT Name FROM HR;

-- INTERSECT (common tuples)
SELECT S1.name FROM Sailors S1, Boats B1, Reserves R1
WHERE S1.sid = R1.sid AND R1.bid = B1.bid AND B1.color = 'red'
INTERSECT
SELECT S2.name FROM Sailors S2, Boats B2, Reserves R2
WHERE S2.sid = R2.sid AND R2.bid = B2.bid AND B2.color = 'green';

-- EXCEPT / MINUS (set difference)
SELECT sid FROM Reserves WHERE bid IN (SELECT bid FROM Boats WHERE color = 'red')
EXCEPT
SELECT sid FROM Reserves WHERE bid IN (SELECT bid FROM Boats WHERE color = 'green');
```

---

### Aggregate Functions

```sql
SELECT COUNT(*)          FROM Sailors;               -- row count
SELECT AVG(age)          FROM Sailors WHERE rating > 8.5;
SELECT MIN(age), MAX(age) FROM Sailors;
SELECT SUM(salary)       FROM Employees;
SELECT COUNT(DISTINCT rating) FROM Sailors;          -- distinct values
```

**Rules:**
- If `SELECT` uses an aggregate, it must *only* contain aggregates — unless `GROUP BY` is used
- Cannot use aggregates in `WHERE` — use a subquery or `HAVING` instead

---

### GROUP BY and HAVING

```sql
SELECT rating, AVG(age) AS avg_age
FROM Sailors
GROUP BY rating
HAVING COUNT(*) > 1;   -- only groups with more than 1 sailor
```

**Evaluation order:**
1. `FROM` + `WHERE` — filter tuples
2. `GROUP BY` — partition into groups
3. `HAVING` — filter groups
4. `SELECT` — compute output per group
5. `ORDER BY` — sort

**NULL in aggregation**: NULL is *ignored* in aggregation functions. `COUNT(*)` counts all rows; `COUNT(col)` ignores NULLs. `SUM`, `AVG`, `MIN`, `MAX` all skip NULLs.

---

### Subqueries (Nested Queries)

```sql
-- Correlated subquery in WHERE
SELECT S.name
FROM Sailors S
WHERE S.sid IN (
    SELECT R.sid FROM Reserves R WHERE R.bid = 103
);

-- Scalar subquery
SELECT S1.name, S1.age
FROM Sailors S1
WHERE S1.age = (SELECT MAX(S2.age) FROM Sailors S2);
```

**Set comparison operators:**

| Operator | Meaning |
|----------|---------|
| `IN` | Value is in the set (= ANY) |
| `NOT IN` | Value is not in the set (<> ALL) |
| `> ANY` / `> SOME` | Greater than at least one value in the set |
| `> ALL` | Greater than every value in the set |
| `EXISTS (...)` | Subquery returns at least one row |
| `NOT EXISTS (...)` | Subquery returns no rows |

**`EXISTS` vs `IN`**: prefer `EXISTS` when checking membership — it short-circuits on the first match rather than scanning the entire subquery result.

---

### Special Values and Operators

**NULL:**
```sql
WHERE age IS NULL        -- correct
WHERE age IS NOT NULL    -- correct
-- WHERE age = NULL      -- WRONG — always evaluates to NULL, never TRUE
```

**LIKE (pattern matching):**
```sql
WHERE name LIKE 'Ja%'    -- starts with 'Ja'
WHERE name LIKE '_i%'    -- second character is 'i'
WHERE name LIKE 'J\_%'   -- literal underscore (escaped)
```
Avoid leading wildcards (`'%abc'`) — cannot use an index.

**ORDER BY:**
```sql
ORDER BY rating ASC, age DESC   -- sort by rating ascending, then age descending
ORDER BY A + B DESC              -- can use expressions
```

---

### CHECK Constraints

```sql
-- Attribute-level (checked on INSERT/UPDATE of that attribute)
CREATE TABLE Sailors (
    sid    INTEGER,
    rating INTEGER CHECK (rating >= 1 AND rating <= 10),
    age    INTEGER CHECK (age > 0)
);

-- Tuple-level (checked whenever any attribute of the tuple changes)
CHECK (rating >= 1 AND rating <= 10 AND age > 0)

-- Domain definition with CHECK
CREATE DOMAIN rtval INTEGER DEFAULT 1
    CHECK (VALUE >= 1 AND VALUE <= 10);
```

---

### SQL Query Optimisation Tips

| Tip | Why |
|-----|-----|
| `SELECT col1, col2` instead of `SELECT *` | Avoids transferring unnecessary data |
| Avoid `SELECT DISTINCT` unless required | Duplicate elimination is expensive |
| Use `UNION ALL` instead of `UNION` when duplicates are acceptable | `UNION` must de-duplicate |
| Keep wildcards at the **end** of `LIKE` patterns (`'Ram%'`, not `'%Ram%'`) | Leading `%` cannot use an index |
| Use `EXISTS` instead of `COUNT(*) > 0` | `EXISTS` stops at first match |
| Replace correlated subqueries with `JOIN` + `GROUP BY` | Joins are processed once; correlated subqueries re-execute per row |
| Choose the correct JOIN type | Avoid implicit cross-products; use `INNER JOIN` with an `ON` condition |
| Use indexes on `WHERE`, `JOIN ON`, and `ORDER BY` columns | See [[concepts/database-indexing-transactions]] |

---

## See Also

- [[concepts/relational-database-fundamentals]] — Relational model, keys, integrity constraints
- [[concepts/database-normalisation]] — FDs and schema refinement using RA theory
- [[concepts/database-indexing-transactions]] — How the DBMS implements RA operators efficiently
- [[concepts/er-diagrams]] — Conceptual design that produces the schemas queried here
