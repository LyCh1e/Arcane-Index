---
type: example
status: established
created: 2026-09-24
updated: 2026-09-24
name: ict3113-t05-worked-examples
description: ICT3113 Tutorial Week 05 — worked problems on performance basics from a job log, throughput/response-time bounds, MapReduce execution model, and Erlang B connection pool sizing with full recursion
domain: performance-engineering
course: ICT3113
address: c-000127
tags: [ict3113, performance-engineering, performance-bounds, erlang-b, execution-models, mapreduce, utilisation-law, littles-law, worked-examples, tutorial]
---

# ICT3113 Tutorial Week 05 — Worked Examples

**Source:** [[sources/ict3113-pod-t05]]  
**Concepts:** [[concepts/performance-metrics]] · [[concepts/queueing-theory]] · [[concepts/performance-engineering]]

---

## Q1 — Performance Basics from a Job Log

Five requests in window [0, 10 s]:

| Job | S (s) | R (s) |
|-----|-------|-------|
| 1 | 3 | 4 |
| 2 | 1.5 | 2 |
| 3 | 0.5 | 2 |
| 4 | 2 | 3 |
| 5 | 1 | 3 |

| Quantity | Formula | Result |
|----------|---------|--------|
| Average service time S | (3+1.5+0.5+2+1)/5 | **1.6 s/job** |
| Service rate μ | 1/S | **0.625 jobs/s** |
| Average response time R | (4+2+2+3+3)/5 | **2.8 s/job** |
| Arrival rate λ | 5 jobs / 10 s | **0.5 jobs/s** |
| Interarrival time | 1/λ | **2 s** |
| Throughput X | 5 jobs / 10 s | **0.5 jobs/s** |

*X = λ* because every job completed inside the window.  
*Waiting time:* W = R − S = 2.8 − 1.6 = **1.2 s/job**.  
*Utilisation:* U = X × S = 0.5 × 1.6 = **80 %**.

---

## Q2 — Performance Bounds (5-Device System)

| Device | Vᵢ | Sᵢ (ms) | Dᵢ = Vᵢ × Sᵢ (ms) |
|--------|-----|---------|-------------------|
| 1 | 2 | 15 | 30 |
| 2 | 3 | 10 | 30 |
| 3 | 1 | 30 | 30 |
| 4 | 4 | 10 | **40** ← D_max |
| 5 | 1 | 25 | 25 |
| **Σ** | | | **155** |

**R_min = Σ Dᵢ = 155 ms** (best-case response time, no queueing anywhere).  
**X_max = 1 / D_max = 1 / 0.040 = 25 requests/s** (Device 4 is the bottleneck).

At X = 25 req/s: Device 4 at 100 %; Devices 1–3 at 75 %; Device 5 at 62.5 %.

---

## Q3 — Execution Model: MapReduce

n = 8 processors, r = 100,000 records.  
Three phases (Map and Reduce are serial; Compute is parallel):

| Phase | Formula | Value |
|-------|---------|-------|
| Map (partition) | r × (15 ms / 1,000) | 1,500 ms |
| Compute (parallel) | (r/n) × 0.1 ms | 12,500 × 0.1 = **1,250 ms** |
| Reduce | n × 1 ms | **8 ms** |
| **Total S** | | **2,758 ms ≈ 2.76 s** |

**General formula (n processors, r records):**

```
S(n, r) = 0.015r  +  0.1r/n  +  n    [ms]
           ↑ Map      ↑ Compute  ↑ Reduce
```

> [!key-insight] Optimal processor count
> The partition term (0.015r) is serial — a floor independent of n. The reduce term grows with n. Minimising: dS/dn = −0.1r/n² + 1 = 0 → **n* = √(0.1r)**  
> For r = 100,000: n* = √10,000 = **100 processors** (beyond this, extra processors increase total time).

---

## Q4 — Erlang B: Connection Pool Sizing

λ = 15 req/s, S = 50 ms, target loss ≤ 0.1 % = 0.001.

**ρ = λ × S = 15 × 0.050 = 0.75 Erlangs**

Applying the recursion B(m) = ρ B(m−1) / (m + ρ B(m−1)), B(0) = 1:

| m | Working | B(m, 0.75) |
|---|---------|------------|
| 0 | — | 1.000000 (100 %) |
| 1 | 0.75×1 / (1 + 0.75×1) | **42.857 %** |
| 2 | 0.75×0.42857 / (2 + 0.75×0.42857) | **13.846 %** |
| 3 | 0.75×0.13846 / (3 + 0.75×0.13846) | **3.346 %** |
| 4 | 0.75×0.03346 / (4 + 0.75×0.03346) | **0.623 %** |
| 5 | 0.75×0.00623 / (5 + 0.75×0.00623) | **0.093 %** ✓ ≤ 0.1 % |

**Answer: m = 5 connections.**

With 4 connections: 0.623 % > 0.1 % — more than six times the target.  
Refused rate at m = 5: 15 × 0.00093 ≈ **0.014 req/s** (about 1 in 1,070).
