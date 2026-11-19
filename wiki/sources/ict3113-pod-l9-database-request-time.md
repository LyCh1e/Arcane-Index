---
type: source
title: "ICT3113 POD — L9: Where a Database-Backed Request Spends Its Time"
address: c-000136
domain: performance-engineering
source-type: lecture-slides
course: ICT3113
status: ingested
created: 2026-11-19
updated: 2026-11-19
tags: [ict3113, lecture, connection-pool, hold-time, little-law, n-plus-one, explain-analyze, index, histogram, saga, ai-generated-code]
---

# Source: ICT3113 Lecture 09 — Where a Database-Backed Request Spends Its Time

**File:** `raw/ICT3113 Performance Optimisation and Design - Lec09 Where a Database-Backed Request Spends Its Time.md`
**Presenter:** A/Prof Donny Soh, ICT Cluster, Singapore Institute of Technology
**Type:** 17-slide lecture deck (the printed footers read "x / 21")
**Subtitle:** Three contributors to connection hold time
**Concept pages:** [[concepts/connection-pool-diagnosis]] · [[concepts/n-plus-one-query-problem]] · [[concepts/query-plans-and-slow-queries]] · [[concepts/saga-pattern]]
**Worked numbers:** [[examples/ict3113-lec09-worked-examples]]

> [!key-insight] This is the missing lecture behind the Week 12 lab
> [[sources/ict3113-pod-lab-wk12-slow-endpoint]] says it accompanies "Lecture 08" and relies on connection pools, hold time and three causes, but the vault's `Lec08` file is the Dell Docker and Kubernetes session. This deck supplies that method: pool ceiling `c / S`, hold time, the three contributors with their three instruments, and the four-step method (spot the pressure, find the cause, choose the fix, check the knee moved). The lab's formulas and tables match this deck. The lab's numbering ("Lecture 08") and this file's ("Lec09") differ, so treat the lab and this deck as one topic.

---

## Summary

Lecture 07 tested a service whose data lived in process memory. Once a service uses a database, the stress test usually finds the knee there, because the web tier scales out but there is one database. The lecture asks one question: **where does a database-backed request spend its time and capacity?** Its unit is **hold time**, the time a request keeps a database connection from borrowing it to giving it back.

- Response time at the database tier = **wait time + hold time**. Hold time can be shortened; wait time grows when it is not.
- A pool of `c` connections is a queue with `c` servers: ceiling = `c / S`, utilisation = `λ × S / c`.
- `hold time ≈ N × average time per query + other time while borrowed`, which gives **three contributors**, each with its own instrument and fixes.
- The reflex of a bigger pool raises the ceiling, but it lets more queries run at once and, once the database is the limit, makes every query slower. Shorten hold time first.
- Students will not write SQL; the AI does that. The skill examined is reading the evidence and saying what to change.

## Slide guide

