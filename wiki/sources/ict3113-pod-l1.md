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

## Linked Concepts

- [[concepts/performance-engineering]] — core philosophy, measure/model/optimise/deploy loop
- [[concepts/performance-metrics]] — detailed reference: metric properties, response time, percentiles, utilisation law
