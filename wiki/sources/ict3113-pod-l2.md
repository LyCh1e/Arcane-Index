---
type: source
title: "ICT3113 POD — Lecture 2: Performance Metrics and System Modelling"
source_file: "raw/ICT3113 Performance Optimisation and Design - Lec02 Performance Metrics and System Modelling.md"
domain: performance-engineering
tags: [ict3113, performance-metrics, response-time, throughput, utilisation, percentiles, queueing, utilisation-law]
created: 2026-08-31
---

# Source Index — ICT3113 POD Lecture 2: Performance Metrics and System Modelling

Course: **ICT3113 Performance Optimisation and Design** — A/Prof Donny Soh

---

## Motivating Case Study — Mars Climate Orbiter (1999)

Ground software (Lockheed Martin) supplied navigation data in **pound-force seconds** (imperial). The NASA system expected **newton-seconds** (SI). The same quantity crossed a system boundary in inconsistent units — a violation of the **consistency** property of metrics.

The discrepancy had been noticed by at least two navigators, but their concerns were dismissed for procedural reasons. The spacecraft was lost. **Cost: $327.6M mission destroyed by a unit mismatch.**

Lesson: a metric needs an agreed definition, unit, and measurement boundary wherever it is exchanged.

---

## Properties of Good Performance Metrics

Six properties required of any good performance metric (Lilja 2000, cited by Bondi):

| Property | Meaning |
|---------|---------|
| **Linearity** | Responds in a linear fashion to the phenomenon being measured |
| **Reliability** | If the metric says A > B, then A genuinely outperforms B in real-world usage |
| **Repeatability** | Gives the same results under the same conditions |
| **Ease of measurement** | Easily measured or computed (note: mean needs only a running sum; percentile needs full distribution) |
| **Consistency** | Same definition across all systems under comparison |
| **Independence** | Not shaped by vendors or sponsors whose systems it will compare |

**Exam question clue**: "A metric consistently reports System A higher than System B, but in real-world usage System B outperforms A" → violation of **reliability**.

---

## Three Classes of Metrics

| Class | What It Measures | Key Metric |
|-------|-----------------|-----------|
| **User Experience (Outcome)** | Phenomena affecting users' experience | **Response Time** — time from request initiation to completion |
| **Demand** | Level of demand for a service (counted at entrance) | **Arrival Rate λ** — units of work offered per unit time |
| **Supply** | What the system delivers and consumes | **Throughput X** and **Utilisation U** |

---

## Response Time

**Response Time = Wait Time + Service Time**

- **Wait Time (W)**: time the request waits for the system to be available
- **Service Time (S)**: time the system spends actively servicing the request
- For end-to-end requests, add network and communication delays

### User Perception Thresholds (Miller 1968; Nielsen 1993)

| Response Time | User Experience |
|--------------|----------------|
| ~0.1 s | Feels instantaneous |
| ~1 s | Delay noticed; flow of thought largely maintained |
| ~10 s | Attention hard to hold; show a progress indicator |

*Historical usability heuristic, not a universal performance law.*

---

## Percentiles and Tail Latency

Real systems produce a **distribution** of response times — not a single number.

- Distributions are **right-skewed**: most requests are fast; a few are very slow (cache misses, GC pauses, retries, queueing)
- The **mean is pulled up** by the slow outliers
- The **p50 (median)** describes the typical request
- **p95, p99** describe the tail — the slow ones

**Definition**: the p-th percentile is the value below which p% of requests fall. "p99 = 300 ms" means 99% of requests completed within 300 ms.

Latency objectives are expressed as percentiles because averages hide tail behaviour.

### SLI / SLO / SLA

| Term | Definition |
|------|-----------|
| **SLI** (Service Level Indicator) | The metric being measured (e.g. p99 latency) |
| **SLO** (Service Level Objective) | The target for the SLI (e.g. p99 < 200 ms) |
| **SLA** (Service Level Agreement) | A formal agreement that may carry objectives and consequences |

### Why the Tail Matters

Two reasons a "1% of requests" tail is not negligible:

1. **Fan-out**: one page load may trigger 100 backend calls, and the user waits for the **slowest** one.
   - P(at least one of 100 calls slower than its p99) = 1 − 0.99¹⁰⁰ ≈ **63%**
   - Most page loads hit the tail *(assumes independent call latencies)*
2. **Heavy users**: users who make the most requests encounter the tail most often — and they are typically the most valuable users.

*(Kleppmann 2017)*

---

## Demand Metrics: Arrival Rate (λ)

**Arrival rate λ**: number of units of work offered per unit time, **counted at the entrance**.

