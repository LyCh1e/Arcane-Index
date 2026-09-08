---
type: example
status: established
created: 2026-09-08
updated: 2026-09-08
name: ict3113-lab1-profiling
description: ICT3113 Week 2 lab — an Introduction to Profiling notebook completed and executed locally, exercising time.perf_counter / timeit / cProfile / gprof2dot / py-spy / memory_profiler / tracemalloc / psutil on insertion, merge and quick sort plus recursive Fibonacci
metadata:
  type: example
domain: performance-engineering
course: ICT3113
tags: [profiling, cprofile, py-spy, timeit, memory-profiler, tracemalloc, psutil, flame-graph, jupyter, lab]
---

# ICT3113 Lab 1 (Week 2) — Introduction to Profiling

**Lab file:** `Labs/Lab1/ICT3113_Week02_Introduction_to_Profiling_Student_clean.ipynb`
**Concept:** [[concepts/python-profiling]]
**Stack:** Jupyter notebook, Python 3.14, Windows 11 (lab is written for Google Colab / Linux — adapted to run locally)

The notebook is a guided tour of Python profiling tools. It shipped as a student skeleton — narrative markdown with empty code cells. Completing it meant filling every code cell so the notebook runs top to bottom, then executing it with `jupyter nbconvert --execute`.

---

## Learning objectives (from the notebook)

1. Use Google Colab (adapted: local Jupyter).
2. Deterministic vs statistical profilers.
3. Profile **running time**.
4. Profile **memory consumption**.
5. Profile **CPU / system** resources.

---

## What each section does

| § | Tool | Cell work |
|---|---|---|
| 2.1 | `psutil` | `cpu_count()`, `cpu_freq()`, `virtual_memory()`, `platform.*` — record the machine before measuring |
| 2.3.1 | `time.perf_counter` | single-shot timing of `insertion_sort(5000)` |
| 2.3.2 | `timeit` | `repeat(..., number=1)` with fresh `setup` per run; report `min`; compare insertion vs merge across n = 500…4000 |
| 2.3.3 | `cProfile` | CLI (`-s tottime`) and API (`cProfile.run`); `%%writefile` the target script; explain ncalls/tottime/cumtime |
| — | `gprof2dot` | `.pstats` → `.dot` call graph; PNG render needs Graphviz; matplotlib bar chart from `pstats` as the no-Graphviz fallback |
| — | recursive `fib` | naive vs memoised — profile shows the call-count collapse |
| 2.3.4 | `py-spy` | `record --format flamegraph`; reconstruct `py-spy top` from `--format raw`; compare to `cProfile` |
| 2.4.1 | `memory_profiler` | `@profile` + `python -m memory_profiler`; `%memit` |
| 2.4.2 | `tracemalloc` | snapshot diff + `get_traced_memory()` peak; quick sort added as a third specimen |

---

## Key results from the local run (Ryzen, 16 logical CPUs, Python 3.14)

**Complexity is visible in the timings.** insertion vs merge sort:

| n | insertion | merge | ratio |
|---|---|---|---|
| 500 | 0.0066 s | 0.0010 s | ×6.7 |
| 1000 | 0.0276 s | 0.0022 s | ×12.6 |
| 2000 | 0.137 s | 0.0055 s | ×24.7 |
| 4000 | 0.510 s | 0.0101 s | ×50.4 |

The ratio itself grows ~linearly with n — the signature of O(n²) vs O(n log n).

**Deterministic profiling overhead.** The call-heavy `multiple_calls.py` (32,000,000 calls to an empty `func_e`): **1.83 s** unprofiled → **9.56 s** under `cProfile` (~5.2×). `tottime` split: `func_b` 3.5 s, `func_c` 3.2 s, `func_e` 2.8 s.

**Sampling overhead is negligible.** `long_multiple_calls.py`: **37.2 s** under `cProfile`; no perceptible slowdown under `py-spy` at 100 Hz (~720 samples). py-spy leaf attribution: `func_b` 49%, `func_c` 32%, `func_e` 18% — matches the flame-graph widths.

**Memoisation, measured.** Naive `fib(30)` = **2,692,537** recursive calls (24 primitive); the profile is one function at 100% tottime. Memoised `fib(34)` = **35** calls — exponential → linear, straight from the profiler.

**Memory: in-place vs copying.** `tracemalloc` peak on the same 2000-element input — `insertion_sort` **0.8 KiB**, `quick_sort` **1.7 KiB**, `merge_sort` **19.5 KiB** (it slices `left_copy`/`right_copy` at every level). `memory_profiler` on `insertion_sort` shows Increment ≈ 0 on every line (it allocates nothing); on the recursive `merge_sort` it prints an unreadable stack of repeated per-call tables — the lab's point about recursion + line profilers.

---

## Adaptations for local / Windows execution

- **Graphviz `dot` is not on Windows by default.** `gprof2dot` still emits `output.dot`; the cell renders the PNG only `if shutil.which("dot")`, else prints a note and a matplotlib bar chart of the top functions by cumtime/tottime stands in.
- **`/proc/cpuinfo` and `/proc/meminfo`** → `psutil` + `platform` (cross-platform).
- **`py-spy top`** is an interactive terminal UI that can't render in a notebook → captured with `--format raw` and re-aggregated to self-time percentages in Python.
- **`timeit` `setup`-once trap** — `timeit(number=n)` runs `setup` once, so an in-place sort would process already-sorted data on runs 2…n. Fixed by calling `timeit(..., number=1)` in a 10-iteration list comprehension (`timeit.repeat` does the same thing) so `setup` re-randomises before every measurement; report `min`.
- Tools installed into the user site: `memory_profiler`, `py-spy`, `gprof2dot`, `snakeviz`, `jupyter`, `nbconvert`.

---

## Handout bug noted (comment left in the cell)

The provided memoised `fib` has, in the "compute fib(n-2)" branch:

```python
return_2 = fib(fib_dict, n-1)      # should be n-2
```

It still returns the correct final number only because the `n-1` branch above has already populated `fib_dict[n-2]` on the way down, so the mislabelled recursive call hits the cache. Flagged with a `# NOTE` in the notebook rather than silently rewritten.

---

## Connections

- [[concepts/python-profiling]] — the concept page this lab instantiates
- [[concepts/performance-engineering]] — Measure step
- [[concepts/sorting-and-searching]] · [[concepts/algorithm-complexity]] — the specimens and what the numbers mean
- [[examples/ict3112-lab1-nunit-tdd-calculator]] — sibling Y3 lab (ICT3112), same "complete the skeleton + verify" shape
