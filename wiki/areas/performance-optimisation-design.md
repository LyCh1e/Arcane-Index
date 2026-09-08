---
type: area
title: "Performance Optimisation and Design"
domain: performance-engineering
status: established
created: 2026-08-31
updated: 2026-09-08
tags: [performance-engineering, performance-optimisation, queueing-theory, profiling, ict3113]
---

# Area: Performance Optimisation and Design

This area covers the ICT3113 course content and related knowledge on software performance engineering — the systematic discipline of measuring, modelling, and optimising how software systems behave under load.

---

## Core Concept Pages

| Page | Description | Complexity |
|------|------------|------------|
| [[concepts/performance-engineering\|Performance Engineering]] | Measure → Model → Optimise → Deploy philosophy; classical optimisation techniques; application to AI workloads and production deployment | high |
| [[concepts/performance-metrics\|Performance Metrics]] | 6 metric properties; response time (R = W + S); percentiles and tail latency; SLI/SLO/SLA; arrival rate; throughput; utilisation; Utilisation Law (U = XS); non-linear utilisation → response time relationship | high |
| [[concepts/workload-identification\|Workload Identification]] | Workload components (transaction types, arrival rates, service demand); business-driven estimation; order-of-magnitude decomposition; peak vs average; peak-within-peak; workload mix; architecture decisions driven by workload; three worked examples (manufacturing, healthcare, IT flash sale) | high |
| [[concepts/python-profiling\|Python Profiling]] | Program-level Measure step: deterministic (`cProfile`) vs statistical (`py-spy`) profiling; `timeit` done right; `gprof2dot` call graphs and flame graphs; memory profiling (`memory_profiler` per-line RSS, `tracemalloc` allocation sites); `psutil` system inventory; profile-first method | medium |

---

## Lab Examples

| Page | Content |
|------|---------|
| [[examples/ict3113-lab1-profiling\|Lab 1 (Wk 2): Introduction to Profiling]] | Completed + executed notebook exercising `perf_counter` / `timeit` / `cProfile` / `gprof2dot` / `py-spy` / `memory_profiler` / `tracemalloc` / `psutil` on insertion/merge/quick sort and recursive Fibonacci; measured cProfile ~5× overhead, memoisation 2.69M→35 calls, in-place vs copying memory peaks |

---

## Source Pages (ICT3113)

| Page | Content |
|------|---------|
| [[sources/ict3113-pod-l1\|L1: Course Overview]] | Module philosophy (Measure/Model/Optimise/Deploy), 14-week schedule, assessment breakdown, teaching approach (demonstrations over facts) |
| [[sources/ict3113-pod-l2\|L2: Performance Metrics and System Modelling]] | Mars Climate Orbiter case study, 6 metric properties, 3 metric classes, response time, percentiles, tail latency, demand/supply distinction, Utilisation Law, non-linear utilisation/response relationship, worked examples |
| [[sources/ict3113-pod-l3\|L3: Workload Identification]] | Pont des Arts motivation; workload definition; business drivers; decomposition methodology; e-Filing worked example; peak vs average; Taylor Swift case study; workload mix; MRT architecture comparison; three exercises (manufacturing, polyclinic, flash sale) |

---

## Planned Topics (Future Lectures)

| Topic | When | Notes |
|-------|------|-------|
| ~~Profiling (Lab 1)~~ | Wk 2 | ✅ Ingested — [[concepts/python-profiling]], [[examples/ict3113-lab1-profiling]] |
| ~~Workload Identification~~ | Wk 3 | ✅ Ingested — [[concepts/workload-identification]] |
| Performance Modelling I | Wk 4 | Queues and Little's Law |
| Performance Modelling II | Wk 5 | M/M/1, performance bounds, execution models |
| LLM Inference Performance | Wk 8 | TTFT, tokens/s, batching, GPU utilisation |
| Agentic AI Performance | Wks 9–10 | Agent loop as execution model; tool call fan-out |
| Docker for Performance | Wk 11 | Resource limits as capacity planning |
| Kubernetes for Performance | Wk 12 | HPA as control loop over utilisation |

---

## Related Areas

- [[areas/software-verification-validation]] — ICT3112; complementary module on software quality; testing verifies system meets spec, performance engineering measures how well it meets it
- DevOps / Deployment area (Docker, Kubernetes, GitHub Actions)
- [[concepts/database-indexing-transactions]] — indexing as a classical performance optimisation
