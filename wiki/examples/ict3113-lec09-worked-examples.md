---
type: example
title: "ICT3113 Lecture 09 — Worked Numbers (pool ceilings, N+1, query ranking, plans, hold time)"
address: c-000140
domain: performance-engineering
course: ICT3113
status: established
created: 2026-11-19
updated: 2026-11-19
tags: [ict3113, worked-example, connection-pool, little-law, explain-analyze, saga]
---

# Lecture 09 — Worked Numbers

All figures are the lecture's **illustrative** ones ([[sources/ict3113-pod-l9-database-request-time]]). Working checked: every result below was recomputed. State units in every line, as the Week 12 lab requires.

## 1. Pool ceilings (slide 5)

Ceiling = c / S; utilisation at λ = 20 req/s is λ × S / c.

| c | S | Ceiling | Utilisation at 20 req/s | Reading |
|---|---|---|---|---|
| 10 | 400 ms | 10 / 0.4 = 25 req/s | 20 × 0.4 / 10 = 0.80 | Near the ceiling; response time several times S |
| 10 | 100 ms | 100 req/s | 0.20 | Same pool, query made 4× faster |
| 40 | 400 ms | 100 req/s | 0.20 | Pool grew 4×, but 40 queries now run at once on the database; is each still 400 ms? |
| 10 | 40 ms | 250 req/s | 0.08 | 200 queries collapsed into 1 (cause 1) |

Rows 2 and 3 reach the same ceiling by different routes; row 3 works only if the database has headroom. **Little's Law on the wait queue:** 5 requests waiting at 20 req/s means each waits 5 ÷ 20 = **0.25 s = 250 ms** before its first query runs.

## 2. N+1 travel cost (slide 7)

201 queries (1 + 200) at each distance: same machine ≈ 25 ms total; 1 ms apart: 201 × 1 ms ≈ 200 ms; 20 ms away: 200 × 20 ms = 4 s. N went from 2 to 201, so `hold ≈ N × t̄` grew about 100×.

## 3. Ranking queries (slide 8)

Total per second = runs/s × time per run: 500 × 5 ms = **2.5 s**; 50 × 40 ms = **2.0 s**; 20 × 15 ms = 0.3 s; 0.01 × 3 s = 0.03 s. Fix the top two. Values above 1 s per second are possible because queries overlap.

## 4. Plan arithmetic (slides 10 and 11)

- Expected rows: 1,500,000 ÷ 10 customers = 150,000; a date range covering a third: 150,000 ÷ 3 = 50,000. Actual: 70,000 and 17,000.
- Own time of Filter: 95 − 90 = **5 ms**; the index lookup (90 ms) is where the time went.
- Rows read: 1,500,000 (scan) → 70,000 (`customer_id` index) → 17,000 (composite index).

## 5. Wrong estimate (slide 12)

1,500,000 ÷ 5 statuses = 300,000 expected; actual `delivered` = 1,200,000 (80% of the table). With a scan threshold of about 750,000 (half the table), 300,000 chooses the lookup and 1,200,000 should choose the scan.

## 6. Hold time before and after (slide 14)

| | Working | Result |
|---|---|---|
| Before: hold | 2 + 300 + 3 | 305 ms |
| Before: ceiling | 10 / 0.305 | ≈ 32.8 ≈ 33 req/s |
| After: hold | 5 + 3 | 8 ms |
| After: ceiling | 10 / 0.008 | 1,250 req/s |
| Share of 305 ms that is database work | 5 / 305 | ≈ 1.6% |

The 300 ms charge still happens after the fix, so a request's **response time is still about 300 ms or more**; only the connection's hold time fell. The same distinction is made in the Week 12 lab ([[examples/ict3113-lab-wk12-slow-endpoint-worked]]).

## Self-test

1. Pool of 20, hold 250 ms: ceiling? (20 / 0.25 = 80 req/s.)
2. At 60 req/s, how many requests are waiting if each waits 100 ms? (60 × 0.1 = 6.)
3. Which instrument finds 201 queries for one request? (The query log, not the plan.)
4. A plan shows `rows=100000` expected and `actual rows=900000` on the slow step. Which cause, and what fix? (Wrong estimate, 2.2; a histogram, then re-check the plan.)
5. Why is `WHERE DATE(order_date) = '2025-10-15'` slow when `order_date` is indexed? (It computes `DATE()` on every row, so the index order is useless; rewrite as a range on the bare column.)

Related: [[concepts/connection-pool-diagnosis]] · [[concepts/query-plans-and-slow-queries]] · [[concepts/n-plus-one-query-problem]] · [[concepts/saga-pattern]]
