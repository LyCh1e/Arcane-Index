---
type: example
status: established
created: 2026-09-15
updated: 2026-09-15
name: ict3113-lab2-jmeter-testing
description: ICT3113 Week 3 lab — Flask profiling with flask-profiler and JMeter load/stress testing, completed and executed locally on Windows; reproduces and root-causes the notebook's "recursive use of cursors" server crash under concurrent load
metadata:
  type: example
domain: performance-engineering
course: ICT3113
tags: [flask, flask-profiler, jmeter, load-testing, virtual-environments, sqlite, threading, jupyter, lab]
---

# ICT3113 Lab 2 (Week 3) — Introduction to Testing

**Lab file:** `Labs/Lab2/ICT3113_Week03_Introduction_to_Testing.ipynb`
**Concept:** [[concepts/performance-engineering]] · [[concepts/performance-metrics]]
**Stack:** Jupyter notebook (Colab-authored, run locally), Python 3.14, Flask 3.1.3, flask-profiler 1.8.1, Apache JMeter 5.6.3, Windows 11

Unlike [[examples/ict3113-lab1-profiling]] (a blank student skeleton), this notebook shipped **fully worked** — every code cell already runs. "Completing" it locally meant: adding logic comments to the pre-filled cells (per standing preference), then actually standing up the parts the notebook only describes narratively (installing flask-profiler, running the Flask server locally, building and executing a JMeter non-GUI test plan against it) so the lab's claims could be verified with real numbers instead of just read.

---

## What the notebook covers

1. **3.1** Profiling/monitoring a Flask server — plain Flask `/sort` endpoint, then the same endpoint wrapped with `flask-profiler` (`@flask_profiler.profile()`, sqlite storage, dashboard at `/flask-profiler`).
2. **3.2** Introduction to JMeter — GUI walkthrough (Thread Group → HTTP Request → View Results Tree) against a public site, then against the Colab-hosted `/sort` endpoint.
3. **3.3** Virtual environments — `python -m venv`, `pip freeze` before/after, motivated by dependency-version conflicts between projects.
4. **3.4** Running and testing the web server **locally** — same Flask+flask-profiler server, JMeter re-pointed at `127.0.0.1:5000`, then JMeter **non-GUI mode** (`jmeter -n -t plan.jmx -l results.csv -e -o report/`) for a real test run (1000s of threads, looking for the "knee" in the response-time-vs-concurrency curve).

---

## Local setup

```
cd Labs/Lab2
python -m venv test_env
test_env\Scripts\activate
pip install flask flask-profiler==1.8.1
```

flask-profiler 1.8.1 (last released 2018, expects an old Flask) installed and ran cleanly against **Flask 3.1.3 / Python 3.14** with no compatibility shims needed — worth knowing since the version pin looked risky on paper.

The 3.4.1 server was extracted from the notebook cell into `Labs/Lab2/local_server/server.py`, with one change: the notebook hardcodes `app.config["flask_profiler"]["storage"]["FILE"] = "/flask_profiler.sql"` (a Colab/Linux VM-root path); on Windows this isn't writable, so it's redirected to a path next to the script.

Verified `/`, `/sort?unsorted_list=[...]`, and `/flask-profiler/api/measurements` all work as documented — flask-profiler correctly captures method, args, headers, and elapsed time per call.

**Gotcha:** testing `/sort` with `curl` from a shell needs `-g` (globoff) or the query string quoted — unescaped `[` `]` in a URL is brace/range-expansion syntax to curl and silently produces an empty request that never reaches the server.

---

## JMeter test plan (non-GUI, section 3.4.3)

Built `Labs/Lab2/local_server/sort-test-plan.jmx` by hand (Thread Group with parametrised `${THREADS}`/`${RAMPUP}`/`${LOOPS}` via `__P()`, one HTTP Request sampler for `GET /sort?unsorted_list=[3,4,5,3,2,3,445,5,5,44,4]`) so the whole test is reproducible from the command line without opening the JMeter GUI:

```
jmeter -n -t sort-test-plan.jmx -Jthreads=50 -Jrampup=5 -Jloops=10 -l results.csv -e -o report-folder
```

---

## Reproduced the notebook's "recursive use of cursors" bug — and found the root cause

The notebook (§3.4.2/3.4.3) warns that pushing enough concurrent JMeter load at the local server "**strangely changes the text colour to purple**" and then crashes with a sqlite "**recursive use of cursors**" error, suggesting the fix is to swap the storage engine from sqlite to MongoDB — without explaining *why* it happens.

**Reproduced exactly.** 50 threads / 5 s ramp-up / 10 loops (500 requests) against the stock `server.py`: **100% error rate**, server dead within ~5 seconds, log showing:

```
sqlite3.ProgrammingError: Recursive use of cursors not allowed.
```

**Root cause, isolated by experiment:**
1. Flask's `app.run()` has **enabled threaded mode by default since Flask 1.0** (undocumented in the lab, easy to miss — `threaded` isn't passed explicitly anywhere in the notebook).
2. flask-profiler's sqlite backend (`storage/sqlite.py`) opens **one shared `sqlite3.Cursor` object for the entire app's lifetime** (`check_same_thread=False` only lifts sqlite's cross-thread guard — it does not make concurrent `.execute()` calls on the *same* cursor object safe).
3. Under JMeter's concurrent load, two request-handling threads really do call `self.cursor.execute()` on that one shared cursor at overlapping instants → sqlite raises "recursive use of cursors" → unhandled exception → dev server dies.

**Confirmed with a control run.** Same server, same JMeter plan, only difference `app.run(..., threaded=False)`: **0% errors**, 500/500 requests succeeded, avg 158 ms, server stayed up for the whole run. This isolates the bug to Flask's threading model + flask-profiler's cursor sharing — not JMeter, not the network stack, not the `/sort` logic.

This also explains *why* the lab's suggested fix (MongoDB storage engine) works: the MongoDB Python driver manages its own per-thread/pooled connections instead of one hand-rolled shared cursor. A cheaper fix for a single dev box, with no extra service to install, is `app.run(threaded=False)` (trades concurrency for correctness) or wrapping the shared cursor's access in a `threading.Lock`.

---

## Connections

- [[concepts/performance-engineering]] — Measure step; load/stress testing as a verification technique
- [[concepts/performance-metrics]] — response time, throughput, error rate under load
- [[examples/ict3113-lab1-profiling]] — the Week 2 profiling lab this one builds on
- [[concepts/docker-compose]] — the natural next step for isolating tester/server load (raised in §3.4 but not required this lab)
