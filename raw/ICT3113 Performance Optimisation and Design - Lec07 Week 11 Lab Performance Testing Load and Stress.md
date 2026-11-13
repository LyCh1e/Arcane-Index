# Week 11 Lab (Lecture 07): Performance Testing. Load and Stress

In this lab you run two of the lecture's tests, a load test and a stress test, against a build of the order API you have not seen before (Build C). You read the results the way the lecture did and work out what each test can and cannot tell you.

The point of the lab is not the service. It is knowing which test answers which question, and reading the table by column.

## Learning outcomes

By the end of this lab you should be able to:

1.  Run a load test and a stress test with pyload.py and read the one-row result from analyse.py.

2.  Decide pass or fail against a written requirement, not against a chart.

3.  Read a stress table by column: knee, ceiling, failure mode, and which resource is the ceiling.

## 0. Environment and software requirements

Everything runs on your own laptop. Nothing else should be running during a test.

**Software.** Python 3.10 or later, then pip install flask requests psutil pandas matplotlib.

**Files.** Download lab07.zip and unzip it to a plain local folder such as C:\lab07. **Not** under OneDrive, Google Drive, Dropbox or a synced Desktop or Documents folder. The service reads a file on every request, and a sync client sitting in that path slows it down enough to change every result in this lab. The layout is the lecture's:

```
lab07/
  service/app.py            Build C of the order API
  service/catalogue.json
  data/orders.csv
  scripts/single_request.py
  scripts/monitor.py
  scripts/pyload.py         the load generator
  scripts/analyse.py        turns .jtl files into the results table
  results/                  empty. Your files go here
```

**Three Command Prompt windows.** Open them now and keep them open for the whole lab. Every command in this sheet says which window it goes in.

| Window       | What runs in it                                                             | Working folder   |
|--------------|-----------------------------------------------------------------------------|------------------|
| **Window A** | the service, app.py. Started once per section, left running                 | C:\lab07\service |
| **Window B** | the monitor, monitor.py. Started before each test, stopped after            | C:\lab07\scripts |
| **Window C** | everything else: single_request.py, pyload.py, analyse.py, counting the log | C:\lab07\scripts |

**Mac or Linux.** Use export instead of set, rm instead of del, grep -c instead of find /c. On a Mac, port 5000 may be taken by AirPlay Receiver; turn it off in System Settings.

**Why** pyload.py **and not JMeter.** The lecture named JMeter as the module's tool and then ran every demo with pyload.py. Same here. pyload.py is about 60 lines, you can read all of it, and it does one thing: open-loop arrivals at a fixed rate, with the same body checks as the JMeter plans, written to a JMeter-format .jtl. JMeter does the same job in its Open Model Thread Group and the results files are interchangeable.

## 1. Start the service

The service is the order API from the lecture: a small Flask app that accepts POST /orders, checks the customer's token, checks the items against the catalogue, and stores the order in a dictionary in memory.

The token check is the function verify() in app.py. Every order carries a customer_id and a token, like a password. verify() hashes the token with PBKDF2 (100,000 rounds of SHA-256) and compares the result with the hash stored for that customer when the service started. The 100,000 rounds are deliberate, to make a stolen hash slow to crack, and they are also why this one function is almost all of the service time S. The lecture ran it as Build A. The version in your folder is Build C: the same app with one change made to app.py after the lecture. You are not told what the change is. Do not open app.py until section 4.

**Window A** (service):

```
cd C:\lab07\service
del orders.log
set ORDERS_BUILD=C
python app.py
```

Leave it running. Open http://127.0.0.1:5000/health in a browser. It should report "build": "C" and "orders_in_memory": 0.

**Window C** (commands):

```
cd C:\lab07\scripts
echo %NUMBER_OF_PROCESSORS%
python single_request.py --n 20
```

Fill in:

|                                                                     | Your value |
|---------------------------------------------------------------------|------------|
| Core count, c                                                       |            |
| Service time S (mean, in ms; divide by 1000 before using it in c/S) |            |
| Laptop and operating system                                         |            |

**Window B** (monitor):

```
cd C:\lab07\scripts
python monitor.py --out ../results/demo1-r1-mem.csv --interval 10
```

Leave it running until the load test is finished.

**Remark.** The file names in this lab (demo1-r1, demo2-r1) match what analyse.py expects, so you can use the lecture's script as it is. demo1 is the load test and demo2 is the stress test, same as the lecture.

## 2. Load test

The requirement you are testing against, in the lecture's format:

| Field                  | LAB-01                                                                                                                                                                                           |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1\. Requirement number | LAB-01                                                                                                                                                                                           |
| 2\. Title              | Order creation response time                                                                                                                                                                     |
| 3\. Statement          | 95% of POST /orders requests shall complete within 200 milliseconds, measured at the load generator, when the service is offered 5 requests per second (open loop) for 3 minutes on your laptop. |
| 8\. Assumptions        | Build C at 100,000 iterations. Store empty at the start. Nothing else running. Generator and service on the same machine.                                                                        |
| 9\. Measurement        | pyload.py open, first 20 seconds dropped as warm-up (analyse.py does this). monitor.py every 10 seconds. One run.                                                                                |

