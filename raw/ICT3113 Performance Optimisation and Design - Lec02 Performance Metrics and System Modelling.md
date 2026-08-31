# ICT3113 Performance Optimisation and Design
## Lecture 2: Performance Metrics and System Modelling

**Presented by** A/Prof Donny Soh
Programme Leader, Applied Artificial Intelligence
Programme Leader, SITxNVIDIA (SNAIC) AI Training
InfoComm Technology (ICT) Cluster
Singapore Institute of Technology

*SIT Internal*

---

## Learning Outcomes

1. Define performance metrics and explain the essential properties of good metrics (linearity, reliability, repeatability, ease of measurement, consistency, independence).
2. Differentiate between classes of metrics: user experience, demand, and resource usage.
3. Explain and compute core metrics such as response time, throughput, and device utilisation.
4. Apply the utilisation law to estimate or sanity-check system performance parameters.
5. Model simple workloads by identifying arrival rate, service time, interarrival time, and utilisation.

---

## Mars Climate Orbiter Case Study

The primary cause of this discrepancy was that one piece of ground software supplied by Lockheed Martin produced results in imperial units (pound force seconds) while a second system, supplied by NASA, expected those results to be in SI units (newton seconds).

This discrepancy had been noticed earlier by at least two navigators, whose concerns were dismissed because they "did not follow the rules about filling out [the] form to document their concerns".

**The same quantity crossed a system boundary in inconsistent units: a failure of consistency. A metric needs an agreed definition, unit and measurement boundary wherever it is exchanged. The discrepancy had been noticed, but the project's processes did not resolve it.**

---

## Performance Metrics

A metric is a standard by which something can be measured.

We need both a standard (units) and a way of measuring against it.

- Metric: the distance between two points
- Standard (unit): metre
- Measurement tool: a tape measure

### Properties of good performance metrics

Performance metrics should have the following:

- **linearity**: the metric should respond in a linear fashion to the phenomenon being measured
- **reliability**: if the metric says that A is better than B, then A should outperform B
- **repeatability**: the metric should give the same results under the same conditions
- **ease of measurement**: the metric should be easily measured or computed
- **consistency**: the metric should have the same definition across all systems under testing
- **independence**: the metric should not be shaped by the vendors or sponsors whose systems it will be used to compare

*(from Lilja (2000), quoted by Bondi)*

### In-class question

Which of the following best illustrates a violation of the reliability property of a performance metric?

A. A benchmark score doubles when system resources double, but actual user performance only improves slightly.
B. Two independent runs of the same benchmark on the same hardware give different scores.
C. Different labs use the same benchmark name, but calculate the metric differently.
D. A metric consistently reports higher scores for System A than for System B, but in real-world usage System B outperforms System A.

---

## Outcome, Demand Side and Supply Side

**Demand Side**
Work offered to the system. Counted at the entrance.
Metrics: arrival rate λ, number of users, requests submitted
In the fab: wafer starts per week, lots arriving at a tool

**Supply Side**
Work the system completes. Counted at the exit.
Metrics: throughput X, service rate μ (capacity)
In the fab: wafer outs per week, scanner rated wafers per hour

**Outcome**
What the user gets when the two meet: time from entrance to exit.
Metrics: response time = wait time + service time
In the fab: cycle time of a lot at the litho step

### Example: one lithography scanner, rated at 150 wafers per hour (wph)

```
Lots arrive (λ = 120 wph) → WIP queue → Scanner (μ = 150 wph) → Wafers out (X = 120 wph)
```

- **Demand 120 wph:** throughput 120 wph, scanner busy 80% of the time, WIP stable. Here λ = X.
- **Demand 180 wph:** throughput caps at 150 wph. WIP grows by 30 wafers every hour and cycle time climbs.

The two sides agree only while the tool keeps up. X never exceeds μ: overtime raises μ, it does not lift X above it.

---

## Performance Metrics: Outcome, Demand, Supply

| | User Experience Metrics | Demand Metrics | Supply Metrics |
|---|---|---|---|
| **Description** | measure phenomena that affect users' experience of the system, e.g. the time taken to respond to the press of a button | measure the level of demand for a service, e.g. visitors to a web site per minute | measure what the system delivers, and what it consumes to deliver it, e.g. delivers: wafers per hour. Consumes: memory and disk. |
| **Key metric** | **Response Time** — the time that elapses between the initiation of request and its completion. Particularly important for interactive systems. | **Arrival Rate** — the number of units of work offered in a given amount of time. Counted at the entrance, not the exit. | **Throughput and Utilisation** — Throughput: units of work completed per unit time. Utilisation: the proportion of time a device is busy, or of its capacity in use. |

