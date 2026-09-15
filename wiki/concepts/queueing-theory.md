---
type: concept
title: "Queueing Theory for Performance Engineering"
aliases: ["queueing theory", "M/M/c queue", "Kingman formula", "forced flow law", "service demand law", "bottleneck analysis", "interactive response time law", "Sakasegawa", "coefficient of variation", "four sources"]
tags: [queueing-theory, performance-engineering, bottleneck, variability, kingman, operational-laws, interactive-systems, ict3113]
created: 2026-09-14
updated: 2026-09-14
status: established
domain: performance-engineering
address: c-000131
---

# Queueing Theory for Performance Engineering

Queueing theory gives precise, measurable models of how requests accumulate and wait in systems under load. The core insight is that **response time is dominated not by service time but by queueing delay** — and queueing delay depends on three things: utilisation, variability, and number of servers.

This page covers the analytical toolkit introduced in ICT3113 Lec04, building on the M/M/1 single-server model from Lec03.

> "Three levers act on latency: utilisation, service time, and variability. Standard dashboards show only the first two." — A/Prof Donny Soh

---

## 1. Multi-Server Queues (M/M/c)

When a single queue feeds c identical servers, the model becomes **M/M/c**:

- Arrivals: Poisson process, rate λ
- Each server: service rate μ (i.e. average service time S = 1/μ)
- **Traffic intensity per server:** ρ = λ / (c × μ)
- **Stability condition:** ρ < 1, i.e. λ < c × μ

Real-world M/M/c examples: a load balancer feeding c API servers, a thread pool with c workers, c GPUs sharing one request queue.

### One Fast Server vs Many Slow Servers

Given a fixed aggregate capacity (same total throughput), a single server of rate c × μ always gives lower latency than c servers of rate μ:

- At low load: the single fast server processes each job at the full rate c × μ; multiple slow servers each run at μ
- The latency gap narrows at high load but never reverses
- **Real systems still use many servers:** a single device cannot scale up indefinitely, and redundancy matters — one failed server removes 1/c of capacity, not all of it

The case for multiple servers is operational (fault tolerance, cost, scaling limits), not a queueing advantage.

### Worked Example — API Tier

Running case: λ = 8 transactions/s, S = 148 ms per request, c = 3 servers.

| Scenario | Per-server ρ | Mean wait at API queue |
|----------|-------------|----------------------|
| Normal (c = 3) | 8 × 0.148 / 3 ≈ **0.40** | ≈ 7 ms (negligible) |
| One server down (c = 2) | 8 × 0.148 / 2 ≈ **0.60** | ≈ 58 ms (≈ 8× worse) |

The M/M/c arithmetic captures exactly what happens when capacity is reduced: same arrivals, same service time, sharply higher wait because ρ has risen and the non-linear portion of the utilisation curve has been entered.

---

## 2. Operational Laws

When a transaction visits several devices — some multiple times — we need a language for describing multi-device systems. The operational laws provide it.

### 2.1 Visit Counts and the Forced Flow Law

**Visit count Vₖ**: the average number of times one transaction visits device k.

**Forced Flow Law:**
```
Xₖ = Vₖ × X
```

All device throughputs are forced into fixed proportion to the system throughput by the visit counts. If you know X and all Vₖ, you know the throughput at every device.

**Example (E.4.1):** Each web transaction issues 4 SQL queries on average. The web server completes 25 transactions per second.

```
X(db) = V(db) × X = 4 × 25 = 100 queries per second
```

**Running case verification:** V(db) = 4.02 (the extra 0.02 is report queries). At X = 8.06 tps:
```
X(db) = 4.02 × 8.06 ≈ 32.4 qps — exactly what the log shows
```

### 2.2 Service Demand

**Service demand Dₖ**: the total service time one transaction requires at device k across all its visits.

```
Dₖ = Vₖ × Sₖ
```

**Service Demand Law:**
```
Uₖ = X × Dₖ
```

This is the Utilisation Law (U = XS) restated per device using demands instead of per-visit service time. It is the same law, applied systematically.

