---
type: source
title: "ICT3113 POD — Week 12 Lab (Lec08): Diagnosing a Slow Endpoint"
domain: performance-engineering
source-type: lab-handout
course: ICT3113
status: ingested
created: 2026-11-13
updated: 2026-11-13
tags: [ict3113, lab, connection-pool, hold-time, little-law, diagnosis, query-log, explain-analyze, ai-generated-code]
---

# Source: ICT3113 Week 12 Lab (Lecture 08) — Diagnosing a Slow Endpoint

**File:** `raw/ICT3113 Performance Optimisation and Design - Lec08 Week 12 Lab Diagnosing a Slow Endpoint.md`
**Presenter:** A/Prof Donny Soh, ICT Cluster, Singapore Institute of Technology
**Type:** 8-slide pen-and-paper lab with no code to run
**Worked answers:** [[examples/ict3113-lab-wk12-slow-endpoint-worked]]
**Method page:** [[concepts/connection-pool-diagnosis]]

> **Gap:** the lab says "answer using the Lecture 08 content", but Lec08 in the vault is the Dell "Learning Docker & Kubernetes Fundamentals – Intro" session ([[sources/ict3113-pod-lec11-12-kubernetes-docker]]). It contains nothing on connection pools, hold time, query logs or `EXPLAIN ANALYZE`, so the pool, hold-time and three-causes method has no source in the vault except this lab deck. It may have been taught live or in material not yet added. Everything on this page comes from the lab deck and its reference slide.

---

## Summary

A single case, an **AI-generated endpoint** `GET /customers/{id}/summary` that returns a customer's recent orders with a payment check, is used for four questions that follow the four steps of the Lecture 08 method: **spot the pressure, find its cause, choose the fix, check the knee moved**. The stress test put the knee at **18 req/s** against a target of **40**, with database CPU at only **22%**.

## Ground rules

1. Read the case first; all four questions use it.
2. Use the Lecture 08 formulas (reference slide).
3. **State the unit in every answer and every step of the working.** An answer without units is incomplete.
4. Say which piece of evidence each conclusion rests on. "The method matters more than the final number."

## The case data

| Evidence | Value |
|---|---|
| Knee / target | 18 req/s / 40 req/s |
| Database CPU at the knee | 22% |
| Query log (one request) | 4 queries: `customers` lookup, `orders` (latest 20), `order_items` (`IN` list), `UPDATE customers SET last_seen`; **10 ms** of database time |
| Pool size | 10 |
| Average hold time | 480 ms |
| Average wait for a connection | 310 ms |
| Average query time per request | 10 ms |
| Connections in use | 10 / 10 |
| Plan of the biggest query | Index lookup on `orders` using `ix_cust_date`; expected 20 rows, actual 20, **3 ms** |

The three instruments are labelled by what each one is: the query log lists every query one request sent, the pool metrics are **averages over the stress test at 18 req/s** (pool size is c, hold time is S), and the plan is `EXPLAIN ANALYZE` on the slowest of the four queries.

## The four questions

| Question | Task |
|---|---|
| 1. Spot the pressure | From the pool metrics compute the pool ceiling, utilisation at the knee, requests waiting, and the total time from asking for a connection to returning it. Decide which resource is at its limit, the database or the pool |
| 2. Find its cause | Use query log (cause 1), plan (cause 2) and pool metrics (cause 3) to decide which cause is dominant |
| 3. Choose the fix | What to ask the AI to change, which business rules must hold, how to check the transaction can end before the payment check; why a pool of 30 is not the answer; two things it does not fix |
| 4. Check the knee moved | Predict hold time, ceiling, utilisation at 40 req/s and wait after the fix; explain whether one request now finishes in about 10 ms; predict where the knee goes and how to check |

## Reference slide

| Quantity | Formula |
|---|---|
| Utilisation | λ × S / c |
| Ceiling | c / S |
| Little's Law | requests waiting = λ × wait time |
| Hold time | sum of query elapsed times + other time while borrowed |
| Hold time, N similar queries | N × average time per query + other time while borrowed |

| Cause | Instrument |
|---|---|
| 1. Too many queries per request | Query log |
| 2. Too much time per query | Plan (`EXPLAIN ANALYZE`) |
| 3. Other work while holding the connection | Pool metrics |

Notation: c pool size, S hold time (borrow to return), λ arrival rate, N queries per request.

## Related pages

- [[examples/ict3113-lab-wk12-slow-endpoint-worked]] — all answers worked through with units
- [[concepts/connection-pool-diagnosis]] — the reusable method
- [[sources/ict3113-pod-lab-wk11-load-stress]] — the previous lab, which finds a serialisation fault with the same c/S arithmetic
- [[concepts/queueing-theory]] — M/M/c, ceilings and bottleneck analysis
- [[concepts/performance-metrics]] — Little's Law, Utilisation Law
- [[concepts/database-indexing-transactions]] — indexes and transaction scope
- [[learning/n-plus-one-remote-queries-token-usage]] — a related "too many queries per request" case (cause 1)
