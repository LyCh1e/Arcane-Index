---
type: concept
title: "Python Profiling — Time, Memory, and CPU"
domain: performance-engineering
course: ICT3113
complexity: medium
tags: [profiling, cprofile, py-spy, timeit, memory-profiler, tracemalloc, psutil, deterministic-profiling, statistical-profiling, flame-graph, ict3113]
updated: 2026-09-08
status: established
created: 2026-09-08
---

# Python Profiling — Time, Memory, and CPU

The **Measure** step of [[concepts/performance-engineering|Measure → Model → Optimise → Deploy]], done at the level of a single Python program. Profiling answers *where* a program spends its time or memory, so optimisation effort lands on the part that actually matters rather than on a guess.

> Profile before you optimise. The bottleneck is almost never where intuition puts it, and a 2× speed-up of code that runs 1% of the time is invisible.

---

## 1. Deterministic vs statistical profiling

| | **Deterministic** (tracing) | **Statistical** (sampling) |
|---|---|---|
| Mechanism | Instruments *every* call, return, and exception; times each event | Interrupts the process N times/second and records the current call stack |
| Overhead | High — 2–10× slowdown; distorts the very thing measured | Low — a few % or less; safe on production |
| Data | Exact call counts and per-function timings | Statistical estimate — a function's sample share ≈ its time share |
| Blind spots | None within Python; C internals opaque | Anything between two samples; rare paths under-counted |
| Python tools | `cProfile`, `profile`, `timeit` | `py-spy`, `pyinstrument`, `perf` |
| Use when | You need call counts / a precise call graph, offline | The program is long-running, in production, or you can't change/restart it |

*(Source framing: Python docs, "Deterministic Profiling".)*

The overhead is real and measurable. A call-heavy toy script that runs in **1.8 s** unprofiled takes **9.6 s** under `cProfile` (~5×) and **37 s** for a longer variant; the same longer script under `py-spy` at 100 Hz shows no perceptible slowdown.

---

## 2. Timing code

### `time.perf_counter()` — one measurement

High-resolution monotonic clock. Read it, run the code, read it again, subtract. Fine for coarse "does this take 10 ms or 10 s?" checks; too noisy for short snippets (scheduler, cache state, GC all leak in).

```python
from time import perf_counter
start = perf_counter(); work(); print(perf_counter() - start)
```

### `timeit` — many measurements, done right

Runs a statement `number` times and returns the **total** seconds. Two traps:

1. **`setup` runs only once.** For code that mutates its input (an in-place sort), runs 2…N operate on already-processed data and understate the cost. Fix: `timeit.repeat(stmt, setup, repeat=k, number=1)` → a list of single-run timings, each with fresh setup.
2. **Report the minimum, not the mean.** The min is the run least disturbed by background activity; the mean is inflated by noise and is not more "representative".

```python
from timeit import repeat
t = repeat("insertion_sort(a)", setup="a = fresh_array()", globals=globals(),
           repeat=10, number=1)
print(min(t))
```

Timing two algorithms on a growing input surfaces their complexity classes directly — insertion sort (O(n²)) vs merge sort (O(n log n)) diverge from ~7× at n=500 to ~50× at n=4000.

### `cProfile` — where the time goes

Deterministic, standard library. Run over a whole script or a single call:

```python
python -m cProfile -s tottime script.py      # CLI, sorted by self-time
```
```python
import cProfile; cProfile.run("f(30)")        # API — better for recursion
cProfile.run("f(30)", "out.pstats")           # dump for later analysis
```

Column meanings:

| Column | Meaning |
|---|---|
| **ncalls** | number of calls (`36/1` = 36 total, 1 primitive/non-recursive) |
| **tottime** | time in this function **only**, excluding sub-calls — *this is where to optimise* |
| **percall** | tottime / ncalls |
| **cumtime** | time in this function **and everything it calls**, invocation to return |
| **percall** | cumtime / primitive calls |
| **filename:lineno(function)** | location |

Sort by `tottime` to find hot spots (leaf work); sort by `cumtime` to find expensive call trees.

### Visualising a profile

- **`gprof2dot`** converts a `.pstats` dump to a Graphviz `.dot` call graph; `dot -Tpng` renders it. `dot` (Graphviz) is a separate native binary — present on Colab via `apt-get install graphviz`, **not installed by default on Windows** (`winget install Graphviz.Graphviz`).
- **`snakeviz`** — interactive icicle chart in the browser from a `.pstats` file.
- **Fallback with no Graphviz:** read the dump back with the stdlib `pstats` module and bar-chart the top functions by cumtime/tottime with matplotlib.

---

## 3. Sampling profilers — `py-spy`