**Measuring demand without tracing visits:**
```
Dₖ = Uₖ / X
```

This lets you compute demands directly from monitoring data (utilisation and throughput), without needing per-request visit counts.

**Example (E.4.2):** Each of V = 4 queries takes S = 5 ms on average.

```
D(db) = 4 × 5 = 20 ms per transaction
U(db) = X × D = 30 × 0.020 = 0.60 (60%) at 30 tps
```

**Running case — measured demands (BEFORE window):**

| Device | V | S | D | U (at X = 8.06 tps) |
|--------|---|---|---|---------------------|
| API tier (c = 3 servers) | 1.00 | 148 ms | 148 ms | 8.06 × 0.148 / 3 ≈ **0.40 per server** |
| Database (c = 1) | 4.02 | 19.4 ms | 78 ms | 8.06 × 0.078 ≈ **0.63** |
| Storage (c = 2 nodes) | 2.00 | 8.0 ms | 16 ms | 8.06 × 0.016 / 2 ≈ **0.06 per node** |

All match dashboards. Nothing is saturated — yet p95 = 3.5 s. The puzzle is variability (see §5).

---

## 3. Bottleneck Analysis

### 3.1 Capacity Bottleneck vs Congestion Hotspot

Two distinct concepts, often confused:

| Term | Definition |
|------|-----------|
| **Capacity bottleneck** | The device with the lowest throughput ceiling — the one that would saturate first as load increases |
| **Congestion hotspot** | The device where queueing *actually* accumulates. Often the same device, but not always: a station can be the first to cap throughput without ever building a queue, while queueing piles up elsewhere for variability reasons |

### 3.2 Throughput Ceilings

As throughput X rises, every utilisation Uₖ = X × Dₖ rises in proportion to demand. The device with the largest demand reaches saturation first.

**For a single-server device:**
```
X ≤ 1 / Dmax
```

**For a device with c servers:**
```
X ≤ c / D
```

The bottleneck is the device with the **lowest ceiling** — which is not necessarily the one with the largest demand once server counts differ.

**Response time lower bound:** at zero load (no queueing anywhere), a transaction still needs at least its total demand:
```
R ≥ D₁ + D₂ + ... + Dₙ
```
This is the best possible response time — a quick feasibility check before any detailed model.

### 3.3 Worked Example — Running Case (E.4.3 / E.4.4)

Measured demands: API 148 ms, database 78 ms, storage 16 ms.

| Device | Servers | Ceiling | Note |
|--------|---------|---------|------|
| API tier | 3 | 3 / 0.148 ≈ **20.3 tps** | Largest demand, but not the bottleneck |
| Database | 1 | 1 / 0.078 ≈ **12.8 tps** | **Lowest ceiling — capacity bottleneck** |
| Storage | 2 | 2 / 0.016 ≈ **125 tps** | Far from binding |

Minimum response time: R ≥ 148 + 78 + 16 = **242 ms**

A target of 20 tps is infeasible without changing the database — it saturates at 12.8 tps.

**E.4.3 (single-server fab):** Demands: deposition 6.7 h, litho 8.6 h, etch 5.4 h, ion implant 3.2 h, CMP 2.6 h, metrology 1.6 h.

```
Bottleneck = photolithography (largest demand 8.6 h)
X ≤ 1 / 8.6 lots/h = 24 / 8.6 ≈ 2.8 lots/day
```

**E.4.4 (three litho tools, one fails):**

```
c = 3: litho ceiling = 3 / 8.6 ≈ 8.4 lots/day
       new binding ceiling = deposition = 24 / 6.7 ≈ 3.6 lots/day

c = 2 (one tool fails): litho ceiling = 2 / 8.6 ≈ 5.6 lots/day
       still above arrival rate of 3.05 lots/day → no saturation
       rising queue times are a variability effect, not a capacity shortfall
```

### 3.4 Improving the Bottleneck

Because D = V × S, two independent levers reduce demand:

