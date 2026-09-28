---
type: concept
title: "Performance Engineering"
domain: performance-engineering
complexity: high
status: established
created: 2026-08-31
updated: 2026-08-31
tags: [performance-engineering, performance-optimisation, bottleneck-analysis, profiling, measurement, queueing-theory, ict3113]
---

# Performance Engineering

Performance engineering is the discipline of measuring, modelling, and optimising how software systems behave under load. It treats performance as a first-class engineering concern — something to be measured before any optimisation is attempted, and verified after.

---

## The Measure → Model → Optimise → Deploy Loop

All performance work follows the same four-phase cycle:

| Phase | What happens | Key tools and techniques |
|-------|-------------|--------------------------|
| **Measure** | Quantify what the system is doing — latency, throughput, utilisation, and the workload driving them | Profilers, load generators (JMeter), observability dashboards |
| **Model** | Predict behaviour before hitting the limit — where is the bottleneck? | Queueing models, Little's Law, M/M/1, execution models, utilisation bounds |
| **Optimise** | Improve the bottleneck — algorithmic improvement, indexing, caching, concurrency | Code changes verified by re-measurement, not intuition |
| **Deploy** | Keep the gains in production — enforce resource bounds and scaling policies | Container resource limits, Kubernetes HPA, autoscaling policies |

The loop is cyclic: after deploying, re-measure to confirm the gain held and to find the next bottleneck.

---

## Foundational Principle: Measure First

> *"Take a system you did not write, measure it, model where its bottleneck is, fix it, and show with numbers that the fix worked."*
> — ICT3113 module goal

Optimising without measuring is guessing. Fixes that are not verified with numbers may have had no effect, or may have shifted the bottleneck elsewhere.

**Profiling AI-generated code**: tools and AI assistants can write code that passes tests but contains O(n²) routines invisible to the author. A profiler finds these; intuition does not. Generated code is not exempt from measurement.

---

## When to Optimise

Performance engineering deals with trade-offs, not universal rules. Three conditions that justify optimisation:

1. **A bottleneck has been identified by measurement** — not suspected, not guessed
2. **The gain is significant enough to justify the cost** — Amdahl's Law bounds the maximum benefit of optimising one component
3. **The fix can be verified with numbers** — A/B comparison or before/after measurement under the same workload

Optimising the wrong component wastes effort and may make the system harder to maintain without improving user experience.

---

## Classical Optimisation Techniques

These appear throughout performance engineering regardless of workload type:

| Technique | Mechanism | Typical effect |
|-----------|----------|---------------|
| **Indexing** | Adds a lookup structure so queries avoid full scans | Query time drops from O(n) to O(log n) |
| **Caching** | Stores results of expensive operations for reuse | Reduces service time; effect depends on hit rate (90%→99% hit rate: large mean latency reduction) |
| **Concurrency** | Runs work in parallel; throughput rises until a resource saturates | Throughput increases then falls as contention grows — produces the classic throughput curve |
| **Algorithmic improvement** | Replaces O(n²) with O(n log n), etc. | Scales better; verified by profiling the hot path |

---

## Application to AI Workloads

The same measure → model → optimise → deploy loop applies directly to LLM and agentic AI systems:

### LLM Inference Servers

An inference server is a server. The performance vocabulary is the same:

| AI metric | General performance metric |
|-----------|--------------------------|
| Time to first token (TTFT) | Response time — first byte |
| Tokens per second | Throughput |
| Batch size | Service capacity |
| GPU utilisation | Device utilisation |

The inference server is a **queueing system** (requests arrive, wait, are processed). M/M/1 and utilisation bounds apply directly.

### Agent Loops

An agent loop is an execution model with real numbers:

- **Timeout values** → maximum acceptable wait time per hop
- **Retry policies** → add to expected response time under failure; affect tail latency
- **Caching** → reduces round trips; cache hit rate arithmetic applies
- **Tool call fan-out** → each external call adds to response time; tail latency fan-out formula applies

Modelling an agent loop: identify the critical path (longest chain of sequential operations), find the bottleneck (highest utilisation component), and optimise that component.

---

## Deploy and Scale

Production systems are run with **headroom** — deliberate excess capacity — because near-100% utilisation causes non-linear increases in queueing delay. Deployment artefacts enforce performance policies:

