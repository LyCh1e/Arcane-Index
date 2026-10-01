---
type: source
title: "ICT3113 POD — Tutorial Week 05: Performance Modelling"
source_file: "raw/ICT3113 Performance Optimisation and Design - Tutorial Week05 Performance Modelling_1.md"
module: ICT3113 Performance Optimisation and Design
domain: performance-engineering
tags: [ict3113, performance-engineering, performance-bounds, erlang-b, erlang-recursion, execution-models, mapreduce, utilisation-law, littles-law, tutorial, worked-examples]
created: 2026-09-24
updated: 2026-09-24
lecturer: "A/Prof Donny Soh"
address: c-000125
---

# Source Index — ICT3113 POD: Tutorial Week 05 — Performance Modelling

**Module:** ICT3113 Performance Optimisation and Design  
**Lecturer:** A/Prof Donny Soh  
**Raw file:** `raw/ICT3113 Performance Optimisation and Design - Tutorial Week05 Performance Modelling_1.md`  
**Concept pages:** [[concepts/performance-metrics]] · [[concepts/queueing-theory]] · [[concepts/performance-engineering]]  
**Examples page:** [[examples/ict3113-t05-worked-examples]]

Four-question tutorial covering the full Lec05 toolkit: reading basic performance quantities from a job log, computing throughput and response-time bounds from service demands, estimating service time from an execution model (MapReduce), and sizing a connection pool using Erlang B. Also provides the most complete Erlang B reference table in the module (ρ = 0.25 to 4, m = 1 to 10) and the recursion formula for off-table values.

---

## Section Coverage

| Question | Topic | Key Technique |
|----------|-------|--------------|
| Q1 | Performance basics from job log | S = mean service time; μ = 1/S; R = mean response time; λ = X = jobs/window; W = R − S |
| Q2 | Performance bounds (5-device system) | D_i = V_i × S_i; R_min = Σ D_i; X_max = 1/D_max; bottleneck = device with largest D |
| Q3 | Execution model — MapReduce | Map (serial, scales with r); Compute (parallel, time = r/n × 0.1); Reduce (serial, scales with n); optimise n* = √(0.1r) |
| Q4 | Erlang B — connection pool | ρ = λ × S; find m with B(m, ρ) ≤ 0.001 using recursion B(m) = ρB(m−1)/(m + ρB(m−1)) |

---

## Key New Formulae (vs Lec05)

### Erlang B Recursion (Q4 + Reference)

More practical than the closed-form for computing B(m, ρ) step-by-step:

```
B(0) = 1
B(m) = [ρ × B(m−1)] / [m + ρ × B(m−1)]
```

This is equivalent to the closed-form but avoids computing large factorials. Use it when ρ is not in the Erlang B table.

### Notation

| Symbol | Meaning |
|--------|---------|
| λ | arrival rate |
| X | throughput |
| S | average service time |
| μ | service rate = 1/S |
| R | response time |
| W | waiting time = R − S |
| n̄ | average number in system |
| ρ | traffic intensity = λ × S |
| U | utilisation = X × S |
| Dᵢ | service demand at device i = Vᵢ × Sᵢ |
| m | server / pool capacity |
| B(m, ρ) | Erlang B loss probability |

---

## Extended Erlang B Table (Tutorial Week 05 Reference)

Values are percentages (× 100). Use the recursion for ρ values not in this table.

| m | ρ=0.25 | ρ=0.5 | ρ=0.75 | ρ=1 | ρ=1.5 | ρ=2 | ρ=3 | ρ=4 |
|---|--------|-------|--------|-----|--------|-----|-----|-----|
| 1 | 20.000 | 33.333 | 42.857 | 50.000 | 60.000 | 66.667 | 75.000 | 80.000 |
| 2 | 2.439 | 7.692 | 13.846 | 20.000 | 31.034 | 40.000 | 52.941 | 61.538 |
| 3 | 0.203 | 1.266 | 3.346 | 6.250 | 13.433 | 21.053 | 34.615 | 45.070 |
| 4 | 0.013 | 0.158 | 0.623 | 1.538 | 4.796 | 9.524 | 20.611 | 31.068 |
| 5 | <0.001 | 0.016 | 0.093 | 0.307 | 1.418 | 3.670 | 11.005 | 19.907 |
| 6 | <0.001 | 0.001 | 0.012 | 0.051 | 0.353 | 1.208 | 5.216 | 11.716 |
| 7 | <0.001 | <0.001 | 0.001 | 0.007 | 0.076 | 0.344 | 2.186 | 6.275 |
| 8 | <0.001 | <0.001 | <0.001 | <0.001 | 0.014 | 0.086 | 0.813 | 3.042 |
| 9 | <0.001 | <0.001 | <0.001 | <0.001 | 0.002 | 0.019 | 0.270 | 1.334 |
| 10 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | 0.004 | 0.081 | 0.531 |

**How to use:** read down the column for your ρ; take the smallest m at or below the loss target. For off-table ρ, apply the recursion above.

---

## Connections

- [[concepts/queueing-theory]] — Erlang B (§9): recursion formula and extended table added from this tutorial; performance bounds (§8)
- [[concepts/performance-engineering]] — execution models; MapReduce as a concrete example
- [[concepts/performance-metrics]] — service time, response time, waiting time, utilisation, throughput
- [[examples/ict3113-t05-worked-examples]] — full solutions for all four questions
- [[sources/ict3113-pod-l5]] — Lec05: source material for bounds and Erlang B theory
- [[areas/performance-engineering]] — parent area