| Lever | Mechanism | Example |
|-------|-----------|---------|
| **Reduce V** | Cache results so fewer requests reach the device | Halving database visits (4 → 2) halves D |
| **Reduce S** | Add an index so each visit completes faster | Index on a hot query column |
| **Add capacity** | Replicas or faster hardware reduce effective D per capacity unit | Read replica for the database |

**Optimisation is iterative:** after fixing one bottleneck, recompute demands — the new bottleneck is now a different device with a new ceiling.

---

## 4. Interactive Systems

### 4.1 Open vs Closed Systems

| Model | Description | Examples |
|-------|-------------|---------|
| **Open system** | Requests arrive from an unbounded external population at rate λ | Web server receiving HTTP requests |
| **Closed system** | Fixed population of N users cycling between thinking and waiting | Load testing tools; database connection pools |

In a closed system, each user alternates between:
- **Thinking** (not using the system) — average duration Z
- **Waiting for a response** — average duration R

### 4.2 Interactive Response Time Law

Apply Little's Law to the entire closed system, users included:

```
N = X × (R + Z)
```

Rearranging:

```
R = N / X − Z
```

**Interpretation:** the tool fixes N (virtual users) and Z (think time), measures X (throughput), and the law gives R (experienced response time). A doubling of N while throughput is capped at the bottleneck ceiling appears entirely as added response time.

**Example (E.4.5):** N = 200 users, Z = 10 s, measured X = 18 tps.

```
R = 200 / 18 − 10 = 11.11 − 10 = 1.11 seconds
```

**Simpler worked case:** N = 100, Z = 5 s, X = 15 tps:

```
R = 100 / 15 − 5 = 6.67 − 5 = 1.67 seconds
```

---

## 5. Variability and the Kingman Formula

### 5.1 Coefficient of Variation

The M/M/1 result assumes Markov (exponential) arrivals and service times. Real workloads differ. The **coefficient of variation** captures how far reality departs from this:

```
C = standard deviation / mean
```

- **Cₐ** — coefficient of variation of inter-arrival times
- **Cₛ** — coefficient of variation of service times

| Value | Interpretation |
|-------|---------------|
| C = 0 | Perfectly regular (deterministic) |
| C = 1 | Markov (exponential) — the M/M/1 assumption |
| C > 1 | Bursty or highly mixed workload |

**Example:** an API serving mostly 20 ms lookups with occasional 5-second report queries has a high Cₛ even though the *mean* service time looks moderate. Averages hide this completely.

### 5.2 The Kingman Formula (G/G/1)

For a **single-server queue** with general arrival and service time distributions:

```
W ≈ [ρ / (1 − ρ)] × [(Ca² + Cs²) / 2] × S
```

Three factors:
1. **Utilisation term** `ρ/(1−ρ)` — the same steep M/M/1 growth; approaches infinity as ρ → 1
2. **Variability term** `(Ca²+Cs²)/2` — scales the entire curve up or down; with Ca = Cs = 1 this is 1 and the formula reduces to M/M/1
3. **Service time** S — anchor for the time scale

> At Ca = Cs = 1 the formula is exact for M/M/1. For other distributions it is an approximation, but a very useful one for first-order reasoning.

### 5.3 Worked Comparison (E.4.6)

Three systems: ρ = 0.8, S = 100 ms. Utilisation term = 0.8 / 0.2 = 4.

| Scenario | Ca² | Cs² | Variability term | W |
|----------|-----|-----|-----------------|---|
| Regular (deterministic) | 0 | 0 | 0 | ≈ **0 ms** |
| Markov (M/M/1) | 1 | 1 | 1 | 4 × 1 × 100 = **400 ms** |
| Mixed workload | 1 | 4 | 2.5 | 4 × 2.5 × 100 = **1,000 ms** |

Same hardware, same load, same average service time: a 2.5× difference in waiting, caused entirely by variance.

**E.4.6:** ρ = 0.9, S = 50 ms. Utilisation term = 9.

```
Ca² = Cs² = 1:  W ≈ 9 × 1 × 50 = 450 ms
Ca² = 1, Cs² = 9:  W ≈ 9 × 5 × 50 = 2,250 ms
```