Outcome: where demand meets supply. Demand side. Supply side.

---

## Response Time

Response time is the time that elapses between the initiation of request and its completion. This is particularly important for interactive systems — e.g. the time between selecting a link in a web browser and seeing the web page.

**Response Time = Wait Time + Service Time**, in the single-server model used here. For an end-to-end request, response time may also include network and communication delays.

- **Wait Time (W):** The request waits for the system to be available.
- **Service Time (S):** The system services the request.
- **Response Time (R):** Request → Response
- **Think Time:** The user decides what to do.

### Response Time and User Perception

| Response Time | Effect |
|---|---|
| about 0.1 s | Feels instantaneous |
| about 1 s | Delay noticed; flow of thought largely kept |
| about 10 s | Attention hard to hold; show progress |

Historical usability heuristic, not a universal performance law (Miller 1968; Nielsen 1993)

---

## Percentiles and Tail Latency

The table on the previous slide refers to a single response time. A real system produces a distribution: thousands of requests, each with a different response time.

- These distributions are right-skewed. Most requests are fast; a few are very slow (cache misses, garbage collection, retries, queueing).
- The mean is pulled up by the slow few. The median (p50) describes the typical request. High percentiles (p95, p99) describe the slow ones.
- The p-th percentile is the value below which p% of requests fall. "p95 = 300 ms" means 95% of requests completed within 300 ms.
- Latency objectives are often expressed as percentiles, or as the proportion of requests meeting a threshold, because averages hide tail behaviour. An SLI is what is measured; an SLO is the target for it; an SLA is an agreement that may carry objectives and consequences.

Back to slide 6. Consistency: nearest-rank and interpolated methods give different values under the same name, so agree the definition before comparing systems. Ease of measurement: a mean needs only a running sum; a percentile needs the distribution to be kept.

---

## Why the Tail Matters

1% of requests sounds rare. Two reasons it is not.

- **Fan-out.** One page load can trigger 100 backend calls, and the user waits for the slowest one. P(at least one call slower than its p99) = 1 − 0.99¹⁰⁰ ≈ 63%. Most page loads hit the tail. Assumes the 100 call latencies are independent and the request waits for all of them.
- **Heavy users.** The users who make the most requests encounter the tail most often, and they are usually your most valuable users.

*(Kleppmann 2017)*

Diagram concept: distribution of response times, right-skewed, showing median (p50), mean, and p99 with the "slowest 1%" marked in the tail. (↑ number of requests, response time →)

---

## Response Time: Exercise

Suppose we have a friend taking ICT3102 known as Larry Low. We know that Larry Low is a great procrastinator.

Suppose that Larry Low was told by the lab instructor to carry out the lab exercise. Instead of starting work first, he carries out the following:

The instructor is the client; Larry is the server. Service time is time Larry spends working on the lab. Everything else between the request and its completion is wait time.

- Goes to the washroom for 10 minutes
- Combs his hair for 20 minutes
- Boots up his laptop for 1 minute
- Works on his lab exercise for 2 minutes
- Goes for a tea break for 20 minutes
- Returns and completes his lab exercise in 8 minutes
- Goes to the washroom for 10 minutes

**What is his total response time?**

---

## Response Time: Exercise 2 (Healthcare)

A patient visits a polyclinic. The visit consists of the following steps:

- Takes a queue number and waits in the waiting area: 25 minutes
- Consultation with the doctor: 10 minutes
- Waits at the pharmacy: 15 minutes
- Pharmacist dispenses and explains the medication: 5 minutes

1. What is the total service time?
2. What is the total response time?
3. What proportion of the visit is spent waiting?

---

## Percentiles: Exercise

Ten requests to a food-ordering API return the following response times in milliseconds:

`100, 110, 120, 105, 115, 95, 108, 112, 2000, 118`

1. What is the mean response time?
2. What is the median (p50)?
3. What is the p90? Use the nearest-rank method: the smallest value with at least 90% of observations at or below it.
4. Which statistic best describes typical performance? Which exposes the slow tail? Which would you choose when defining a latency SLO, and why?

---

## Demand Metrics: Arrival Rate

e.g. the number of requests arriving at an API per second
e.g. the number of lots arriving at a lithography tool per hour

**Demand Metrics** measure the level of demand for a service, e.g. visitors to a web site per minute.

**Arrival Rate** is the number of units of work offered in a given amount of time. Counted at the entrance, not the exit.

---

## Throughput: Exercise

Larry is enrolled in 4 modules over a 12-week trimester.

Each module normally has 1 lab per week, so the nominal workload is 4 labs/week.

