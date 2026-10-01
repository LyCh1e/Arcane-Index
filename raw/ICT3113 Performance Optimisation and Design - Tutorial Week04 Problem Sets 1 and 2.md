# ICT3113 Performance Optimisation and Design — Tutorial Week 04

**Problem Sets 1 and 2**
Presented by A/Prof Donny Soh
ICT3113 Performance Optimisation and Design, InfoComm Technology (ICT) Cluster, Singapore Institute of Technology

> All questions are independent unless otherwise stated.

---

# Problem Set 1: E-commerce order API

Questions 1.1 to 1.9. An order API: validation, payment and confirmation, with rejects, declines and retries.

**Pipeline:** Incoming API requests → Validation → Payment → Confirmation → Confirmed orders
(Validation can branch to *Rejected*; Payment can branch to *Declined*.)

---

## Question 1.1: End-to-end success rate

An e-commerce order API handles requests in three stages: validation, payment and confirmation. In one hour, 4,800 requests are rejected at validation and 43,200 proceed to payment. Of these, 1,080 payments are declined. Every approved payment produces a confirmed order. What percentage of all incoming requests result in a confirmed order?

**Answer**

- Incoming requests = rejected + proceeding to payment = 4,800 + 43,200 = **48,000 requests/hour**
- Confirmed orders = 43,200 − 1,080 = **42,120 orders/hour**
- Success rate = 42,120 / 48,000 = 0.8775

**≈ 87.75 % of incoming requests result in a confirmed order.**

(Check by stages: validation pass = 43,200/48,000 = 90 %; payment approval = 42,120/43,200 = 97.5 %; 0.90 × 0.975 = 87.75 %.)

---

## Question 1.2: Working backwards through two loss stages

The business requires 100,000 confirmed orders per day. Validation rejects 4% of incoming requests, and the payment provider declines 5% of the requests that reach it. How many requests must the API receive per day to meet the target?

**Answer**

- Fraction surviving validation = 1 − 0.04 = 0.96
- Fraction surviving payment = 1 − 0.05 = 0.95
- End-to-end yield = 0.96 × 0.95 = 0.912
- Required incoming = 100,000 / 0.912 = 109,649.1 requests/day

**≈ 109,650 requests per day** (round up, since a fraction of a request cannot be received).

---

## Question 1.3: Peak-hour utilisation

The API receives 6,048,000 requests over a 24-hour day. Traffic is not uniform: the arrival rate in the peak hour is 3 times the daily average rate. Validation runs on a single instance and takes 2 ms of processing time per request. What is the utilisation of the validation instance during the peak hour?

**Answer**

- Daily average arrival rate = 6,048,000 requests / (24 × 3,600 s) = 6,048,000 / 86,400 = **70 requests/s**
- Peak arrival rate = 3 × 70 = **210 requests/s**
- Utilisation Law: U = X × S = 210 requests/s × 0.002 s/request = 0.42

**U = 42 %.**

---

## Question 1.4: Service time budget under a utilisation cap

Operations policy caps every service at 70% utilisation, to leave headroom for traffic spikes and instance failures. The peak arrival rate at validation is 350 requests per second on a single instance. What is the maximum processing time per request that keeps validation within policy?

**Answer**

- U = X × S → S = U / X
- S_max = 0.70 / 350 requests/s = 0.002 s/request

**S_max = 2 ms per request.**

---

## Question 1.5: Retries and effective load

Payment attempts sometimes time out at the bank: on average 10% of attempts fail and are automatically retried, and retried attempts fail at the same 10% rate. The platform confirms 90 orders per second, and each payment attempt takes 8 ms on a single payment instance. What is the rate of payment attempts, and what is the utilisation of the payment instance?

**Answer**

Each attempt succeeds with probability 0.9, and retries continue until success. The number of attempts per order is geometric with mean 1 / 0.9 = 1.111 attempts/order (equivalently 1 + 0.1 + 0.1² + … = 1/(1 − 0.1)).

- Payment attempt rate = 90 orders/s × (1 / 0.9) attempts/order = **100 attempts/s**
- Utilisation: U = X × S = 100 attempts/s × 0.008 s/attempt = 0.80

**Attempt rate = 100 attempts/s; U = 80 %.**

---

## Question 1.6: Minimum number of instances

Each payment attempt takes 40 ms. At peak, the payment service must handle 250 attempts per second, and per-instance utilisation must not exceed 80%. Load is spread evenly across instances. What is the minimum number of payment instances required?

**Answer**

- Total demand (offered load) = X × S = 250 attempts/s × 0.040 s/attempt = 10 busy-instances (10 Erlangs)
- Per-instance utilisation ≤ 0.80 → number of instances m ≥ 10 / 0.80 = 12.5

**Minimum = 13 payment instances.** (Check: 10/13 = 76.9 % ≤ 80 %; with 12 instances, 10/12 = 83.3 % > 80 %.)