- Arrival rate can exceed capacity (demand side metric)
- When λ > μ (capacity), throughput caps, WIP grows, cycle time climbs

---

## Supply Metrics: Throughput and Utilisation

**Throughput X**: units of work **completed** per unit time, **counted at the exit**.  
X never exceeds the service rate μ (capacity). Overtime raises μ; it does not lift X above it.

**Utilisation U**: proportion of time a device is busy, or of its capacity in use.

### Supply Metric Sub-categories

| Category | Example Metrics |
|---------|----------------|
| **CPU** | CPU Time, CPU Utilisation |
| **Memory** | Virtual memory amount, paging activity level |
| **Disk** | Busy time, idle time, transfer speed |
| **Network** | Bandwidth (link capacity, bps); Observed throughput (bytes/s); Packets/s |
| **Energy / Power** | Energy: J, Wh, kWh; Power: W |

---

## Performance Modelling Basics — Key Terms

| Symbol / Term | Definition |
|--------------|-----------|
| **λ** (arrival rate) | Number of arrivals per unit time — demand entering the system |
| **Interarrival time** | Elapsed time between consecutive arrivals |
| **S** (service time) | Time spent actively servicing one job (excludes waiting) |
| **X** (throughput) | Jobs completed per unit time |
| **μ** (service rate / capacity) | For single server with mean service time S: μ = 1/S when continuously busy |
| **U** (utilisation) | Proportion of time server is busy |

**Important observation boundary note**: in a long-running stationary workload, mean interarrival time ≈ 1/λ. In a short finite trace, the sample mean of observed gaps **≠ 1/λ** because the boundaries of the observation window affect the count.

### Worked Example (4 jobs in [0, 10]s)

| Job | Arrival | Start | Finish | Wait | Service | Response |
|-----|---------|-------|--------|------|---------|---------|
| A | 0 | 0 | 2 | 0 | 2 | 2 |
| B | 1 | 2 | 6 | 1 | 4 | 5 |
| C | 3 | 6 | 7 | 3 | 1 | 4 |
| D | 5 | 7 | 10 | 2 | 3 | 5 |

| Metric | Calculation | Value |
|--------|------------|-------|
| Arrival rate λ | 4 jobs / 10 s | 0.4 jobs/s |
| Mean observed gap | (1+2+2)/3 | 1.67 s |
| 1/λ | 1/0.4 | 2.5 s *(≠ mean gap)* |
| Mean service time S | 10/4 | 2.5 s |
| Service rate μ | 1/2.5 | 0.4 jobs/s |
| Utilisation U | 0.4 × 2.5 | **1.0** (saturated — server busy all 10 s) |

---

## Utilisation Law

**U = X × S**

The average utilisation is the product of average throughput and average service time. Derivation: over any interval, busy time = jobs completed × average service time; divide both sides by interval length.

**Constraint**: U ≤ 1.0 (100%) — a device cannot be busy more than all of the time.

**Arrival rate vs throughput**:
- In a stable steady-state system with no lost/rejected/abandoned work: **X = λ** → so **U = λS** (special case)
- If demand exceeds capacity, or work is dropped: λ and X diverge → use **U = XS** (general operational law)

### Utilisation Law — Key Exercises

| Given | Find | Formula |
|-------|------|---------|
| λ and S | U | U = λS |
| U and λ | S | S = U/λ |
| S | Max λ | λ_max = 1/S (when U = 1) |

---

## Utilisation and Response Time — Non-linear Relationship

The Utilisation Law says nothing about waiting. In queueing systems with variable arrivals or service times:

- **Low utilisation**: arriving request usually finds server free → response time ≈ service time
- **Rising utilisation**: more requests arrive while server is busy → wait time grows
- **Growth is non-linear**: 60%→80% hurts far less than 80%→90%; near 100%, small load increases cause large queueing increases

Production systems are deliberately run with **headroom** rather than at full utilisation. Utilisation alone does not determine waiting time — arrival variability, service-time variability, number of servers, and queue discipline all matter.

---

## References

- Bondi, A. B. (2014). *Foundations of Software and System Performance Engineering.* Addison-Wesley.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications.* O'Reilly. (percentiles and tail latency)
- Lilja, D. J. (2000). *Measuring Computer Performance.* Cambridge University Press.
- Miller, R. B. (1968). Response time in man-computer conversational transactions. *AFIPS FJCC.*
- Nielsen, J. (1993). *Usability Engineering.* Academic Press.
- NASA (1999). Mars Climate Orbiter Mishap Investigation Board, Phase I Report.

---

## Linked Concepts

- [[concepts/performance-metrics]] — comprehensive reference for all metrics in this lecture
- [[concepts/performance-engineering]] — module philosophy and context
