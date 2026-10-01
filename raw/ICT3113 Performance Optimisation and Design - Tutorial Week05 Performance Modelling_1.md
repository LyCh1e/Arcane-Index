# ICT3113 Performance Optimisation and Design — Tutorial Week 05

**Performance Modelling**
Presented by A/Prof Donny Soh
ICT3113 Performance Optimisation and Design, InfoComm Technology (ICT) Cluster, Singapore Institute of Technology

---

## Instructions

1. Answer the four questions using the lecture content. The formulas, notation and Erlang B table you need are on the reference slides at the end of this deck.
2. State the unit of measurement in every answer and in every step of your working. An answer without units is incomplete.
3. Show your working. The method matters more than the final number.

### Coverage

- **Question 1:** basic performance quantities from a job log (service time, service rate, response time, arrival rate, interarrival time, throughput)
- **Question 2:** response time and throughput bounds from service demands
- **Question 3:** estimating service time from an execution model (MapReduce)
- **Question 4:** sizing a connection pool for a loss target (Erlang B)

---

## Question 1: Performance modelling basics

An API server handled five requests in the window [0, 10] seconds. All five arrived, started and completed inside the window.

| Job | Service time (s) | Response time (s) |
|---|---|---|
| 1 | 3 | 4 |
| 2 | 1.5 | 2 |
| 3 | 0.5 | 2 |
| 4 | 2 | 3 |
| 5 | 1 | 3 |

From the table, calculate: (1) the average service time, (2) the average service rate, (3) the average response time, (4) the average arrival rate, (5) the average interarrival time, (6) the average throughput.

### Answer

**(1) Average service time**
S = (3 + 1.5 + 0.5 + 2 + 1) s / 5 jobs = 8 s / 5 jobs = **1.6 s per job**

**(2) Average service rate** (μ = 1 / S)
μ = 1 / 1.6 s per job = **0.625 jobs/s**

**(3) Average response time**
R = (4 + 2 + 2 + 3 + 3) s / 5 jobs = 14 s / 5 jobs = **2.8 s per job**

**(4) Average arrival rate** (all five arrived in the 10 s window)
λ = 5 jobs / 10 s = **0.5 jobs/s**

**(5) Average interarrival time** (1 / λ)
1 / 0.5 jobs/s = **2 s between arrivals**

**(6) Average throughput** (all five completed in the 10 s window)
X = 5 jobs / 10 s = **0.5 jobs/s**

Notes: X = λ because every arriving job completed inside the window. Response time (2.8 s) exceeds service time (1.6 s) since R = W + S, so the average waiting time is W = 2.8 − 1.6 = **1.2 s per job**. Also, μ = 0.625 jobs/s > λ = 0.5 jobs/s, so the server is not overloaded (ρ = λ / μ = 0.5 × 1.6 = 0.8 Erlangs; U = X × S = 0.5 jobs/s × 1.6 s = 80 %).

---

## Question 2: Performance bounds

One request visits five devices. The table gives the number of visits per request and the service time per visit. Assume no parallelism and no waiting time at any device.

| Device | Visits per request | Service time per visit (ms) |
|---|---|---|
| 1 | 2 | 15 |
| 2 | 3 | 10 |
| 3 | 1 | 30 |
| 4 | 4 | 10 |
| 5 | 1 | 25 |

For this system, find: (1) the minimum response time of a request, (2) the maximum throughput of the system. State which device limits the throughput.

### Answer

Service demand at device i: Dᵢ = Vᵢ × Sᵢ

| Device | Vᵢ (visits) | Sᵢ (ms/visit) | Dᵢ = Vᵢ × Sᵢ (ms/request) |
|---|---|---|---|
| 1 | 2 | 15 | 30 |
| 2 | 3 | 10 | 30 |
| 3 | 1 | 30 | 30 |
| 4 | 4 | 10 | **40** |
| 5 | 1 | 25 | 25 |
| **Total** | | | **155** |

**(1) Minimum response time.** With no parallelism and no waiting, a request just passes through each device in sequence (R₀ ≥ Σ Vᵢ Rᵢ, with Rᵢ = Sᵢ when there is no waiting):
R_min = ΣDᵢ = 30 + 30 + 30 + 40 + 25 = **155 ms per request**

