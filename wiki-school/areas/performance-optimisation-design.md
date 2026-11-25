---
type: area
title: "Performance Optimisation and Design"
domain: performance-engineering
status: established
created: 2026-08-31
updated: 2026-11-24
tags: [performance-engineering, performance-optimisation, queueing-theory, profiling, ict3113]
---

# Area: Performance Optimisation and Design

This area covers the ICT3113 course content and related knowledge on software performance engineering — the systematic discipline of measuring, modelling, and optimising how software systems behave under load.

---

## Core Concept Pages

| Page | Description | Complexity |
|------|------------|------------|
| [[performance-engineering\|Performance Engineering]] | Measure → Model → Optimise → Deploy philosophy; classical optimisation techniques; application to AI workloads and production deployment | high |
| [[performance-metrics\|Performance Metrics]] | 6 metric properties; response time (R = W + S); percentiles and tail latency; SLI/SLO/SLA; arrival rate; throughput; utilisation; Utilisation Law (U = XS); non-linear utilisation → response time relationship | high |
| [[workload-identification\|Workload Identification]] | Workload components (transaction types, arrival rates, service demand); business-driven estimation; order-of-magnitude decomposition; peak vs average; peak-within-peak; workload mix; architecture decisions driven by workload; three worked examples (manufacturing, healthcare, IT flash sale) | high |
| [[connection-pool-diagnosis\|Connection Pool Diagnosis]] | Pool as a c-server queue (ceiling c/S, utilisation λS/c); hold time; three causes with three instruments (query log, plan, pool metrics); four-step method; why a bigger pool is not the fix | high |
| [[n-plus-one-query-problem\|N+1 Query Problem]] | Cause 1 of hold time: 1 + N queries per request, hidden from `EXPLAIN`, found in the query log; fix with one join (eager loading); round-trip cost by distance | medium |
| [[query-plans-and-slow-queries\|Query Plans and Slow Queries]] | Cause 2: ranking queries by runs/s × time per run; reading `EXPLAIN ANALYZE`; missing index, wrong estimate (histogram), and three ways to defeat an index | high |
| [[saga-pattern\|Saga Pattern]] | Cause 3 fix: short transactions around slow external calls, compensating transactions, idempotency key, recovery job; 305 ms to 8 ms | medium |
| [[python-profiling\|Python Profiling]] | Program-level Measure step: deterministic (`cProfile`) vs statistical (`py-spy`) profiling; `timeit` done right; `gprof2dot` call graphs and flame graphs; memory profiling (`memory_profiler` per-line RSS, `tracemalloc` allocation sites); `psutil` system inventory; profile-first method | medium |

---

## Lab Examples

| Page | Content |
|------|---------|
| [[ict3113-lab1-profiling\|Lab 1 (Wk 2): Introduction to Profiling]] | Completed + executed notebook exercising `perf_counter` / `timeit` / `cProfile` / `gprof2dot` / `py-spy` / `memory_profiler` / `tracemalloc` / `psutil` on insertion/merge/quick sort and recursive Fibonacci; measured cProfile ~5× overhead, memoisation 2.69M→35 calls, in-place vs copying memory peaks |
| [[ict3113-lab-wk11-load-stress-build-c\|Lab Wk 11: Load and Stress Test on Build C]] | Method, count reconciliation (`.jtl` + 21 = log), reading the stress table by column, c/S versus measured ceiling, lock-serialisation diagnosis; not yet run |
| [[ict3113-lec09-worked-examples\|Lec09 Worked Numbers]] | Pool ceilings, N+1 travel cost, query ranking, plan arithmetic, hold time before and after the saga fix, self-test |
| [[ict3113-lab-wk12-slow-endpoint-worked\|Lab Wk 12: Diagnosing a Slow Endpoint (worked)]] | Pool ceiling 20.8 req/s, utilisation 86% at the knee, 470 of 480 ms hold time is non-database work; fix and prediction (hold 10 ms, ceiling 1,000 req/s) |

---

## Source Pages (ICT3113)

| Page | Content |
|------|---------|
| [[ict3113-pod-l1\|L1: Course Overview]] | Module philosophy (Measure/Model/Optimise/Deploy), 14-week schedule, assessment breakdown, teaching approach (demonstrations over facts) |
| [[ict3113-pod-l2\|L2: Performance Metrics and System Modelling]] | Mars Climate Orbiter case study, 6 metric properties, 3 metric classes, response time, percentiles, tail latency, demand/supply distinction, Utilisation Law, non-linear utilisation/response relationship, worked examples |
| [[ict3113-pod-l3\|L3: Workload Identification]] | Pont des Arts motivation; workload definition; business drivers; decomposition methodology; e-Filing worked example; peak vs average; Taylor Swift case study; workload mix; MRT architecture comparison; three exercises (manufacturing, polyclinic, flash sale) |
| [[ict3113-pod-l7\|L7: Performance Testing]] | Six test types with demos, open/closed loop, Bondi requirements, test environment and scaling, playbook; transcript adds the AI-cannot-run-tests framing, scale-in/scale-down example and load generators |
| [[ict3113-pod-l9-database-request-time\|L9: Where a Database-Backed Request Spends Its Time]] | Hold time, pool as c-server queue, three contributors with three instruments, plans, indexes, saga; the lecture behind the Wk 12 lab |
| [[ict3113-pod-l10-intro-ai-agents\|L10: Introduction to AI Agents]] | Model alone vs chatbot vs workflow vs agent; think-act-observe loop; agent = model + harness; six harness components; llama3.2 p95 demo; why the harness matters for performance |
| [[ict3113-pod-lab-wk11-load-stress\|Wk 11 Lab (Lec07): Load and Stress]] | Lab handout: LAB-01 load test, seven-step stress test, count reconciliation, find the lock in Build C, prove the fix with r2 and r3 |
| [[ict3113-pod-lab-wk12-slow-endpoint\|Wk 12 Lab (Lec08): Diagnosing a Slow Endpoint]] | Four-question lab: spot the pressure, find the cause, choose the fix, check the knee moved (connection pool, hold time, three causes) |

---

## Planned Topics (Future Lectures)

| Topic | When | Notes |
|-------|------|-------|
| ~~Profiling (Lab 1)~~ | Wk 2 | ✅ Ingested — [[python-profiling]], [[ict3113-lab1-profiling]] |
| ~~Workload Identification~~ | Wk 3 | ✅ Ingested — [[workload-identification]] |
| Performance Modelling I | Wk 4 | Queues and Little's Law |
| Performance Modelling II | Wk 5 | M/M/1, performance bounds, execution models |
| LLM Inference Performance | Wk 8 | TTFT, tokens/s, batching, GPU utilisation |
| Agentic AI Performance | Wks 9–10 | Agent loop as execution model; tool call fan-out. *Lec10 introduces the harness ([[agent-harness]]); agent loops under load are still to come* |
| Docker for Performance | Wk 11 | Resource limits as capacity planning |
| Kubernetes for Performance | Wk 12 | HPA as control loop over utilisation |

---

## Related Areas

- [[software-verification-validation]] — ICT3112; complementary module on software quality; testing verifies system meets spec, performance engineering measures how well it meets it
- DevOps / Deployment area (Docker, Kubernetes, GitHub Actions)
- [[database-indexing-transactions]] — indexing as a classical performance optimisation