**Window C** (commands):

```
python pyload.py open --rate 5 --minutes 3 --out ../results/demo1-r1.jtl
```

Wait for it to finish (3 minutes). Then **Window B**: stop the monitor with Ctrl+C. Then **Window C**:

```
python analyse.py --results ../results
```

Copy the Load row from results_table.csv into this table:

| offered | samples | p50 | p95 | p99 | err_pct | throughput | cpu_pct |
|---------|---------|-----|-----|-----|---------|------------|---------|
|         |         |     |     |     |         |            |         |

Then, still in **Window C**, check that the generator and the server agree on how many requests there were. Two commands, two counts. Do this **before** you restart the service in section 3, because section 3 deletes the log.

```
find /c "POST /orders" ..\results\demo1-r1.jtl
find /c "order=" ..\service\orders.log
```

**What the two counts are.** The first is the generator's view: one line per request pyload.py sent during the 3 minutes. The second is the server's view: one line per order app.py stored. They come from two different programs on two sides of the connection.

**Why the log is bigger by 21.** Before the load test, single_request.py sent 1 order to check the body and then 20 more to measure S. Those 21 are in the server log but not in the .jtl. So the check is: .jtl count + 21 = log count.

**Why** samples **in the table is smaller than both.** analyse.py throws away the first 20 seconds of the run before working out p50, p95 and throughput, so start-up noise does not pull the numbers around. samples is what is left after that. It is not supposed to match the counts above.

**Why the match matters.** If the two counts agree, every request the generator timed was served and stored, so the p95 and throughput in the table are about this service and nothing else. If the log is short, some requests never became orders (timed out, failed, hit a stale server from an earlier run). If the log is long, something else was sending requests, or an old log was not deleted. Lecture Demo 6 is the case this protects against: the generator reported 100% success while the server had logged nothing but errors.

Fill in:

|                                                                                        | Your value |
|----------------------------------------------------------------------------------------|------------|
| Requests in demo1-r1.jtl                                                               |            |
| Requests in .jtl + 21                                                                  |            |
| Lines in orders.log                                                                    |            |
| Do they match?                                                                         |            |
| LAB-01: pass or fail? (decide against the statement in field 3, not against the chart) |            |

**Remark.** A load test tells you whether the system meets its target at one load. It tells you nothing about any other load, and if it fails it does not tell you why. Write down the result as it is and move on.

## 3. Stress test

**Window A** (service): stop app.py with Ctrl+C, then start it again from an empty store:

```
del orders.log
set ORDERS_BUILD=C
python app.py
```

**Window B** (monitor):

```
python monitor.py --out ../results/demo2-r1-mem.csv --interval 10
```

**Window C** (commands):

```
python pyload.py open --rate 5,10,15,20,25,30,40 --minutes 1 --timeout 20 --out ../results/demo2-r1.jtl
```

Seven steps of one minute each. Do not touch the laptop for 7 minutes. Then **Window B**: stop the monitor with Ctrl+C. Then **Window C**:

```
python analyse.py --results ../results --step 60 --rates 5,10,15,20,25,30,40
```

This prints one row per step. Copy the rows here:

| offered | p95 | p50 | thr | err | cpu_pct |
|---------|-----|-----|-----|-----|---------|
| 5       |     |     |     |     |         |
| 10      |     |     |     |     |         |
| 15      |     |     |     |     |         |
| 20      |     |     |     |     |         |
| 25      |     |     |     |     |         |
| 30      |     |     |     |     |         |
| 40      |     |     |     |     |         |

Read the table by column, as in the lecture:

- **p95 column:** the knee is the first step where p95 stops being flat and climbs.

- **thr column:** the ceiling is the throughput that stops rising however much more is offered.

- **err column:** the failure mode. When do errors start, and are they timeouts or refusals?

- **cpu_pct column:** what the machine is doing at each step.

Fill in:

|                                               | Your reading | Which row shows it |
|-----------------------------------------------|--------------|--------------------|
| Knee (offered rate where p95 starts climbing) |              |                    |
| Ceiling (highest throughput reached)          |              |                    |
| Failure mode (timeouts, refusals, both)       |              |                    |
| cpu_pct at the ceiling                        |              |                    |

**Remark.** cpu_pct is whole-machine. On a laptop with c cores, one fully busy core reads about 100/c percent. So a low cpu_pct does not always mean the service has room to spare. It can also mean the service is only using one core.

## 4. What the numbers say

Answer these from your tables before you open any code.

1.  From section 1 you have S and c. If every core could work on a request at the same time, the ceiling would be about c/S requests per second. What is that number for your laptop? What ceiling did the stress test measure?

2.  What did cpu_pct read at the ceiling? What would it read if all c cores were busy?

