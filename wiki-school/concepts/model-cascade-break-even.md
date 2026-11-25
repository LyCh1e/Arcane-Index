---
type: concept
title: "Model Cascade Break-Even (small model first, escalate to large)"
domain: performance-engineering
course: ICT3113
created: 2026-11-13
updated: 2026-11-13
tags: [ict3113, llm-cascade, latency, escalation, performance-testing]
related:
  - examples/ict3113-a1-ticket-triage-service
  - concepts/performance-engineering
---

# Model Cascade Break-Even

A cascade sends every request to a small, fast model first and escalates to a large model only when a rule says the small answer cannot be trusted.

## Mean latency

`mean cascade time = t_small + f × t_large`, where `f` is the escalation fraction.

The cascade beats the large model alone on **mean** latency when

`f < 1 − t_small / t_large`

Example (ICT3113 A2, CPU-only Ollama): `llama3.2:1b` ≈ 1.8 s, `qwen2.5:7b` ≈ 7.7 s, so break-even is f ≈ 77%. At 57% escalation the cascade mean is about 6.2 s against 7.7 s.

## What the mean hides

- **Escalated requests are always slower** than the large model alone (they pay for both), so the **tail (p95, max) does not improve** and can get worse.
- Latency is **bimodal**. With f near 50% the median sits in the gap between the two groups, so p50 swings between runs. Report the escalation fraction next to every p50.
- It is easy to conclude wrongly that "a cascade above 50% escalation is slower than the large model". That is true per escalated request, not on average.

## Accuracy ceiling

`accuracy ≈ (1 − f) × precision_small_on_accepted + f × accuracy_large_on_escalated`

If the small model's accepted answers are right only ~28% of the time, accepting 43% of traffic caps accuracy near 69% even with a perfect large model. A cascade only works when the escalation signal separates the small model's right answers from its wrong ones. A small model that collapses onto one or two default labels gives no such signal: its predicted label says little about whether it is right.

## Method notes

- Simulate the cascade offline from single-model prediction records (answer + latency per ticket) before building it. Do this on a tuning split only; keep the test split unseen.
- Under load, both models can run at once on the same cores (Ollama keeps several models loaded), so the small model's latency is inflated while the large one is busy.
