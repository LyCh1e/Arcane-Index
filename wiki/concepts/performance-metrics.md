---
type: concept
title: "Performance Metrics"
domain: performance-engineering
complexity: high
status: established
created: 2026-08-31
updated: 2026-08-31
tags: [performance-metrics, response-time, throughput, utilisation, percentiles, tail-latency, utilisation-law, queueing, little-s-law, ict3113]
---

# Performance Metrics

Performance metrics are the quantitative vocabulary of performance engineering. This page covers what makes a good metric, the three classes of performance metrics, and the core operational laws used to relate them.

---

## What Is a Metric?

A metric requires three things:
1. A **standard** (unit) — agreed upon and documented
2. A **measurement method** — reproducible
3. A **consistent definition** — same across all systems being compared

**Mars Climate Orbiter case study**: ground software supplied navigation data in pound-force seconds (imperial); the NASA system expected newton-seconds (SI). A unit mismatch at a system boundary destroyed a $327.6M spacecraft. The discrepancy had been noticed but the project's processes did not resolve it.

---

## Properties of Good Performance Metrics

Six properties required of any performance metric (Lilja 2000, cited by Bondi 2014):

| Property | Definition | Violated when… |
|----------|-----------|---------------|
| **Linearity** | Responds linearly to the phenomenon measured | A 2× resource increase produces a 0.1× improvement |
| **Reliability** | If metric says A > B, A genuinely outperforms B | Metric consistently favours System A; System B wins in practice |
| **Repeatability** | Same result under same conditions | Two identical runs give different scores |
| **Ease of measurement** | Easily computed | Requires full distribution to compute (percentile harder than mean) |
| **Consistency** | Same definition everywhere it is used | Different labs compute "the same benchmark" differently |
| **Independence** | Not shaped by vendors whose systems it compares | Benchmark co-designed by one of the vendors under test |

---

## Three Classes of Performance Metrics

| Class | Counted at | Key metric | Description |
|-------|-----------|-----------|-------------|
| **Outcome / User Experience** | Between entrance and exit | Response Time R | Time from request initiation to completion |
| **Demand** | Entrance | Arrival Rate λ | Units of work offered per unit time |
| **Supply** | Exit / device | Throughput X, Utilisation U | Work completed per unit time; proportion of device busy |

---

## Response Time

**R = W + S**

| Component | Symbol | Definition |
|-----------|--------|-----------|
| Wait time | W | Time request spends waiting for the system to be available |
| Service time | S | Time system spends actively processing the request |
| Response time | R | Total elapsed time from initiation to completion |

For end-to-end requests, R also includes network and communication delays.

### W/S/R Classification Exercises (Lec01)

These exercises build the habit of correctly identifying what counts as service time versus wait time — a common exam trap.

**Exercise A — Larry the Procrastinator**

The instructor is the client; Larry is the server. *Service time* = only the time Larry spends actively working on the lab. Everything else is wait time.

| Activity | Type |
|----------|------|
| Going to washroom, combing hair, setting up laptop | Wait (W) |
| Working on Lab Part 1 (2 min) | Service (S) |
| Interruption / distraction | Wait (W) |
| Working on Lab Part 2 (8 min) | Service (S) |
| After submission | Not counted (outside response window) |

Service time S = 2 + 8 = **10 min**. Response time runs from "request issued" to "lab submitted." Time elapsed after the response is complete is not part of R.

**Exercise B — Healthcare: Polyclinic Visit**

| Phase | Duration | Type |
|-------|----------|------|
| Queue before registration | 25 min | Wait (W) |
| Doctor consultation | 10 min | Service (S) |
| Waiting for results / next stage | 15 min | Wait (W) |
| Follow-up procedure | 5 min | Service (S) |
| **Total (R)** | **55 min** | — |

- Service time: 10 + 5 = **15 min**
- Wait time: 25 + 15 = **40 min**
- Proportion of visit spent waiting: 40 / 55 ≈ **73%** — a queue-dominated experience

**Key insight — service time reduction propagates to wait time:** If consultation drops from 10 to 7 minutes, the doctor is free 3 minutes sooner; each subsequent patient enters service earlier; the queue drains faster. The reduction in wait time across all patients exceeds the 3-minute cut in service time. This is why service-time optimisation matters even in queue-dominated systems.

> "If you reduce the consultation time, it's not necessarily that you only reduce by those minutes — if you reduce this, you actually can reduce the wait as well. That is one thing that many people don't realise." — A/Prof Donny Soh

