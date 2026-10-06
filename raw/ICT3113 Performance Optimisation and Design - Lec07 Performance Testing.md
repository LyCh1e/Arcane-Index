# ICT3113 Performance Optimisation and Design — Lecture 07: Performance Testing

**Types of test, test environment, load generation**

Presented by A/Prof Donny Soh
Programme Leader, Applied Artificial Intelligence
Programme Leader, SITxNVIDIA (SNAIC) AI Training
InfoComm Technology (ICT) Cluster
Singapore Institute of Technology

> Converted from the lecture slides (65 slides). Slides that are purely charts, screenshots or recordings carry no extractable text; where the surrounding text describes them, that description is kept and a *[Figure]* note marks the spot.

---

## Learning outcomes

*This lecture closes the loop from estimate to measurement.*

- Distinguish six types of performance test and say which question each one answers.
- Set up a test environment that can stand in for production, and know when it cannot.
- Build a load model and generate load correctly, including the difference between open-loop and closed-loop load.
- Write a performance requirement and a playbook that another person can run.
- Read a results table and tell saturation apart from a bug.

### Where we are

- **Lecture 02:** metrics, percentiles, the Utilisation Law.
- **Lecture 03:** workload identification and estimation.
- **Lectures 04 and 05:** queueing models and bounds.
- **This lecture:** checking the model against the real system.

---

## Four documents carry performance work from requirement to operations

| Document | What it contains | Who reads it |
|---|---|---|
| Performance requirements document | Each requirement in a fixed structure: what, how much, under what conditions, measured how, traced to what need. | Everyone. It is the contract. |
| Performance measurement plan | The instruments: which tool measures which quantity, where it runs, what it costs to run. | Testers and operations. |
| Performance test plan | The tests: which type, what load model, what environment, what playbook, what counts as pass. | Testers. |
| Capacity management plan | How the system is monitored after deployment, and what triggers more hardware or a redesign. | Operations. |

In practice the four are often one document with four sections. The separation matters because the readers differ: the requirement is agreed with whoever is paying for the system; the playbook is run by whoever is on shift.

This lecture covers the first three: the requirement (next slides), the instruments (the monitor and the generator), and the test plan (the playbook and load model). The capacity management plan is what operations runs after go-live, and is not covered here.

---

# Part 1: Performance requirements document

*What we test against, and how to write it down so that it can be tested.*

### In this part

1. **The four documents** — Requirements, measurement plan, test plan, capacity management plan, and who reads each.
2. **One requirement, ten fields** — Bondi's structure, a worked example for the order API, and sentence patterns to fill in.
3. **Exercise 7.1** — Rewrite "fast and scalable" into something a test can pass or fail.
4. **What good looks like** — Unambiguous, measurable, verifiable, complete, consistent, traceable, time scale stated.

Everything in this part comes before any load is generated. If the requirement is wrong, every test that follows answers the wrong question.

---

## Bondi's structure for a single performance requirement

| # | Field | What it holds |
|---|---|---|
| 1 | Requirement number | PERF-01, PERF-02. Stable identifiers that tests and results refer to. |
| 2 | Title | Short name: Order creation response time. |
| 3 | Statement | The requirement itself, in one sentence with a number, a percentile or statistic, a condition and a time scale. |
| 4 | Supporting commentary | What the statement does not say. Known exclusions, context. |
| 5 | Precedents, sources, standards | Where the number comes from: a study, a regulation, a competitor, a prior system. |
| 6 | Derivation of quantities | The arithmetic. How the workload model and the source produced this number. |
| 7 | Dependent requirements | Other requirements that assume this one holds. |
| 8 | Assumptions | Conditions under which the requirement applies. Load level, hardware, network. |
| 9 | Measurement | The instrument and the procedure. Which tool, where it runs, which run window. |
| 10 | Subject matter expert | A named person who can answer questions about this requirement. |

*Bondi (2015), Table 7.2.* Fields 3, 6, 8 and 9 are where requirements most often fall short. Field 6 is the one that connects this document to Lecture 03.

---

## A worked example: one requirement, all ten fields

| Field | PERF-01 |
|---|---|
| 1. Requirement number | PERF-01 |
| 2. Title | Order creation response time |
| 3. Statement | 95% of POST /orders requests shall complete within 200 milliseconds, measured at the load generator, when the service is offered 10 requests per second (open loop) for a sustained 10 minute window on the reference hardware. |
| 4. Supporting commentary | Applies to order creation only. Catalogue reads and order lookups are covered by PERF-04. Response time in the customer's browser will be higher by the network round trip, which is outside this requirement. |
| 5. Precedents, sources, standards | Miller (1968) and Nielsen (1993): under about 100 ms feels instantaneous, under 1 s keeps the flow of thought. 200 ms at the API leaves room for the page to render inside 1 s. |
| 6. Derivation of quantities | 10 per second is the weekday evening peak from the workload model: 36,000 orders per hour, 2.5 times the daily average. 95th percentile rather than mean so that one slow request in twenty is tolerated and the rest are not hidden by it. |
| 7. Dependent requirements | PERF-02 (sustained throughput) assumes PERF-01 holds. The capacity estimate in the proposal assumes PERF-01 holds on the production hardware. |
| 8. Assumptions | Reference hardware as recorded in the test environment. No other workload on the server. Token hashing at 100,000 iterations as pinned in the config. Store empty at the start of the window. |
| 9. Measurement | JMeter Open Model Thread Group, results from the .jtl excluding the first 2 minutes of warm-up. Three runs; the requirement is met if all three meet the threshold. Server CPU and memory logged by monitor.py every 30 seconds. |
| 10. Subject matter expert | Name and role of the person who can answer questions about this requirement. |

*Numbers are illustrative. Yours come from your own workload model and your own single-request measurement.*

---

## Sentence patterns for the statement: pick one from each column

Eckhardt et al. (2016) found that most well-formed performance requirements follow one of two sentence shapes. Filling the columns forces the missing details into the open.

### Response time

| Condition | Subject | Modal | Statistic | Comparison | Quantity | Unit |
|---|---|---|---|---|---|---|
| In x% of all cases | the system | shall | a mean response time | of less than | x | milliseconds |
| In case of x (a named scenario) | the operation (name it) | must not | a median response time | of no more than | | seconds |
| Between event A and event B | the component (name it) | should | a 95th percentile response time | of no less than | | minutes |
| Under a load of x per second | | | a maximal response time | of more than | | hours |

*(Each column is a menu: pick one entry from each column to assemble a sentence.)*

### Throughput

| Condition | Subject | Modal | Statistic | Comparison | Quantity | Unit |
|---|---|---|---|---|---|---|
| In x% of all cases | the system | shall | a transaction rate | of at least | x | requests per second |
| In case of x (a named scenario) | the operation (name it) | must not | a mean throughput | of no more than | | orders per minute |
| During the period x to y | the component (name it) | should | a sustained processing rate | of less than | | bytes per hour |

### Assembled

- "In 95% of all cases, under a load of 10 requests per second, the order creation endpoint shall have a response time of no more than 200 milliseconds."
- "During the weekday evening peak, the service shall sustain a processing rate of at least 10 orders per second with an error rate below 1%."

