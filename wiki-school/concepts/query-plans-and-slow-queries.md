---
type: concept
title: "Query Plans and Slow Queries (Cause 2: Too Much Time per Query)"
address: c-000138
aliases: ["EXPLAIN ANALYZE", "reading a query plan", "missing index", "histogram statistics", "non-sargable query"]
domain: performance-engineering
complexity: high
status: established
created: 2026-11-19
updated: 2026-11-19
tags: [ict3113, explain-analyze, query-plan, index, statistics, histogram, mysql, database, performance]
---

# Query Plans and Slow Queries

**Cause 2 of connection hold time:** the average time per query is large. The instrument is the **plan** (`EXPLAIN ANALYZE`). Source: [[ict3113-pod-l9-database-request-time]] (slides 8 to 13). Figures are the lecture's illustrative ones.

---

## 1. Which queries matter

A service runs many queries; a few cause most of the work. Rank each query by

```
total elapsed time per second = runs per second × elapsed time per run
```

(elapsed, not CPU: queries overlap and elapsed includes waiting). The top three or four usually exceed half of the database's time; leave the rest alone.

| Query | Runs/s | Per run | Total per second |
|---|---|---|---|
| Get order by id | 500 | 5 ms | 2.5 s |
| List orders for a customer | 50 | 40 ms | 2.0 s |
| Search products | 20 | 15 ms | 0.3 s |
| Monthly revenue report | 0.01 | 3 s | 0.03 s |

The report looks slow but is not the problem. Cutting "get order by id" from 5 ms to 1 ms saves more than cutting the report from 3 s to 0.3 s.

## 2. How the database runs a query

| Parse | Optimise | Execute |
|---|---|---|
| SQL becomes a tree; names are checked | Considers possible plans, estimates the cost of each from **statistics** (row counts, distinct values, sometimes the spread), picks the cheapest estimate | Runs the chosen plan; this is where the time goes |

SQL says *what* is wanted, not *how*. Three causes of a slow query: **2.1 missing index**, **2.2 wrong estimate**, **2.3 query written so the index cannot be used**. The plan tells you which.

## 3. Reading a plan (MySQL 8.0.18 or later)

```
EXPLAIN ANALYZE SELECT order_date, total_amount FROM orders
WHERE customer_id = 7 AND order_date >= '2025-07-01'
-> Filter: order_date >= '2025-07-01'          (rows=50000)  (actual time=4..95 rows=17000 loops=1)
    -> Index lookup on orders (customer_id = 7) (rows=150000) (actual time=4..90 rows=70000 loops=1)
```

- The first `rows=` is the **expected** count; the `rows=` after `actual` is what really came back; `loops=` is how often the step ran; `actual time=a..b` is first row at a ms, last row at b ms.
- The plan is a tree: read from the **most indented** line outward.
- A step's time includes the steps under it, so its own added time is roughly *finish time minus its child's finish time*: Filter 95 − 90 ≈ 5 ms; the index lookup (90 ms) took the time. This is approximate and only this simple for a plain parent and child.
- Expected values come from statistics: 1,500,000 rows ÷ 10 distinct customers = 150,000; a date range covering a third = 50,000.

**Three questions for any plan:**

1. Which step took the time?
2. Why is it slow: full table scan or index? How many rows touched? How many loops? (Here an index was used, but 70,000 rows were read to keep 17,000, so the `order_date` filter should be in the index.)
3. Did the database expect that? Compare the two `rows=` numbers. Here, no harm: an index lookup is right for 150,000 or 70,000.

Plain `EXPLAIN` gives expected numbers without running the query (use it when the query takes an hour). PostgreSQL has `EXPLAIN ANALYZE` with different output; SQL Server calls it the actual execution plan.

## 4. Cause 2.1 — Missing index

An index is an ordered structure with a pointer back to each row, like a phone book. Same query, 1,500,000 orders, this customer has 70,000, 17,000 in the date range:

| Plan | Rows read | Rows kept |
|---|---|---|
| Table scan | 1,500,000 | 17,000 |
| Index on `customer_id` | 70,000 | 17,000 |
| Index on `(customer_id, order_date)` | 17,000 | 17,000 |

Index the columns the query filters or joins on, the most selective first (`customer_id`), then re-run `EXPLAIN ANALYZE`. If the plan still scans, the optimiser thinks a scan is cheaper; find out why before keeping the index. **Cost:** every new row is written into every index, so each index slows writes. Index for the few queries that matter. See [[database-indexing-transactions]] for how a B+ tree works.

## 5. Cause 2.2 — Wrong estimate, wrong plan

Without better statistics, the database estimates rows ÷ distinct values: fine when values are even, wrong when a few dominate. Example: 1,500,000 orders, 5 `status` values, so it expects 300,000 per status; in fact 1,200,000 are `delivered` and 30,000 are `cancelled`.

- For `delivered`, it expects 300,000 and picks an index lookup, which fetches rows one at a time. It gets 1,200,000. A table scan would have been faster.
- Suppose a scan is cheaper above about 750,000 matching rows (half the table). 300,000 favours the lookup; 1,200,000 favours the scan. On the previous slide, 150,000 and 70,000 both sit below the threshold, so the wrong guess did no harm.
- **Sign:** on the slow step, expected `rows=300000` against `actual rows=1200000`.
- **Fix:** tell the database the real spread with a histogram, `ANALYZE TABLE orders UPDATE HISTOGRAM ON status`. It then expects 1,200,000 for `delivered` and 30,000 for `cancelled`, and picks a scan for one and a lookup for the other. Check the plan afterwards.
- **Testing consequence:** test data with every status equally common never shows this. **Test data must carry the real skew.**

## 6. Cause 2.3 — Query written so the index cannot be used

The index exists, but the query defeats it. The plan shows a `Scan` where an index lookup was expected, or a huge `rows=` on an index step. Generated code writes all three by default, and all three pass tests on a 200-row table.

| Written | Plan shows | Why | Fix | Rows read |
|---|---|---|---|---|
| `WHERE DATE(order_date) = '2025-10-15'` | Scan, rows = 1,500,000 | Index stores `order_date`; `DATE(order_date)` is a different value computed per row | `WHERE order_date >= '2025-10-15' AND order_date < '2025-10-16'` | 1,500,000 → 2,000 |
| `WHERE legacy_code = 4242` (column is VARCHAR) | Scan, rows = 5,000 | Number compared with text; every stored string is converted, so index order no longer applies; no error, right rows | `WHERE legacy_code = '4242'` | 5,000 → 1 |
| `ORDER BY order_date LIMIT 20 OFFSET 400000` | Index scan, rows = 400,020 | `OFFSET` produces 400,020 rows and discards 400,000; no way to jump | `WHERE order_date > :last_seen ORDER BY order_date LIMIT 20` | 400,020 → 20 |

## Related pages

- [[connection-pool-diagnosis]] — where cause 2 sits among the three
- [[n-plus-one-query-problem]] — cause 1, which plan reading cannot see
- [[relational-algebra-and-sql]] — SQL background
