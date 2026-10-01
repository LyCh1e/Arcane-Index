---
type: example
status: established
created: 2026-09-24
updated: 2026-09-24
name: ict3113-t04-worked-examples
description: ICT3113 Tutorial Week 04 — fully worked problem sets on pipeline capacity, bottleneck analysis, retries, Little's Law, percentiles, and multi-year capacity planning with read replicas
domain: performance-engineering
course: ICT3113
address: c-000126
tags: [ict3113, performance-engineering, utilisation-law, bottleneck, littles-law, retries, read-replicas, capacity-planning, worked-examples, tutorial]
---

# ICT3113 Tutorial Week 04 — Worked Examples

**Source:** [[sources/ict3113-pod-t04]]  
**Concepts:** [[concepts/performance-metrics]] · [[concepts/queueing-theory]] · [[concepts/performance-engineering]]

---

## Problem Set 1: E-Commerce Order API

Pipeline: Incoming → Validation → Payment → Confirmation  
(Validation can reject; Payment can decline.)

---

### Q1.1 — End-to-End Yield

4,800 rejected at validation + 43,200 proceed to payment = **48,000 requests/hour** incoming.  
1,080 payments declined → 43,200 − 1,080 = **42,120 confirmed orders/hour**.  
Yield = 42,120 / 48,000 = **87.75 %**.

*Check:* validation pass = 90 %; payment approval = 97.5 %; 0.90 × 0.975 = 87.75 %. ✓

---

### Q1.2 — Working Backwards Through Two Loss Stages

Target: 100,000 confirmed orders/day. Validation rejects 4 %; payment declines 5 %.  
End-to-end yield = 0.96 × 0.95 = **0.912**.  
Required incoming = 100,000 / 0.912 = **≈ 109,650 requests/day** (round up).

---

### Q1.3 — Peak-Hour Utilisation

6,048,000 requests / 86,400 s = 70 req/s daily average.  
Peak = 3 × 70 = **210 req/s**.  
U = 210 × 0.002 s = **42 %**.

---

### Q1.4 — Service Time Budget Under Utilisation Cap

U_cap = 70 %, X = 350 req/s.  
S_max = 0.70 / 350 = **2 ms per request**.

---

### Q1.5 — Retries and Effective Load

Each attempt fails with p = 0.10; retry until success.  
Mean attempts per order = 1/(1 − 0.10) = **1.111 attempts/order**.  
Attempt rate = 90 orders/s × 1.111 = **100 attempts/s**.  
U = 100 × 0.008 = **80 %**.

> [!key-insight] Retry visit count
> For geometric retries: V = 1/(1 − p_fail). This multiplies both the attempt rate and the utilisation of the retried stage.

---

### Q1.6 — Minimum Number of Instances

Offered load = 250 attempts/s × 0.040 s = **10 Erlangs**.  
m ≥ 10 / 0.80 = 12.5 → **minimum 13 instances**.  
Check: 10/13 = 76.9 % ≤ 80 %; 10/12 = 83.3 % > 80 %. ✓

---

### Q1.7 — Maximum Confirmed Orders (bottleneck = payment)

24 instances × (1 / 0.040 s) = **600 attempts/s** at full utilisation.  
Approved = 600 × 0.96 = **576 orders/s** → **2,073,600 orders/hour**.

---

### Q1.8 — Validation Utilisation at Max Rate

Payment runs at 600 attempts/s. Validation passes 80 % → incoming = 600 / 0.80 = **750 req/s**.  
Per instance: 750 / 3 = 250 req/s.  
U = 250 × 0.002 = **50 %**.

---

### Q1.9 — Confirmation Utilisation at Max Rate

576 orders/s / 4 instances = 144 orders/s per instance.  
U = 144 × 0.005 = **72 %**.

*Bottleneck check:* payment 100 % → confirmation 72 % → validation 50 %. Payment is the bottleneck. ✓

---

## Problem Set 2: Food Delivery Backend

Architecture: Users → Load balancer → App servers ×10 → Database (primary + 2 read replicas) + Cache

---

### Q2.1 — Mixed Workload Utilisation

90 % browsing (5 ms CPU) + 10 % checkout (30 ms CPU).  
Mean demand = 0.9 × 5 + 0.1 × 30 = **7.5 ms/request**.  
Per-instance rate = 1,200 / 10 = 120 req/s.  
U = 120 × 0.0075 = **90 %**.

---

### Q2.2 — Fan-Out to Database (Forced Flow Law)

Mean queries/request = 0.9 × 2 + 0.1 × 8 = **2.6 queries/request**.  
Query rate = 2.6 × 1,200 = **3,120 queries/s**.

---

### Q2.3 — Bottleneck Identification

| Resource | Total demand | Servers | Per-server demand |
|----------|-------------|---------|-------------------|
| App CPU | 7.5 ms | 10 | 0.75 ms |
| Database | 2.5 × 4 = 10 ms | 1 | **10 ms** ← bottleneck |
| Cache | 1.2 × 0.5 = 0.6 ms | 1 | 0.6 ms |

**X_max = 1 / 0.010 = 100 requests/s** (database saturates first).

---

### Q2.4 — Little's Law and Thread Pool

n̄ = 250 req/s × 0.120 s = **30 requests in flight**.  
Total threads = 4 × 12 = 48 > 30 → **pool is large enough** (on average).  
Caveat: mean ≠ peak; at R = 48/250 = 192 ms the pool would be exhausted.

---

### Q2.5 — Percentiles and SLO

p99 = 900 ms ≤ 1,000 ms → **SLO met**.  
Requests slower than 320 ms = 5 % of 1,080,000 = **54,000 requests**.

---

### Q2.6 — Database Utilisation at Peak

U = 400 req/s × 0.002 s = **80 %**.

---

### Q2.7 — Growth to Saturation

U(t) = 0.80 × 1.2^t ≥ 1 → 1.2^t ≥ 1.25 → t ≥ ln(1.25)/ln(1.2) ≈ **1.22 years**.

| Year | Peak (req/s) | Utilisation |
|------|-------------|-------------|
| 0 | 400 | 80 % |
| 1 | 480 | 96 % |
| **2** | 576 | **115 % — saturated** |

**Database saturates in Year 2.**

---

### Q2.8 — Option A: Query Optimisation

D_new = 1.25 ms → X_max = 0.80 / 0.00125 = **640 req/s**.  
3-year peak = 400 × 1.728 = **691.2 req/s** > 640.  
**Option A is insufficient** — it only buys ≈ 2.6 years.

---

### Q2.9 — Option B: Read Replicas

Reads (70 % of demand) spread over primary + 2 replicas.  
Primary demand = 0.30 × 2 ms + (0.70 × 2 ms)/3 = 0.6 + 0.467 = **1.067 ms/request**.  
U_primary = 691.2 × 0.001067 = **73.7 %** ≤ 80 %. ✓  
**Option B meets the cap** at the 3-year peak; Option A does not.
