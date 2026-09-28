# ICT3113 Performance Optimisation and Design
## Lecture 05: Estimating Performance and Lost Work

**Presented by** A/Prof Donny Soh
Programme Leader, Applied Artificial Intelligence
Programme Leader, SITxNVIDIA (SNAIC) AI Training
InfoComm Technology (ICT) Cluster
Singapore Institute of Technology

*SingaporeTech.edu.sg — SIT Internal*

---

## Contents

This lecture consolidates the modelling block before the midterm. The laws are the ones you already have; the worked examples are new.

- Upper Bound on Throughput
- Lower Bound on Response Time
- Estimating Service Time with Execution Models
- Lost Work (queuing with the Erlang loss formula)

---

## Where We Are: The Modelling Block

By this point you should be able to state and apply each of these. The midterm covers up to this lecture.

- Utilisation Law U = X × S and Little's Law n = λ × R (Lecture 03)
- M/M/1 and the response time curve; the 70% planning rule (Lecture 03)
- demand D = V × S, Forced Flow Law, Service Demand Law (Lecture 04, revised here)
- bottleneck analysis: ceilings X ≤ 1/D, or c/D with c servers; capacity bottleneck vs congestion hotspot (Lecture 04)
- multi-server queues, interactive response time law, variability and Kingman (Lecture 04)
- bounds on throughput and response time; background load (this lecture)
- estimating S before a system exists; lost work and Erlang B (this lecture, new)

---

# 01 — Upper Bound on Throughput

## Demand

We define the demand on service i as **D(i) = V(i) × S(i)**, where:

- S(i) is the service time of service i
- V(i) is the number of times ("visits") that service i is used in response to each request to the system as a whole

In Lecture 04 the visits came from measurements. Here we work from estimates, before the system exists.

---

## Upper Bound on Throughput

The Forced Flow Law states that **X(i) = V(i) × X0**, where:

- X0 is the throughput of the system as a whole
- X(i) is the throughput of service i

Intuitively: the throughput of any single service equals the throughput of the overall system multiplied by the number of times that service is used per request.

Multiply both sides by the average service time S(i):

**X(i) × S(i) = X0 × V(i) × S(i) = X0 × D(i)**

By the Utilisation Law the left side is U(i), so **U(i) = X0 × D(i)**: the utilisation of service i is the product of total throughput and that service's demand.

---

## Upper Bound on Throughput (continued)

For the system to function, the utilisation of every service must stay below 100%: **U(i) = X0 × D(i) < 1**

Let D(b), the bottleneck, be the largest of all the D(i). Then:

**X0 < 1 / D(b)**

The service with the largest demand caps the throughput of the whole system.

Recall from the M/M/1 discussion: in practice, plan for utilisation of about 70% or less, so the practical ceiling sits below this bound.

---

## Upper Bound on Throughput: Example (I)

An e-commerce checkout request touches five services, with the visit counts and service times below. What is the maximum throughput of this system?

| Service | Visits (V) | Average service time (S) |
|---|---|---|
| API gateway | 1 | 5 ms |
| Auth service | 1 | 10 ms |
| Product DB | 3 | 12 ms |
| Cache | 4 | 1 ms |
| Payment gateway | 1 | 25 ms |

---

## Upper Bound on Throughput: Example (II), Background Load

The table shows demand D(k) and background load b(k) for the devices of a database server. Demands are per request at one request per second; Capacity is the total available.

1. Calculate the maximum arrival rate each device can support.
2. Which device is the bottleneck?
3. What is the maximum number of requests per second this system can support?

| Device | D(k) | b(k) | Capacity |
|---|---|---|---|
| CPU | 0.5% | 0% | 100% |
| Memory | 10 KB | 2 GB | 8 GB |
| Disk1 | 20 MB | 50 GB | 500 GB |
| Disk2 | 100 KB | 500 GB | 2 TB |

---

# 02 — Lower Bound on Response Time

## A Lower Bound on Response Time

Assume a request must be serviced by each service in sequence (no parallelism).

The total response time is at least the sum of the response times of each service over every visit:

**R0 ≥ Σ V(i) × R(i)**

If there is no waiting anywhere, R(i) = S(i), so V(i) × R(i) = V(i) × S(i) = D(i), and therefore:

**R0 ≥ Σ D(i)**

The sum of the demands is the best response time the design can ever achieve.

---

## Lower Bound on Response Time: Example

What is the minimum response time for the checkout system from Example (I)?

| Service | Visits (V) | Average service time (S) |
|---|---|---|
| API gateway | 1 | 5 ms |
| Auth service | 1 | 10 ms |
| Product DB | 3 | 12 ms |
| Cache | 4 | 1 ms |
| Payment gateway | 1 | 25 ms |

---

# 03 — Estimating Service Time

## Estimating Service Time with Execution Models

The bounds above need service times. Before a system exists, we estimate them from the design using UML activity or sequence diagrams:

- estimate the time required for each activity or message
- estimate the number of times each activity occurs or message is sent
- estimate the probability that each branch is taken

