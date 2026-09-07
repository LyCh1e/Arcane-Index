# ICT3113 Performance Optimisation and Design
## Lecture 3: Workload Identification

**Presented by** A/Prof Donny Soh
Programme Leader, Applied Artificial Intelligence
Programme Leader, SITxNVIDIA (SNAIC) AI Training
InfoComm Technology (ICT) Cluster
Singapore Institute of Technology

*SIT Internal*

---

## Learning Outcomes

- Define a workload in terms of transaction types, arrival rates, and service demand per transaction.
- Identify the business drivers behind a system's workload.
- Estimate arrival rates from business quantities using order-of-magnitude decomposition.
- Distinguish peak from average demand, and explain how peak demand influences capacity planning.
- Apply workload estimates to the Utilisation Law to sanity-check a proposed design.

---

## Pont des Arts, June 2014

In June 2014, a section of railing on the Pont des Arts in Paris collapsed under the weight of "love locks" — padlocks attached by couples, estimated at around 45 tonnes across the bridge by the time the city removed them.

- No single padlock mattered. The workload arrived one small transaction at a time, over years, and nobody was measuring it.
- The bridge was designed for pedestrians. The actual workload was pedestrians plus the accumulated steel it was never designed to carry.

Many capacity failures happen because the actual workload is different from the workload the system was designed for — the workload nobody identified.

---

## What is a Workload?

The workload of a system is the demand placed on it: what requests arrive, how often they arrive, and how much work each one needs.

- **Transaction types** — what kinds of requests the system serves.
- **Arrival rates** — how many of each type arrive per unit time.
- **Service demand** — how much processing each transaction requires.

A workload statement reads like this: "740 displays across 185 stations, each refreshed once per minute, 50 ms of controller work per refresh."

What a workload is not: a benchmark score, a load-test setting, or a number invented after the system is built.

---

## Workload Drivers

Arrival rates are business numbers in disguise. To estimate a workload, start from the business quantity, not from the server.

- **MRT:** station count, number of displays and refresh frequency drive display updates; ridership drives passenger-facing transactions such as gate activity.
- **Digital payments:** payday, billing cycles and major campaigns create predictable peaks in transaction volume. The end of the month looks nothing like the middle.
- **Tax filing:** the deadline drives submissions. Most of the year's load arrives in the final weeks.

The business calendar is the first performance document you should read.

---

## Estimating a Workload

Decompose from a quantity you can defend:

**population → active fraction → actions per active user → time window → arrival rate**

- Early in design, order-of-magnitude estimates are often enough to eliminate infeasible architectures: you are choosing between 1, 100 and 10,000 requests per second. Refine the estimate as you approach capacity and SLO decisions, where 100 versus 120 can matter.
- State every assumption so it can be challenged. An estimate with hidden assumptions cannot be corrected.
- Add headroom for growth and estimation error. For illustration, we may test headroom of ×2 to ×5; the appropriate headroom depends on uncertainty, burstiness, redundancy, scaling delay and the SLO.

---

## Worked Example: e-Filing Deadline

1. Assume 2 million taxpayers file online, and 20% file on the final day: 400,000 filings.
2. Assume filings spread over a 12-hour window: 400,000 / 12 ≈ 33,000 per hour ≈ 9.3 per second on average.
3. Assume the evening peak is 3× the window average: ≈ 28 filings per second.
4. Each filing session generates about 30 web requests: ≈ 830 requests per second at the web tier.
5. Sanity check with the Utilisation Law: at 20 ms per request, that is 830 × 0.02 ≈ 16.6 units of continuously busy service capacity. Modelling each server as one service centre handling one request at a time, at an illustrative 70% utilisation target: ≈ 24 servers.

Every number above is an assumption. That is the point: each one is visible, and each one can be challenged and refined.

---

## Peak vs Average

Design for peak demand and the SLO. How much capacity you actually keep provisioned depends on your scaling, queueing and admission-control strategy.

- A system averaging 100 requests per second with peaks of 1,000, sized for the average, is down precisely when the most users are watching.
- Many important peaks are behavioural and predictable: payday, lunchtime, deadlines, launches. They often appear on the business calendar in advance.
- Peak-within-peak: when results are released at 12:00 sharp, the hour's load does not spread across the hour. It lands in the first minute.