---

## Question 1.7: Maximum confirmed orders

*Questions 1.7, 1.8 and 1.9 are related.*

Suppose payment is the bottleneck of the pipeline. Each attempt takes 40 ms, the platform runs 24 payment instances, and 4% of attempts are declined (declined orders are not retried). What is the maximum number of confirmed orders per hour?

**Answer**

- Payment capacity at 100 % utilisation = 24 instances / 0.040 s = **600 attempts/s**
- Approved fraction = 1 − 0.04 = 0.96
- Maximum confirmed rate = 600 × 0.96 = **576 orders/s**
- Per hour: 576 orders/s × 3,600 s/h = 2,073,600

**Maximum = 2,073,600 confirmed orders per hour.**

---

## Question 1.8: Utilisation of validation

Validation rejects 20% of incoming requests and takes 2 ms per request, with load spread evenly across 3 validation instances. When payment is running at the maximum rate from 1.7, what is the utilisation of each validation instance?

**Answer**

- Requests reaching payment = 600 requests/s (declines are not retried, so every attempt is a distinct request)
- Only 80 % of incoming requests pass validation → incoming rate = 600 / 0.80 = **750 requests/s**
- Per validation instance: 750 / 3 = 250 requests/s
- U = 250 requests/s × 0.002 s/request = 0.50

**U = 50 % per validation instance.**

---

## Question 1.9: Utilisation of confirmation

The confirmation service sends one confirmation per successful order and takes 5 ms per order, with load spread evenly across 4 instances. At the maximum rate from 1.7, what is the utilisation of each confirmation instance?

**Answer**

- Confirmation rate = 576 orders/s (from 1.7)
- Per instance: 576 / 4 = 144 orders/s
- U = 144 orders/s × 0.005 s/order = 0.72

**U = 72 % per confirmation instance.**

(Consistency check: payment is at 100 %, confirmation at 72 %, validation at 50 %, so payment is indeed the bottleneck.)

---

# Problem Set 2: Multi-tier online service

Questions 2.1 to 2.9. A food delivery backend: mixed workloads, bottlenecks, Little's Law, percentiles and capacity planning.

**Architecture:** Users → Load balancer → App servers ×10 → Database (primary)
(App servers use a Cache; the Database has Read replicas ×2.)

---

## Question 2.1: Mixed workload utilisation

During the lunch peak, the app tier of a food delivery platform receives 1,200 requests per second: 90% are menu browsing requests taking 5 ms of app CPU each, and 10% are checkout requests taking 30 ms each. Load is spread evenly across 10 app instances. What is the utilisation of each app instance?

**Answer**

- Mean CPU demand per request = 0.90 × 5 ms + 0.10 × 30 ms = 4.5 + 3.0 = **7.5 ms/request**
- Per-instance arrival rate = 1,200 / 10 = 120 requests/s
- U = 120 requests/s × 0.0075 s/request = 0.90

**U = 90 % per app instance.**

---

## Question 2.2: Fan-out to the database

The platform serves 1,200 requests per second: 90% browsing, 10% checkout. A browsing request makes 2 database queries on average; a checkout request makes 8. What is the query rate arriving at the database?

**Answer** (Forced Flow Law: X_db = V_db × X₀)

- Mean queries per request = 0.90 × 2 + 0.10 × 8 = 1.8 + 0.8 = **2.6 queries/request**
- Query rate = 2.6 queries/request × 1,200 requests/s = **3,120 queries/s**

(Split: browsing 0.9 × 1,200 × 2 = 2,160 queries/s; checkout 0.1 × 1,200 × 8 = 960 queries/s.)

---

## Question 2.3: Finding the bottleneck

Each request uses, on average: 7.5 ms of app CPU spread evenly across 10 app instances, 2.5 database queries at 4 ms each on a single database server, and 1.2 cache lookups at 0.5 ms each on a single cache node. Which resource is the bottleneck, and what is the maximum request rate the system can sustain?

**Answer** (service demand D = V × S; the resource with the largest demand per server is the bottleneck)

| Resource | Working | Demand per request | Servers | Demand per server |
|---|---|---|---|---|
| App CPU | 7.5 ms total | 7.5 ms | 10 | 7.5 / 10 = **0.75 ms** |
| Database | 2.5 × 4 ms | 10 ms | 1 | **10 ms** |
| Cache | 1.2 × 0.5 ms | 0.6 ms | 1 | **0.6 ms** |

- **Bottleneck = the database** (largest per-server demand, 10 ms).
- X_max = 1 / D_max = 1 / 0.010 s = **100 requests/s**

At that rate: app U = 100 × 0.00075 = 7.5 %, cache U = 100 × 0.0006 = 6 %, database U = 100 %.

---

## Question 2.4: Little's Law and thread pools

