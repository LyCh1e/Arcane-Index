---
type: source
title: "ICT3113 POD — Lecture 1: Course Overview"
source_file: "raw/ICT3113 Performance Optimisation and Design - Lec01 Course Overview.md"
domain: performance-engineering
tags: [ict3113, performance-engineering, performance-optimisation, course-overview]
created: 2026-08-31
---

# Source Index — ICT3113 POD Lecture 1: Course Overview

Course: **ICT3113 Performance Optimisation and Design** — A/Prof Donny Soh  
Singapore Institute of Technology

---

## Module Philosophy

**Performance engineering**: measuring, modelling and optimising how software systems behave under load.

The module is built around a four-phase loop:

| Phase | Activity |
|-------|---------|
| **Measure** | Quantify what a system is doing: latency, throughput, utilisation, and the workload driving them |
| **Model** | Predict behaviour before it happens: queueing models and execution models that say where the limit is |
| **Optimise** | Improve it: indexing, caching, concurrency, algorithmic changes — verified by measurement |
| **Deploy** | Keep the gains in production: container resource limits and autoscaling as performance controls |

**Module goal**: take a system you did not write, measure it, model where its bottleneck is, fix it, and show with numbers that the fix worked.

---

## Module Structure — Four Phases

| Phase | Weeks | Topic |
|-------|-------|-------|
| **MEASURE** | 2–3 | Metrics and workload identification |
| **MODEL** | 4–5 | Queues, Little's Law, execution models |
| *(Midterm — Wk 6, Break — Wk 7)* | | |
| **APPLY TO AI** | 8–10 | LLM inference, agentic AI loop performance |
| **DEPLOY AND SCALE** | 11–12 | Docker and Kubernetes |

Weeks 2–5 are the foundational measurement/modelling/optimisation content. Everything after the break applies these methods to new workloads — no new theory introduced.

---

## 14-Week Schedule

| Wk | Lecture | Lab |
|----|---------|-----|
| 1 | Course overview and introduction | No lab |
| 2 | Performance Metrics | Introduction to Profiling |
| 3 | Workload Identification | JMeter |
| 4 | Performance Modelling I | JMeter / load testing |
| 5 | Performance Modelling II | Modelling exercises |
| 6 | **Midterm** | — |
| 7 | Trimester break | — |
| 8 | LLM Inference: Measurement and Optimisation | LLM performance lab |
| 9 | Agentic AI 1: harness as a performance system | Agentic AI |
| 10 | Agentic AI 2: modelling and optimising agent loops | Agentic AI |
| 11 | Docker: deploying for performance (industry — Dell/VMware) | Docker Fundamentals |
| 12 | Kubernetes: scaling for performance (industry — Dell/VMware) | Docker Fundamentals |
| 13 | Revision | Kubernetes Fundamentals |
| 14 | **Exam week** | — |

---

## Assessment

| Weight | Component | Details |
|--------|-----------|---------|
| **25%** | Midterm | Week 6, individual. Covers Wks 2–5: metrics, workload, modelling |
| **35%** | Final exam | Week 14, individual. Covers Wks 8–12, plus integration with Wks 2–5 methods |
| **35%** | Project | Group work across trimester. Brief released separately |
| **5%** | Group formation | Professionalism component. Form by end of Wk 2 |

**Key note**: Weeks 2–5 material is examined **twice** — directly in the midterm, and again in the final through application (e.g. modelling an inference server as a queue, reasoning about autoscaling from measured utilisation).

---

## Topic Previews

### Weeks 2–5: Fundamentals
- **Wk 2 — Performance Metrics**: latency, throughput, utilisation, percentiles — what to measure and how to report it honestly
- **Wk 3 — Workload Identification**: characterising what a system is actually asked to do (measurement without its workload means nothing)
- **Wk 4 — Performance Modelling I**: queues and Little's Law — relating jobs in system, arrival rate, and time in system
- **Wk 5 — Performance Modelling II**: M/M/1, performance bounds, execution models — predicting the limit before hitting it

Classical optimisation techniques (indexing, caching, concurrency, algorithmic improvement) appear as demonstrations within these weeks.

### Weeks 8–10: AI Workloads
- **Wk 8 — LLM Inference**: time to first token, tokens per second, batching, utilisation — measured with Wk 2 tools
- **Wk 9 — Agentic AI 1**: agent loop as an execution model; timeouts, retries, caching as performance mechanisms
- **Wk 10 — Agentic AI 2**: inference server as queueing system; Wk 4–5 models applied to agent loops

### Weeks 11–12: Deploy and Scale (Industry Sessions — Dell/VMware)
- **Wk 11 — Docker**: container resource requests and limits as capacity planning in YAML; getting them wrong is a performance decision
- **Wk 12 — Kubernetes**: horizontal pod autoscaler is a control loop over utilisation; reads a Wk 2 metric and acts on it

---

## Teaching Approach

Every claim in this module is something that can be reproduced in a lab — measurable phenomena, not facts to memorise.

| Demonstration | Description |
|--------------|-------------|
| **Query plan before and after** | Same query with and without an index; EXPLAIN ANALYZE output read, not asserted |
| **Cache hit-rate arithmetic** | Moving from 90% to 99% hit rate; small percentage, large effect on mean latency |
| **Throughput curve** | Throughput rising as threads are added, then falling — students produce this themselves |
| **Profiling AI-generated code** | Profiler catching an O(n²) routine an AI assistant wrote — generated code is not exempt from measurement |

---

---

## Transcript Additions (Live Lecture)

*Source: `raw/ICT3113 Performance Optimisation and Design - Lec01_transcript.md`*

The live Lec01 recording covered the course overview and then proceeded directly into performance metrics content. Key additions not fully captured in the slide deck:

### Context — AI-Generated Code and Scale

> "Especially in today's age of AI, we generate code very frivolously. It may work at a very small scale, but as the scale gets larger, you may find your systems are not performing as well. That is where you need to do things preemptively."

The module's practical framing: generated code is not exempt from measurement. A profiler catching an O(n²) routine an AI assistant wrote is the canonical lab demonstration.

> "Our value doesn't come from writing code. Our value comes from giving solutions. We are here to solve people's problems — through technical means."

### W/S/R Classification Exercises

**Exercise 1 — Larry the Procrastinator**

Context: instructor = client; Larry = server; service time = time Larry spends **actively working** on the lab; everything else = wait time.

Timeline (transcript, approximate):
- Goes to washroom, combs hair, sets up laptop → **wait time**
- Works on Lab Part 1 (2 min) → **service time**
- Distraction / interruption → **wait time**
- Works on Lab Part 2 (8 min) → **service time**
- Submits → response complete

Service time = 2 + 8 = **10 min**. Everything else is wait. The response time runs from "request issued" to "lab submitted" — time spent after submission is not counted.

Key teaching point: service time is the resource's active processing time, not the elapsed calendar time. A student who spends 3 hours procrastinating before a 10-minute task has a response time of 3h10m and a service time of 10 minutes.

**Exercise 2 — Healthcare: Polyclinic Visit**

| Phase | Duration | Type |
|-------|----------|------|
| Queue before registration | 25 min | Wait (W) |
| Doctor consultation | 10 min | Service (S) |
| Waiting for results / next stage | 15 min | Wait (W) |
| Follow-up procedure | 5 min | Service (S) |
| **Total** | **55 min** | R = W + S |

- Total service time: 10 + 5 = **15 min**
- Total wait time: 25 + 15 = **40 min**
- Proportion of visit spent waiting: 40 / 55 ≈ **73%** — a queue-dominated experience

**Key insight:** reducing service time also reduces wait time, not just service time. If consultation drops from 10 to 7 minutes, the doctor is free 3 minutes earlier; the next patient enters service sooner; the queue clears faster across all subsequent patients. The wait-time saving compounds.

> "If you reduce the consultation time, it's not necessarily that you only reduce by those minutes. If you reduce this, right, you actually can reduce the wait as well. That is one thing that many people don't realise."

This is why service-time optimisation matters even when wait time dominates response time — it propagates backwards through the queue.

### Percentile Exercise — SLO Selection

A/Prof Soh presented 10 response-time samples and asked students to compute:

| Statistic | Value | Notes |
|-----------|-------|-------|
| Mean | 298.3 ms | Pulled high by slow outliers; misleading as a target |
| P50 (median) | 111 ms | Mean of 5th and 6th sorted values — the "typical" request |
| P90 | 120 ms | 9th value in sorted order — the upper boundary for 90% of requests |

**SLO selection logic:**

- The mean is not a useful SLO: it misrepresents the typical user's experience and does not bound the tail.
- The median (P50) describes the typical request but makes no promise about the half above it.
- **P90 (120 ms)** is the defensible SLO: it commits that 90% of users receive a response within 120 ms, and makes the remaining 10% explicitly visible.

> "You want to guarantee that 90% of your customers are happy — then 120 will be your service level objective."

### Arrival Rate Exercises

**Exercise A — Larry's Labs (Student Context)**

| Parameter | Value |
|-----------|-------|
| Modules enrolled | 4 |
| Labs per module per week | 1 |
| Normal arrival rate (demand) | 4 labs/week |
| Maximum throughput (weeks 9–12) | 5 labs/week |
| Weeks 1–8 throughput = demand | 4 labs/week (no backlog) |
| Weeks 9–12 arrival rate | 5 labs/week |
| Total expected (demand) | 48 labs |
| Total actually completed | 44 labs |
| Shortfall | 4 labs (≈ 8.3%) |

When demand exceeds throughput, X < λ: the system falls behind. The shortfall of 4 labs represents uncompleted work — not dropped (Larry eventually does them), but deferred, increasing his WIP and response time for each outstanding lab.

**Exercise B — Semiconductor Factory**

| Day | Condition | Output |
|-----|-----------|--------|
| Monday–Tuesday | Full capacity (1,200 units/day) | 2,400 |
| Wednesday | Machine breakdown — half capacity | 600 |
| Thursday–Friday | Overtime (1,400 units/day) | 2,800 |
| **Weekly total** | | **5,800 units (approx)** |

- Target throughput: 1,200 × 5 = **6,000 units/week**
- Actual (with overtime): approximately **5,008 units** (transcript figure)
- Average throughput: 5,008 / 5 ≈ **1,001 units/day** (vs. 1,200 target)
- Shortfall: ≈ **992 units** (≈ 16.5%)

Key message: overtime partially compensates for lost capacity but cannot fully recover time already past. A one-day breakdown at half capacity removes 600 units of output; overtime at +200 units/day for two days adds back only 400. The gap persists.

> "You can tell how bad the situation is — if a machine breaks down, immediately there's a shortfall, even though they try to compensate by doing overtime."

### Demand/Supply Intuition — Labubu Analogy

> "There was this recent craze about a funny soft toy — 'Labubu'. You have a lot of people queuing up. The arrival rate — the demand — is very, very high. The supply was very low. So what happened was that the response waiting time was very, very long."

When λ >> μ: throughput X caps at μ, WIP grows without bound, and response time climbs. Both sides agree (X = λ) only when arrival rate equals throughput: a stable, non-overloaded queue.

---

## Linked Concepts

- [[concepts/performance-engineering]] — core philosophy, measure/model/optimise/deploy loop
- [[concepts/performance-metrics]] — detailed reference: metric properties, response time, percentiles, utilisation law