---

## Exercise 7.1: Rewrite this requirement so that it can be tested

> "The ordering system shall be fast and scalable, and shall handle peak loads without noticeable slowdown."

- This sentence appears, in some form, in most first drafts. Rewrite it as one or more requirements in Bondi's structure. You do not need all ten fields; fields 1, 2, 3, 6, 8 and 9 are enough.
- Use the order API from the demos. Where you need a number you do not have, state the number you would use and where you would get it.
- Check your statement against: unambiguous, measurable, verifiable, complete, time scale stated.

Write yours out before looking at the answer. Compare it field by field.

---

## Good performance requirements pass the same checks as functional ones

| Check | Meaning |
|---|---|
| **Unambiguous** | "Average response time under five seconds": average over what period, for which requests? Name the request, the statistic and the window. |
| **Measurable** | Refers to a quantity an instrument can produce, and names the instrument. "CPU utilisation measured with top at 1 second intervals", not "efficient". |
| **Verifiable** | There is a procedure, written down, that someone can run to decide pass or fail. The playbook is that procedure. |
| **Complete** | All parameters and context stated. "50,000 transactions per second" is incomplete. "50,000 fund transfers per second, weekdays 11 am to 2 pm" is complete. |
| **Consistent** | Does not contradict another requirement or an engineering constraint. 5 per second with a 5 second response time on a service with 2 workers cannot both hold (Little's Law). |
| **Traceable** | Says why it exists, who asked for it and how the number was derived. Fields 5 and 6 of the structure. |
| **Time scale** | Averages over a day hide the peak. Averages over a second exaggerate noise. Pick the window the business cares about and state it. |

Lecture 02 covered the metric side of these checks. This slide applies them to the requirement as a whole.

---

# Part 2: Performance measurement plan

*What we measure, with which instruments, and what each kind of test is for.*

### In this part

1. **Open loop and closed loop** — How the load generator behaves while it waits, and why it changes what you measure.
2. **Six types of test, one demo each** — Load, stress, soak, regression, benchmark, pipe-clean. For each: what it is, a recorded run on the order API, what the run showed.
3. **Two instruments** — The generator sees the service from outside, the monitor from inside. One row of output, column by column.
4. **Exercises 7.2 and 7.3** — Which test produced each chart; what a passing test actually measured.

The longest part of the lecture. Demo 1 is worth slowing down on: every later demo is Demo 1 with one thing changed.

---

## Closed-loop load waits for the system. Open-loop load does not.

### Closed loop: N virtual users, each waits for its response

*[Figure: User 1, User 2, User 3 each connected to the System.]*

- Each user sends a request, waits for the reply, thinks, sends the next.
- Offered load = N / (response time + think time). As the system slows down, the users send less. The load backs off automatically.
- This is what JMeter's standard Thread Group does.

### Open loop: requests arrive at a fixed rate regardless of replies

*[Figure: Arrival process → Queue → System.]*

- Requests arrive at λ per second whether or not earlier ones have been answered. If the system falls behind, the queue grows.
- This is how real traffic behaves. Customers do not stop arriving because the last customer is still waiting.
- In JMeter this is the Open Model Thread Group (or the Throughput Shaping Timer plugin). In k6 it is a constant-arrival-rate executor.

The queueing models in Lectures 04 and 05 assume open-loop arrivals. A closed-loop test does not reproduce those conditions, so its results cannot be compared with the model's predictions.

---

## Pokémon Go, 2016: Niantic planned for 5x the expected traffic and got 50x

- Niantic launched Pokémon Go in July 2016 on Google Cloud.
- Before launch they estimated the expected player traffic and provisioned for a worst case of five times that estimate.
- Within days actual traffic was about fifty times the original estimate, ten times the worst case they had planned for.
- Players saw login failures, server errors and frozen games for most of the first week. The international rollout was paused while capacity was added.
- Google's own account of the launch (Google Cloud blog, 2016) is the source for these figures.

**Question: which of the performance tests in this lecture would have caught this before launch?**

Pause here and write down your answer before going to the next slide.

*[Figure: Google Trends, worldwide web search interest, May 2016 to Jul 2026. The spike at the far left is the July 2016 launch; the entire decade since fits under it.]*

---

## Answer: a load test would not have caught it; a stress test would have

### Load test

- A load test checks the system at the load you specify. Niantic specified up to 5x their estimate. The system handled 5x. The test passed, and it was right to pass.
- At 50x the load test is silent. It was never asked about 50x. That number came from the workload estimate (Lecture 03), and no test can fix an estimate.

### Stress test

- A stress test raises load until the system breaks and records how it breaks. It would have found the ceiling, somewhere above 5x, and the failure mode past it.
- The failure mode was the real damage: logins failing, sessions dropping, the app unusable for everyone, not just the overflow. That is ungraceful degradation, and it is visible in a stress test before launch.

### What the stress test result changes

Knowing the system falls over completely past the ceiling, you design for the case where the estimate is wrong: admission control or a waiting room so that at 50x most players still get in, slowly, instead of nobody getting in. Niantic added capacity after the fact; the stress test would have made the shape of the failure a known quantity before launch.

### For the rest of this lecture

The load test tells you whether you meet the target. The stress test tells you what happens when the target is wrong. You need both, because the target is often wrong.

---

## Six types of performance test, each answering a different question

| Type | Question it answers | What you vary | Typical finding |
|---|---|---|---|
| Load test | Does the system meet its targets at the expected load? | Nothing. Hold the expected load steady. | Response time and error rate at the agreed load. |
| Stress test | Where does it break, and how? | Load, upward, past the expected range. | The knee, the ceiling, and whether degradation is graceful. |
| Soak test | Does it stay healthy over time? | Time. Hold a steady load for hours. | Memory growth, leaked connections, slow drift in response time. |
| Regression test | Did the last change make it slower? | The build. Same test, new code. | A performance defect introduced by a code change. |
| Benchmark | How does it compare to a standard or a baseline? | The system, against a fixed load. | Numbers that can be compared across versions or products. |
| Pipe-clean test | Is the test itself correct? | Nothing. Run the test at low load and check the plumbing. | Scripts that pass while measuring the wrong thing. |

Two more that come up: isolation testing (one component at a time) and user acceptance testing (users say it feels slow). Both are covered later.

Each of the six gets three slides: what the test is, a recorded run on the same small service, and a summary of what the run showed.

---

## 1. Load test: the system at the load you expect

### What it is

- A load test holds the expected load steady and checks whether the system meets its performance requirements at that load.
- It simulates normal use. The load is the number from the workload model, not a guess and not the maximum.
- Also called volume testing.

### How it is run

- Set the arrival rate from the workload model. Use an open-loop generator so the rate does not depend on the system's response.
- Run long enough to get past warm-up and into steady state, then for the window the requirement names.
- Record every request, plus CPU and memory on the server.

### What you look for

- Response time flat over the run, not drifting upward.
- Throughput equal to the offered load. A gap means work is queueing or failing.
- Error rate near zero.
- Pass or fail is decided against the written requirement, not by looking at the chart.

A load test tells you whether the system meets its targets at one load. It tells you nothing about any other load, or about what happens after an hour.

---

## Demo 1 on screen: four windows, four jobs

| Window | Component | Command | What it does |
|---|---|---|---|
| Top left | **The service** | `python app.py` | Answers requests. Knows nothing about the test. One log line per order. |
| Top right | **Check, then monitor** | `single_request.py` · `monitor.py` | One order by hand to see a correct body and measure S (64 ms here). Then the server-side instrument: one CPU and memory row every 10 s. |
| Bottom left | **The load generator** | `pyload.py open --rate 10 --minutes 3` | Open loop: a new order every 100 ms on average, random spacing, regardless of replies. The client-side instrument: one .jtl line per request. |
| Bottom right | **The monitor file, live** | `demo1-r1-mem.csv` | What the machine is doing while the generator runs. Joined to the .jtl by timestamp. Columns on the next slide. |

Two of the four are instruments. Outside view (generator) and inside view (monitor); neither alone explains a number.

*[Figures: screen recordings of the four windows.]*

---

## The monitor file, column by column

```
time,epoch,cpu_pct,mem_used_mb,mem_avail_mb,rss_mb[app.py],rss_mb[jmeter],rss_mb[pyload]
2026-10-05 12:12:44,1791173564,17.0,22984.8,10961.1,46.9,0.0,37.6
```

| Column | Example | Meaning |
|---|---|---|
| `time` | 12:12:44 | Wall clock of the sample. For reading by eye. |
| `epoch` | 1791173564 | The same instant in Unix seconds. This is the join key to the .jtl, whose timeStamp column is in Unix milliseconds. |
| `cpu_pct` | 17.0 | CPU busy across the whole machine since the last sample. On an 8 core laptop one saturated core reads as about 12.5%, so compare with cores × utilisation, not with 100%. |
| `mem_used_mb` | 22984.8 | Memory in use across the whole machine. Mostly everything else on the laptop. Useful only for its trend. |
| `mem_avail_mb` | 10961.1 | Headroom. When this reaches zero the machine swaps and every number on this slide stops meaning anything. |
| `rss_mb[app.py]` | 46.9 | Resident memory of the service process. The column that matters for the soak test: at constant load it should be constant. A straight line upward is growth that nobody is clearing. |
| `rss_mb[jmeter]` | 0.0 | Memory of any JMeter process. Zero here because the Python generator was used instead. |
| `rss_mb[pyload]` | 37.6 | Memory of the load generator. Non-zero only while a run is in progress, so it also marks where the run starts and ends in this file. If it grows, the generator is storing results in memory and is a problem of its own. |

**Interval:** 10 seconds: fine enough to see a slope over a 3 minute run, coarse enough that the monitor itself is not a measurable load. Your samples arrive 11 to 13 seconds apart on Windows; that is psutil, not a problem.

---

## After the run: analyse.py reads the two files and prints one row

| test | offered | run | samples | p50 | p95 | p99 | err_pct | throughput | cpu_pct | mem_start_mb | mem_end_mb |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Load | 10.02 | 1 | 1595 | 0.07 | 0.12 | 0.15 | 0.0 | 9.97 | 16.16 | 22964.8 | 22050.4 |

| Column | Value | Meaning |
|---|---|---|
| `offered` | 10.02 | Requests actually sent per second, counted from the .jtl. Asked for 10; the random spacing averaged out to 10.02. This is the λ that goes into the Utilisation Law. |
| `samples` | 1595 | Requests recorded after dropping the first 20 seconds of warm-up. Reconcile this against the lines in orders.log for the same window; if they differ, the run is discarded. |
| `p50 / p95 / p99` | 0.07 / 0.12 / 0.15 s | Response time at the generator, in seconds. Half of all orders came back within 70 ms; 19 in 20 within 120 ms; 99 in 100 within 150 ms. Against a 200 ms requirement, this passes at p95 and at p99. |
| `err_pct` | 0.0 | Requests whose body did not contain order_id, or contained error, or timed out. Zero. In Demo 6 this column is the one that lies. |
| `throughput` | 9.97 | Successful orders completed per second. Equal to the offered rate, so the service kept up; nothing queued for long or failed. |
| `cpu_pct` | 16.16 | Average whole-machine CPU during the run, from the monitor. Prediction: λ × S = 10 × 0.064 = 0.64 of one core, which is 8% of 8 cores. The machine was already using about 7% at idle, and the generator and monitor run on it too. 8 + 7 is 15; measured 16. The model holds. |
| `mem_start / mem_end` | 22964.8 / 22050.4 | Whole-machine memory used at the first and last monitor sample. It went down by 900 MB during the run: something else on the laptop released memory. This column is about the machine, not the service. For the service, look at rss_mb[app.py] in the monitor file. |

This one row is the whole lecture in miniature: a load you chose, a prediction, two instruments, a reconciliation, and a pass or fail against a requirement. The other demos change what you put in the first column.

---

## Demo 1. Load test at 10 requests per second for 3 minutes, three runs

### Setup

- The order API: one Flask file, in-memory store. POST /orders verifies the customer token (PBKDF2, the CPU cost per request), checks stock against a catalogue, computes the total and stores the order in a dict. For the recordings, service and load generator ran on one machine with one core.
- Single-request check first: one order on its own takes **S = 34 ms**. That is the service time.

### Prediction, written down first

- Utilisation Law (Lecture 02): with c cores, utilisation is about λ × S / c. For λ = 10 per second, S = 34 ms, c = 1, that is **0.34**.
- Well below 1, so the service should keep up: throughput 10 per second, p50 near S, p95 somewhat above it because arrivals bunch, no errors.
- If response time drifts upward instead, utilisation is nearer 1 than we think, and the workload model and the hardware disagree.

### Chart from the recording

*[Figure: Demo 1, three 3 minute load tests at 10 requests per second — p50 and p95 response time, error rate and throughput against time.]*

### What to watch

- Response time line: flat or climbing.
- Throughput against offered load: should match.
- Server CPU against the predicted utilisation.
- Any errors at all.

*Sandbox run: one core, generator on the same machine, S = 34 ms. The laptop run on the previous three slides had S = 64 ms on 8 cores; same shape, different numbers.*

---

## Demo 1 summary

### What the run showed

- Response time stayed flat in all three runs: p50 40 ms against S = 34 ms, p95 100 to 120 ms. The p95 is above S because arrivals bunch and queue briefly, which is what the open-loop generator is for.
- Throughput matched the offered 10 per second in all three runs. The service kept up.
- Server CPU averaged 35 to 37% across the runs against a predicted 34%.
- No errors.

### What to take from it

- A pass against the requirement, with three conditions attached: this hardware, this load, this duration. Change any one and the result no longer applies.
- The prediction and the measurement agreed. When they do not, the gap is where the work is.
- A load test answers one question: does it meet the target at the expected load. It was not asked about anything else.

**What it did not tell us:** what happens above 10 per second, or after an hour. The next two tests.

*Sandbox run: one core, generator on the same machine, S = 34 ms. The laptop run on the previous three slides had S = 64 ms on 8 cores; same shape, different numbers.*

---

## 2. Stress test: the system beyond its capacity

### What it is

- A stress test raises the load past the expected range until the system can no longer cope, and records what happens when it cannot.
- It establishes the limits within which the system can be expected to operate.
- It also checks for graceful degradation: whether the system slows down or falls over.

### How it is run

- Start at a load the system is known to handle. Step the offered rate up at fixed intervals, holding each step long enough to settle.
- Stop when errors appear or response time is far beyond the target.
- Record the same quantities at every step: p50, p95, p99, error rate, throughput, server CPU and memory.

### What you look for

- **The knee:** the load at which response time stops being flat and starts climbing steeply.
- **The ceiling:** the throughput that stops rising no matter how much more is offered.
- **The failure mode:** slower but correct, or errors, timeouts, crashes, wrong output.
- Whether it recovers when the load drops back.

A stress test is not a load test with bigger numbers. Its output is a limit and a failure mode, not a pass or fail.

---

## Demo 2 on screen: one row per step, and what the CPU column adds

| offered | p95 | p50 | thr | err | cpu_pct | Reading |
|---|---|---|---|---|---|---|
| 5 | 0.36 | 0.12 | 5.00 | 0.00 | 14.0 | Below the knee. Utilisation 0.36. p95 three times p50: arrivals bunching, nothing more. |
| 10 | 2.24 | 0.69 | 9.30 | 0.00 | 13.7 | Past the knee. Utilisation 0.71. Throughput still almost matches offered, but the queue has formed: p95 2.2 s. |
| 15 | 8.82 | 3.78 | 12.85 | 0.89 | 15.4 | At the ceiling. Throughput 12.9 against 15 offered. First errors. Pinned core at 100%: the machine figure is idle baseline plus one full core. |
| 20 | 12.16 | 8.67 | 12.98 | 31.59 | 15.5 | Over the ceiling. Throughput does not move. A third of requests refused. CPU unchanged: the core has nothing more to give. |
| 25 | 11.92 | 7.10 | 14.60 | 40.65 | 17.1 | Same throughput, more refusals. The extra CPU is the generator and the OS handling connections that go nowhere. |
| 30 | 11.79 | 2.07 | 15.33 | 50.22 | 18.0 | Half refused. p50 falls to 2 s because refused requests take milliseconds and count. The survivors still wait 12 s. |

Read down the `thr` column for the ceiling, down the `p95` column for the knee, and down the `err` column for the failure mode. The `cpu_pct` column says which resource is the ceiling: one core, saturated from 15 per second on.

---

## Demo 2. Stress test, 5 to 30 requests per second, service on one core

### Setup

- Same order API, same laptop (8 cores). This time the service is pinned to one core with `start /affinity 1`, so the ceiling is reachable. Generator and monitor on the other seven.
- Sequential check: **S = 112 ms** (min 94). Includes a fresh connection per request, so an upper bound on the CPU cost.
- Offered load in steps: 5, 10, 15, 20, 25, 30 per second, 60 s each. Timeout 20 s.

### Prediction, written down first

- From the sequential S: ceiling 1 / 0.112 = **9 per second**.
- From the 8 core run's CPU figures (about 35 ms of CPU per request): ceiling about **28 per second**.
- So somewhere between 9 and 28, knee below it. How it fails past the ceiling is unknown.

### Chart from the recording

*[Figure: Demo 2, stepped load, 5 to 30 per second, one core. One point per 60 second step: p50 and p95 response time; successful throughput against offered, with error rate.]*

### What to watch

- The step where p95 jumps: between 5 and 10.
- Where successful throughput stops rising: about 13 to 15.
- Errors from 20 per second, half of all requests by 30.
- Why p50 goes down again at 30: the failures are fast.

---

## Demo 2 summary

### What the run showed

- **Ceiling:** successful throughput flattened at 13 to 15 per second from 15 per second offered. About 70 ms of core time per order, not the 35 ms estimated from the 8 core run and not the 112 ms from the sequential check. Both predictions bracketed it; neither hit it.
- **Knee** between 5 and 10 per second: p95 0.36 s at utilisation 0.36, then 2.2 s at 0.71. The 1 / (1 − ρ) curve from Lecture 04, on screen.
- **Failure mode:** from 20 per second, 32% of requests failed, rising to 50% at 30. Response time for the ones that got through sat at 12 s. The failures were fast, not timeouts, which is why p50 drops to 2 s at 30: a refused request takes milliseconds and still counts.
- **Monitor:** whole-machine CPU 14% at 5 per second, 18% at 30. One pinned core is 12.5% of eight; the rise above the idle baseline is that core going to 100% by 15 per second, and the generator doing more work after that.

### What to take from it

- **Ungraceful.** Past the ceiling the service did not just slow down; it started turning requests away. A customer at 30 per second has a coin-flip chance of an error. That is a design finding, and it would not have been found by any load test.
- The per-core cost measured on many cores did not transfer to one core. Parsing, logging, the catalogue read and Windows itself all landed on the one core that was left. Scaling an estimate down is not the same as measuring it scaled down.
- Three S values from one afternoon: 112 ms sequential, 35 ms inferred from 8 core CPU, 70 ms from the one core ceiling. Record all three with how each was obtained. The ceiling is the one that matters for capacity.
- A percentile that goes down as load goes up is a signal to look at the error column, not a good sign.

*Sandbox run for comparison (one core, no affinity tricks): ceiling 29 per second, knee between 25 and 30, no errors within the 90 second steps. Same shape, different hardware, and it stopped before the failure mode appeared.*

---

## 3. Soak test: the system over a long time

### What it is

- A soak test holds a moderate, steady load for a long period and checks for problems that appear slowly: memory leaks, connection exhaustion, log files filling disks, slow drift in response time.
- Also called stability or endurance testing.
- The load is not the variable. Time is.

### How it is run

- Pick a load comfortably below the knee from the stress test, so that anything that changes is due to time and not to saturation.
- Hold it for as long as you can afford: 30 minutes shows the slope; hours or days show the failure.
- Record resource usage on the server at regular intervals, not just response time.

### What you look for

- Memory rising in a straight line with no plateau.
- Response time following it upward, usually after a delay.
- Anything that only shows up with time: open connections, file handles, disk usage, cache size.
- A rise that levels off is a cache filling. A rise that does not is a leak.

The size of the leak over the run is not the point. The slope is. From the slope you extrapolate the time to failure.

---

## Demo 3. Soak test, 8 requests per second for 10 minutes

### Setup

- Same service, no changes. The store is a dict in process memory. Every order stays in it, with its request and a rendered invoice text kept for audit, about 4 kB each. Nothing archives it.
- That is not a planted bug. It is what an in-memory store does unless someone writes the code that empties it.
- 8 requests per second, well below the knee from Demo 2, for 10 minutes: about 4,900 orders.

### Prediction, written down first

- **Memory:** 4,900 × 4 kB is about 20 MB of growth, in a straight line, no plateau. Small, but visible against the process baseline.
- **Extrapolated:** at this rate a 16 GB machine runs out in about six days of continuous load. At a real peak rate, sooner.
- **Response time:** no visible effect expected in 10 minutes. Lookups are by dict key, so they do not slow down as the store grows. We say that now so no one is surprised when p95 is flat.

### Chart from the recording

*[Figure: Demo 3, 10 minute soak at 8 requests per second — service process memory (MB) and p95 response time against time.]*

### What to watch

- The memory line. Load is constant, so memory should be constant. A straight upward line is a leak regardless of slope.
- Whether it plateaus.
- The p95 line: expect flat.
- Anything else that drifts.

---

## Demo 3 summary

### What the run showed

- Service process memory rose from 33 MB to 68 MB in 10.5 minutes, **3.4 MB per minute**, in a straight line with no plateau. The prediction was 1.9 MB per minute: the 4 kB per order became about 7 kB once Python's per-object overhead is counted. Right shape, wrong slope by 1.8x.
- p95 stayed flat, as expected: dict lookups do not slow down as the dict grows.
- Nothing in Demo 1 or Demo 2 would have caught this. Both ran for too short a time and both looked at response time, not memory.

### What to take from it

- A soak test finds what the other tests cannot: anything that depends on elapsed time rather than on load.
- Report the slope and the extrapolated time to failure, not the absolute growth over the run. At 3.4 MB per minute, 16 GB lasts about 3.3 days at this load.
- The fix is not hard (archive old orders, cap the audit copy), but nobody writes it until something shows that it is needed. The soak test is what shows it.

Memory on the server is worth recording in every test, not only the soak. It costs nothing and it is the first place leaks show.

---

## 4. Performance regression test: did the last change make it slower?

### What it is

- A performance regression test runs the same test against each new build and compares the result with the previous one.
- A result that got worse is a defect, treated like any functional defect.
- The first result, before any tuning or change, is the **baseline**. Everything after is reported relative to it.

### How it is run

- Fix the test: same plan, same load, same data, same environment, same playbook. The build is the only thing that changes.
- Run it on every build, or every merge. Put it in the CI pipeline so it is not optional.
- Keep it short enough that it actually runs. A five minute test that runs beats a one hour test that is skipped.

### What you look for

- p95 and throughput against the baseline, with a threshold for what counts as a regression (for example p95 up by more than 10%).
- Which change caused it. One change per build makes this easy; ten changes per build makes it guesswork.
- Changes that were meant to improve something else. A better prompt, a bigger model, more logging. Each has a performance cost.

Adding features has always slowed systems down. Today the bigger source is volume of change: code generated by AI tools lands faster than anyone profiles it. The regression test is the control.

---

## Demo 4. The same 5 per second load against two builds, 8 minutes each

### Setup

- Service on one core, as in Demo 2. Load 5 per second, below the knee, so any change in response time is the build and not queueing.
- **Build A:** the service as in Demos 1 and 2.
- **Build B:** one feature added. Reject an order if the same customer placed an identical one in the last 60 seconds. Written the obvious way: loop over every stored order and compare.
- Each run starts from an empty store. 8 minutes puts 2,400 orders in it.

### Prediction, written down first

- **Build A:** flat, near the Demo 2 value at 5 per second (p50 0.12 s).
- **Build B:** starts level with A, then drifts up as the store fills, because the duplicate check costs more per order as there are more orders to scan.
- **How much:** unknown. The scan of 2,400 small records may be milliseconds, which would hide inside the noise.

### Chart from the recording

*[Figure: Demo 4 — Build B minute by minute, Build A as reference lines.]*

Build A whole run: p50 0.13 s, p95 0.46 s. Build B whole run: p50 0.17 s, p95 0.66 s. 2,250 and 2,280 samples.

### What to watch

- Whether B sits above A at all.
- Whether B climbs minute by minute, or just sits higher.
- Minute 6: one bad minute, or the start of the slope?
- Errors: none on either build.

---

## Demo 4 summary

### What the run showed

- Build B was slower: p50 up 30% (0.13 to 0.17 s), p95 up 45% (0.46 to 0.66 s), on the same load, same machine, same data, same playbook. The regression test flagged it.
- Build B did not climb. Minute-by-minute p95 wandered between 0.50 and 0.68 s with one minute at 1.08. At 2,400 orders the scan costs a few milliseconds on this CPU, inside the run-to-run noise.
- One run of each. A 30% shift from a single pair of runs is a signal to investigate, not yet a measurement. A second Build A run says whether 30% is the feature or the afternoon.

### What to take from it

- This is what a regression test usually looks like in practice: a shift, a question of whether it is noise, and a reason to look closer. Not a clean curve.
- It only works because the test was fixed. Had the load or the data changed between A and B, a 30% difference would mean nothing.
- The mechanism is a prediction here, not an observation. To see it, the store has to be much bigger: a longer run, or a higher rate. The sandbox run below did both.

### Sandbox comparison

The same two builds on the sandbox: one slower core, 10 per second, 4 minutes. Build A flat at p95 100 ms. Build B p95 120 ms in minute one, 200 ms in minute four; p50 37 to 58 ms. The slope is the scan cost growing with the store, visible because the per-order cost was higher relative to S and the store filled twice as fast.

Same code, two machines, two different pictures of the same regression. Both are correct. The fix is the same: a per-customer index instead of a full scan, and the fixed test would show it working.

---

## 5. Benchmark: performance against a standardised load

### What it is

- A benchmark is a fixed, standardised load used to compare systems, products or versions. The load is the standard; the system is what varies.
- **External benchmarks** compare products: TPC for databases, MLPerf for inference, SPEC for CPUs. Reviewers use them to compare vendors.
- **Internal benchmarks** compare your own candidates: two models, two configurations, two hosting options.

### How it is run

- Define the load precisely and keep it identical across every candidate: same requests, same data, same rate, same duration.
- Change one thing per comparison. Model and prompt changed together tells you nothing about either.
- Record the same quantities for every candidate, in one table.

### What you look for

- The numbers side by side: response time, throughput, resource use, and whatever quality measure matters (accuracy, here).
- Where the candidates differ and where they do not.
- Whether the benchmark load resembles your real load. A benchmark on the wrong workload ranks the candidates wrongly.

A benchmark gives you the numbers. It does not make the decision. The decision is a trade-off, and someone has to own it.

---

## Demo 5. The same 5 per second load against three token-hashing settings

### Setup

- Service on one core, Build A. Load 5 per second for 2 minutes, identical for every candidate.
- Three candidates, one at a time: PBKDF2 at **25,000**, **100,000** and **400,000** iterations. More iterations makes a stolen token hash harder to crack, and costs CPU on every request.
- For each: p50, p95, successful throughput, error rate, server CPU.

### Prediction, written down first

- From the sequential S at 100,000 (112 ms, mostly hashing): 25,000 about 30 to 50 ms, 400,000 about 400 ms.
- One core: ceiling about 2.5 per second at 400,000. Offered 5 is twice that. Expect a growing queue, p95 climbing, errors before the 2 minutes are up.
- 25,000 and 100,000 both below the knee; 100,000 a few times slower, not sixteen.

### Results

*[Figure: Demo 5, three settings, same load, same machine.]*

| Setting | p50 | p95 | Throughput | Errors | CPU |
|---|---|---|---|---|---|
| 25,000 | 40 ms | 110 ms | 5.2 | 0 | 13% |
| 100,000 | 150 ms | 480 ms | 5.1 | 0 | 15% |
| 400,000 | 20,010 ms | 20,040 ms | 0.8 | 83% | 16% |

### What to watch

- 25k to 100k: p50 roughly four times. The hash is most of the request on this core.
- 400k: p50 equals the timeout. Nearly every request waited the full 20 s and was abandoned.
- Successful throughput at 400k: 0.8 per second, far below the ceiling, not at it.
- CPU 16%: the core flat out, on work nobody is waiting for.

---

## Demo 5 summary

### What the run showed

- 25,000: p95 110 ms. 100,000: p95 480 ms. Four times the hashing bought four times the median response time at this load. On one core the hash is the request.
- **400,000 did not get slower. It collapsed.** 83% of requests timed out at 20 s; successful throughput 0.8 per second against a ceiling of roughly 2.5.
- **Why below the ceiling:** the queue grew until every request waited past the client's 20 s timeout. The client gave up; the server did not know, and kept hashing tokens for orders nobody was waiting for. The core ran flat out (CPU 16%) producing almost nothing useful.
- Prediction said errors. The run said near-total loss. The direction was right; the severity was not predicted, because the model has no notion of abandoned work.

### What to take from it

- A benchmark gives the numbers; the decision is a trade-off. 100,000 costs 370 ms of p95 over 25,000 at this load and buys four times the cracking cost for an attacker. Whether that is worth it is a security question the test cannot answer.
- The ranking depends on the load. At 1 per second, 400,000 would have been fine. At 5 it is unusable. A benchmark result without its load attached is not a result.
- Over the ceiling with timeouts, throughput falls *below* the ceiling, not to it. Servers that cannot tell a client has left waste their capacity on ghosts. Admission control, or a queue with a limit, is the usual fix, and it is what a stress test with timeouts would tell you to add.
- One change per comparison. The iteration count was the only variable, which is why three bars can be read.

*Sandbox run for comparison: same three settings at 10 per second on its one core. 25k p95 20 ms, 100k p95 100 ms, 400k 48% timeouts and 5.3 per second useful. Same shape, milder collapse, because its 400k ceiling was closer to the offered load.*

---

## 6. Pipe-clean test: is the test itself correct?

### What it is

- A pipe-clean test is a low-load run whose only purpose is to confirm that the scripts, assertions, instrumentation and result collection all work.
- It validates the performance test, not the system. It is done before every real run, not once at the start.
- The failure it catches is the quiet one: the test runs, reports numbers, and the numbers are about something other than the service.

### How it is run

- Send one request by hand and compare the body with what the generator records for the same request.
- Check that every assertion in the plan actually checks the body, not only the status code.
- Run at low load for a minute and reconcile: requests in the generator's output equal requests in the server log, and the response times are in the plausible range.

### What you look for

- Assertions that cannot fail. A plan with no body assertion passes anything.
- Response times outside the range the model and hardware allow. Too fast is as suspicious as too slow.
- Counts that do not reconcile between generator and server.
- Configuration drift: a renamed model, a changed port, a moved log path.

When the plan is generated by an AI tool, this step matters more, not less. The tool does not know what a correct response from your service looks like. You do.

---

## Demo 6. A load test with a broken configuration and no assertions

### Setup

- Service on one core, Build A, 100,000 iterations. One change: `ORDERS_CATALOGUE` points at `C:\nope\catalogue.json`, which does not exist.
- The handler opens the catalogue first, catches the error, and returns a JSON error body with HTTP status 200, because that is how it was written.
- Generator: the Demo 1 plan with `--noassert`, so it checks the status code and nothing else. 5 per second for 1 minute.

### Prediction, written down first

- If the test were correct we would expect the Demo 2 figures at 5 per second: p50 120 ms, p95 360 ms.
- We know the configuration is broken. The question is whether the generator will say so.
- Prediction: it will not. 100% success, response time well below S, because no token is ever hashed.

### Generator summary, 60 second run

| samples | p95 | success | throughput |
|---|---|---|---|
| 294 | 39 ms | 100.0% | 4.89 / s |

### Server log, same minute (orders.log)

```
POST /orders 200 ERROR "[Errno 2] No such file or directory: 'C:\\nope\\catalogue.json'" elapsed_ms=1
POST /orders 200 ERROR "[Errno 2] No such file or directory: 'C:\\nope\\catalogue.json'" elapsed_ms=1
POST /orders 200 ERROR "[Errno 2] No such file or directory: 'C:\\nope\\catalogue.json'" elapsed_ms=2
(294 lines, all ERROR)
/health: "orders_in_memory": 0
```

### What to watch

- The success column: 100%. The generator had no way to know.
- p95 39 ms against 360 ms for a real request at this load: nine times faster than the service can do. The 39 is the per-request overhead on this laptop (log write, connection), paid whether or not any work happens.
- The server log and /health: every request an error, zero orders stored. Two views of the same minute, complete disagreement.

---

## Demo 6 summary

### What the run showed

- The generator reported a passing load test: 294 samples, 100% success, p95 39 ms, 4.9 per second.
- The server created zero orders. Every request hit the error path and was answered with a 200.
- The one number that gave it away was the response time, and only because the Demo 2 figure at the same load (p95 360 ms) was written down. On this laptop the gap was nine times, not the hundred times the sandbox showed, because the error path still pays the log write and connection cost.
- Nothing in the generator's output was false. Every request did return 200 in 39 ms. The output answered a question nobody asked.

### What to take from it

- **A green result means the test ran, not that the system worked.**
- Assert on the body. Status codes are set by whoever wrote the handler, and handlers that return 200 on error are common. The assertion that catches this is: the body contains `order_id`.
- Compare every result with the prediction before reporting it. A number outside the plausible range is a test defect until shown otherwise. Where the overhead is high, as here, the range is narrower, and the body assertion carries more of the weight.
- Reconcile counts: samples in the .jtl, lines in the server log, orders in /health. **294, 294, 0.** The third number is the one that ends the discussion.

This is step B1 (one request by hand, read the body) and step C3 (reconcile generator against server) of the playbook. Every run, not once.

---

## Exercise 7.3: What did this test actually measure?

A team submits the following as evidence that their service meets its throughput requirement of 50 orders per second.

**JMeter Summary Report (excerpt)**

| Metric | Value |
|---|---|
| Samples | 3,000 |
| Average (ms) | 3 |
| 95th percentile (ms) | 6 |
| Error % | 0.00 |
| Throughput | 50.4 / sec |

**Server log, same window (excerpt)**

```
12:04:11 POST /orders 200 ERROR "No such file: /etc/catalogue-prod.json"
12:04:11 POST /orders 200 ERROR "No such file: /etc/catalogue-prod.json"
12:04:11 POST /orders 200 ERROR "No such file: /etc/catalogue-prod.json"
(repeats for all 3,000 requests)
```

- What did the test measure? What did it not measure?
- Which single line in a JMeter plan would have caught this, and what should it check?
- The single-request check measured S at 112 ms on this machine. How should that have been used here?

---

## Isolation testing and user acceptance testing cover the gaps

### Isolation testing

- Test one component at a time: the web framework alone, the token check alone, the store alone.
- Used when the full-system test shows a problem and you need to find which tier owns it.
- For the order API: time the PBKDF2 call on its own in a loop. If it accounts for S, Flask and the store are not where the time goes. For a service with a real database, run the queries directly against it at the same rate.
- The stub replaces the slow component with a fixed delay. That lets you test the rest of the system at loads the real component could not sustain.

### User acceptance testing

- Real users, real tasks, and the question is whether it feels acceptable.
- Not a substitute for measurement. Users report that the system is slow; they do not report p95.
- Useful for setting the targets in the first place (Lecture 02, Miller and Nielsen thresholds) and for catching the case where the numbers pass but the experience does not.
- Common outcome: the requirement said 2 seconds, the system delivers 1.9 seconds, and users still complain, because the 2 seconds was never the right number.

---

# Part 3: Performance test plan

*How a test is set up and run so that someone else can run it again and get the same answer.*

### In this part

1. **Tests as experiments** — Reproducible, controlled, instrumented, recorded. The observer effect, measured.
2. **The test environment** — Matching production in structure; scale-up, scale-out, and what a scaled-down environment cannot tell you.
3. **Playbook, load model, scripts** — The written steps, the virtual users and how they arrive, and the generator's own cost.

Exercises 7.4 and 7.5 are in this part: your laptop as the test environment, and why a closed-loop result is not evidence of throughput.

---

## A performance test is an experiment, and the same rules apply

| Rule | Meaning |
|---|---|
| **Reproducible** | Someone else, following your written procedure, gets the same result within normal variation. If they cannot, the result is an anecdote. |
| **Unambiguous procedure** | Every step written down: how the system is started, what state the data is in, what commands are run, in what order. |
| **Controlled** | Nothing else running on the machine. No browser, no updates, no second test. On a laptop this means closing everything and checking with a process monitor. |
| **Validated instruments** | The tools that measure are themselves checked (Demo 6, the pipe-clean test). A profiler with a bug reports confident, wrong numbers. |
| **Recorded** | Raw output kept, not just the summary: the .jtl file and the server log, in the repo, for every run you report. |

Three runs per configuration is the minimum. One run tells you a number; three runs tell you whether the number means anything.

---

## Setting up the environment is most of the work

| Step | Task | Detail |
|---|---|---|
| 1 | Provision hardware and software | The machine or machines the test runs on, the operating system, the runtime, the model files. Write down versions. |
| 2 | Provision the load testing tools | JMeter on its own machine where possible. Java version recorded. Plugins installed and listed. |
| 3 | Develop use cases and scripts | Which requests, in what sequence, with what data. Scripts tested at low load first (pipe-clean). |
| 4 | Create test data | Realistic in size and shape. For the order API: a thousand distinct orders across fifty customers and two hundred SKUs, not the same order a thousand times. |
| 5 | Instrument | Decide what is measured and how before the first run. Server-side CPU and memory, not just client-side response time. |
| 6 | Deal with what the tests find | A performance test that finds a problem creates work. Budget for it. |

*After Molyneaux (2014), Chapter 3.*

---

## The measurement tools compete with the system under test

- Profilers, system monitors and logging are processes. They use CPU, memory and disk on the same machine as the thing you are measuring.
- On a CPU-bound service, the request handler already wants every core. Anything else you run on that machine takes cycles away from it and shows up in the response time. In the recordings here the load generator itself shared the one core with the service, and the stress test ceiling shows it.
- Instrumenting code changes the code. Timing calls, extra logging and debug flags all add work to the request path.
- Measurement tools have bugs. A sampling profiler that samples at the wrong interval, a monitor that reports the wrong unit.
- The practical rule: **measure the cost of measuring once, then decide what to leave on.**

### Demo 7 (sandbox): the Demo 1 load test, with and without a profiler attached

| Run | p50 (ms) | p95 (ms) | Throughput |
|---|---|---|---|
| No profiler (Demo 1, run 1) | 40 | 100 | 9.7 |
| Service under `python -m cProfile` | 40 | 110 | 10.5 |

Here the gap was small: cProfile instruments Python function calls, and this service spends almost all its time inside one C call (the PBKDF2 derivation). On a handler written in pure Python the same profiler can double the response time. The lesson is the same either way: you cannot know the cost is small until you have measured it.

Run the load generator on a different machine from the service where you can arrange it. If you cannot, say so in the test environment description and treat it as a known source of error.

---

## The test environment must match production in structure, not just size

| Aspect | Requirement |
|---|---|
| **Configuration** | Same operating system family, same runtime versions, same server settings. A different Python version or a different number of worker threads is a different system. |
| **Data** | The store and the request data should look like production in size, distribution and shape. A store with ten orders in it does not behave like one with a million. |
| **State** | Record the state of the system at the start and end of each run. If the database grew during the run, the next run starts from a different place. |
| **External dependencies** | Anything you cannot include (a third party API, a hardware device) is simulated with a stub that reproduces its delay and failure behaviour. |
| **Network** | If production has a network hop between tiers, the test should too. Running the generator and the service on one laptop removes every network delay from the measurement, and makes them compete for the same cores. |

The last point is the one that applies to every team in this module. Note it on your Test Environment slide rather than pretend it is not there.

---

## Scale-up and scale-out: two ways to shrink production for testing

### Production

*[Figure: Load balancer → Web server 1, Web server 2, Web server 3 → Database server.]*

Three web servers behind a load balancer, one database. Expected load: L requests per second.

### Test environment, two options

*[Figure: Load injector → Web server → Database server.]*

- **Scale-out production, scaled-down test:** One web server identical to a production web server, offered one third of the load (L/3). Tests one node at its real share.
- **Scale-up production, scaled-down test:** One web server with one third of the CPU and memory of the production server, offered one third of the load. Tests the shape at reduced size.

Neither option tests the load balancer, the shared database under full load, or the network between three web servers and one database. **Write down what the scaled-down environment does not test. That list is as much a result as the numbers are.**

---

## A scaled-down environment must scale every component together

- The rule from the previous slide: if you cut the load to a third, cut the CPU, memory, data size and storage to a third as well. Cutting one and not the others changes the ratios, and the ratios are what you are measuring.
- For the order API the two resources do not scale together. The ceiling is set by cores: c / S. The time to failure under soak is set by memory: free RAM divided by bytes per order times order rate. Cutting cores by a third changes the first and leaves the second alone.
- So a test on a small machine can get the ceiling right in proportion and the time to failure completely wrong, or the other way round.

### Same service, three machines (illustrative)

| Machine | Cores | RAM | Ceiling (c / S) | Soak at 8/s, 4 kB per order: RAM gone in |
|---|---|---|---|---|
| Recording sandbox | 1 | small | 29 /s | see Demo 3 |
| Laptop | 8 | 16 GB | about 235 /s | about 3 days |
| Server | 16 | 64 GB | about 470 /s | about 12 days |

Ceiling scales with cores. Time to failure scales with RAM. Neither scales with the other, and the load you test at changes which one bites first.

### What this means when the test machine is a laptop

Your laptop is not a scaled-down version of the production server. It is a different machine running the same code. The honest statement is: these are the numbers on this hardware; here is what we expect to change on the production hardware, and why. That expectation is a prediction, written down before anyone measures on the real thing.

---

## A playbook makes the test repeatable by someone who was not there

*Two hosts: **meter** (JMeter) and **api** (Flask + store), connected by HTTP.*

### A. Initialise

- **A1.** `[api]` Append date, time and git commit hash to `/tests/log/runs.log`.
- **A2.** `[api]` Record the settings: build, PBKDF2 iterations, catalogue path (from `orders.conf`).
- **A3.** `[api]` Start the service from an empty store. Confirm `/health` reports 0 orders.
- **A4.** `[api]` Clear the request log. Record free memory and CPU idle. Start `monitor.py`.

### B. Run

- **B1.** `[meter]` Send one order by hand (`single_request.py`). Confirm `order_id` in the body and S in range.
- **B2.** `[meter]` `jmeter -n -t /scripts/load-01.jmx -l /output/load-01-YYYYMMDD-r1.jtl`
- **B3.** `[meter]` Watch for errors until the plan completes. Do not touch either machine during the run.

### C. Record

- **C1.** `[api]` Copy the request log and the monitor CSV to `/tests/log/` with the run name.
- **C2.** `[meter]` Copy the .jtl to the team repo under `results/`.
- **C3.** `[api]` Record end state: orders in memory from `/health`, free memory, request count in log equals samples in .jtl.

### What makes it a playbook and not a note

- Every step names the machine it runs on.
- Every command is written out, not described.
- Every artefact has a path and a naming rule with the date and run number in it.
- The start state and the end state are both recorded, so a change in the system between runs is visible.
- Step B1 is the pipe-clean check, done every time.
- Step C3 is the reconciliation: the server saw what JMeter sent. If the counts differ, the run is discarded.

The three-letter machine tags are a convention; use whatever names your team uses, but use them consistently.

*Adapted from the three-host playbook in the original ICT3102 notes (meter / www / sql), rewritten for the order API.*

---

## Load generators simulate users. JMeter is ours; you will meet others

- A load generator sends requests to the system under test at a controlled rate or with a controlled number of simulated users, and records what comes back.
- The generator has to be programmed. Out of the box it knows nothing about your service. The script is where the workload model (Lecture 03) becomes actual requests.
- There is usually more than one kind of user. An order API has customers placing orders, a dashboard polling order counts, and a nightly export job. Each is a different script.
- The generator records response time from its own point of view: request sent to response received, including the network. Server-side timing is a separate measurement and the two will not match.

| Tool | Where you will meet it | Note |
|---|---|---|
| Apache JMeter | This module, most enterprises | Java, GUI for building plans, command line for running them. Open Model Thread Group for open-loop load. |
| k6 | Newer web teams, CI pipelines | Scripts in JavaScript, runs from the command line, designed for open-loop arrival rates. |
| Locust | Python teams | Scripts in Python. Closed-loop by default; needs care for open-loop. |
| LoadRunner | Large enterprises, banks | Commercial. The tool in the original case study for this lecture. |

The concepts transfer between tools. The mistakes transfer too, particularly the open-loop and closed-loop one on the next slides.

---

## The load model: who the virtual users are, how many, how they arrive

| Element | Meaning |
|---|---|
| **User types** | Each distinct behaviour gets its own script and its own count. The mix should match the workload model, not what is convenient to script. |
| **Think time** | The pause between a user's requests. A human reading a result pauses; a batch job does not. Think time of zero turns a user into a tight loop and changes the load completely. |
| **Pacing** | How users enter and leave. All at once (big bang) tests the startup transient. Ramp-up over minutes tests the steady state. Ramp-down tests recovery. |
| **Load profile** | The shape of offered load over the run: flat, stepped (stress), a spike, or a recorded trace replayed from production. |
| **Duration** | Long enough to pass the warm-up and reach steady state. Report numbers from the steady window only, and say where the window starts. |

The load model is the workload model (Lecture 03) turned into generator settings. Every number in it should trace back to a figure in the workload model.

---

## Scripts come from use cases, not from the functional test cases

- A functional test case exercises a feature once and checks the output. A performance script represents what a typical user does over a session, with realistic data and realistic pauses.
- The set of scripts should cover the requests that carry most of the load, not every request the system supports. Ten use cases covering 90% of traffic is normal.
- Scripts need to be tested for correctness before they are used to test anything else. A script that silently submits the same order three thousand times tests the cache, not the service.
- Data comes from a file the script reads, not from constants in the script. JMeter's CSV Data Set Config is the usual mechanism.

### Example script: one customer places one order

1. **HTTP GET `/catalogue?q=...`** — Browse. Cheap read, but it is most of the traffic.
2. **Think time: 3 seconds** — The customer looks at the results.
3. **HTTP POST `/orders`** body: `{customer_id, token, items}` — Token check, stock check, store. This is where the CPU time goes.
4. **Think time: 5 seconds** — The customer reads the confirmation.
5. **HTTP GET `/orders/{id}`** — Reads it back. Cheap: a dict lookup.

Compare with the original example in the notes: GET index.html, GET stylesheet, GET image, think 10 seconds, GET links.html. Same structure, twenty years apart.

---

## From estimate to measurement: where this lecture sits in the module

| Stage | Lecture | What it gives |
|---|---|---|
| **Workload model** | Lecture 03 | How many requests, of what kind, when. The target load. |
| **Performance model** | Lectures 04, 05 | What the queueing model predicts for that load. The expected numbers. |
| **Performance test** | This lecture | What the system actually does under that load, measured in a controlled environment. |
| **Diagnosis** | Then | Model against measurement. Where they differ, and why. The recommendation. |

### If one thing is remembered from today

A test can only check the number you give it, in the environment you give it, with the load you generate. Each of those three is a decision you make before the first request is sent, and each one can make a correct measurement answer the wrong question.

### Next

The order store in these demos lives in process memory, and Demo 3 showed the cost. Next lecture asks what changes when it lives in a database: what gets faster, what gets slower, and why the database is usually where the knee is.

---

## References cited in the slides

- Bondi (2015), Table 7.2 — structure of a performance requirement.
- Eckhardt et al. (2016) — sentence shapes for well-formed performance requirements.
- Miller (1968) and Nielsen (1993) — response time thresholds (about 100 ms instantaneous; under 1 s keeps the flow of thought).
- Molyneaux (2014), Chapter 3 — setting up the test environment.
- Google Cloud blog (2016) — account of the Pokémon Go launch.
