---
type: concept
title: "Connection Pool Diagnosis (Hold Time, Ceiling and Three Causes)"
aliases: ["connection pool sizing", "pool hold time", "slow endpoint diagnosis", "pool as a queue"]
domain: performance-engineering
complexity: high
status: established
created: 2026-11-13
updated: 2026-11-13
tags: [ict3113, connection-pool, hold-time, littles-law, utilisation, diagnosis, stress-test, database, ai-generated-code]
---

# Connection Pool Diagnosis

A database connection pool is a **queue with c servers**. A request borrows a connection, holds it for time S, and returns it. If every connection is held, new requests wait. The same arithmetic as for CPU cores applies, so a stress-test knee can be traced to a cause with three instruments.

Source: Week 12 lab deck for Lecture 08 ([[sources/ict3113-pod-lab-wk12-slow-endpoint]]). Worked numbers: [[examples/ict3113-lab-wk12-slow-endpoint-worked]].

---

## 1. The pool as a queue

| Quantity | Formula | Unit |
|---|---|---|
| Ceiling | c / S | requests per second |
| Utilisation | λ × S / c | dimensionless (state as %) |
| Requests waiting (Little's Law) | λ × wait time | requests |
| Time to get a connection and return it | wait + hold | seconds |
| Connections in use on average | λ × S | connections |

c = pool size, S = **hold time** (borrow to return), λ = arrival rate. Convert milliseconds to seconds before dividing.

## 2. Hold time

```
hold time = sum of query elapsed times + other time while borrowed
          ≈ N × average time per query + other time while borrowed
```

The pool cares about **how long a connection is held, not how much work the database does**. Time spent holding a connection while the application does something else (an HTTP call, a slow computation, waiting on a user) counts in S but costs the database nothing.

## 3. Three causes, three instruments

| Cause | Instrument | What to look at |
|---|---|---|
| 1. Too many queries per request (N too large) | Query log | Number of queries per request and their total time |
| 2. Too much time per query | Plan (`EXPLAIN ANALYZE`) | Slow plan; rows read far above rows returned (a missing index shows as expected versus actual row counts) |
| 3. Other work while holding the connection | Pool metrics | Hold time minus the queries' time |

## 4. The four-step method

1. **Spot the pressure.** Compare the pool with the database. Pool in use at c / c and growing waits, while database CPU is low, means the **pool**, not the database, is the limit.
2. **Find the cause.** Check each cause with its own instrument and compute how much of the hold time each explains.
3. **Choose the fix.** The cause decides the fix. A bigger pool treats the symptom only.
4. **Check the knee moved.** Predict hold time, ceiling, utilisation and wait after the fix, then stress test again and compare with the prediction.

## 5. Why not simply enlarge the pool

A larger pool raises the ceiling (c / S) but leaves S unchanged, so:

- each request still takes as long (latency does not improve);
- connections are still held while idle, which wastes database resources and meets connection limits at the next growth step;
- the fault that caused the long hold is untouched.

*Inference from the lab's own arithmetic:* with the case figures, 30 connections lift the ceiling from 20.8 to 62.5 req/s, which clears a 40 req/s target, but the fix of removing the other work lifts it to 1,000 req/s and also shortens the time a connection is tied up.

## 6. After the fix, the knee moves to the next resource

Removing a bottleneck does not remove limits; it exposes the next one. After the pool stops limiting, candidates are database CPU, application worker threads (in-flight requests = λ × response time, by Little's Law) and the downstream service doing the "other work". Re-measure; do not assume. Compare [[concepts/queueing-theory]] §3.4: optimisation is iterative.

## 7. Link to the Week 11 serialisation fault

[[sources/ict3113-pod-lab-wk11-load-stress]] uses the same logic with c = number of cores: throughput that stops near 1/S while the machine is mostly idle means requests are taking turns. In Week 11 a lock held around the slow hash causes it; in Week 12 a database connection held around non-database work causes it. In both, **a resource is held while slow work that does not need it is done**, and the fix is to shrink the scope of what is held.

## Related pages

- [[concepts/performance-metrics]] — Utilisation Law, Little's Law
- [[concepts/queueing-theory]] — M/M/c queues, Erlang B for finite pools (§9), throughput ceilings (§3.2)
- [[concepts/performance-engineering]] — stress testing, reading the table
- [[concepts/database-indexing-transactions]] — index lookups and transaction boundaries
- [[learning/n-plus-one-remote-queries-token-usage]] — cause 1 in practice
