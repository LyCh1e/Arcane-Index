# ICT3113 Performance Optimisation and Design
## Lecture 5: JMeter Recap

**Presented by** Donny Soh

*SIT Internal*

---

## Learning Outcomes

- Write a proper test plan from number of concurrent users, average session time and arrival rate.

---

## Flask App to Profile

First make sure that all the components are working on the GUI mode first.

```python
@app.route("/sort", methods=['GET'])
@flask_profiler.profile()
def sort():
    if request.method == "GET":
        unsorted = (request.args.get("unsorted_list"))
        unsorted = unsorted.replace('[', '')
        unsorted = unsorted.replace(']', '')

        unsorted = list(unsorted.split(","))
        unsorted = [int(i) for i in unsorted]
        unsorted.sort()
        return (json.dumps(unsorted))

app.run()
```

Testing in the browser:

```
http://localhost:5000/sort?unsorted_list=[3,4,22,5,3,4]
```

Response:

```
[3, 3, 4, 4, 5, 22]
```

---

## JMeter Test

**Thread Group**

| Field | Value |
|---|---|
| Name | Thread Group |
| Action to be taken after a Sampler error | Continue (selected), Start Next Thread Loop, Stop Thread, Stop Test, Stop Test Now |
| Number of Threads (users) | 1 |
| Ramp-up period (seconds) | 1 |
| Loop Count | 1 (Infinite unchecked) |
| Same user on each iteration | checked |
| Delay Thread creation until needed | unchecked |
| Specify Thread lifetime | unchecked |

**HTTP Request** (under Test Plan → Thread Group → HTTP Request → View Results Tree)

| Field | Value |
|---|---|
| Name | HTTP Request |
| Protocol | http |
| Server Name or IP | 127.0.0.1 |
| Port Number | 5000 |
| Method | GET |
| Path | sort |
| Parameter: unsorted_list | [3,4,5,3,2,3,445,5,5,44,4] |
| Content-Type | text/plain |

---

## JMeter Test Plan

The View Results Tree shows the HTTP Request's response body:

```
[2, 3, 3, 3, 4, 4, 5, 5, 5, 44, 445]
```

- This shows that the JMeter test and the Flask app are both working.
- After this we can start the cmd mode of the testing.

```
jmeter -n -t lab03.jmx -l test-results.csv -e -o report
```

---

## JMeter Properties

**Thread Properties (initial):**

| Number of Threads (users) | Ramp-up period (seconds) | Loop Count |
|---|---|---|
| 1 | 1 | 1 |

- Number of threads would be the number of users to the site.
- The ramp up would be the time it takes for the number of users to come to the site.

**Thread Properties (scaled up):**

| Number of Threads (users) | Ramp-up period (seconds) | Loop Count |
|---|---|---|
| 500 | 500 | 1 |

- This would mean that on average one user would come per second.

---

## A More Complex Test Plan

**Constant Timer** (Test Plan → Thread Group → HTTP Request → Constant Timer → HTTP Request → View Results Tree)

| Field | Value |
|---|---|
| Name | Constant Timer |
| Thread Delay (in milliseconds) | 3000 |

- Constant Timer added in between two HTTP requests. **Use this for a fixed think time.**

**Gaussian Random Timer** (Test Plan → Thread Group → HTTP Request → Gaussian Random Timer → HTTP Request → View Results Tree)

| Field | Value |
|---|---|
| Name | Gaussian Random Timer |
| Deviation (in milliseconds) | 10000 |
| Constant Delay Offset (in milliseconds) | 10000 |

- Gaussian Random Timer added in between two HTTP requests. **Use this for think time that varies randomly around an average.**

---

## What Do the Timers Mean?

Each user (U1–U5) fires two requests, T1 and T2, staggered one second apart across users — the ramp-up spreading five users' first requests across five seconds, with each user's second request (T2) following after its think-time delay:

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| **U1** | T1 | | | T2 | | | | |
| **U2** | | T1 | | | T2 | | | |
| **U3** | | | T1 | | | T2 | | |
| **U4** | | | | T1 | | | T2 | |
| **U5** | | | | | T1 | | | T2 |

This is confirmed against the View Results Tree: eight sequential HTTP Request results are shown (one per T1/T2 firing across the five threads), each with fields such as Thread Name, Sample Start, Load time, Connect Time, Latency, Size in bytes, Sample Count, Error Count, Response code (200), and Response message (OK). Sample response body across the run:

```
[2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,
4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,44,44,44,44,44,44,44,44,
445,445,445,445,445,445,445,445]
```

---

## What is Our Objective?

We want to be able to replicate the load that there are n number of users at the same time on the server.

Assume that each user comes once per second and spends 5 seconds on the server.

