---
type: concept
title: "N+1 Query Problem (Cause 1: Too Many Queries per Request)"
address: c-000137
aliases: ["N+1", "N plus one queries", "eager loading", "too many queries per request"]
domain: performance-engineering
complexity: medium
status: established
created: 2026-11-19
updated: 2026-11-19
tags: [ict3113, n-plus-one, orm, eager-loading, query-log, hold-time, database]
---

# N+1 Query Problem

**Cause 1 of connection hold time:** a request sends far more queries than its task needs. One query fetches a list, then the code sends one more query per row. Source: [[ict3113-pod-l9-database-request-time]] (slide 7).

## The pattern

```python
orders = db.query('SELECT ... FROM orders WHERE customer_id = ?', cid)
for o in orders:
    o.items = db.query('SELECT ... FROM order_items WHERE order_id = ?', o.id)
```

One query returns 200 orders, then 200 more fetch their items: **1 + 200 = 201 queries** for one request. An ORM (Django ORM, SQLAlchemy, Hibernate) does this by default when code touches `order.items` inside a loop, and generated code often looks correct and passes tests on small data.

## Why plan reading cannot find it

`EXPLAIN` on any one of the 201 queries looks fully optimised: an index lookup returning one row. **The instrument is the query log**, which shows 201 queries for one request. Going straight to the plan is the mistake the lecture warns against ([[connection-pool-diagnosis]] §3).

## What it costs

Each round trip has fixed overhead: the database receives, parses, plans, runs and returns the query. For a one-row lookup, that overhead is larger than the lookup. Travel time then multiplies by N:

| Database distance | Travel for 201 queries |
|---|---|
| Same machine | about 25 ms in total |
| 1 ms away | about 200 ms of travel alone |
| 20 ms away (another region) | about 4 s |

The connection is held for the whole loop, so in `hold ≈ N × t̄ + other` the value of N went from 2 to 201. **Making each query faster does not help**, because the multiplier is the problem.

## The fix

One query that joins, so the database matches rows itself:

```sql
SELECT o.order_id, i.product_id, i.qty
FROM orders o LEFT JOIN order_items i ON i.order_id = o.order_id
WHERE o.customer_id = ?
```

Use `LEFT JOIN` so an order with no items still appears, as it did in the loop. In ORM terms this is **eager loading**. Effect on the pool: with c = 10 and a drop from 400 ms to 40 ms of hold time (200 queries collapsed into 1), the ceiling goes from 25 to 250 req/s ([[ict3113-lec09-worked-examples]] §1).

## Related

- [[n-plus-one-remote-queries-token-usage]] — a real case: 57 users, one serial remote query each, 13.8 s to 3.4 s
- [[query-plans-and-slow-queries]] — cause 2
- [[relational-algebra-and-sql]] — joins