Same server, same utilisation: five times longer wait purely from service time variance.

### 5.4 Sakasegawa's G/G/c Approximation

For a **multi-server queue** (c > 1), Kingman's single-server formula does not apply. The multi-server extension is:

```
W ≈ [(Ca² + Cs²) / 2] × [ρ^(√(2(c+1))−1) / (c(1−ρ))] × S
```

The same three-factor structure holds — variability term, (modified) utilisation term, service time — but the utilisation term is adjusted for multiple servers. Used as a mechanism-teacher even when its precise assumptions are not fully met.

### 5.5 Variability in Practice

| Situation | Mechanism | Mitigation |
|-----------|-----------|-----------|
| **Mixed workloads** | Long requests queue in front of short ones, inflating wait for all | Separate heavy and light traffic into distinct queues (reduces Cₛ) |
| **Bursty arrivals** | Retry storms, on-the-hour scheduled jobs | Jittered retries, request smoothing (reduces Cₐ) |
| **Headroom rule** | The common 70–80% utilisation ceiling is a variability allowance | Uniform batch jobs can run higher; interactive systems cannot |
| **LLM inference** | Token count per request varies widely → high Cₛ | Continuous batching; separate prefill from decode (variance reduction) |

---

## 6. Four Sources of Performance Problems

Every performance problem in a queuing system traces to one of four root causes. This taxonomy is the diagnostic starting point:

| Source | Formula / Model | Symptom |
|--------|----------------|---------|
| **Demand** | D = V × S — how much work each transaction brings | High utilisation without obvious load; bottleneck shifts unexpectedly |
| **Capacity** | X ≤ c / D — the ceiling the largest demand imposes | Throughput plateaus; adding more load has no effect |
| **Variability** | W ≈ Kingman / Sakasegawa | High response time or tail latency despite moderate utilisation; individual requests vary wildly |
| **Population** | N = X × (R + Z) — number of users cycling | Response time grows with user count even when throughput seems unconstrained |

**Running case diagnosis:** demand unchanged, capacity never binding (db ceiling 12.8 tps, actual X = 8.06 tps), but Cs² ≈ 34 at the database → variability is the root cause of p95 = 3.5 s.

**Fab case diagnosis:** demand unchanged (litho had largest demand all along), capacity reduced (c = 3 → c = 2) but never binding at λ = 3.05 lots/day, variability amplified (high Cₐ ≈ 1.5 from bursty arrivals) → congestion hotspot, not capacity shortfall.

---

## 7. Running Case Study — Online Service

A system with load balancer, three API servers, one database, and two storage nodes. One transaction = 1 API request + 4 DB queries + 2 storage accesses + 2% chance of a report query.

### 7.1 The Diagnosis Problem

At X = 8.06 tps, all utilisations are moderate (API 0.40, DB 0.63, storage 0.06). But p95 = 3.5 s. Dashboard shows nothing alarming.

**The tell:** the database service time distribution reveals two populations separated by two orders of magnitude — standard queries (~5 ms) and report queries (~375 ms) sharing one queue.

```
Cs² ≈ 34 at the database: extreme, arising from the mix, not noise
A report query ≈ 75 standard queries' worth of work
4 quick queries routinely wait behind 1 report
```

Mean DB service time = 19.4 ms. Almost no query actually takes 19.4 ms. Averages hide the structure completely.

### 7.2 The Intervention — Split the Queues

Report queries moved to a read replica (DB-RPT); standard queries keep DB-01.

| Metric | BEFORE | AFTER |
|--------|--------|-------|
| DB-01 utilisation | 0.63 | 0.38 |
| DB-01 Cs² | ≈ 34 | ≈ 0 (collapsed) |
| DB-01 mean wait per query | 165 ms | 5 ms |
| DB-RPT utilisation | — | 0.23 |
| DB-RPT wait | — | ≈ 0.27 s (invisible on a 1.5 s operation) |
| Transaction p95 | 3.48 s | **0.44 s** (8× improvement) |