| Slide | Topic | Key content |
|---|---|---|
| 1–2 | Title; the one question | Hold time; wait + hold; three causes of pressure; slide numbers are illustrative unless stated as measured |
| 3 | Web tier scales out, database does not | Three web servers, one database; adding a fourth server sends the database more work, so the knee is usually at the database |
| 4 | The pool is a queue with c servers | Utilisation = λS/c, ceiling = c/S; pool of 10, hold 400 ms gives 25 req/s; three symptoms (low database CPU with rising response time; waits then "could not get connection"; more web servers make it worse) |
| 5 | Little's Law on the pool | Four-row table of pool and hold combinations; 5 waiting at 20 req/s means 250 ms wait; "the pool size is the last knob, not the first" |
| 6 | Hold time and three contributors | Formula; instrument per contributor (query log, plan, pool metrics); count and time multiply, other time adds |
| 7 | Cause 1: too many queries (N+1) | 1 + 200 orders = 201 queries; `EXPLAIN` cannot catch it, the query log can; fix is one `LEFT JOIN` (eager loading); round-trip cost scales with distance |
| 8 | Cause 2: which queries matter | Rank by runs per second × elapsed time per run; top three or four exceed half of database time |
| 9 | How the database runs a query | Parse, optimise, execute; statistics drive the plan; three causes of a slow query (2.1, 2.2, 2.3) |
| 10 | Reading a plan (MySQL 8) | `EXPLAIN ANALYZE`; expected `rows=` vs actual; `actual time=a..b`; own time = finish time minus child's finish time; three questions to ask of any plan |
| 11 | 2.1 Missing index | Table scan 1,500,000 rows; index on `customer_id` 70,000; composite `(customer_id, order_date)` 17,000; indexes slow writes |
| 12 | 2.2 Wrong estimate | Skewed `status` column; expected 300,000, actual 1,200,000; histogram fix; test data must carry the real skew |
| 13 | 2.3 Query the index cannot use | `DATE(col)`, type mismatch, `OFFSET` paging; each with plan sign, fix and rows read |
| 14 | Cause 3: other work while holding the connection | Payment call (300 ms) inside a transaction; split into three steps; 305 ms to 8 ms; ceiling 33 to 1,250 req/s |
| 15 | The saga pattern | Transactions T1..Tn with compensations C1..Cn; trip-booking example; payment as a saga |
| 16 | The method | Spot the pressure, find its cause, choose the fix, check the knee moved; do not go straight to the plan |
| 17 | Summary | One number (hold time), three contributors, three places to look, three fixes |

## Facts worth keeping exact

| Item | Value |
|---|---|
| Ceiling | `c / S` |
| Utilisation | `λ × S / c` |
| Requests waiting | `λ × wait time` |
| Hold time (N similar queries) | `N × average time per query + other time while borrowed` |
| Instruments | Cause 1 query log · cause 2 plan (`EXPLAIN ANALYZE`) · cause 3 pool metrics |
| Ranking queries | runs per second × elapsed time per run (elapsed, not CPU: queries overlap and elapsed includes waiting) |
| Plan own time | node finish time minus its child's finish time (approximate, simple parent and child only) |
| Index cost | every index slows every write to the table |

## Connections to existing wiki pages

- [[concepts/connection-pool-diagnosis]] now has its lecture source (previously the lab deck alone).
- [[concepts/queueing-theory]] and [[concepts/performance-metrics]]: Lecture 04 queue with `c` servers, Little's Law.
- [[concepts/database-indexing-transactions]]: B+ trees and transaction scope (INF2003); this deck uses indexes as a performance lever.
- [[concepts/performance-engineering]]: Lecture 07 stress test and knee; this lecture is "what to do next".
- [[learning/n-plus-one-remote-queries-token-usage]]: a real N+1 case in the Learnix token-usage page.
- [[sources/ict3113-pod-lab-wk12-slow-endpoint]] and [[examples/ict3113-lab-wk12-slow-endpoint-worked]]: the lab that applies this method.

## Gaps and cautions

> [!gap] Slides not in the file
> The footers run from 2 to 17 of **21**, and the file has 17 slides, so printed pages 18 to 21 are absent. Slide 6 says "a later slide covers what changes when the data is huge" (a different scale for cause 2, not a fourth contributor); that slide is not in this file. The "Next" note on the last slide points to LLM inference performance.

- The PDF order differs slightly from the printed footers: the method slide (footer 7) comes after the saga slide (footer 16). The wiki follows PDF order.
- **All figures are illustrative** unless a slide says they were measured (the lecture says so on slide 2). Do not quote them as benchmarks.
- **Syntax:** the plan slides use MySQL 8.0.18 or later; PostgreSQL has `EXPLAIN ANALYZE` with different output, and SQL Server calls it the actual execution plan.
- Exam-style answers should follow the lab's rule: state the unit in every step and say which piece of evidence each conclusion rests on.
