---
type: source
title: "ICT3113 POD — Tutorial Week 04: Problem Sets 1 and 2"
source_file: "raw/ICT3113 Performance Optimisation and Design - Tutorial Week04 Problem Sets 1 and 2.md"
module: ICT3113 Performance Optimisation and Design
domain: performance-engineering
tags: [ict3113, performance-engineering, utilisation-law, forced-flow-law, bottleneck, littles-law, capacity-planning, retries, read-replicas, percentiles, tutorial, worked-examples]
created: 2026-09-24
updated: 2026-09-24
lecturer: "A/Prof Donny Soh"
address: c-000124
---

# Source Index — ICT3113 POD: Tutorial Week 04 — Problem Sets 1 and 2

**Module:** ICT3113 Performance Optimisation and Design  
**Lecturer:** A/Prof Donny Soh  
**Raw file:** `raw/ICT3113 Performance Optimisation and Design - Tutorial Week04 Problem Sets 1 and 2.md`  
**Concept pages:** [[concepts/performance-metrics]] · [[concepts/queueing-theory]] · [[concepts/performance-engineering]]  
**Examples page:** [[examples/ict3113-t04-worked-examples]]

Two problem sets applying the Lec01–Lec04 toolkit to realistic multi-stage systems. Problem Set 1 models an e-commerce order API pipeline (validation → payment → confirmation) with retries and capacity scaling. Problem Set 2 models a food delivery backend (app tier + database + cache) with mixed workloads, bottleneck identification, SLO reasoning, and a three-year capacity planning comparison.

---

## Section Coverage

| Question | Topic | Key Technique |
|----------|-------|--------------|
| 1.1 | End-to-end yield through two loss stages | Multiply stage pass-rates; confirmed = total − rejected − declined |
| 1.2 | Work backwards from output target | Required input = target / (yield₁ × yield₂) |
| 1.3 | Peak-hour utilisation | Peak rate = k × daily average; U = X × S |
| 1.4 | Service time budget under utilisation cap | S_max = U_cap / X |
| 1.5 | Retries and effective load | Geometric series: V_attempts = 1/(1−p_fail); attempt rate = X × V |
| 1.6 | Minimum instance count | m ≥ ceil(X × S / U_cap) |
| 1.7 | Maximum confirmed orders at bottleneck | X_max = c / D; approved rate = X_max × (1 − decline_rate) |
| 1.8 | Upstream utilisation at max rate | Invert pass-rate to get incoming rate; U = (rate/instances) × S |
| 1.9 | Downstream utilisation at max rate | Confirmation rate = approved rate; U = (rate/instances) × S |
| 2.1 | Mixed workload utilisation | Weighted mean demand = Σ pᵢ × Sᵢ; U = (X/instances) × D̄ |
| 2.2 | Fan-out (Forced Flow Law) | V̄ = Σ pᵢ × Vᵢ; query rate = V̄ × X₀ |
| 2.3 | Bottleneck identification | Per-server demand = D / servers; bottleneck = max; X_max = 1 / D_bottleneck |
| 2.4 | Little's Law + thread pool sizing | n̄ = X × R; compare to total thread capacity; note: mean ≠ peak |
| 2.5 | Percentiles and SLO | p99 ≤ SLO threshold → met; slow requests = (1 − pN) × total |
| 2.6 | Database utilisation at peak | U = X × D |
| 2.7 | Growth to saturation | U(t) = U₀ × (1+g)^t; saturation year = ceil(ln(1/U₀) / ln(1+g)) |
| 2.8 | Option A — query optimisation | New X_max = U_cap / D_new; compare to 3-year peak |
| 2.9 | Option B — read replicas | Primary demand = writes + reads/replicas; U_primary = X × D_primary |

---

## Key Techniques Demonstrated

### Retry visit count
When a stage retries until success with per-attempt failure probability p:
```
V_attempts = 1 / (1 − p)    [geometric series: 1 + p + p² + … = 1/(1−p)]
Attempt rate = X_output × V_attempts
```
Example (Q1.5): p = 0.10 → V = 1/0.9 = 1.111; 90 orders/s → 100 attempts/s.

### Growth to saturation
```
U(t) = U₀ × (1 + g)^t
Saturates when U(t) ≥ 1 → t* = ln(1/U₀) / ln(1+g)
```
Example (Q2.7): U₀ = 0.80, g = 0.20 → t* = ln(1.25)/ln(1.2) ≈ 1.22 years → saturates in Year 2.

### Read replica demand split
```
D_primary = D_write + D_read / (1 + replicas)
```
Example (Q2.9): 30% writes + 70% reads over 3 servers → D_primary = 0.30×D + (0.70×D)/3 = 0.30D + 0.233D = 0.533D per request.

### Minimum instances
```
m ≥ ceil(X × S / U_cap)     or equivalently ceil(offered_load / U_cap)
```

---

## Connections

- [[concepts/performance-metrics]] — Utilisation Law, Little's Law, service demand, throughput
- [[concepts/queueing-theory]] — bottleneck analysis, Forced Flow Law, Service Demand Law
- [[concepts/performance-engineering]] — Measure–Model–Optimise–Deploy; capacity planning
- [[examples/ict3113-t04-worked-examples]] — full solutions for all 18 questions
- [[sources/ict3113-pod-l3]] — Lec03: workload identification, Utilisation Law, Little's Law
- [[sources/ict3113-pod-l4]] — Lec04: operational laws, bottleneck analysis
- [[areas/performance-engineering]] — parent area