**Lesson:** attack the variance, not the load. Same total workload; same hardware; dramatically different latency.

### 7.3 Kingman Validation

DB-RPT meets Kingman's assumptions (G/G/1, independent arrivals):

```
Inputs: ρ = 0.23, Ca² = 1.0, Cs² = 0.26, S = 1.43 s
Predicted: W ≈ (0.23/0.77) × (1.0 + 0.26)/2 × 1.43 ≈ 0.30 s
Measured from log: W = 0.27 s (within 8%)
```

The same check on the shared DB-01 (BEFORE window) over-predicts by 2–3×, because in a network the arrivals feed back on themselves — they are not independent. **Kingman is precise for stations meeting its assumptions; a mechanism-teacher everywhere else.**

---

## 8. Capstone Case — Wafer Fab

525 lots processed through 6 steps. Dataset: `fab_cycle_time_2026H1.csv`. Average lot cycle time rose from 1.8 days (January) to 2.2 days (June) despite no change in process recipes.

### 8.1 Demands

| Step | S | V | D |
|------|---|---|---|
| Deposition | 6.3 h | 1.06 (rework) | **6.7 h** |
| Photolithography | 8.3 h | 1.03 | **8.6 h** — largest demand |
| Etch | 5.2 h | 1.04 | **5.4 h** |
| Ion implant | 3.1 h | 1.03 | **3.2 h** |
| CMP | 2.5 h | 1.03 | **2.6 h** |
| Metrology | 1.5 h | 1.04 | **1.6 h** |

Total demand per lot: **28 hours**. Healthy cycle time (January): 43 hours. Even in the healthy period, ~35% of a lot's life was queue time.

### 8.2 LITHO-02 Failure

Photolithography station: M/M/c with c = 3 tools sharing one queue.

From April, LITHO-02 output fell from 30 lots/month to 8 — effectively c = 2.

| | c = 3 | c = 2 |
|--|-------|-------|
| Litho ceiling | 3 / 8.6 ≈ 8.4 lots/day | 2 / 8.6 ≈ 5.6 lots/day |
| Deposition ceiling | 24 / 6.7 ≈ 3.6 lots/day | 3.6 lots/day (unchanged) |
| Arrival rate λ | ≈ 3.05 lots/day | ≈ 3.05 lots/day |

At 3.05 lots/day, no ceiling binds anywhere — the fab does not saturate. LITHO-02's partial failure turned photolithography into a **congestion hotspot** (variability-driven), not a capacity bottleneck.

### 8.3 Why Queueing Tripled

Per-tool ρ rose from 0.36 to 0.54. But the mechanism is variability:

- **Cₐ ≈ 1.5** (bursty arrivals) — mirror image of the online-service case, where Cₛ was high and Cₐ was smooth
- **Cₛ ≈ 0.2** (very regular service — wafer processing is highly controlled)
- Priority discipline: Hot lots averaged 3.2 h in queue; Normal lots averaged 8.0 h

Applying Sakasegawa conceptually: both the utilisation term (ρ jumped when c dropped) and the arrival variability (Cₐ was high throughout) multiplied together to inflate wait time — despite spare capacity in aggregate.

**The diagnostic chain applied to the fab:**
- Demand: unchanged
- Capacity: reduced but never binding at λ = 3.05
- Variability: amplified (high Cₐ, ρ increase in utilisation term)
- Population: open system, not applicable here

---

## Key Connections

- [[concepts/performance-metrics]] — R = W + S; Utilisation Law (U = XS); M/M/1 single-server foundation this page extends; Little's Law (N = X × R used in Interactive Response Time Law)
- [[concepts/performance-engineering]] — measure/model/optimise/deploy loop; bottleneck and variability as the two main optimisation levers
- [[concepts/workload-identification]] — deriving λ and Dₖ from business quantities; the inputs to every model on this page
- [[sources/ict3113-pod-l4]] — source material for this page
- [[areas/performance-engineering]] — parent area