**(2) Maximum throughput.** The device with the largest demand saturates first (Utilisation Law with Uᵢ ≤ 1, and Forced Flow Law Xᵢ = Vᵢ × X₀):
X_max = 1 / D_max = 1 / 40 ms per request = 1 / 0.040 s = **25 requests/s**

**Limiting device: Device 4** (D₄ = 40 ms per request, the largest service demand, i.e. the bottleneck). At X = 25 requests/s its utilisation is 25 × 0.040 = 100 %, while the others are at U₁ = U₂ = U₃ = 25 × 0.030 = 75 % and U₅ = 25 × 0.025 = 62.5 %.

---

## Question 3: Estimating service time

MapReduce splits one computing task across n processors working in parallel.

- **Map:** Divide the input data into n equal partitions and send one partition to each of the n processors.
- **Compute:** Each processor computes the result for its partition. All n run in parallel.
- **Reduce:** Aggregate the n partial results into the final result.

**(1)** Estimate the service time of one MapReduce job with:
- Number of processors: 8
- Number of input records: 100,000
- Time to partition the input: 15 ms per 1,000 records
- Time to process one record: 0.1 ms
- Time to reduce the results: 1 ms per partition

**(2)** Derive a general formula for the service time with n processors and r records, keeping the other settings the same.

### Answer

Service time = Map time + Compute time + Reduce time (the three phases run one after another; only the compute phase is parallel).

**(1) n = 8, r = 100,000 records**

- **Map (partitioning):** 100,000 records × (15 ms / 1,000 records) = 100 × 15 ms = **1,500 ms**
- **Compute (parallel):** each processor handles 100,000 / 8 = 12,500 records; all 8 run at once, so the phase takes 12,500 records × 0.1 ms/record = **1,250 ms**
- **Reduce:** 8 partitions × 1 ms/partition = **8 ms**

S = 1,500 ms + 1,250 ms + 8 ms = **2,758 ms ≈ 2.76 s per job**

**(2) General formula (n processors, r records; S in ms)**

- Map: (15 ms / 1,000 records) × r = 0.015 r ms
- Compute: (r / n) × 0.1 ms = 0.1 r / n ms
- Reduce: n × 1 ms = n ms

**S(n, r) = 0.015 r + 0.1 r / n + n  [ms]**

Check: n = 8, r = 100,000 → 1,500 + 1,250 + 8 = 2,758 ms ✓

Remarks: the partitioning term (0.015 r) is independent of n and is serial, so it sets a floor on the service time however many processors are added; the reduce term grows with n. Minimising S over n gives dS/dn = −0.1 r / n² + 1 = 0 → n* = √(0.1 r) = √10,000 = 100 processors for r = 100,000 (beyond which extra processors make the job slower).

---

## Question 4: Lost work

Sizing a database connection pool. A request that finds no free connection is refused, not queued.

A database server receives 15 requests per second. Each request holds a connection for 50 ms on average.

How many connections must the pool have so that no more than 0.1% of requests are refused? Show the loss probability for each pool size you try.

### Answer

This is an Erlang loss system (requests are refused, not queued), so use the Erlang B formula.

**Traffic intensity:**
ρ = λ × S = 15 requests/s × 0.050 s/request = **0.75 Erlangs** (connections busy on average)

**Target:** B(m, 0.75) ≤ 0.1 % = 0.001

**Loss probability for each pool size** (Erlang B recursion B(m) = ρ B(m−1) / (m + ρ B(m−1)), B(0) = 1):

| m (connections) | Working (ρ = 0.75) | B(m, 0.75) | ≤ 0.1 %? |
|---|---|---|---|
| 0 | — | 1 | — |
| 1 | 0.75 × 1 / (1 + 0.75 × 1) = 0.75 / 1.75 | 0.42857 = **42.857 %** | No |
| 2 | 0.75 × 0.42857 / (2 + 0.75 × 0.42857) = 0.32143 / 2.32143 | 0.13846 = **13.846 %** | No |
| 3 | 0.75 × 0.13846 / (3 + 0.75 × 0.13846) = 0.10385 / 3.10385 | 0.033457 = **3.346 %** | No |
| 4 | 0.75 × 0.033457 / (4 + 0.75 × 0.033457) = 0.025093 / 4.025093 | 0.006234 = **0.623 %** | No |
| 5 | 0.75 × 0.006234 / (5 + 0.75 × 0.006234) = 0.004676 / 5.004676 | 0.000934 = **0.093 %** | **Yes** |