- In weeks 1–4, Larry keeps up and completes 4 labs per week.
- In weeks 5–8, he procrastinates and completes only 2 labs per week.
- In weeks 9–12, he tries to catch up, but can only manage 5 labs per week.

In the language of slide 8: the nominal workload of 4 labs/week is the demand (arrival rate), labs completed per week is Larry's throughput, and the 5 labs/week he manages in weeks 9–12 is his capacity (service rate).

**Questions:**

- What is Larry's total number of labs completed in the trimester?
- What is Larry's average throughput in labs per week?
- Compare Larry's average throughput with the nominal workload, i.e. with demand. What is the percentage shortfall?

---

## Throughput: Exercise 2 (Manufacturing)

A semiconductor packaging line has a nominal capacity of 1,200 units per day. Over a 5-day work week:

- Monday and Tuesday: the line runs at full capacity.
- Wednesday: a machine breakdown limits output to 600 units.
- Thursday and Friday: overtime pushes output to 1,400 units per day.

1. What is the total output for the week?
2. What is the average throughput in units per day?
3. Compare the average throughput with the nominal capacity, i.e. with supply. What is the percentage shortfall?

**Note:** nominal capacity assumes the rated working day. Overtime lengthens the day, so capacity on those days rises above 1,200. Throughput never exceeds capacity; the capacity changed. Watch how much overtime it takes to recover half a day of downtime: lost capacity is expensive to buy back.

---

## Supply Metrics

e.g. the number of bytes transferred per second by an I/O controller
e.g. the percentage of time that the CPU spends executing instructions
e.g. the proportion of RAM that is currently occupied by processes

**Supply Metrics** measure what the system delivers, and what it consumes to deliver it, e.g. delivers: wafers per hour. Consumes: memory and disk.

**Throughput and Utilisation:**
- Throughput: units of work completed per unit time.
- Utilisation: the proportion of time a device is busy, or of its capacity in use.

| Category | Metrics |
|---|---|
| **CPU** | CPU Time, CPU Utilisation |
| **Memory** | Amount of virtual memory, Level of paging activity |
| **Disk** | Busy time, Idle time, Transfer speed |
| **Network** | Bandwidth: link capacity, bits per second; Observed throughput: bytes transmitted or received per second; Packets sent or received per second |
| **Energy and power** | Energy: joule (J), watt-hour (Wh), kilowatt-hour (kWh); Power: watt (W) |

---

## Performance Modelling Basics

- Imagine a computer system that processes a series of requests or jobs
- **Arrival rate λ:** number of arrivals observed per unit time
- **Interarrival time:** elapsed time between consecutive arrivals
- **Service time S:** time spent actively servicing one job
- **Throughput X:** jobs completed per unit time
- **Service rate (capacity) μ:** for a single server with mean service time S, μ = 1/S when continuously busy
- In a long-running stationary workload, mean interarrival time ≈ 1/λ. In a short finite trace, the sample mean of the observed gaps need not equal the reciprocal of N/T, because the observation boundaries matter. The next example shows the two numbers side by side.

---

## Performance Modelling Basics: Example

Suppose four jobs arrived and were completed over the time interval [0, 10] seconds as shown:

Arrivals: A at t = 0, B at 1, C at 3, D at 5. Service: A 0–2, B 2–6, C 6–7, D 7–10.

- What is the wait time, service time and response time for each job?
- Calculate the arrival rate over [0, 10], then the three observed gaps and their mean. Compare with 1/λ.
- Calculate the average service time and average service rate.
- What is the utilisation of the server?

### Solution

| Job | Wait | Service | Response |
|---|---|---|---|
| A | 0 | 2 | 2 |
| B | 1 | 4 | 5 |
| C | 3 | 1 | 4 |
| D | 2 | 3 | 5 |

| Metric | Value |
|---|---|
| Arrival rate λ | 4 / 10 = 0.4 jobs/s |
| Mean observed gap | (1 + 2 + 2) / 3 = 1.67 s |
| 1/λ | 2.5 s (not the mean gap) |
| Service rate μ = 1/S | 0.4 jobs/s |
| Mean service time S | 10 / 4 = 2.5 s |
| Utilisation U = XS | 0.4 × 2.5 = 1.0 |

This server is saturated: busy for the whole interval, so U = 1.0. Three of the four jobs waited.

---

## Performance Modelling Basics: Exercise (IT)

A payment API runs on a single worker. The server log for the interval [0, 20] seconds shows:

- Request A: arrives t = 0, starts processing at 0, completes at 3
- Request B: arrives t = 2, starts processing at 3, completes at 8
- Request C: arrives t = 9, starts processing at 9, completes at 13
- Request D: arrives t = 12, starts processing at 13, completes at 15

