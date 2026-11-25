---
type: concept
title: "Machine Learning Foundations"
domain: machine-learning
course: INF2008
complexity: medium
address: c-000026
tags: [machine-learning, AI, supervised, unsupervised, reinforcement, CRISP-DM, business-value]
updated: 2026-05-11
status: established
created: 2026-05-11
---

# Machine Learning Foundations

Machine learning is the subfield of artificial intelligence that gives computers the ability to learn patterns from data without being explicitly programmed *(Arthur Samuel, 1959)*. It emerged as data volumes exceeded what hand-crafted rules could handle.

---

## Why ML Exists — Exponential Technological Trends

Three concurrent exponential growth curves made large-scale ML viable:

| Trend | Law | Rate |
|-------|-----|------|
| Computation speed | Moore's Law | Transistor count doubles ~every 2 years |
| Storage capacity | Kryder's Law | Magnetic storage density growing faster than Moore's Law |
| Network bandwidth | Edholm's / Nielsen's / Butters' Laws | Bandwidth doubles every 18 months; optical fibre data doubles every 9 months |

> "Imagine the impact on our economy if the pandemic had happened 30 years earlier." — Without these trends, remote work and online commerce would have been impossible.

---

## What is AI?

| Definition | Author |
|------------|--------|
| "The study of intelligent agents that perceive their environment and take actions to achieve goals." | Russell & Norvig, 2010 |
| "The activity devoted to making machines intelligent." | Nilsson, 1998 |
| "Socio-technical systems designed to support or augment human decision-making." | Shneiderman, 2020 |

**Working definition (INF2008):** AI as computational systems that support adaptive decision-making, perception, or reasoning in complex environments — without assuming perfect rationality or human equivalence.

### Four Perspectives on AI (Narrow)

| Perspective | Approach |
|-------------|----------|
| Acting Humanly | Turing Test — can a machine fool a human? |
| Thinking Humanly | Cognitive modelling — simulates human reasoning |
| Thinking Rationally | First-order logic — provably correct inference |
| Acting Rationally | Rational agents — maximise expected value of performance measure |

---

## Expert Systems vs Machine Learning

| Approach | Process |
|----------|---------|
| **Expert Systems** | Domain Expert Rules + Data → Output |
| **Supervised ML** | Data + Known Output → Machine learns rules |
| **Unsupervised ML** | Data → Machine discovers structure |
| **Reinforcement ML** | Data + Reward signal → Machine learns rules |

> Expert Systems use rules to produce output. Machine Learning uses output to generate rules.

---

## Types of Machine Learning

### Supervised Learning

Learning a mapping from inputs X to outputs Y, given labelled example pairs (Bishop, 2006).

| Task | Description | Example |
|------|-------------|---------|
| **Classification** | Predict a discrete class label | Spam vs not-spam; fraud detection |
| **Regression** | Predict a continuous numeric value | House price; loan amount |

### Unsupervised Learning

Discovering hidden structure in unlabelled data X — no Y is given (Bishop, 2006).

Examples: grouping news articles, customer segmentation, topic discovery, gene expression clustering.

### Reinforcement Learning

An agent learns by taking actions in an environment and receiving reward signals (Sutton & Barto, 2018). Goal: maximise cumulative reward.

---

## Steps to Train an ML Model

1. **Data Acquisition** — collect samples with sufficient variance per class (~100+ images for vision tasks); include a background class to prevent the model from always predicting known objects.
2. **Modelling** — select algorithm and hyperparameters; feed training data; iterate.
3. **Model Iteration** — add more class data, handle edge cases, identify dataset biases.
4. **Bias Analysis** — test model behaviour across different backgrounds, lighting, object orientations.
5. **Deployment** — release after adequate testing.

---

## CRISP-DM Methodology

**CRoss-Industry Standard Process for Data Mining** — a six-phase, non-linear process for ML projects. Phases are iterative; moving back and forth is normal.

| Phase | Description | Maps to Production Component |
|-------|-------------|------------------------------|
| **Business Understanding** | Define problem, decision, metric, value | Configuration |
| **Data Understanding** | Explore what data exists and its quality | Data Collection |
| **Data Preparation** | Clean, validate, and engineer features | Data Verification / Feature Extraction |
| **Modelling** | Train and tune models | ML Code |
| **Evaluation** | Validate offline before deployment | Analysis Tools |
| **Deployment** | Serve the model in production | Serving Infrastructure |
| *(cross-cutting)* | Workflow orchestration | Process Management, Monitoring |

> In production ML systems, most complexity lies **outside** the model code — in data pipelines, serving infrastructure, and monitoring.

---

## Business Understanding Framework

Before building any model, frame the problem as a business decision:

| Element | Question |
|---------|----------|
| **Problem** | What pain exists today? |
| **Decision** | What decision is currently made poorly, manually, or too late? |
| **Metric** | How do we know if the decision improved? |
| **Intervention** | What information or capability will ML provide? |
| **Value** | What business outcome changes if the decision improves? |

> If value cannot be clearly articulated and quantified, the ML system is probably unnecessary.

### Example — Telco Customer Churn (MoonHub)

- 4 million users; $20/month; 1% monthly churn = 40,000 users lost = **$800k/month = $9.6M/year**
- ML estimates churn risk → customers ranked for retention
- Reducing churn from 1.0% → 0.9% = 4,000 users retained = **$960k/year retained**

### Example — Loan Processing (JuneBank)

- 500,000 applications/year; 7-day average; 10% abandonment = 50,000 apps × $1,000 = **$50M/year lost**
- ML ranks applications by completion likelihood → prioritise for faster review
- Reducing abandonment from 10% → 9% = **$5M additional retained revenue/year**

---

## Related Concepts

- [[ml-data-understanding]] — CRISP-DM phase 2
- [[ml-model-training-evaluation]] — CRISP-DM phases 4–5
- [[decision-trees-and-ensembles]] — core supervised learning algorithms
- [[neural-networks-linear-models]] — linear and neural supervised models
- [[clustering-and-dimensionality-reduction]] — unsupervised learning methods