The checkout service completes 250 requests per second with a mean response time of 120 ms (queueing plus service). Each in-flight request holds one worker thread. The service runs 4 instances, each with a pool of 12 threads. On average, how many requests are in flight at any moment, and is the thread pool large enough?

**Answer** (Little's Law: n̄ = X × R)

- n̄ = 250 requests/s × 0.120 s = **30 requests in flight** (on average)
- Total thread capacity = 4 instances × 12 threads = **48 threads**
- Per instance: 30 / 4 = 7.5 threads busy on average out of 12 (62.5 % of the pool)

**On average the pool is large enough** (30 < 48, leaving 18 spare threads). Caveat: this is a *mean*. Traffic bursts and slow requests raise the instantaneous in-flight count, so 62.5 % average pool occupancy leaves only moderate headroom for spikes; if response time rose to 192 ms (48 / 250) the pool would be exhausted.

---

## Question 2.5: Percentiles and the SLO

Over one hour, monitoring records 1,080,000 requests with mean response time 80 ms, p50 of 45 ms, p95 of 320 ms and p99 of 900 ms. The SLO states that 99% of requests must complete within 1 second. Is the SLO met, and how many requests in that hour took longer than 320 ms?

**Answer**

- **SLO met: yes.** p99 = 900 ms ≤ 1,000 ms, so at least 99 % of requests completed within 900 ms, hence within 1 s. (The mean and p50 are irrelevant to a percentile SLO.)
- p95 = 320 ms means 95 % of requests finished in ≤ 320 ms, so 5 % took longer.
- Requests slower than 320 ms = 0.05 × 1,080,000 = **54,000 requests**

---

## Question 2.6: Database utilisation at peak

*Questions 2.6 to 2.9 are related.*

At this year's peak, requests arrive at 400 per second and each request generates on average 2 ms of service demand at the database, which runs on a single server. What is the utilisation of the database at peak?

**Answer**

- U = X × D = 400 requests/s × 0.002 s/request = 0.80

**U = 80 %.**

---

## Question 2.7: Growth to saturation

Peak traffic grows 20% per year and the demand per request stays unchanged. In which year does the database saturate, that is, utilisation reaches or exceeds 100%?

**Answer**

U(t) = 0.80 × 1.2ᵗ ≥ 1 → 1.2ᵗ ≥ 1.25 → t ≥ ln(1.25) / ln(1.2) = 0.2231 / 0.1823 ≈ **1.22 years**

| Year | Peak rate (requests/s) | Utilisation |
|---|---|---|
| 0 (now) | 400 | 80 % |
| 1 | 480 | 96 % |
| 2 | 576 | 115.2 % |
| 3 | 691.2 | 138.2 % |

**The database saturates in Year 2** (utilisation is still 96 % at the end of Year 1, so it is on the edge, then exceeds 100 % in Year 2).

---

## Question 2.8: Option A — faster queries

One option is to rewrite the heaviest queries, cutting database demand from 2 ms to 1.25 ms per request. Operations policy caps utilisation at 80%. What peak request rate can the database then sustain, and is that enough for the peak expected in 3 years?

**Answer**

- X_max = U_cap / D = 0.80 / 0.00125 s = **640 requests/s**
- Peak in 3 years = 400 × 1.2³ = 400 × 1.728 = **691.2 requests/s**
- 640 < 691.2 → **not enough.** At 691.2 requests/s, U = 691.2 × 0.00125 = 86.4 %, which is below saturation but breaks the 80 % policy cap.

Option A only buys time: it sustains growth until 640 / 400 = 1.6× current peak, i.e. ln(1.6) / ln(1.2) ≈ 2.6 years, short of the 3-year horizon.

---

## Question 2.9: Option B — read replicas

The other option: 70% of database demand comes from reads, which can be spread evenly across the primary and 2 read replicas; the remaining 30% is writes and must stay on the primary. At the 3-year peak (691.2 requests per second, 2 ms demand per request), what is the utilisation of the primary?

**Answer**

- Demand per request on the DB tier = 2 ms
- Writes (stay on primary): 0.30 × 2 ms = 0.6 ms
- Reads: 0.70 × 2 ms = 1.4 ms, spread over 3 servers (primary + 2 replicas) → 1.4 / 3 = 0.4667 ms on the primary
- Primary demand = 0.6 + 0.4667 = **1.0667 ms/request**
- U_primary = 691.2 requests/s × 0.0010667 s/request = 0.7373

**U_primary ≈ 73.7 %**, which is under the 80 % cap.

**Comparison of options at the 3-year peak:** Option A leaves the single database at 86.4 % (violates the 80 % cap); Option B puts the primary at 73.7 % (meets the cap). Option B is therefore sufficient for the 3-year horizon, whereas Option A is not. (Each replica carries 691.2 × 0.4667 ms = 32.3 % utilisation.)