### User Perception Thresholds (Miller 1968; Nielsen 1993)

| Response Time | User Perception |
|--------------|----------------|
| ≈ 0.1 s | Feels instantaneous; no feedback needed |
| ≈ 1 s | Delay noticed; user's flow of thought largely maintained |
| ≈ 10 s | Attention hard to keep; show a progress indicator |

*Historical usability heuristic, not a universal law.*

---

## Percentiles and Tail Latency

A real system produces a **distribution** of response times — not a single number. Distributions of response times are **right-skewed**: most requests are fast; a small number are very slow (due to cache misses, garbage collection pauses, retries, queueing spikes).

| Statistic | Use |
|-----------|-----|
| **Mean** | Pulled up by slow outliers; hides tail behaviour |
| **p50 (median)** | Describes the typical request |
| **p95** | 95% of requests complete within this value |
| **p99** | 99% of requests complete within this value; "the tail" |

**Definition**: the p-th percentile is the value below which p% of observations fall.

Latency objectives are stated as percentiles: "p99 < 200 ms." This is more meaningful than "average < 200 ms" because averages can mask severe tail behaviour.

**Consistency note**: nearest-rank and linear interpolation methods both compute percentiles but give different values. Agree the method before comparing systems.

**Ease of measurement note**: a mean requires only a running sum and count. A percentile requires the full distribution to be retained.

### SLI / SLO / SLA

| Term | Definition |
|------|-----------|
| **SLI** (Service Level Indicator) | The metric being measured — e.g. p99 response time |
| **SLO** (Service Level Objective) | The target value — e.g. p99 < 200 ms |
| **SLA** (Service Level Agreement) | A formal agreement that may carry objectives and consequences for breach |

### Percentile Exercise — SLO Selection (Lec01)

Ten response-time samples collected from a real system. Sorted ascending, they yield:

| Statistic | Value | Notes |
|-----------|-------|-------|
| Mean | 298.3 ms | Pulled high by slow outliers; misrepresents typical experience |
| P50 (median) | 111 ms | Mean of the 5th and 6th sorted values — the "typical" request |
| P90 | 120 ms | 9th sorted value — the upper bound for 90% of requests |

**SLO selection logic:**

- The mean (298.3 ms) is not a useful SLO: it overstates what most users experience and hides the tail.
- The median (P50 = 111 ms) describes the typical request but makes no commitment about the 50% above it.
- **P90 (120 ms)** is the defensible choice: it commits that 90% of users receive a response within 120 ms and makes the tail explicitly visible.

> "You want to guarantee that 90% of your customers are happy — then 120 will be your service level objective."

Note that P90 and P50 are close here (111 vs 120 ms), implying a tight distribution for most requests — the high mean is driven by a small number of extreme outliers in the top decile.

### Why the Tail Matters

**Reason 1 — Fan-out**: one user-visible request may trigger many backend calls, and the user waits for the **slowest** one.

```
P(at least one of N calls slower than its p99) = 1 − (1 − 0.01)^N
```

For N = 100 independent calls: P ≈ 1 − 0.99¹⁰⁰ ≈ **63%** — the majority of user-visible page loads hit the tail.

**Reason 2 — Heavy users**: users who generate the most requests encounter the tail most frequently — and these are typically the highest-value users.

*(Kleppmann 2017)*

---

## Demand Metrics: Arrival Rate (λ)

**Arrival rate λ**: units of work offered to the system per unit time, **counted at the entrance** (not the exit).

- λ can exceed capacity (the system queues or drops work)
- When λ > μ: throughput X caps at μ, WIP grows, response time climbs indefinitely

### Arrival Rate Exercises (Lec01)

**Exercise A — Larry's Labs (Student Context)**

Larry is enrolled in 4 modules, each with 1 lab per week. Arrival rate = 4 labs/week. In weeks 9–12, a 5th lab per week is added.

| Metric | Value |
|--------|-------|
| Normal arrival rate (demand) | 4 labs/week |
| Weeks 9–12 arrival rate | 5 labs/week |
| Maximum throughput | 5 labs/week |
| Total expected demand (trimester) | 48 labs |
| Total actually completed | 44 labs |
| Shortfall | 4 labs (≈ 8.3%) |

Throughput (44) < demand (48): X < λ. The system fell behind. The shortfall is not dropped work but deferred work — WIP grows, and average response time per outstanding lab increases.

