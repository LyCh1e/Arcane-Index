---
type: example
status: established
created: 2026-11-13
updated: 2026-11-13
name: ict3113-lab-wk12-slow-endpoint-worked
description: ICT3113 Week 12 lab (Lecture 08) — all four questions on the slow customer-summary endpoint worked through with units; the pool, not the database, is the limit and 470 of 480 ms of hold time is non-database work
metadata:
  type: example
domain: performance-engineering
course: ICT3113
tags: [ict3113, lab, connection-pool, hold-time, littles-law, utilisation, diagnosis, worked-example]
---

# ICT3113 Week 12 Lab — Diagnosing a Slow Endpoint (Worked Answers)

**Source:** [[sources/ict3113-pod-lab-wk12-slow-endpoint]]
**Method:** [[concepts/connection-pool-diagnosis]]
**Authorship note:** the lab deck contains the questions and data only. The answers below were worked out for the wiki from that data and the deck's reference formulas. They are not an official solution. Statements marked *inference* go beyond the deck.

**Given:** knee 18 req/s; target 40 req/s; database CPU at the knee 22%; pool size c = 10; hold time S = 480 ms = 0.48 s; wait for a connection 310 ms = 0.31 s; 4 queries per request totalling 10 ms; connections in use 10 / 10.

---

## Question 1 — Spot the pressure

| # | Quantity | Working | Answer |
|---|---|---|---|
| 1 | Ceiling of the pool | c / S = 10 / 0.48 s | **20.8 req/s** |
| 2 | Utilisation at the knee | λ × S / c = 18 req/s × 0.48 s / 10 | **0.864 (86.4%)** |
| 3 | Requests waiting for a connection | λ × wait = 18 req/s × 0.31 s | **5.6 requests** |
| 4 | Time from asking for a connection to giving it back | wait + hold = 310 ms + 480 ms | **790 ms** |
| 5 | Resource at its limit | pool 10 / 10 in use with a ceiling of 20.8 req/s just above the 18 req/s knee; database CPU only 22% | **The pool, not the database** |

**Which cause does that point to?** With the database at 22% CPU, the time is not going into database work, so cause 2 (slow queries) is unlikely. Connections are held for long periods without the database being busy, which points to causes 1 or 3. Question 2 separates them.

**Reading note.** The ceiling of 20.8 req/s is only 16% above the knee of 18 req/s. Waiting becomes large well before utilisation reaches 100% (see [[concepts/queueing-theory]]), so a knee at 86% utilisation is expected. The average number of connections in use is λ × S = 18 × 0.48 = 8.6, while the table reports 10 / 10; the table most likely shows the pool state at the knee rather than the average (*inference*).

## Question 2 — Find the cause

| Cause | Evidence | Verdict |
|---|---|---|
| 1. Too many queries | Query log: **N = 4** queries, **10 ms** in total (average 2.5 ms each) | Not the cause. Four queries is few and they take little time |
| 2. Too much time per query | Plan: index lookup via `ix_cust_date`, expected 20 rows and actual 20 rows, **3 ms** | Not the cause. The slowest query reads exactly the rows it returns |
| 3. Other work while holding the connection | Hold time 480 ms − query time 10 ms = **470 ms** other time while borrowed | **Dominant**: 470 / 480 = 98% of hold time |

Check with the formula: hold ≈ N × average time per query + other time = 4 × 2.5 ms + 470 ms = **480 ms**.

**Dominant cause: 3.** The deck does not say what the other work is. Since the endpoint includes a payment check, the likely candidate is that check running while the connection is held (*inference*).

## Question 3 — Choose the fix

### 3.1 What to ask the AI to change

Move the non-database work (the payment check) **outside the borrowed connection**: borrow the connection, run the queries, return it, then do the other work, or do the other work before borrowing at all. The deck's own wording is that the transaction must be able to end before the payment check.

Business rules to preserve, and how to check that the transaction can safely end first (*inference from the deck's questions*):

- Does the payment check need anything read inside the transaction that could change before it finishes? If it does, read and copy that data first.
- Does any later write depend on the payment result? If so, make it a separate short transaction after the check.
- Does the `UPDATE customers SET last_seen` have to be atomic with the reads or with the payment outcome? If not, it can commit immediately.
- Verify with tests that response bodies and stored data are identical before and after the change, and that a failed payment check still produces the same result for the caller.

### 3.2 A teammate proposes a pool of 30 (no code change)

| Quantity | Working | Answer |
|---|---|---|
| Ceiling | 30 / 0.48 s | **62.5 req/s** |
| Utilisation at 40 req/s | 40 req/s × 0.48 s / 30 | **0.64 (64%)** |

### 3.3 Does a pool of 30 reach 40 req/s, and what does it not fix?

On the pool alone, **yes**: the ceiling of 62.5 req/s is above 40 req/s and utilisation is 64%. It does not fix:

1. **Per-request latency.** Each request still holds a connection for about 480 ms, so the request still takes about 480 ms or longer.
2. **The cause.** Connections are still tied up doing non-database work. Thirty connections are held mostly idle instead of ten, which uses more database connections for no extra work, and the ceiling is still only 62.5 req/s.

## Question 4 — Check the knee moved

Assume the other work runs outside the connection, so other time while borrowed drops from 470 ms to 0 ms. Pool size stays at 10.

| # | Prediction | Working | Answer |
|---|---|---|---|
| 1 | Average hold time | 4 × 2.5 ms + 0 ms | **10 ms** |
| 2 | Ceiling of the pool | 10 / 0.010 s | **1,000 req/s** |
| 3 | Utilisation at 40 req/s | 40 req/s × 0.010 s / 10 | **0.04 (4%)** |
| 4 | Average wait for a connection | utilisation 4%, so queueing is negligible | **about 0 ms** |

Connections in use on average: 40 × 0.010 = 0.4 of 10.

**5. Does one request now finish in about 10 ms?** **No.** The 10 ms is only the time the connection is held. The 470 ms of other work still has to happen on the request's path, so the end-to-end response time stays at about 480 ms (10 ms of queries plus 470 ms of other work, with no waiting for a connection). The fix raises capacity; it does not shorten that work.

**6. Where does the knee go, and how to check?** The pool no longer limits (ceiling 1,000 req/s against a target of 40), so the knee moves to whichever resource is next. Two candidates (*inference*):

- **Database CPU:** 22% at 18 req/s is about 1.2% per req/s; if it scales linearly, 40 req/s would use about 49%. That is below saturation.
- **Application worker threads or the payment service:** in-flight requests = λ × response time = 40 × 0.48 = about 19 requests, so the application needs at least about 20 concurrent workers, and the downstream service must sustain 40 req/s.

**Check:** repeat the same stress test and compare with the prediction in the pool metrics (hold time about 10 ms, wait about 0 ms, connections in use well below 10 / 10), confirm the knee has moved to at least 40 req/s, and identify which resource limits next.

---

## Lessons

- **A low database CPU with a full pool is the signature of a pool problem, not a database problem.**
- **Hold time includes everything done while borrowed.** The database's share (10 ms) can be a tiny fraction of it (480 ms).
- **Always carry units.** Mixing ms and s in c / S is the commonest error in this lab.
- **A prediction before the re-test is the point.** The lab asks for the predicted pool metrics first so that a mismatch after the fix shows something unexpected.
