---
type: study-notes
title: "ICT3113 — Formula Quick Reference"
tags: [study-notes, ict3113, formula-sheet, exam-prep]
created: 2026-09-14
---

# ICT3113 — Formula Quick Reference Sheet

> Print-friendly one-page reference. For derivations and worked examples see [[study notes/ICT3113 - Performance Optimisation Exam Notes]].

---

## Core Laws

| Formula | Law | When to use |
|---------|-----|------------|
| **R = W + S** | Response Time | Always — decompose any timing problem |
| **U = X × S** | Utilisation Law | Always — U = λS only when X = λ (stable) |
| **N = X × R** | Little's Law | Any stable system; any subsystem |
| **N = X × (R + Z)** | Little's Law (closed) | Closed system with think time Z |

---

## Queueing Models

| Model | Traffic Intensity | Stability | Queue Wait W |
|-------|-----------------|-----------|-------------|
| **M/M/1** | ρ = λ/μ = λS | ρ < 1 | ρ/(1−ρ) × S |
| **M/M/c** | ρ = λ/(c × μ) | ρ < 1 | Use Erlang C (conceptual) |

---

## Operational Laws

| Formula | Name | Notes |
|---------|------|-------|
| **X_k = V_k × X** | Forced Flow Law | Device throughput from system throughput + visit counts |
| **D_k = V_k × S_k** | Service Demand | Total service time per transaction at device k |
| **U_k = X × D_k** | Service Demand Law | Utilisation Law per-device using demands |
| **D_k = U_k / X** | Demand from monitoring | No visit tracing needed |

---

## Bottleneck Analysis

| Formula | Meaning |
|---------|---------|
| **X ≤ 1 / D_max** | Throughput ceiling — single server per device |
| **X ≤ c / D** | Throughput ceiling — c servers at device |
| **R ≥ Σ D_k** | Response time lower bound — best possible R |
| Bottleneck = device with **lowest** c/D ceiling | NOT necessarily the largest D |

---

## Interactive Response Time Law

$$R = \frac{N}{X} - Z$$

- N = number of concurrent users
- X = measured throughput
- Z = average think time (user pause between requests)

---

## Variability

**Coefficient of Variation:**

$$C = \frac{\sigma}{\mu}$$

- Cₐ = arrivals; Cₛ = service times
- C = 0: regular; C = 1: Markov (M/M/1 assumption); C > 1: bursty/mixed

**Kingman Formula (G/G/1 — single server):**

$$W \approx \frac{\rho}{1-\rho} \times \frac{C_a^2 + C_s^2}{2} \times S$$

**Sakasegawa (G/G/c — c servers):**

$$W \approx \frac{C_a^2 + C_s^2}{2} \times \frac{\rho^{\sqrt{2(c+1)}-1}}{c(1-\rho)} \times S$$

---

## Kingman — Worked Values

| ρ | ρ/(1−ρ) |
|---|---------|
| 0.5 | 1.0 |
| 0.6 | 1.5 |
| 0.7 | 2.33 |
| 0.8 | **4.0** |
| 0.9 | **9.0** |
| 0.95 | 19.0 |

At Ca = Cs = 1: variability term = 1 → Kingman = M/M/1 result.

---

## Four Sources Diagnostic

```
Symptom → Root Cause → Fix

High U + throughput plateau     → CAPACITY       → add servers / replicas
High tail despite moderate U    → VARIABILITY    → split queues / jitter
R grows with user count         → POPULATION     → Interactive Law; raise X
Bottleneck shifts unexpectedly  → DEMAND         → reduce V or S
```

---

## Utilisation Calculator

| Given | Find | Calc |
|-------|------|------|
| λ = 3/s, S = 100 ms | U | 3 × 0.1 = 30% |
| U = 0.9, λ = 100/s | S | 0.9/100 = 9 ms |
| S = 10 ms | λ_max | 1/0.01 = 100 tps |
| λ = 8, S = 148 ms, c = 3 | ρ | 8 × 0.148/3 ≈ 0.395 |

---

## Kingman Calculator

| ρ | Ca² | Cs² | Variability | S | W |
|---|-----|-----|-------------|---|---|
| 0.8 | 1 | 1 | 1 | 100 ms | 4 × 1 × 100 = **400 ms** |
| 0.8 | 1 | 4 | 2.5 | 100 ms | 4 × 2.5 × 100 = **1,000 ms** |
| 0.9 | 1 | 1 | 1 | 50 ms | 9 × 1 × 50 = **450 ms** |
| 0.9 | 1 | 9 | 5 | 50 ms | 9 × 5 × 50 = **2,250 ms** |

---

## All Assignments — Answers at a Glance

| ID | Question | Answer |
|----|----------|--------|
| E.4.1 | V=4, X=25 tps → X(db)? | 100 qps |
| E.4.2 | V=4, S=5 ms, X=30 → D, U? | D=20 ms, U=60% |
| E.4.3 | Fab, single tools, which bottleneck? | Litho (8.6 h); X≤2.8 lots/day |
| E.4.4 | c=3 litho, one fails at λ=3.05? | Ceiling 5.6 > 3.05 → no saturation |
| E.4.5 | N=200, Z=10 s, X=18 → R? | 1.11 s |
| E.4.6 | ρ=0.9, S=50 ms, Cs²=1 vs 9 | 450 ms vs 2,250 ms |

---

## Symbol Cheat Sheet

| Symbol | Name |
|--------|------|
| λ | Arrival rate (demand) |
| μ | Service rate = 1/S |
| S | Service time |
| X | Throughput (supply) |
| U | Utilisation |
| W | Wait time (in queue) |
| R | Response time = W + S |
| ρ | Traffic intensity |
| N | Average number in system |
| Z | Think time (closed systems) |
| V_k | Visit count to device k |
| D_k | Service demand at device k |
| c | Number of servers |
| Cₐ | CV of inter-arrival times |
| Cₛ | CV of service times |
