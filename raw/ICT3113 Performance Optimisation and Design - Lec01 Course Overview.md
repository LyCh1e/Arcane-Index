# ICT3113 Performance Optimisation and Design
## Lecture 1: Course Overview

**Presented by** A/Prof Donny Soh
Programme Leader, Applied Artificial Intelligence
Programme Leader, SITxNVIDIA (SNAIC) AI Training
InfoComm Technology (ICT) Cluster
Singapore Institute of Technology

*SingaporeTech.edu.sg — SIT Internal*

---

## What this module is about.

**Performance engineering:** measuring, modelling and optimising how software systems behave under load.

| | |
|---|---|
| **Measure** | Quantify what a system is doing: latency, throughput, utilisation, and the workload driving them. |
| **Model** | Predict behaviour before it happens: queueing models and execution models that say where the limit is. |
| **Optimise** | Improve it: indexing, caching, concurrency and algorithmic changes, verified by measurement. |
| **Deploy** | Keep the gains in production: container resource limits and autoscaling as performance controls. |

By the end of the trimester you should be able to take a system you did not write, measure it, model where its bottleneck is, fix it, and show with numbers that the fix worked.

---

## Learning outcomes.

On completing this module you should be able to:

1. Describe and distinguish the different factors that affect the performance of a computer system.
2. Establish requirements for the performance of a computer system.
3. Develop and apply appropriate metrics for evaluating the performance of computer systems.
4. Use performance profiling and monitoring tools to evaluate the performance of a computer system.
5. Identify performance bottlenecks and anti-patterns.
6. Analyse trade-offs of an optimisation point and make correct decisions on whether to conduct optimisation.
7. Recommend, apply and evaluate improvements to the performance of a computer system.

---

## The module in one line.

**MEASURE** (Weeks 2 to 3) → **MODEL** (Weeks 4 to 5) → **APPLY TO AI** (Weeks 8 to 10) → **DEPLOY AND SCALE** (Weeks 11 to 12)

- **MEASURE** — Weeks 2 to 3: Metrics and workload identification
- **MODEL** — Weeks 4 to 5: Queues, Little's Law, execution models
- **APPLY TO AI** — Weeks 8 to 10: LLM inference and agent loops
- **DEPLOY AND SCALE** — Weeks 11 to 12: Docker and Kubernetes

Weeks 2 to 5 are the measurement, modelling and optimisation fundamentals. Everything after the break applies them to new workloads.

**Week 6:** midterm. **Week 7:** trimester break. **Week 13:** revision. **Week 14:** exam week.

---

## The 14-week schedule.

| Wk | Lecture | Lab |
|---|---|---|
| 1 | Course overview and introduction to performance engineering | No lab |
| 2 | Performance Metrics | Introduction to Profiling |
| 3 | Workload Identification | JMeter |
| 4 | Performance Modelling I | JMeter / load testing |
| 5 | Performance Modelling II | Modelling exercises |
| 6 | **Midterm** | — |
| 7 | Trimester break | — |
| 8 | LLM Inference: Measurement and Optimisation | LLM performance lab |
| 9 | Agentic AI 1: the harness as a performance system | Agentic AI |
| 10 | Agentic AI 2: modelling and optimising agent loops | Agentic AI |
| 11 | Docker: deploying for performance (industry session) | Docker Fundamentals |
| 12 | Kubernetes: scaling for performance (industry session) | Docker Fundamentals |
| 13 | Revision | Kubernetes Fundamentals |
| 14 | **Exam week** | — |

---

## Weeks 2 to 5: the fundamentals.

Measurement, modelling and optimisation: the core of the module and the full scope of the midterm.

**Week 2 — Performance Metrics**
Latency, throughput, utilisation and percentiles: what to measure and how to report it honestly. Lab: profiling a running program.

**Week 3 — Workload Identification**
Characterising what a system is actually asked to do, because a measurement without its workload means nothing. Lab: JMeter.

**Week 4 — Performance Modelling I**
Queues and Little's Law: relating the number of jobs in a system, their arrival rate and their time in the system. Lab: JMeter and load testing.

**Week 5 — Performance Modelling II**
M/M/1, performance bounds and execution models: predicting the limit of a system before you hit it. Lab: modelling exercises.

Classical optimisation techniques (indexing, caching, concurrency, algorithmic improvement) appear as demonstrations inside these weeks rather than as separate topics.

---

## Weeks 8 to 10: performance engineering for AI workloads.

The same methods from weeks 2 to 5, applied to a workload that did not exist a few years ago.