**If each user comes once per second:**

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **U1** | T1 | T1 | T1 | T1 | T1 | | | | | | | | | | | | | | | | | | | |
| **U2** | | T2 | T2 | T2 | T2 | T2 | | | | | | | | | | | | | | | | | | |
| **U3** | | | T3 | T3 | T3 | T3 | T3 | | | | | | | | | | | | | | | | | |
| **U4** | | | | T4 | T4 | T4 | T4 | T4 | | | | | | | | | | | | | | | | |
| **U5** | | | | | T5 | T5 | T5 | T5 | T5 | | | | | | | | | | | | | | | |

This is the maximum number of users (5 concurrent, since each user's 5-second session overlaps the next user's arrival).

**If each user comes once every two seconds**, the same 5-second-session shape repeats, but user arrivals are now spaced twice as far apart, roughly halving the peak overlap.

---

## Add a Sleep into the Route

```python
@app.route("/sort", methods=['GET'])
@flask_profiler.profile()
def sort():
    if request.method == "GET":
        unsorted = (request.args.get("unsorted_list"))
        unsorted = unsorted.replace('[', '')
        unsorted = unsorted.replace(']', '')

        time.sleep(5)

        unsorted = list(unsorted.split(","))
        unsorted = [int(i) for i in unsorted]
        unsorted.sort()
        return (json.dumps(unsorted))

app.run()
```

- Adds a 5 seconds to the sort function.
- So if 5 users come in 5 seconds, the max number of users will be 5.
- If 30 users come in 5 seconds, the max number of users will be 30.
- If 30 users come in 30 seconds, the max number of users will be 5.

So to calculate the number of concurrent users, you can use the following formula:

**Number of users / Time × Average session time**

Time is the window in which the users arrive (the ramp-up period). This is Little's Law: L = λ × W.

---

## 30 Users in 5 Seconds

Users are batched into groups of 6, each group starting on a successive second, all sharing the same 5-second session:

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| **U1 to U6** | T1 | T1 | T1 | T1 | T1 | | | | |
| **U7 to U12** | | T2 | T2 | T2 | T2 | T2 | | | |
| **U13 to U18** | | | T3 | T3 | T3 | T3 | T3 | | |
| **U19 to U24** | | | | T4 | T4 | T4 | T4 | T4 | |
| **U25 to U30** | | | | | T5 | T5 | T5 | T5 | T5 |

30 users here (peak overlap across all five groups mid-window).

---

## What Parameters to Use?

- Assume we want the number of concurrent users to be 100.
- The average session time we know is 5 seconds.
- Assume we are expecting a maximum of 200 users.
- The time will be 200 × 5 / 100

**Number of users / Time × Average session time**

---

## Report Folder

**Test and Report information**

| Field | Value |
|---|---|
| Source file | "test-results.csv" |
| Start Time | "10/21/24 3:31 AM" |
| End Time | "10/21/24 3:31 AM" |
| Filter for display | "" |

**APDEX (Application Performance Index)**

| Apdex | T (Toleration threshold) | F (Frustration threshold) | Label |
|---|---|---|---|
| 0.000 | 500 ms | 1 sec 500 ms | Total |
| 0.000 | 500 ms | 1 sec 500 ms | HTTP Request |

**Requests Summary:** PASS 98.5%, FAIL 1.5%

**Active Threads Over Time:** peaks at about 76 active threads around elapsed time 21:03:31 (granularity: 1 min).

- Apdex is 0.000 here because the 5-second sleep pushes every request past the 500 ms toleration threshold.

---

## Let's Extend the Time the Function Spends

- Assume we want the number of concurrent users to be 100.
- The average session time we know is 240 seconds.
- Assume we are expecting a maximum of 200 users.
- The time will be 200 × 240 / 100

---

## Example 1

Assume you have the following parameters:

- 100 users come in within 5 seconds.
- The average session time is 10 seconds.

**Number of users / Time × Average session time**

**Solution:**

- Number of concurrent users = 100 / 5 × 10 = 200
- The number must be capped by the total number of users, hence the number of concurrent users = 100.

---

## Example 2

Assume you have the following parameters:

- 100 users come in within 5 seconds.
- They spend 150 seconds actively browsing on the first url.
- There is on average a 50 seconds delay after the last active browsing to them clicking on the second url.
- They spend 300 seconds actively browsing on the second url.
- They leave the site.

**Number of users / Time × Average session time**

**Solution:**

- The time they spend on the site on average is 150 + 50 + 300 = 500.
- The estimated number of concurrent users = 100 / 5 × 500 = 10,000.
- The number must be capped by the total number of users, hence the number of concurrent users = 100.

---

## Example 3

Assume you have the following parameters:

- The arrival rate is 20 users per second.
- They spend 150 seconds actively browsing on the first url.
- There is on average a 50 seconds delay after the last active browsing to them clicking on the second url.
- They spend 300 seconds actively browsing on the second url.
- They leave the site.

**Number of users / Time × Average session time**

**Solution:**

- The time they spend on the site on average is 150 + 50 + 300 = 500.
- The estimated number of concurrent users = 20 × 500 = 10,000.
- There is no cap here because no maximum number of users is given.

---
*SIT Internal — ICT3113 Performance Optimisation and Design, Singapore Institute of Technology*