**Exercise B — Semiconductor Factory**

Factory target: 1,200 units/day × 5 days = 6,000 units/week.

| Day | Condition | Output |
|-----|-----------|--------|
| Monday–Tuesday | Full capacity | 2,400 |
| Wednesday | Machine breakdown — half capacity | 600 |
| Thursday–Friday | Overtime (1,400/day) | 2,800 |
| **Total** | | **5,800 units (approx)** |

- Reported total (transcript figure): approximately **5,008 units**
- Average throughput: ≈ **1,001 units/day** (target: 1,200/day)
- Shortfall: ≈ 992–1,000 units (≈ 16–17%)

Key lesson: overtime partially compensates but cannot recover time already lost. A one-day breakdown at half capacity removes 600 units; overtime at +200 units/day over two days recovers only 400. The gap persists regardless of effort expended after the fact.

> "You can tell how bad the situation is — if a machine breaks down, immediately there's a shortfall, even though they try to compensate by doing overtime."

---

## Supply Metrics: Throughput and Utilisation

**Throughput X**: units of work **completed** per unit time, **counted at the exit**.
- X never exceeds the service rate μ (capacity of the server)
- Overtime raises μ (increases the denominator of service time); it does not allow X to exceed the new μ

**Utilisation U**: proportion of time a device is busy, or the fraction of capacity in use.

### Supply Metric Sub-categories

| Resource | Metrics |
|---------|--------|
| **CPU** | CPU time (seconds), CPU utilisation (%) |
| **Memory** | Amount of virtual memory allocated; paging activity rate |
| **Disk** | Busy time, idle time, transfer rate (MB/s) |
| **Network** | Bandwidth (link capacity, bps); Observed throughput (bytes/s); Packets/s |
| **Energy / Power** | Energy: joule (J), Wh, kWh; Power: watt (W) |

---

## Performance Modelling Basics

The vocabulary for queueing analysis:

| Symbol | Name | Definition |
|--------|------|-----------|
| λ | Arrival rate | Jobs offered per unit time — demand at the entrance |
| Interarrival time | — | Elapsed time between successive arrivals |
| S | Service time | Time the server spends processing one job (not including wait) |
| X | Throughput | Jobs completed per unit time — supply at the exit |
| μ | Service rate / capacity | μ = 1/S for a single continuously busy server |
| U | Utilisation | Fraction of time the server is busy |

### Observation Boundary Effect

In a long-running stationary workload: mean interarrival time ≈ 1/λ.

In a **short finite trace**, the sample mean of observed interarrival gaps ≠ 1/λ because the observation boundaries affect the count of arrivals. Always report which calculation you are using when these diverge.

### Worked Example A — 10-second window (Lec02)

Four jobs in the interval [0, 10] s (arrivals at t = 0, 1, 3, 5; service FIFO):

| Job | Wait (W) | Service (S) | Response (R) |
|-----|----------|------------|-------------|
| A | 0 | 2 | 2 |
| B | 1 | 4 | 5 |
| C | 3 | 1 | 4 |
| D | 2 | 3 | 5 |

| Metric | Value |
|--------|-------|
| λ = 4/10 | 0.4 jobs/s |
| Mean observed gap = (1+2+2)/3 | 1.67 s |
| 1/λ | 2.5 s ← not equal to mean gap |
| Mean S = 10/4 | 2.5 s |
| μ = 1/S | 0.4 jobs/s |
| U = XS = 0.4 × 2.5 | **1.0 — saturated** |

The server is busy for all 10 seconds; 3 of 4 jobs waited.

**Why mean gap ≠ 1/λ**: the three observed gaps span t = 1 to t = 5 (not the full 10-second window). 1/λ accounts for the full interval; the sample mean of gaps does not. In a long-running stationary workload the two converge; in short finite traces they routinely diverge.

### Worked Example B — 20-second window (Lec03 API Server)

Single-server system. Requests arrive at t = 0, 2, 9, 12 over a 20-second observation window. Server processes FIFO.

| Request | Arrives | Starts service | Ends | W | S | R |
|---------|---------|----------------|------|---|---|---|
| A | 0 | 0 | 3 | 0 | 3 | 3 |
| B | 2 | 3 | 8 | 1 | 5 | 6 |
| C | 9 | 9 | 13 | 0 | 4 | 4 |
| D | 12 | 13 | 15 | 1 | 2 | 3 |