1. What is the wait time, service time and response time for each request?
2. Calculate the arrival rate over the 20-second observation window. Then calculate the three observed interarrival times and their sample mean. Why is the reciprocal of the window arrival rate different from that sample mean?
3. Calculate the average service time and average service rate.
4. What is the utilisation of the worker?

**Note:** a real system gives you a log of timestamps, not a Gantt chart. Reconstruct the picture from the timestamps.

---

## Utilisation Law

The Utilisation Law states that:

**U = XS**

That is, the average utilisation is the product of the average throughput and average service time. A server cannot be busy for more than all of the time, so:

**U ≤ 100%**

Where does this come from? Over any interval, busy time = jobs completed × average service time. Divide both sides by the interval length: the left side becomes utilisation, the right side becomes X × S. In the example earlier: the server completed 4 jobs of 2.5 s each in 10 s, so U = (4/10) × 2.5 = 1.0.

**Arrival rate or throughput?** In a stable steady-state system with no lost, rejected or abandoned work, long-run throughput equals the arrival rate: X = λ. If demand exceeds sustainable capacity, or work is dropped or rejected, λ and X need not be equal. So U = λS is a special case; U = XS is the general operational law.

---

## Utilisation Law: Exercise 1

Assume a stable system with no rejected or lost work, so X = λ.

1. If three transactions arrive at a server every second, and the server takes 100 milliseconds to serve each transaction on average, what is the average utilisation of the server?
2. If the average utilisation of a device has been measured at 90% and 100 jobs arrive every second on average, what is the average service time?
3. What is the maximum transaction rate for a device with an average service time of ten milliseconds per transaction?

---

## Utilisation Law: Exercise 2 (Healthcare)

Assume a stable system with no rejected or lost work, so X = λ.

1. An MRI scanner receives 2 scan requests per hour on average, and each scan takes 25 minutes. What is the utilisation of the scanner?
2. A CT scanner's measured utilisation is 60%, and 12 patients arrive per hour on average. What is the average scan time?
3. What is the maximum number of patients per hour for an X-ray room with an average of 6 minutes per patient?

---

## Utilisation and Response Time

The Utilisation Law itself says nothing about waiting. In queueing systems with variable arrivals or service times, higher utilisation generally means more waiting, often sharply as utilisation approaches 100%.

- At low utilisation an arriving request usually finds the server free: response time ≈ service time.
- As utilisation rises, more requests arrive while the server is busy, and wait time grows with it.
- The growth is not linear: 60% to 80% hurts far less than 80% to 90%. Near 100%, small increases in load produce large increases in queueing.
- Utilisation alone does not determine waiting time. Arrival variability, service-time variability, number of servers and queue discipline also matter.

The MRI scanner at 83% utilisation has relatively little spare capacity; whether that causes problematic waiting depends on arrival patterns, scan-time variability and scheduling. Either way, production systems are deliberately run with headroom rather than at full utilisation.

Recall the polyclinic: 40 of the 55 minutes were spent waiting, so the observed delay is queue-dominated. But the queue may still be caused by insufficient service capacity, variability, scheduling, or another bottleneck. Diagnose why the queue forms before deciding what to optimise.

---

## Summary

- A metric needs a unit, a way of measuring, and one definition everywhere it is used (Mars Climate Orbiter).
- Good metrics are linear, reliable, repeatable, easy to measure, consistent and independent.
- Three classes: outcome (response time), demand (arrival rate), supply (throughput, service rate, utilisation).
- Response time = wait time + service time. Real systems produce a distribution: report percentiles, not just the mean.
- Arrival rate is counted at the entrance and can exceed capacity. Throughput is counted at the exit and cannot.
- Utilisation Law: U = X × S, and X = λ while the system keeps up. Enough to sanity-check a design.
- With variable arrivals or service times, higher utilisation means more waiting, and not linearly. Systems are run with headroom for a reason.

---

## References

- Bondi, A. B. (2014). *Foundations of Software and System Performance Engineering.* Addison-Wesley.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications.* O'Reilly Media. Chapter 1, on percentiles and tail latency.
- Lilja, D. J. (2000). *Measuring Computer Performance: A Practitioner's Guide.* Cambridge University Press.
- Miller, R. B. (1968). Response time in man-computer conversational transactions. *Proceedings of the AFIPS Fall Joint Computer Conference.*
- Nielsen, J. (1993). *Usability Engineering.* Academic Press.
- NASA (1999). Mars Climate Orbiter Mishap Investigation Board, Phase I Report.

---
*SIT Internal — ICT3113 Performance Optimisation and Design, Singapore Institute of Technology*