These match the ρ = 0.75 column of the Erlang B table (42.857, 13.846, 3.346, 0.623, 0.093 %).

**Answer: the pool needs m = 5 connections** (loss probability 0.093 % ≤ 0.1 %). With 4 connections the refusal rate would be 0.623 %, more than six times the target.

At m = 5, refused requests ≈ 15 requests/s × 0.000934 ≈ 0.014 requests/s (about 1 in 1,070).

---

# Reference: formulas

Use these where needed. Each is covered in the lectures.

**Basic laws**

- Utilisation Law: U = X × S
- Little's Law: n̄ = X × R
- Traffic intensity: ρ = λ / μ = λ × S
- Response time: R = W + S
- Service time: S = 1 / μ

**M/M/1**

- M/M/1 queue length: n̄ = ρ / (1 − ρ)
- M/M/1 response time: R = 1 / (μ − λ)

**Queueing networks**

- Forced Flow Law: Xᵢ = Vᵢ × X₀
- Service demand: Dᵢ = Vᵢ × Sᵢ
- Sequential service: R₀ ≥ Σ Vᵢ Rᵢ

**Loss systems**

- Erlang loss formula: B(m, ρ) = (ρᵐ / m!) / Σₖ₌₀..ₘ (ρᵏ / k!)
- Erlang B recursion: B(m) = ρ B(m−1) / (m + ρ B(m−1)), B(0) = 1

---

# Reference: notation

| Symbol | Meaning |
|---|---|
| λ | arrival rate |
| X | throughput |
| S | average service time |
| μ | service rate |
| R | response time |
| W | waiting time |
| n̄ | average number in system |
| ρ | traffic intensity (Erlangs) |
| U | utilisation |
| X₀ | system throughput |
| Xᵢ | throughput of device i |
| Vᵢ | visits to device i per request |
| Dᵢ | service demand at device i |
| R₀ | system response time |
| m | number of servers, or pool size |
| B(m, ρ) | probability a request is refused |

---

# Reference: Erlang B loss probability

B(m, ρ) is the probability that an arriving request finds all m servers (or connections) busy and is refused. ρ = λ × S in Erlangs. Values are percentages.

| m | ρ = 0.25 | ρ = 0.5 | ρ = 0.75 | ρ = 1 | ρ = 1.5 | ρ = 2 | ρ = 3 | ρ = 4 |
|---|---|---|---|---|---|---|---|---|
| 1 | 20.000 | 33.333 | 42.857 | 50.000 | 60.000 | 66.667 | 75.000 | 80.000 |
| 2 | 2.439 | 7.692 | 13.846 | 20.000 | 31.034 | 40.000 | 52.941 | 61.538 |
| 3 | 0.203 | 1.266 | 3.346 | 6.250 | 13.433 | 21.053 | 34.615 | 45.070 |
| 4 | 0.013 | 0.158 | 0.623 | 1.538 | 4.796 | 9.524 | 20.611 | 31.068 |
| 5 | <0.001 | 0.016 | 0.093 | 0.307 | 1.418 | 3.670 | 11.005 | 19.907 |
| 6 | <0.001 | 0.001 | 0.012 | 0.051 | 0.353 | 1.208 | 5.216 | 11.716 |
| 7 | <0.001 | <0.001 | 0.001 | 0.007 | 0.076 | 0.344 | 2.186 | 6.275 |
| 8 | <0.001 | <0.001 | <0.001 | <0.001 | 0.014 | 0.086 | 0.813 | 3.042 |
| 9 | <0.001 | <0.001 | <0.001 | <0.001 | 0.002 | 0.019 | 0.270 | 1.334 |
| 10 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | 0.004 | 0.081 | 0.531 |

To size a pool: read down the column for your ρ and take the smallest m whose value is at or below the loss target. For values off the table, use the recursion B(m) = ρ B(m−1) / (m + ρ B(m−1)) with B(0) = 1.