| Metric | Calculation | Value |
|--------|-------------|-------|
| λ | 4 / 20 s | **0.2 jobs/s** |
| Mean observed gap | (2 + 7 + 3) / 3 | **4 s** |
| 1/λ | 1 / 0.2 | **5 s** ← diverges from mean gap |
| Mean S | 14 / 4 | **3.5 s** |
| μ = 1/S | 1 / 3.5 | **2/7 jobs/s ≈ 0.286/s** |
| U | 14 / 20 | **70%** |

The gap mean (4 s) and 1/λ (5 s) differ because the observed gaps run only from t = 0 to t = 12, not the full 20-second window. In production log analysis, always compute λ from the observation interval length, not from the sample mean of inter-arrival times.

---

## Utilisation Law

**U = X × S**

**Derivation**: over any observation interval of length T, the total busy time = (jobs completed) × (average service time). Dividing both sides by T: U = X × S.

**Constraint**: U ≤ 1.0 (100%) — a device cannot be busy for more than all of the time.

### Arrival Rate vs Throughput

| Condition | Relationship |
|-----------|-------------|
| Stable system, no lost/rejected work | X = λ, so U = λS |
| Demand exceeds capacity, or work is dropped | X < λ, must use U = XS |

U = XS is the **general operational law**. U = λS is a special case valid only under stability.

### Common Exam Calculations (IT Domain)

| Given | Find | Solution |
|-------|------|---------|
| λ = 3/s, S = 100 ms | U | U = 3 × 0.1 = **0.3 (30%)** |
| U = 0.9, λ = 100/s | S | S = 0.9/100 = **9 ms** |
| S = 10 ms | λ_max (at U = 1) | λ_max = 1/0.01 = **100 tps** |

### Utilisation Law — Pie-Eating Analogy

An intuitive first-principles derivation:

> 60-minute pie-eating contest. You eat 5 pies, each taking 10 minutes. Busy time = 50 min. You rest for the final 10 minutes.

| Element | Value |
|---------|-------|
| Observation window T | 60 min |
| Jobs completed | 5 pies |
| Service time S | 10 min/pie |
| Busy time | 5 × 10 = 50 min |
| U = busy / T | 50/60 ≈ **83%** |
| Throughput X | 5/60 pies/min |
| U = X × S | (5/60) × 10 = 50/60 ✓ |

Dividing the total-busy-time equation `jobs × service_time` by the observation interval on both sides yields U = X × S directly.

### Utilisation Law Exercises — Healthcare Domain (MRI Scanner)

| Question | Given | Find | Working | Answer |
|----------|-------|------|---------|--------|
| 1 | λ = 2 scans/hr, S = 25 min | U | Busy = 2 × 25 = 50 min; U = 50/60 | **≈ 83%** |
| 2 | U = 60%, λ = 12 patients/hr | S | λ/min = 12/60 = 0.2; S = 0.6/0.2 | **3 min** |
| 3 | S = 6 min/patient | X_max | U_max = 1; X = 1/S = 60/6 | **10 patients/hr** |

**Practical note from Q1:** at 83% utilisation a small demand increase will begin forming a queue. This is how to sanity-check a department's capacity before purchasing additional equipment.

---

## Utilisation and Response Time — Non-linear Relationship

The Utilisation Law alone says nothing about waiting. In systems with variability in arrivals or service times:

- **Low U**: arriving request usually finds server free → R ≈ S
- **U rising**: more requests arrive while server is busy → W grows, R > S
- **Non-linear growth**: 60%→80% causes much less queueing growth than 80%→90%
- **Near 100%**: small load increases produce large queueing increases

Production systems are deliberately run with **headroom** — excess capacity — to avoid operating on the steep part of the utilisation→response time curve.

**Factors that affect waiting beyond utilisation**: arrival variability, service-time variability, number of servers, queue discipline.

```
Example:
- Polyclinic visit: total 55 min; 40 min waiting, 15 min service time
- Queue-dominated experience
- Root cause may be: insufficient capacity, variability, scheduling, or a bottleneck elsewhere
- Diagnose before optimising
```

---

## Key Connections

- [[concepts/performance-engineering]] — the measure/model/optimise/deploy philosophy that uses these metrics
- [[sources/ict3113-pod-l2]] — full source with exercises and worked examples
- [[sources/ict3113-pod-l1]] — module context: where these metrics feed into modelling and deployment
