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

## Performance Testing

Performance testing checks the model's predictions against a real running system. It is the **Measure** phase in the cycle, done under controlled conditions so that results are reproducible and comparable.

### Four documents carry performance work from requirement to operations

| Document | Contains | Audience |
|---|---|---|
| **Performance requirements document** | Each requirement: what, how much, under what conditions, measured how, traced to what need | Everyone — it is the contract |
| **Performance measurement plan** | Instruments: which tool measures which quantity, where it runs, what it costs | Testers and operations |
| **Performance test plan** | Tests: type, load model, environment, playbook, pass/fail criteria | Testers |
| **Capacity management plan** | Post-deployment monitoring and trigger conditions for more hardware or redesign | Operations |

---

### Writing a performance requirement — Bondi's 10-field structure

A well-formed performance requirement has ten fields (Bondi 2015, Table 7.2). Fields 3, 6, 8, and 9 are where requirements most often fail.

| # | Field | What it holds |
|---|---|---|
| 1 | Requirement number | Stable identifier (PERF-01) that tests and results reference |
| 2 | Title | Short name: "Order creation response time" |
| 3 | **Statement** | The requirement in one sentence: metric, statistic, condition, time scale |
| 4 | Supporting commentary | Known exclusions, context not in the statement |
| 5 | Precedents / sources | Where the number came from (study, regulation, prior system) |
| 6 | **Derivation** | The arithmetic connecting the workload model to this number |
| 7 | Dependent requirements | Other requirements that assume this one holds |
| 8 | **Assumptions** | Load level, hardware, data state, config under which the requirement applies |
| 9 | **Measurement** | Instrument, procedure, run window — how to decide pass or fail |
| 10 | Subject matter expert | Named person who owns this requirement |

**Worked example — PERF-01:**
> "95% of POST /orders requests shall complete within 200 ms, measured at the load generator, when the service is offered 10 requests per second (open loop) for a sustained 10-minute window on the reference hardware."

Derivation: 10/s is the weekday evening peak (36,000 orders/hr, 2.5× daily average). 95th percentile so one slow request in twenty is tolerated.

**Sentence patterns (Eckhardt et al. 2016):** pick one entry per column:

| Condition | Subject | Modal | Statistic | Comparison | Quantity | Unit |
|---|---|---|---|---|---|---|
| In 95% of all cases | the system / the operation | shall / must not | mean / p50 / p95 / max response time | of less than / no more than | *n* | ms / s |
| Under a load of *x*/s | the component | should | transaction rate | of at least | *n* | req/s |

