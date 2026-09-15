---
type: learning
status: resolved
created: 2026-09-15
updated: 2026-09-15
name: ict3113-fib-memoisation-off-by-one
description: An off-by-one typo (n-1 instead of n-2) in ICT3113's memoised Fibonacci handout shifts every cached value up by one index; the official solutions notebook ships the same typo and "fixes" it by reading fib_dict[n-1] instead of fib_dict[n] — masking the bug rather than fixing it
metadata:
  type: learning
domain: performance-engineering
course: ICT3113
skill: python-debugging
tags: [memoisation, off-by-one, fibonacci, dynamic-programming, debugging]
---

# ICT3113 memoised-Fibonacci handout: an off-by-one bug present in both the student skeleton and the official solutions

## The bug

`ICT3113_Week02_Introduction_to_Profiling` (both the student skeleton *and* the instructor's own `_solutions.ipynb`) hands out this "top-down memoised Fibonacci" as the fix for the naive recursive version's exponential blow-up:

```python
def fib(fib_dict, n):
  if n in fib_dict: return fib_dict[n]
  if n == 0: return 0
  if n == 1: return 1

  if (n-1) in fib_dict:
    return_1 = fib_dict.get(n-1)
  else:
    return_1 = fib(fib_dict, n-1)
    fib_dict[n-1] = return_1

  if (n-2) in fib_dict:
    return_2 = fib_dict.get(n-2)
  else:
    return_2 = fib(fib_dict, n-1)      # <-- should be n-2
    fib_dict[n-2] = return_2

  fib_dict[n] = fib_dict[n-1] + fib_dict[n-2]
  return fib_dict[n]
```

In the "compute the `n-2` term" branch, the recursive call is `fib(fib_dict, n-1)` — the same argument as the branch immediately above it — instead of `fib(fib_dict, n-2)`.

## Why it doesn't crash, and why the numbers still "look right"

The call-count collapse (naive `fib(34)` = 18,454,929 recursive calls → memoised = 35 calls) still happens, because the typo still hits the cache (`fib_dict`) instead of recursing freely — so the headline lesson of the exercise (memoisation turns O(φⁿ) into O(n)) survives untouched. What breaks is *which* numbers end up in the cache.

Traced by direct execution (`fib_driver(34)`, `fib_dict = {}`):

```
fib_dict[0] = 1     naive F(0) = 0      naive F(1) = 1
fib_dict[1] = 1     naive F(1) = 1      naive F(2) = 1
fib_dict[2] = 2     naive F(2) = 1      naive F(3) = 2
fib_dict[3] = 3     naive F(3) = 2      naive F(4) = 3
...
fib_dict[k] = naive_F(k + 1)     for every k
```

**Every cached value is shifted up by exactly one Fibonacci index.** This falls out directly from the typo: the branch that is supposed to populate `fib_dict[n-2]` with `F(n-2)` instead populates it with the *same* value as `fib_dict[n-1]` (since it recurses on `n-1` again) — but because of how the recursion bottoms out and re-uses cached neighbours on the way back up, that shared value systematically comes out one index high rather than simply duplicating `fib_dict[n-1]`. The net effect, verified for all k up to 34, is `fib_dict[k] == F(k+1)`.

So after `fib(fib_dict, 34)` returns:

- `fib_dict[34]` = F(35) = **9,227,465** (matches the lab's separate iterative-`fib_iter(35)` cell exactly — cell 43 of the solutions notebook)
- `fib_dict[33]` = F(34) = **5,702,887** (matches the naive recursive `fib(34)` from cell 37/39)

## The official solutions notebook's "fix": read the wrong index instead of fixing the bug

The instructor's `fib_driver` doesn't call `fib_dict[n]`. It calls `fib_dict[n-1]`:

```python
def fib_driver(n):
  fib_dict = {}
  fib(fib_dict, n)
  print(fib_dict[n-1])     # not fib_dict[n]
```

Given the shift above, `fib_dict[n-1] == F(n)` — which is exactly the "expected" answer for `fib(n)`. **The off-by-one in the driver's read cancels the off-by-one in the cache**, so the printed number (5,702,887 for n=34) matches the naive implementation and looks completely correct. Nothing about the output would tip off a student that the underlying cache is wrong — the cancellation is exact and holds for every `n`, not just the one tested.

This is a textbook case of **debugging by matching the expected output rather than reading the code**: the two bugs were almost certainly introduced and "fixed" independently (one in the recursive function, one in the driver), each masking the other, and the instructor's own test (does the printed number match?) could not have caught it because it always passes.

## Why this is worth recording

- **A profiler cannot catch this class of bug.** cProfile correctly reports the call-count collapse (18M → 35 calls) either way — the *performance* story is unaffected. Only reading `fib_dict` directly, or testing intermediate values (`fib_dict[10]` should be F(10)=55, not F(11)=89), reveals it.
- **"The final number is right" is a weak correctness signal for a cache/table.** The lesson generalises past Fibonacci: any memoisation/DP table can be internally shifted, transposed, or otherwise wrong in a way that a single spot-checked output cannot detect, if the read site has a matching, compensating bug.
- **It survived instructor review.** This isn't a student typo — it's shipped, executed, and saved-with-outputs in the official `_solutions.ipynb`. Confirms that "the solutions say so" is not sufficient verification on its own; re-deriving expected values independently (as done here via a from-scratch naive `fib_naive`) is what actually caught it.

## Where this was found

- Local completion of the student skeleton (`Labs/Lab1/ICT3113_Week02_Introduction_to_Profiling_Student_clean.ipynb`) first flagged the `n-1`/`n-2` typo with a `# NOTE` comment, reasoning (correctly, but only partially) that the cache absorbs the mistake.
- Ingesting the official `_solutions.ipynb` (already executed on Colab, outputs saved) confirmed the identical typo in the instructor's copy, and its `fib_dict[n-1]` read — prompting the full trace above.

## Connections

- [[examples/ict3113-lab1-profiling]] — the lab this bug lives in, with the cProfile/memoisation results either way
- [[concepts/python-profiling]] — memoisation as the profiling-driven optimisation this lab teaches
- [[concepts/algorithm-complexity]] — O(2ⁿ) → O(n), the lesson the bug does not break
- [[learning/prompt-injection-in-lab-handout-pdf]] — sibling "don't trust the handout at face value" finding from a different course
