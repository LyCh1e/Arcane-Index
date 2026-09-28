---
type: source
title: "ICT3113 POD — L5: Estimating Performance and Lost Work"
source_file: "raw/ICT3113 Performance Optimisation and Design - Lec05 Estimating Performance and Lost Work.md"
module: ICT3113 Performance Optimisation and Design
domain: performance-engineering
tags: [ict3113, performance-engineering, throughput-bounds, response-time-bounds, erlang-b, lost-work, execution-models, bottleneck, background-load]
created: 2026-09-24
updated: 2026-09-24
lecturer: "A/Prof Donny Soh"
address: c-000122
---

# Source Index — ICT3113 POD: Lecture 5 — Estimating Performance and Lost Work

**Module:** ICT3113 Performance Optimisation and Design  
**Lecturer:** A/Prof Donny Soh  
**Raw file:** `raw/ICT3113 Performance Optimisation and Design - Lec05 Estimating Performance and Lost Work.md`  
**Concept pages:** [[concepts/queueing-theory]] · [[concepts/performance-engineering]] · [[concepts/performance-metrics]]

Consolidation lecture before the midterm. Applies the laws from Lec03–Lec04 to two new problems: (1) deriving hard ceilings on throughput and response time from service demands, and (2) estimating how many resources to provision so that rejected-job probability stays below a target (Erlang B / lost work).

---

## Section Coverage

| Section | Key Content |
|---------|-------------|
| Where We Are | Review of modelling block: utilisation law, Little's Law, M/M/1, Forced Flow, Service Demand, bottleneck analysis, Kingman — all prior lectures |
| Upper Bound on Throughput | D(i) = V(i) × S(i); X0 < 1/D(b) where D(b) is the bottleneck demand; practical 70% planning rule |
| Background Load | Devices have pre-existing utilisation b(k); effective capacity for new requests = (Capacity − b(k)) / D(k) |
| Lower Bound on Response Time | R0 ≥ Σ D(i); best-case response time is the sum of all demands (no queueing anywhere) |
| Execution Models | Estimating S from UML activity/sequence diagrams before a system exists; Smith & Williams (2001) |
| Lost Work / Erlang B | Erlang loss formula B(m, ρ); sizing m given offered load ρ and target loss probability ε |
| Worked Example: Throughput | E-commerce checkout: five services; bottleneck = payment gateway (D = 25 ms) → X0 < 40 req/s |
| Worked Example: Background Load | Database server with four devices (CPU, Memory, Disk1, Disk2); effective ceilings per device |
| Worked Example: Response Time | Minimum response time for checkout system = Σ D(i) |
| Worked Example: Service Estimation | Async network request + three-way branch; parallel max + weighted branch expected value |
| Worked Example: Erlang Router | λ = 300 pkt/s, μ = 500 pkt/s → ρ = 0.6; find m such that B(m, 0.6) < 10⁻⁶ → m = 7 |
| Worked Example: Connection Pool | λ = 7 req/s, S = 100 ms → ρ = 0.7; 99.9% availability → at least one spare → find m |

---

## Core Formulae

```
Demand:
  D(i) = V(i) × S(i)
  where V(i) = visit count, S(i) = average service time per visit

Upper bound on throughput:
  U(i) = X0 × D(i)     [from Utilisation Law + Forced Flow Law]
  X0 < 1 / D(b)        [D(b) = max demand across all services]

With background load b(k) on device k, capacity C(k):
  Max arrival rate for device k = (C(k) − b(k)) / D(k)

Lower bound on response time (no queueing, sequential):
  R0 ≥ Σ D(i) = Σ V(i) × S(i)

Execution model time rules:
  Sequential tasks: sum the times
  Parallel tasks: take the maximum
  Branches: Σ p(branch) × t(branch)

Erlang B (loss formula):
  ρ = λ × S    (offered load)
  B(m, ρ) = (ρᵐ / m!) / Σₖ₌₀ᵐ (ρᵏ / k!)
  Size m as: smallest m such that B(m, ρ) ≤ ε
```

---

## Worked Examples (Solutions)

### Throughput Upper Bound — Checkout System

| Service | V | S (ms) | D = V × S (ms) |
|---------|---|--------|----------------|
| API gateway | 1 | 5 | 5 |
| Auth service | 1 | 10 | 10 |
| Product DB | 3 | 12 | 36 |
| Cache | 4 | 1 | 4 |
| Payment gateway | 1 | 25 | **25** (bottleneck) |

**X0 < 1 / 0.025 = 40 req/s.** Practical ceiling at 70%: ≈ 28 req/s.

### Lower Bound on Response Time — Same System

R0 ≥ 5 + 10 + 36 + 4 + 25 = **80 ms** (best possible, no queueing).

### Erlang B — Router Buffer Sizing

ρ = 300 / 500 = 0.6. Target: B < 10⁻⁶. From table: B(7, 0.6) = 3.0 × 10⁻⁶ > 10⁻⁶; B(8, 0.6) = 2.3 × 10⁻⁷ < 10⁻⁶ → **m = 8 buffers.**

### Erlang B — Connection Pool

ρ = 7 × 0.1 = 0.7. "At least one unused connection 99.9% of the time" means P(all m connections busy) < 0.001 → find smallest m with B(m, 0.7) < 10⁻³. From table: B(5, 0.7) = 7.0 × 10⁻⁴ < 10⁻³ → **m = 5 connections.**

---

## Connections

- [[concepts/queueing-theory]] — M/M/1, bottleneck analysis, response time bounds (this lecture adds Erlang B section)
- [[concepts/performance-engineering]] — execution models; Measure–Model–Optimise–Deploy cycle
- [[concepts/performance-metrics]] — utilisation law, Little's Law, service demand law
- [[sources/ict3113-pod-l4]] — Lec04: operational laws, bottleneck analysis, Kingman formula (prerequisite)
- [[sources/ict3113-pod-l6]] — Lec06: JMeter Recap — applying Little's Law to test plan sizing
- [[areas/performance-engineering]] — parent area
