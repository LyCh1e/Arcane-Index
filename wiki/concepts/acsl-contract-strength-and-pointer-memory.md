---
type: concept
title: "ACSL Contracts: Strength, Vacuity, Runtime Errors and Pointer Memory"
domain: formal-verification
status: established
created: 2026-10-27
updated: 2026-10-27
sources: [ict3112-frama-c-lab1-lab2-pointers-slides]
tags: [acsl, frama-c, wp, rte, contracts, valid, assigns, separated, labels, aliasing, ict3112]
---

# ACSL Contracts: Strength, Vacuity, Runtime Errors and Pointer Memory

A checklist for writing a contract WP can use. Source: [[sources/ict3112-frama-c-lab1-lab2-pointers-slides]]; runs: [[examples/ict3112-frama-c-lab3-pointers-run]]; tool: [[resources/frama-c]]; theory: [[concepts/hoare-logic]]. A contract is the Hoare triple `{requires} body {ensures}`.

## 1. Two different questions

- **Is the body correct against the contract?** WP answers this (the function's own goals).
- **Does the contract say what I meant?** Nothing answers this except the callers. At a call WP uses *only the contract*, so a too-weak `ensures` fails in the *caller* (`max` with `\result == a || \result == b` is proved but `assert c == 42` is not).

Treat each `ensures` as a set of allowed results; the contract is their intersection. `{a, b} ∩ {max(a,b), max(a,b)+1, …} = {max(a,b)}`.

## 2. Vacuous contracts

Contradictory `requires` (`a < 0 && a > 0`, or `h <= 23 && m <= 59 && h*60+m >= 1440`) make every `ensures` provable, including `\false`, and every later `assert` in the caller. Symptom: the call-site *precondition* goal is `Prove: false`. Detector: `-wp-smoke-tests` ("Doomed"). Also read the proved-too-easily postcondition with suspicion.

## 3. Runtime errors are your preconditions

`-wp-rte` turns C's undefined behaviour into assertions: signed overflow, `\valid`/`\valid_read` memory access, bounds, division by zero, shifts, float casts. An RTE goal you cannot prove is usually a **missing `requires`**: `-val` needs `INT_MIN < val`; `counter + 1` needs `counter < INT_MAX`; `*a + *b` needs `INT_MIN <= *a + *b <= INT_MAX` (ACSL `+` is over mathematical integers, so this bounds the C sum).

## 4. Pointers: validity, effects, aliasing

| Need | Write | Why |
|---|---|---|
| Read and write `*p` | `requires \valid(p)` | RTE needs write access on the left of `=` |
| Read only (incl. `const` data) | `requires \valid_read(p)` | `\valid(&const_var)` is false |
| Array prefix | `\valid(a + (0 .. 2))`, `\valid_read(t + (0 .. 3))` | range notation `a + (s .. e)` |
| Say what changes | `assigns *a, *b;` / `assigns \nothing;` | without it a call may change *everything*; WP also proves the body obeys it |
| Preserve one global | `ensures h == \old(h)` | weaker than `assigns` |
| Pointers differ | `requires \separated(a, b)` | with `a == b`, `*a += *b` breaks `*b == \old(*b)` |

Order of repair for a failing pointer function: `\valid`/`\valid_read` → `assigns` → `\separated` → overflow bounds.

## 5. Labels and `\old`

- `\old(e)` (only in `ensures`) = `\at(e, Pre)` = value at call time. `\at(e, Post)` only in `ensures`. `\post(e)` does not exist in Frama-C 33.
- `\at(x, L)`: value of `x` at label `L`. A label before the first assignment gives WP no information (`x` unproved), and a variable **declared after** `L` is an annotation error that aborts the whole run (`-kernel-warn-key annot-error=active` downgrades it to a warning).
- Everything inside `\at(..., Pre)` is evaluated at `Pre`: `\at(x[*p], Pre)` also reads `*p` at `Pre`.
- A label placed *between* two statements is not the function start: `\at(balance, First) != \at(balance, Pre)` after one deposit.

## 6. When a goal is not proved: classify it

Open the goal's *Let / Assume / Prove* text and ask whether it is **false** or **true but hard**.

| Evidence | Diagnosis | Action |
|---|---|---|
| A concrete assignment satisfies Assume and falsifies Prove (`*stock=5, n=10`; `i=3` with `t[i+1]`) | goal is **false**: spec or code wrong | add a `requires` / fix the code (`<= 10` should be `< 10`) |
| Goal is a true arithmetic fact (`2xy <= x²+y²`) | **hard**: prover gap | try Z3/CVC5 (`-wp-prover alt-ergo,z3`) or add a helper `assert ((x-y)*(x-y) >= 0)`; more time did not help |
| Z3 and CVC5 say *Unknown* immediately | strong hint the goal is false | stop tuning provers |
| `assert` is half-green | it was proved by assuming an unproved RTE goal above it | fix the RTE goal first |

## 7. Using an LLM safely here

Write English first; give the LLM only prototypes and global names (not the body); use the literal-translation prompt; then read the ACSL back against your English. Round-trip (ACSL → English) and proof-obligation → English are the same tool in reverse. A proved contract can still be the wrong contract.
