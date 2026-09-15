---
type: source
title: "ICT3113 POD — L4: Performance Modelling (II)"
source_file: "raw/ICT3113 Performance Optimisation and Design - Lec04 Performance Modelling (II).md"
module: ICT3113 Performance Optimisation and Design
domain: performance-engineering
tags: [ict3113, performance-engineering, queueing-theory, multi-server, operational-laws, bottleneck, kingman, variability, interactive-systems]
created: 2026-09-14
updated: 2026-09-14
lecturer: "A/Prof Donny Soh"
---

# Source Index — ICT3113 POD: Lecture 4 — Performance Modelling (II)

**Module:** ICT3113 Performance Optimisation and Design  
**Lecturer:** A/Prof Donny Soh  
**Raw file:** [[raw/ICT3113 Performance Optimisation and Design - Lec04 Performance Modelling (II).md]]  
**Concept page:** [[concepts/queueing-theory]]

Extends Lec03's M/M/1 single-server model in three directions: multi-server queues, systems-of-queues operational laws, and variability effects.

---

## Section Coverage

| Section | Key Content |
|---------|-------------|
| Multi-Server Queues (M/M/c) | Single queue feeding c servers; ρ = λ/(c×μ); one fast vs many slow servers; API tier worked example |
| Forced Flow Law | Xₖ = Vₖ × X; visit counts; running-case database verification (V=4.02, X=8.06 → 32.4 qps) |
| Service Demand Law | Dₖ = Vₖ × Sₖ; Uₖ = X × Dₖ; Dₖ = Uₖ/X for measurement without visit tracing |
| Bottleneck Analysis | Capacity bottleneck (lowest ceiling) vs congestion hotspot; X ≤ 1/Dmax, X ≤ c/D; R ≥ ΣDₖ lower bound; three improvement levers |
| Interactive Systems | Closed systems; think time Z; N users; Interactive Response Time Law R = N/X − Z |
| Coefficient of Variation | C = σ/mean; Cₐ (arrivals), Cₛ (service); C=0 regular, C=1 Markov, C>1 bursty |
| Kingman Formula (G/G/1) | W ≈ [ρ/(1−ρ)] × [(Ca²+Cs²)/2] × S; three worked comparisons at ρ=0.8 |
| Sakasegawa's G/G/c | Multi-server extension of Kingman; modified utilisation term |
| Four Sources Framework | Demand, Capacity, Variability, Population — the diagnostic taxonomy |
| Running Case: Online Service | Diagnosis: Cs²≈34 at DB from mixed workload; split-queue fix: p95 3.48s→0.44s; Kingman validated (0.27 vs 0.30 predicted) |
| Capstone: Wafer Fab | 525 lots, 6 steps; LITHO-02 failure → congestion hotspot not capacity bottleneck; Sakasegawa structure; priority discipline |

---

## Key Formulae Introduced

| Formula | Name | Notes |
|---------|------|-------|
| ρ = λ / (c × μ) | M/M/c traffic intensity | Stable iff ρ < 1; one-server case reduces to M/M/1 |
| Xₖ = Vₖ × X | Forced Flow Law | All device throughputs fixed in proportion to visit counts |
| Dₖ = Vₖ × Sₖ | Service demand definition | Total service time per transaction at device k |
| Uₖ = X × Dₖ | Service Demand Law | Utilisation Law restated using demands |
| X ≤ 1 / Dmax | Throughput ceiling (single server) | Dmax = largest demand across all devices |
| X ≤ c / D | Throughput ceiling (c servers) | Bottleneck = device with lowest ceiling |
| R ≥ Σ Dₖ | Response time lower bound | Minimum R when no queueing anywhere |
| R = N/X − Z | Interactive Response Time Law | Closed-system model; N users, Z think time |
| C = σ / mean | Coefficient of variation | Variability measure; C=1 matches Markov assumption |
| W ≈ [ρ/(1−ρ)] × [(Ca²+Cs²)/2] × S | Kingman formula (G/G/1) | Three-factor: utilisation × variability × service time |
| W ≈ [(Ca²+Cs²)/2] × [ρ^(√(2(c+1))−1) / (c(1−ρ))] × S | Sakasegawa (G/G/c) | Multi-server Kingman; same three factors |

---

## Assignments Covered

| ID | Topic | Key Result |
|----|-------|-----------|
| E.4.1 | Forced Flow Law | V=4, X=25 → X(db)=100 qps |
| E.4.2 | Service Demand Law | D=20 ms; U=60% at 30 tps |
| E.4.3 | Bottleneck Analysis (single server) | Litho bottleneck; X ≤ 2.8 lots/day |
| E.4.4 | Bottleneck Analysis (multi-server) | c=3 litho ceiling 8.4; one tool down still not saturated |
| E.4.5 | Interactive Response Time Law | N=200, Z=10 s, X=18 → R=1.11 s |
| E.4.6 | Kingman Formula | ρ=0.9, S=50 ms; W=450 ms at Cs²=1; W=2,250 ms at Cs²=9 |

---

## Connections

- [[concepts/queueing-theory]] — concept page covering all Lec04 content
- [[concepts/performance-metrics]] — Utilisation Law, Little's Law, M/M/1 background
- [[concepts/performance-engineering]] — measure/model/optimise/deploy loop; bottleneck and variability as optimisation targets
- [[concepts/workload-identification]] — Lec03 context: how to derive the arrival rates and demands that feed into the models on this page
- [[areas/performance-engineering]] — parent area
