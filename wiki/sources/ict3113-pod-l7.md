---
type: source
title: "ICT3113 POD Lec07 — Performance Testing"
domain: performance-engineering
source-type: lecture-notes
course: ICT3113
status: ingested
created: 2026-10-06
updated: 2026-10-06
tags: [ict3113, performance-testing, load-test, stress-test, soak-test, regression-test, benchmark, pipe-clean, open-loop, closed-loop, test-environment, playbook, bondi, jmeter]
---

# Source: ICT3113 POD Lec07 — Performance Testing

**File:** `raw/ICT3113 Performance Optimisation and Design - Lec07 Performance Testing.md`
**Presenter:** A/Prof Donny Soh
**Scope:** Types of performance test, test environment, load generation (65 slides)

---

## Summary

Lec07 closes the model-to-measurement arc by showing how to check queueing-model predictions against a real running system. It covers four documents that carry performance work from requirement to operations, six distinct test types with recorded demos on a small order API, the open-loop vs closed-loop distinction, test environment principles, and a playbook that another person can follow to reproduce any result.

---

## Learning Outcomes

- Distinguish six types of performance test and state which question each one answers.
- Set up a test environment that stands in for production, and know when it cannot.
- Build a load model and generate load correctly, including the open/closed-loop difference.
- Write a performance requirement and a playbook another person can execute.
- Read a results table and distinguish saturation from a bug.

---

## Key Concepts Introduced

| Concept | Where developed in wiki |
|---|---|
| Six performance test types | [[concepts/performance-engineering]] §Performance Testing |
| Open-loop vs closed-loop load | [[concepts/performance-engineering]] §Performance Testing |
| Bondi's 10-field requirement structure | [[concepts/performance-engineering]] §Performance Testing |
| Eckhardt sentence patterns | [[concepts/performance-engineering]] §Performance Testing |
| Test environment principles (scale-up/out, observer effect) | [[concepts/performance-engineering]] §Performance Testing |
| Playbook structure | [[concepts/performance-engineering]] §Performance Testing |

---

## Demos (Recorded Runs, Order API)

| Demo | Test type | Setup | Key finding |
|---|---|---|---|
| Demo 1 | Load test | 10 req/s, 3 min × 3 runs, 8 cores | p50 40 ms ≈ S = 34 ms; p95 100–120 ms; CPU 16% ≈ predicted 15%; no errors. Model held. |
| Demo 2 | Stress test | Stepped 5→30 req/s, 1 core pinned | Knee between 5 and 10; ceiling 13–15/s; ungraceful: 50% errors at 30/s; p50 drops when failures are fast |
| Demo 3 | Soak test | 8 req/s, 10 min | Memory: 33→68 MB, +3.4 MB/min (straight line); p95 flat; predicted 1.9, observed 3.4 due to Python object overhead |
| Demo 4 | Regression test | 5 req/s, Build A vs Build B (O(n) duplicate check), 8 min | Build B: p50 +30%, p95 +45% — regression detected; slope only visible at higher load/longer run |
| Demo 5 | Benchmark | 5 req/s, 25k / 100k / 400k PBKDF2 iterations | 25k→100k: p50 ×4; 400k: near-total collapse (83% timeouts, throughput 0.8 < ceiling 2.5) — ghosts waste CPU |
| Demo 6 | Pipe-clean | Broken catalogue path, no body assertion | 100% "success" reported, 0 orders created; p95 39 ms vs expected 360 ms — test measured error overhead, not service |
| Demo 7 | Observer effect | Demo 1 with/without cProfile | p95 100 ms → 110 ms; small here because PBKDF2 is a C call; pure Python handlers can double under cProfile |

---

## Concrete Numbers (Reference)

| Quantity | Value | Context |
|---|---|---|
| S (laptop, 8 cores) | 64 ms | Demo 1 single-request check |
| S (sandbox, 1 core) | 34 ms | Demo 1 sandbox |
| S (sequential, 1 core, fresh connection) | 112 ms | Demo 2 setup |
| Inferred S from CPU (8 cores) | ~35 ms | 8% of 8 cores ÷ λ |
| Actual S from stress ceiling (1 core) | ~70 ms | ceiling ≈ 1/S |
| Store bytes per order (predicted) | 4 kB | 4 kB × ~4,900 = 20 MB |
| Store bytes per order (observed) | ~7 kB | Python object overhead |
| Memory growth rate (soak) | 3.4 MB/min | Demo 3 |
| Time to 16 GB at soak rate | ~3.3 days | Extrapolation |

---

## References Cited

- Bondi (2015), Table 7.2 — 10-field performance requirement structure
- Eckhardt et al. (2016) — sentence patterns for performance requirements
- Miller (1968), Nielsen (1993) — response time thresholds (100 ms / 1 s)
- Molyneaux (2014), Chapter 3 — test environment setup
- Google Cloud blog (2016) — Pokémon Go launch: planned 5×, got 50×

---

## Related Pages

- [[concepts/performance-engineering]] — primary concept page; §Performance Testing added from this lecture
- [[concepts/performance-metrics]] — metric definitions, utilisation law
- [[concepts/queueing-theory]] — M/M/1, knee curve, bounds
- [[sources/ict3113-pod-l2]] — metrics and modelling fundamentals
- [[sources/ict3113-pod-l3]] — workload identification and estimation
- [[sources/ict3113-pod-l5]] — performance bounds, Erlang B
- [[sources/ict3113-pod-l6]] — JMeter test plan sizing, Little's Law