Smith and Williams (2001) call the annotated diagram an **execution model**.

We solve a model by computing the time a request takes to move through the diagram:

- tasks in sequence: add the estimated times
- tasks in parallel: take the maximum estimated time
- branches: compute the expected value over the branch probabilities

---

## Estimating Service Time: Example (I)

Consider the following steps required to service a request:

- the program spends 10 ms deciding what to do
- it makes an asynchronous network request that takes 30 ms
- while waiting for the network, it builds one of three kinds of response:
  - 50% of the time, one that takes 12 ms
  - 40% of the time, one that takes 25 ms
  - 10% of the time, one that takes 40 ms

---

## Estimating Service Time: Example (II)

A product search endpoint first checks a cache, taking 2 ms on average. Analysis of past traffic shows 80% of searches hit the cache. On a miss, the endpoint queries the search index, taking a further 7 ms on average.

Draw an execution model for this endpoint, covering both the cache hit and the cache miss path.

The slide shows the model as a diagram: a start node leads to a 2 ms activity, then a branch (decision) node. The 0.2 branch goes through a 7 ms activity to the end node; the 0.8 branch goes directly to the end node.

```
(start) ──► [ 2 ms ] ──► <branch> ──0.2──► [ 7 ms ] ──► (end)
                            │                             ▲
                            └────────────0.8──────────────┘
```

---

# 04 — Lost Work

## Lost Work

There is often a limit on the number of objects a system can handle at one time: threads or connections in a pool, or space in a buffer.

If a new job arrives when the capacity is exhausted, it is **lost or dropped**.

Queuing theory can estimate the probability that jobs are lost.

The classical tool is the **Erlang loss formula** (Erlang B), developed by A. K. Erlang (1917) for telephone exchanges: jobs were calls, capacity was the number of telephone lines (trunks).

---

## The Erlang Loss Formula

Let m be the capacity, S the average service time, and ρ = λ × S the offered load. The probability that a job is lost is:

**B(m, ρ) = (ρᵐ / m!) / Σ (ρᵏ / k!)  for k = 0 … m**

To size a system: given ρ and a target loss ε, find the smallest m with **B(m, ρ) ≤ ε**. Values of B(m, ρ):

| m | ρ = 0.5 | ρ = 0.6 | ρ = 0.7 | ρ = 0.8 | ρ = 1.0 |
|---|---|---|---|---|---|
| 1 | 3.3×10⁻¹ | 3.7×10⁻¹ | 4.1×10⁻¹ | 4.4×10⁻¹ | 5.0×10⁻¹ |
| 2 | 7.7×10⁻² | 1.0×10⁻¹ | 1.3×10⁻¹ | 1.5×10⁻¹ | 2.0×10⁻¹ |
| 3 | 1.3×10⁻² | 2.0×10⁻² | 2.9×10⁻² | 3.9×10⁻² | 6.2×10⁻² |
| 4 | 1.6×10⁻³ | 3.0×10⁻³ | 5.0×10⁻³ | 7.7×10⁻³ | 1.5×10⁻² |
| 5 | 1.6×10⁻⁴ | 3.6×10⁻⁴ | 7.0×10⁻⁴ | 1.2×10⁻³ | 3.1×10⁻³ |
| 6 | 1.3×10⁻⁵ | 3.6×10⁻⁵ | 8.1×10⁻⁵ | 1.6×10⁻⁴ | 5.1×10⁻⁴ |
| 7 | 9.4×10⁻⁷ | 3.0×10⁻⁶ | 8.1×10⁻⁶ | 1.9×10⁻⁵ | 7.3×10⁻⁵ |
| 8 | 5.9×10⁻⁸ | 2.3×10⁻⁷ | 7.1×10⁻⁷ | 1.9×10⁻⁶ | 9.1×10⁻⁶ |

---

## Lost Work: Example (I)

Suppose that, on average, 300 packets arrive at a router every second.

The router can process 500 packets per second.

If each packet may be up to 1,024 bytes long, how large a buffer does the router need so that fewer than one in a million packets are dropped?

---

## Two Laws Pertaining to Queuing

Recall from Lecture 03:

- the **Utilisation Law**: U = X × S. The average utilisation of a single server is the product of average throughput and average service time. Only meaningful while utilisation stays at or below 100%.
- the **Little's Law**: n = λ × R. The average number in the system is the product of the average arrival rate and the average response time. Named after J. D. C. Little (1961).

---

## Lost Work: Example (II)

A database connection pool is a set of open connections to a database, maintained by an application that makes many queries. Instead of opening a new connection per query, the application uses one from the pool.

The database takes 100 ms on average to serve a query, and on average 7 requests arrive per second.

1. What is the average number of requests being served or waiting at any one time? Indicate the law you use.

---

## Lost Work: Example (II) (continued)

The application's designers want at least one unused connection to be available for 99.9% of database requests on average.

2. How many connections should be in the pool?

---
*SIT Internal — ICT3113 Performance Optimisation and Design, Singapore Institute of Technology*