**Quality checks:** unambiguous (names the request, statistic, window), measurable (names the instrument), verifiable (written procedure), complete (all parameters stated), consistent (not contradicted by Little's Law or hardware), traceable (fields 5 and 6), time scale stated (averages over a day hide the peak).

---

### Open-loop vs closed-loop load

The choice of load model changes what you are measuring.

| | Closed loop (JMeter standard Thread Group) | Open loop (JMeter Open Model Thread Group / k6 constant-arrival) |
|---|---|---|
| **Mechanism** | Each virtual user waits for its response before sending the next request | Requests arrive at a fixed rate regardless of whether earlier ones have been answered |
| **Offered load** | N / (response time + think time) — backs off automatically as the system slows | λ req/s, constant — queue grows if the system falls behind |
| **Models** | Browser/human sessions where users wait | Real web traffic; matches the queueing models from Lectures 04–05 |
| **Risk** | A slow system receives less load, masking saturation | A slow system receives the same load, revealing saturation accurately |

**Rule:** Use open-loop generation for any test whose result will be compared with a queueing model prediction. A closed-loop result cannot be compared with M/M/1 or utilisation-bound predictions.

---

### Six types of performance test

Each type answers a different question. Using the wrong test gives a correct answer to the wrong question.

| Type | Question | What varies | What you look for |
|---|---|---|---|
| **Load test** | Does it meet its targets at the expected load? | Nothing — hold expected load steady | Response time flat, throughput = offered rate, error rate ≈ 0 |
| **Stress test** | Where does it break, and how? | Load, upward past the expected range | The knee (p95 starts climbing), the ceiling (throughput stops rising), the failure mode (slow vs errors vs crash) |
| **Soak test** | Does it stay healthy over time? | Time — hold steady load for hours | Memory slope (leak = straight line, no plateau), response-time drift, open connections, log file growth |
| **Regression test** | Did the last change make it slower? | The build — same test, new code | p95 and throughput vs baseline; threshold for what counts as a regression |
| **Benchmark** | How does it compare to a standard or baseline? | The system/candidate — fixed load | Numbers side by side; one variable changed per comparison |
| **Pipe-clean test** | Is the test itself correct? | Nothing at low load — validate the plumbing | Assertions that cannot fail; response times in plausible range; counts reconcile between generator and server log |

**Pokémon Go case study (2016):** Niantic planned for 5× expected traffic and got 50×. A load test at 5× would have passed and said nothing about 50×. A stress test would have found the ceiling and — critically — revealed the failure mode: complete unavailability rather than graceful slowdown. Knowing the failure mode in advance enables the architectural fix (admission control / waiting room) before launch.

#### Reading a stress-test results table

| offered/s | p95 | throughput | err% | Reading |
|---|---|---|---|---|
| 5 | 0.36 s | 5.00 | 0 | Below knee; U ≈ 0.36 |
| 10 | 2.24 s | 9.30 | 0 | Past knee; queue forming; U ≈ 0.71 |
| 15 | 8.82 s | 12.85 | 0.9 | At ceiling; first errors |
| 20 | 12.16 s | 12.98 | 31.6 | Over ceiling; throughput flat; one in three refused |
| 30 | 11.79 s | 15.33 | 50.2 | Half refused; p50 falls (fast failures count) |

Read the `throughput` column for the ceiling, the `p95` column for the knee, and the `err%` column for the failure mode.

**p50 falling as load rises** means the failure path is faster than the success path — fast errors drag the median down. This is not a good sign; look at the error column.

#### The soak test slope

Report the **slope** (MB/min, connections/min), not the absolute growth over the run. From the slope, extrapolate the time to failure.

Demo result: service memory grew from 33 MB to 68 MB over 10.5 minutes (+3.4 MB/min). Predicted: 1.9 MB/min (4 kB/order). Observed 3.4 MB/min (Python object overhead ≈ 7 kB/order). Extrapolated time to fill 16 GB: ~3.3 days at this load.

#### Regression test: fix the test, change only the build

The test must be identical across builds: same plan, load, data, environment, playbook. One change per build makes the cause of a regression identifiable. Many changes per build makes it guesswork.

Demo result: adding an O(n) duplicate check (scan all orders) produced p50 +30%, p95 +45% at 5 req/s. The slope (cost growing with store size) only became visible on a longer run or at higher load — the first run found the regression; a longer run explained the mechanism.

#### Benchmark: the load is the standard, the system varies

- **External benchmarks** (TPC, MLPerf, SPEC): compare products against a fixed workload.
- **Internal benchmarks**: compare candidates (two models, two configurations, two hosting options) under the same load.
- One variable per comparison. A benchmark result without its load attached is not a result — the ranking depends on the load.

Demo result (PBKDF2 iterations): 25k → p95 110 ms; 100k → p95 480 ms (×4, because hash is most of the request on one core); 400k → near-total collapse (83% timeouts, throughput 0.8/s against ceiling 2.5/s). The collapse occurred because clients abandoned requests after 20 s while the server kept hashing — wasted CPU on work nobody was waiting for. Throughput fell *below* the ceiling, not to it.

#### Pipe-clean: a green result means the test ran, not that the system worked

Demo result: broken catalogue path, no body assertion → generator reported 100% success, p95 39 ms, 4.9/s. Server: 0 orders created, every request an error body returned with HTTP 200. The response time (39 ms vs expected 360 ms) was the only giveaway — caught by comparing with the written-down prediction.

**Rules:**
1. Assert on the body (`order_id` present), not only the status code.
2. Compare every result with the prediction before reporting it. A number outside the plausible range is a test defect until shown otherwise.
3. Reconcile counts: samples in the .jtl, lines in the server log, records in the data store. All three must agree.

---

### Test environment

#### Must match production in structure, not just size

| Aspect | Requirement |
|---|---|
| **Configuration** | Same OS family, runtime versions, server settings. A different Python version or worker count is a different system. |
| **Data** | Realistic in size, distribution, and shape. Ten records behave differently from a million. |
| **State** | Record system state at the start and end of each run. A store that grew during the run changes the baseline for the next. |
| **External dependencies** | Replace anything unavailable (third-party APIs, hardware) with a stub that reproduces its delay and failure behaviour. |
| **Network** | Generator and service on separate machines where possible. Same machine removes network delays and creates CPU contention. |

#### Scale-up vs scale-out

Two ways to test a production system (e.g. 3 web servers + 1 DB at load L) in a smaller environment:

| Option | What it tests | What it misses |
|---|---|---|
| **Scale-out:** one production-identical web server at L/3 | One node at its real per-node share | Load balancer, shared DB under full load, inter-server network |
| **Scale-up:** one web server with 1/3 the CPU/RAM at L/3 | Shape at reduced size | Everything above, plus interactions that only appear at full resource counts |

**Always write down what the scaled-down environment does not test. That list is as much a result as the numbers.**

Ceiling and memory lifetime do not scale together: ceiling = c/S (scales with cores); time to soak failure = free RAM / (bytes/order × rate) (scales with RAM). Cutting cores by one-third changes the first without changing the second.

#### The observer effect

Measurement tools are processes. They compete with the service under test for CPU and memory. Timing calls and extra logging add work to the request path. The practical rule: **measure the cost of measuring once, then decide what to leave on.**

---

### Playbook structure

A playbook is a written procedure another person can follow to reproduce the result. It must specify:

- **Machine** for every step (generator vs service host)
- **Exact commands** written out, not described
- **File paths and naming conventions** (date and run number in every artefact name)
- **Start state and end state** recorded so changes between runs are visible

Minimum phases:

**A. Initialise:** log the run (date, commit hash); record config (build, iterations, catalogue path); start service from empty store; confirm `/health` reports 0 records; clear server log; record free memory and CPU idle; start monitor.

**B. Run:** pipe-clean step first (one request by hand, check body and response time); then run the generator; do not touch either machine during the run.

**C. Record:** copy server log and monitor CSV to the repo; copy the .jtl; record end state (records in store from `/health`, free memory, request count in log equals samples in .jtl). If counts disagree, discard the run.

**Minimum runs:** three per configuration. One run gives a number; three runs show whether the number means anything.

---

### Load model elements

| Element | Notes |
|---|---|
| **User types** | Each distinct behaviour gets its own script; mix must match the workload model (Lecture 03), not what is easiest to script |
| **Think time** | Pause between requests within a session; zero think time turns a user into a tight loop and changes the load completely |
| **Pacing** | Ramp-up over minutes tests steady state; big-bang start tests the startup transient; ramp-down tests recovery |
| **Load profile** | Flat (load test), stepped (stress), spike, or replayed production trace |
| **Duration** | Long enough to pass warm-up and reach steady state; report numbers from the steady window only |

Scripts come from use cases, not from functional test cases. They represent what a typical user does over a session with realistic data and realistic pauses. Data comes from a file the script reads, not from constants in the script.

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
- [[sources/ict3113-pod-l7]] — Lec07: performance testing — six test types, open/closed loop, test environment, playbook