| Tool | Performance role |
|------|-----------------|
| **Docker resource limits** | Prevent one container from starving others; define the capacity μ that drives U = XS |
| **Kubernetes HPA** | Reads a utilisation metric (from Wk 2) and scales pod count; autoscaling is applied performance engineering |

Container resource limits and autoscaling are not configuration details — they are capacity planning enforced in YAML.

---

## JMeter Test Plan Design

Before a test can be run, the **Thread Group parameters** must be derived from a workload description. The bridge between workload parameters and JMeter settings is **Little's Law** (L = λW — see [[concepts/performance-metrics]]).

### Deriving Thread Group settings

Given: total users N, arrival window T (seconds), average session time W (seconds):

```
λ = N / T                         (arrival rate)
L = λ × W = (N / T) × W          (concurrent users)
Cap: L = min(L, N)                (cannot exceed total users)

JMeter Thread Group:
  Number of Threads = N  (total users in the run)
  Ramp-up Period    = T  (how long to reach full load)
  Loop Count        = 1  (single session per user)

To hit a target concurrency L given known W:
  Ramp-up = N × W / L
```

### Think-time timers

Two JMeter timers model user dwell time between successive requests within a session:

| Timer | Behaviour | Use case |
|-------|-----------|----------|
| **Constant Timer** | Fixed delay of D milliseconds | Scripted workflows with known, fixed pauses |
| **Gaussian Random Timer** | Gaussian delay: mean = Deviation + Constant Delay Offset | Realistic pacing where dwell time varies around an average |

Timers are placed *between* HTTP Request samplers in the Thread's sampler chain.

### APDEX

The **Application Performance Index** (0–1) is reported in JMeter's HTML dashboard:

- **T** (toleration threshold, default 500 ms): requests ≤ T → satisfied.
- **F** (frustration threshold, default 1 500 ms): requests > F → frustrated.
- APDEX = (Satisfied + 0.5 × Tolerating) / Total.
- A score of 0.000 means every request exceeded the toleration threshold — a clear signal the system is under distress or artificially slowed (e.g. `time.sleep(5)` in the route).

### Non-GUI mode

```bash
jmeter -n -t plan.jmx -l results.csv -e -o report/
```

Always validate the test plan in GUI mode first (Thread Group → HTTP Request → View Results Tree), then switch to non-GUI mode for the actual load run.

---

## Execution Models (Pre-System Estimation)

When a system does not yet exist, service times cannot be measured. The solution is an **execution model**: an annotated UML activity or sequence diagram where each activity carries a time estimate and each branch a probability (Smith & Williams, 2001).

Solve the model as follows:

| Structure | Computation |
|-----------|-------------|
| Sequential tasks | Sum the times |
| Parallel / async tasks | Take the maximum |
| Branch | Σ p(branch) × t(branch) |

**Example:** 10 ms decision → async 30 ms network call; while waiting, build response (50%: 12 ms, 40%: 25 ms, 10%: 40 ms).  
Branch expected time = (0.5×12) + (0.4×25) + (0.1×40) = **20 ms.** Async network (30 ms) > build (20 ms) → parallel max = 30 ms. **Total = 10 + 30 = 40 ms.**

Execution models support the **Model** phase before a system is built; they feed demand estimates into the bounds analysis (see [[concepts/queueing-theory]] §8).

---

## Key Connections

- [[concepts/performance-metrics]] — detailed reference: metric properties, response time, percentiles, utilisation law, queueing fundamentals; Little's Law
- [[concepts/queueing-theory]] — analytical toolkit: M/M/c queues, operational laws, bottleneck analysis, Kingman formula; bounds (§8) and Erlang B (§9)
- [[concepts/docker-compose]] — container resource configuration
- [[concepts/database-indexing-transactions]] — database indexing as a performance optimisation
- [[sources/ict3113-pod-l1]] — module overview and structure
- [[sources/ict3113-pod-l2]] — performance metrics and modelling fundamentals
- [[sources/ict3113-pod-l5]] — Lec05: performance bounds, execution models, Erlang B (lost work)
- [[sources/ict3113-pod-l6]] — Lec06: JMeter test plan sizing, Little's Law applied, timers, APDEX