**Week 8 — LLM Inference: Measurement and Optimisation**
An inference server is a server: time to first token, tokens per second, batching and utilisation. We measure it with the tools from week 2.

**Week 9 — Agentic AI 1: the harness as a performance system**
An agent loop is an execution model with real numbers attached. Timeouts, retries and caching in the harness are performance mechanisms, and we treat them as such.

**Week 10 — Agentic AI 2: modelling and optimising agent loops**
The inference server behind an agent is a queueing system, so the week 4 and 5 models apply directly. We model the loop, find its bottleneck, and optimise it.

These weeks introduce no new theory. They apply the weeks 2 to 5 material to AI systems.

---

## Weeks 11 to 12: deploying and scaling for performance.

Industry sessions delivered with Dell / VMware.

**Week 11 — Docker: deploying for performance**
Container resource requests and limits are capacity planning enforced in YAML. Getting them wrong is a performance decision, not a configuration detail. Lab: Docker Fundamentals.

**Week 12 — Kubernetes: scaling for performance**
The horizontal pod autoscaler is a control loop over utilisation: it reads a metric from week 2 and acts on it. Scaling policy is applied performance engineering. Lab: Docker Fundamentals, then Kubernetes Fundamentals in week 13.

These two weeks close the loop of the module: the numbers you learn to measure in week 2 are the numbers a production cluster acts on automatically.

---

## The lab sequence.

Labs run alongside lectures and build on each other. There is no lab this week.

| Wk | Lab | Description |
|---|---|---|
| 2 | Introduction to Profiling | Find where time actually goes in a running program. |
| 3 | JMeter | Generate load and measure the response. |
| 4 | JMeter / load testing | Design load tests that reflect a real workload. |
| 5 | Modelling exercises | Apply Little's Law and M/M/1 to measured data. |
| 8 | LLM performance lab | Measure an inference workload. Details released nearer the date. |
| 9–10 | Agentic AI | Instrument and optimise an agent loop. |
| 11–12 | Docker Fundamentals | Containerise and set resource limits. |
| 13 | Kubernetes Fundamentals | Deploy and autoscale what you containerised. |

---

## Assessment.

| Weight | Component | Details |
|---|---|---|
| 25% | **Midterm** | Week 6, individual. Covers weeks 2 to 5: measurement, modelling and optimisation fundamentals. |
| 35% | **Final exam** | Week 14 exam week, individual. Covers weeks 8 to 12 plus integration across the module. |
| 35% | **Project** | Group work across the trimester. Details in the project brief, released separately. |
| 5% | **Group formation** | Professionalism component. Form your project groups by the end of week 2. |

The two written assessments are in weeks 6 and 14. The project runs across the trimester; the brief will be released separately.

---

## What each written assessment covers.

**Midterm**
Weeks 2 to 5 only: performance metrics, workload identification, and performance modelling. If it involves Little's Law, M/M/1, bounds or execution models, it can appear here.

**Final exam**
Weeks 8 to 12: LLM inference, agentic AI, Docker and Kubernetes.

Plus integration: questions that apply the week 2 to 5 methods to the post-break material, for example modelling an inference server as a queue, or reasoning about an autoscaling policy from measured utilisation.

The weeks 2 to 5 material is therefore examined twice: directly in the midterm, and again in the final exam through its application.

---

## How the module is taught.

Measurable phenomena, not facts to memorise. Every claim in this module is something you can reproduce in a lab.

| Demonstration | Description |
|---|---|
| **A query plan, before and after** | The same query with and without an index, compared through EXPLAIN ANALYZE. The improvement is read off the plan, not asserted. |
| **Cache hit-rate arithmetic** | What moving a cache from a 90% to a 99% hit rate does to mean latency. Small percentage, large effect, and you can compute it. |
| **The throughput curve** | Throughput rising as threads are added, then falling. You will produce this curve yourself and explain both halves of it. |
| **Profiling AI-generated code** | A profiler catching an O(n²) routine that an AI assistant wrote. Generated code is not exempt from measurement. |

Lectures are built around demonstrations like these, with the slides serving as the record of what was measured.

---

## This week and next.

**This week**
This overview, then we start on Performance Metrics immediately after.
No lab this week.

**Week 2**
Lecture: Performance Metrics continued, the definitions and reporting conventions used for the rest of the module.
Lab: Introduction to Profiling. Bring a laptop you can install software on.

Reading and lab material will be released on the module site before each session. Questions in between sessions: post on the module forum or email me.

---
*SIT Internal — ICT3113 Performance Optimisation and Design, Singapore Institute of Technology*