---

## When the Peak Arrives All at Once

July 2023: tickets for six Singapore shows of Taylor Swift's Eras Tour went on sale — roughly 330,000 seats at the National Stadium.

- Demand was estimated in the millions. The real workload was not "sell 330,000 tickets". It was "absorb millions of arrivals in the opening minutes, hold them in a fair queue, and keep the queue itself responsive."
- During an extreme peak, the queueing system is the product. If the queue page falls over, it does not matter how fast the checkout is.

Workload identification changes the architecture itself: a virtual waiting room is a design response to an arrival-rate estimate.

---

## Workload Mix

Total volume can stay constant while the workload changes completely.

- A checkout costs many times more than a page view: database writes, inventory checks, a payment gateway round trip.
- A campaign that doubles checkouts without changing total traffic has changed your workload.
- Reads and writes, daily entries and month-end reports, browse and buy: the proportions matter as much as the total.

When you state a workload, state the mix, not just the volume.

---

## Workload Identification – Two Possible Architectures

Identify and estimate the workload for the train control system:

- assume that each display shows new information once per minute
- compare the workload for the two architectures shown below
- estimate the workload for the web server and each controller
- estimate values based on Singapore's MRT system

**Two architectures:**

**With a single central controller**
```
                 → Map
Controller  →   Display
     ↓      →   Display
    Web     →     ...
            →   Display
            →   Display
```

**With sub-controllers at each station**
```
                 → Map
Controller  →   Station → Display
     ↓      →     ...   → Display
    Web     →   Station → Display
                         → Display
```

Consider the workload of our train system.

- Assume each display refresh generates one request to the web server. How long can the web server take to service a single request, if it is to support the workload estimated earlier?
- If it takes 50 milliseconds to update each display, and 50 milliseconds of central-controller work to send an update to a station controller, what is the utilisation of each controller due to display updates, in each of the proposed architectures?

---

## Workload Estimation – Exercise

- Central controller: 185 / minute
- Each station controller: 4 / minute
- Central controller (sub-controller architecture): 185 × 4 / minute

---

## Workload Estimation: Exercise (Manufacturing)

A contract manufacturer must ship 120,000 units this month: 20 working days, one 8-hour shift per day. The bottleneck station needs 4 seconds of machine time per unit.

1. What average production rate, in units per hour, is needed to meet the order book?
2. What is the utilisation of the bottleneck station at that rate?
3. The customer takes 40% of the month's volume in the final week (a retail promotion). Assume units cannot be pre-built. What production rate does that week require, and can a single shift still cope?

---

## Workload Estimation: Exercise (Healthcare)

A polyclinic opens 60 appointment slots per hour and also accepts walk-ins. From past data: 70% of the 8–10 am slots are booked, and walk-ins arrive at 25 per hour in the morning peak. Assume all booked patients attend during their scheduled hour. Registration takes 45 seconds per patient at a single counter.

1. Estimate the total patient arrivals per hour between 8 and 10 am.
2. What is the utilisation of the registration counter?
3. A flu-vaccination drive is expected to add 15 walk-ins per hour. Can one counter still cope?

---

## Workload Estimation: Exercise (IT)

An e-commerce site runs a 12:00 noon flash sale. Marketing data: 500,000 app users received the push notification, and past campaigns show 4% open it within the first minute. Each arriving user generates 6 requests to the product service; each request takes 10 ms. Normal traffic outside the sale averages 40 requests per second.

1. Estimate the user arrivals in the first minute, and the resulting request rate per second at the product service. These are two different numbers: keep both.
2. How many servers are needed for the first minute, if each server should stay at or below 70% utilisation?
3. What is the peak-to-average ratio, and what does it imply about how to provision?

---

## From Workload to Design

Every exercise today used the same chain:

**business driver → arrival rate × service demand → utilisation → capacity decision**

- Estimate at design time; measure in production. When they disagree, the measurement wins and the estimate gets corrected.
- An estimate that is wrong by 10× and caught at design time costs a meeting. The same error caught in production is the Pont des Arts railing.

Next: what happens between arrival and completion — queueing, and why response time rises sharply as utilisation approaches 100%.

---
*SIT Internal — ICT3113 Performance Optimisation and Design, Singapore Institute of Technology*