Written in Rust; profiles a Python process **from the outside** — no import, no code change, can attach to an already-running PID (`py-spy top --pid 1234`).

```python
py-spy record --rate 100 --format flamegraph -o flame.svg -- python script.py
py-spy top -- python script.py        # live, top-style view (terminal only)
py-spy dump --pid 1234                 # one-shot stack dump of a hung process
```

`--rate` = samples per second; higher = finer detail, more overhead. Needs `sudo` on macOS / some Linux; not on Windows or Colab.

**Flame graph** (Brendan Gregg): each box is a stack frame; **y-axis = stack depth** (root at top or bottom); **x-axis = share of samples**, sorted alphabetically **not by time**; box **width = fraction of time that frame was on the stack**. Wide boxes are where the program lives. Colours are cosmetic.

Reconstructing `py-spy top`'s ranking from collapsed-stack (`--format raw`) output: attribute each sample to its **leaf** frame, count per function, divide by total — self-time percentages.

---

## 4. Profiling memory

### `memory_profiler` — per-line RSS

Decorate a function with `@profile`, run `python -m memory_profiler script.py`, get a table: `Mem usage | Increment | Occurrences | Line Contents`. **Increment** is what that line added. IPython: `%load_ext memory_profiler`, then `%memit expr` (peak of an expression) and `%mprun -f func`.

Limitations: samples process RSS (coarse, includes the interpreter — ~64–125 MiB baseline); recursive functions produce an unreadable pile of repeated tables (run several times, average); needs source decoration.

### `tracemalloc` — where Python allocated

Standard library. Traces **Python-level** allocations and remembers the allocation site (file:line, with traceback).

```python
import tracemalloc
tracemalloc.start()
before = tracemalloc.take_snapshot()
work()
after = tracemalloc.take_snapshot()
for stat in after.compare_to(before, "lineno")[:5]:   # net allocations
    print(stat)
current, peak = tracemalloc.get_traced_memory()        # simple pair, no snapshots
```

Filter out noise (`tracemalloc.Filter(False, "<frozen *>")`, the tracemalloc module itself) to see *your* sites. `get_traced_memory()`'s **peak** is the best single number for transient cost: an in-place sort peaks at <1 KiB of Python allocations; a merge sort that copies sub-arrays peaks two orders of magnitude higher on the same input.

### Choosing

| Question | Tool |
|---|---|
| Which **line** grows memory? | `memory_profiler` |
| Which **allocation site** and how much is **still live**? | `tracemalloc` |
| Whole-process RSS over time / another language in the mix | `psutil`, OS tools |

---

## 5. System & CPU inventory — `psutil`

Record the environment *before* profiling — a number is meaningless without the machine that produced it.

```python
import psutil, platform
platform.platform(); platform.python_version()
psutil.cpu_count(logical=True), psutil.cpu_count(logical=False)
psutil.cpu_freq()             # current / max MHz
psutil.virtual_memory()       # total / available / used / percent
psutil.cpu_percent(interval=1, percpu=True)
psutil.Process().memory_info().rss
```

Cross-platform replacement for `cat /proc/cpuinfo` / `cat /proc/meminfo`.

---

## 6. Method

1. **Record the environment** (CPU, RAM, Python version, OS).
2. **Fix the inputs** — seed the RNG so every run and every profile see identical data.
3. **Measure a baseline** unprofiled, so you know profiler overhead and have a target.
4. **Deterministic pass** (`cProfile`) for call counts and exact hot spots; **sampling pass** (`py-spy`) if the program is long-running or can't be instrumented.
5. **Optimise the hot spot** — highest `tottime`, or the widest flame-graph box — then **re-measure**.
6. Repeat until the profile is flat or the target is met.

**Worked case — memoisation.** Naive recursive `fib(30)` makes **2,692,537** calls (exponential, O(φⁿ)); the profile shows one function at 100% `tottime` and a colossal `ncalls`. Adding a cache collapses `fib(34)` to **35** calls (linear, O(n)) — the profile *is* the before/after evidence. This is [[concepts/algorithm-complexity]] made visible.

---

## Connections

- [[concepts/performance-engineering]] — profiling is the program-level **Measure** step
- [[concepts/performance-metrics]] — response time R = W + S; a profile decomposes S; percentiles need many runs
- [[concepts/algorithm-complexity]] — timing across input sizes reveals the complexity class; profiles show which term dominates
- [[concepts/sorting-and-searching]] — insertion / merge / quick sort are the lab's specimens (time *and* memory trade-offs)
- [[concepts/workload-identification]] — profiling gives the **service demand** per transaction that workload models multiply by arrival rate
- [[examples/ict3113-lab1-profiling]] — the ICT3113 Week 2 lab that exercises every tool above
