---
type: source
title: "ICT3112 Frama-C Slide Labs — Specifications, RTE, Labels (Lab 1) and Pointers (Lab 2)"
domain: formal-verification
source-type: lab-handout
course: ICT3112
status: ingested
created: 2026-10-27
updated: 2026-10-27
tags: [ict3112, frama-c, acsl, wp, rte, labels, pointers, valid, assigns, separated, llm-translation, lab]
---

# Source: ICT3112 Frama-C slide labs (Lab 1 and Lab 2 – Pointers)

**Files** (all in `Labs/lab3/`, SIT Frama-C 33 / Ivette slides, Dr David Sanan's course):

| File | Slides | Content |
|---|---|---|
| `ICT3112 - Lab1 - Frama-C.pdf` | 31 | Precise specifications (`max`), the LLM-translation exercise method, inconsistent preconditions, RTE and `abs`, labels (`\at`, `\old`, `\Pre`...), Exercises 1–5 **with solutions** |
| `ICT3112 - Lab2 - Frama-C-pointers.pdf` | 16 | `\valid` vs `\valid_read`, side effects and `assigns`, `\separated`, reading unproved goals in the TIP panel (`sumsq`, `take`) |
| `ICT3112 - Lab2 - Frama-C-pointers_exercises.pdf` | 23 | Same Lab 2 deck plus Exercises 1–6 (no solutions): `copy`, `reset`, `zero3`, `transfer`, `volume_up`, `next` |

Not to be confused with the older handouts [[examples/ict3112-frama-c-lab1-first-steps]] and [[examples/ict3112-frama-c-lab2-loops]] (the `Labs/lab1`, `lab2` folders). The code for these slides is the 19 `.c` files in `Labs/lab3/`. The PDFs were read in full and contain no embedded instructions beyond the lab (see [[learning/prompt-injection-in-lab-handout-pdf]] for the earlier cases in other courses).

## Lab 1 – what the slides teach

1. **Specification strength** (`max`, slides 2–6). `ensures \result == a || \result == b` is proved for `max` yet cannot prove the caller's `assert c == 42`; `ensures \result >= a && \result >= b` alone is also too weak; **both together** pin the result. WP is modular: at a call it uses the *contract only*, never the body.
2. **LLM workflow** (slides 7–8). Write the spec in English, have an LLM translate it to ACSL with a strict "literal translator" prompt (translate clause by clause, add/complete/correct nothing, mark `NOT TRANSLATED`, answer in two parts A/B), read the ACSL yourself, run `frama-c -wp -wp-rte file.c`, then decide whether English, translation or code is wrong. "WP proves the code satisfies the contract; it does not prove the contract says what you meant."
3. **Inconsistent preconditions** (slides 11–14). Contradictory `requires` make the Hoare triple vacuously true: `ensures \false` and `assert i == 3` are "proved". Only warning: the call's precondition goal reduces to `false`. `-wp-smoke-tests` reports the function as *Doomed*. Exercise 2 (`to_midnight`): `h<=23`, `m<=59` give `h*60+m <= 1439`, contradicting `>= 1440`.
4. **RTE** (slides 15–22). `-wp-rte` inserts guards for signed overflow, memory access, bounds, division by zero, shifts, float-to-int casts. For `-val` it asserts `-2147483647 <= val` *inside the then-branch*; fix is `requires INT_MIN < val` (`<limits.h>`). WP skips guards for unaligned pointers and invalid function-pointer calls. Margin bullets in Ivette: green proved, half-green proved-but-relies-on-unproved, yellow unproved.
5. **Labels** (slides 23–27). `\old(e)` only in `ensures`; `\at(e, Pre)` anywhere; `\at(e, Post)` only in `ensures` (Frama-C 33 rejects `\post(*a)`); `\at(x, L)` is the value at label `L` — if `x` is unassigned at `L`, WP knows nothing; if `x` is *declared after* `L`, the annotation is an `annot-error` that aborts the whole run unless `-kernel-warn-key annot-error=active`. Inside `\at(..., Pre)` every sub-expression is read at `Pre` (`x[*p]` trap).
6. **Exercises 1–5 (solved in the deck):** `clamp` (`requires lo <= hi`, four `ensures`), `to_midnight`, `tick` (`requires counter < INT_MAX`, `ensures counter == \old(counter)+1`), temp-free arithmetic swap with `\at(.., Before)` and `x + y == \at(x + y, Before)`, `deposit_twice` (`First` is *between* the deposits, not the start).

## Lab 2 – what the slides teach

- `swap` without `requires \valid(a) && \valid(b)`: four `rte,mem_access` goals fail. `\valid(p)` = read+write; `\valid_read(p)` = read only; `\valid(a + (s .. e))` = a range. RTE asks for the *minimum* access (write on the left of `=`, read on the right).
- A `const` variable is only `\valid_read`: `unref(&value)` with `requires \valid(p)` gives `Prove: false` in `main` (Frama-C adds a `(int *)` cast).
- **Side effects:** with no `assigns`, a caller assumes *anything* may change (`h == 42` after `swap` unproved). Fix is `ensures h == \old(h)` or, better, `assigns *a, *b` (WP also checks the body against it).
- **Aliasing:** `incr_a_by_b(a, b)` with `a == b` breaks `*b == \old(*b)`; add `requires \separated(a, b)`. Overflow needs `requires INT_MIN <= *a + *b <= INT_MAX` (ACSL arithmetic is mathematical, so this really bounds the C sum).
- **Reading unproved goals** (TIP panel: *Let / Assume / Prove*): `sumsq` (`ensures \result >= 2*x*y`) is **true but hard**: Alt-Ergo times out, Z3 proves it in ~0.5 s, or add `//@ assert (x - y) * (x - y) >= 0;`. `take` (`ensures *stock >= 0`) is **false** (stock 5, n 10): no prover helps; fix with `requires 0 <= n <= *stock`. Timeout never means false; Unknown from Z3/CVC4 is a hint the goal may be false.
- **Exercises 1–6:** `copy` (dst `\valid`, src `\valid_read`, because `limit` is `const`), `reset` (`assigns *p, resets`), `zero3` (`\valid(a + (0 .. 2))`, `assigns a[0 .. 2]`), `transfer` (separation + overflow; what if `from == to`?), `volume_up` (find the value satisfying Assume but not Prove), `next` (same, translating the proof obligation to English with an LLM).

## Links

Concept page: [[concepts/acsl-contract-strength-and-pointer-memory]]. Run results: [[examples/ict3112-frama-c-lab3-pointers-run]]. Tooling: [[resources/frama-c]], [[learning/frama-c-wsl-install-gotchas]]. Theory: [[concepts/hoare-logic]].
