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

### Worked Example

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

### Common Exam Calculations

| Given | Find | Solution |
|-------|------|---------|
| λ = 3/s, S = 100 ms | U | U = 3 × 0.1 = 0.3 (30%) |
| U = 0.9, λ = 100/s | S | S = 0.9/100 = 9 ms |
| S = 10 ms | λ_max | λ_max = 1/0.01 = 100/s |

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