3.  Put the two answers together. How many requests is the service working on at the same time?

|                                                                                               | Your answer |
|-----------------------------------------------------------------------------------------------|-------------|
| c/S, with S in seconds (requests per second the laptop could serve if every processor worked) |             |
| Ceiling measured in section 3 (highest value in the thr column)                               |             |
| cpu_pct at the ceiling (same row as the ceiling)                                              |             |
| cpu_pct if every processor were busy (whole-machine figure)                                   |             |
| Requests in service at the same time: ceiling × S in seconds (Little's Law)                   |             |

**How to find the reason.** Work from the numbers to the code, in this order.

1.  Name the shape. Throughput stops near 1/S and cpu_pct stays near idle. The service handles one request at a time while the other processors sit idle. Something is making requests wait for one another.

2.  List what can do that in a threaded Flask app. There are only a few: a lock held while the slow work runs; a single worker; one shared connection to something; pure-Python CPU work under the interpreter lock. This service has no database, and the lecture said the slow step is the PBKDF2 hash and that hashlib releases the interpreter lock. That leaves a lock or a single worker.

3.  Open service/app.py and read create_order. Find the slow step, the verify() call. Then look at what encloses it. Ask: does anything make the threads take turns here? Read any comment that explains why, and ask whether the reason given is true.

4.  Change one thing. The lock should cover only the part that really must not run in two threads at once (writing to the store). Nothing else.

**Then prove it, twice.** First repeat section 3 exactly with the new build (r2), so that r1 and r2 differ in nothing but the code. Then run once more with higher steps (r3) to find where the new ceiling actually is.

**Run r2: same steps as section 3.**

**Window A** (service): stop app.py with Ctrl+C, then start the fixed build from an empty store:

```
del orders.log
set ORDERS_BUILD=C
python app.py
```

**Window B** (monitor):

```
python monitor.py --out ../results/demo2-r2-mem.csv --interval 10
```

**Window C** (commands):

```
python pyload.py open --rate 5,10,15,20,25,30,40 --minutes 1 --timeout 20 --out ../results/demo2-r2.jtl
```

Then **Window B**: Ctrl+C. **Window C**: python analyse.py --results ../results --step 60 --rates 5,10,15,20,25,30,40. analyse.py reports the highest run number it finds, so this shows r2. To see r1 again, copy its two files into a folder of their own and point analyse.py there:

```
mkdir ..\results\r1
copy ..\results\demo2-r1.jtl ..\results\r1\
copy ..\results\demo2-r1-mem.csv ..\results\r1\
python analyse.py --results ../results/r1 --step 60 --rates 5,10,15,20,25,30,40
```

Put r1 and r2 side by side:

| offered | p95 (r1) | p95 (r2) | thr (r1) | thr (r2) | err (r1) | err (r2) | cpu_pct (r1) | cpu_pct (r2) |
|---------|----------|----------|----------|----------|----------|----------|--------------|--------------|
| 5       |          |          |          |          |          |          |              |              |
| 10      |          |          |          |          |          |          |              |              |
| 15      |          |          |          |          |          |          |              |              |
| 20      |          |          |          |          |          |          |              |              |
| 25      |          |          |          |          |          |          |              |              |
| 30      |          |          |          |          |          |          |              |              |
| 40      |          |          |          |          |          |          |              |              |

**Run r3: higher steps.** If the fix worked, r2 never reached the knee: throughput followed offered all the way to 40. A stress test that never reaches the knee has not found the limit, only a lower bound. So go higher.

**Window A**: restart from an empty store as above. **Window B**:

```
python monitor.py --out ../results/demo2-r3-mem.csv --interval 10
```

**Window C**:

```
python pyload.py open --rate 10,20,40,80,120,160,200 --minutes 1 --timeout 20 --out ../results/demo2-r3.jtl
```

Seven minutes. Then **Window B**: Ctrl+C. **Window C**:

```
python analyse.py --results ../results --step 60 --rates 10,20,40,80,120,160,200
```

| offered | p95 | p50 | thr | err | cpu_pct |
|---------|-----|-----|-----|-----|---------|
| 10      |     |     |     |     |         |
| 20      |     |     |     |     |         |
| 40      |     |     |     |     |         |
| 80      |     |     |     |     |         |
| 120     |     |     |     |     |         |
| 160     |     |     |     |     |         |
| 200     |     |     |     |     |         |

Fill in:

|                            | Build C (r1) | After your fix (r3) |
|----------------------------|--------------|---------------------|
| Ceiling (highest thr)      |              |                     |
| cpu_pct at the ceiling     |              |                     |
| Where errors start         |              |                     |
| What you changed in app.py |              |                     |

**Remark.** In this lab the service had every core on your laptop available to it. If it still behaved like one core, something in the code made it so. That is the kind of fault a load test cannot name and a stress test can. And if your r3 ceiling is still far below c/S, something else is in the way; the generator sharing the machine is the first suspect, and the sheet's instruction to work outside OneDrive is the second.
