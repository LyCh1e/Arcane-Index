---
type: resource
title: "Frama-C (WP plugin) and ACSL"
domain: formal-verification
created: 2026-10-20
tags: [frama-c, acsl, wp, smt, why3]
---

# Frama-C / WP / ACSL

Deductive verification of C. Annotations are ACSL comments (`/*@ ... */`, `//@ ...`); the WP plugin turns them into verification conditions (weakest precondition calculus, see [[concepts/hoare-logic]]) and sends them to SMT solvers via Why3 (Alt-Ergo, Z3, cvc5).

## Commands

- `frama-c -wp -rte file.c` — prove contracts plus runtime-error guards (overflow, `\valid`, division). Statuses: Valid, Unknown/Timeout (not a disproof).
- `frama-c-gui -wp -rte file.c` — Ivette GUI (`ivette` before 33.0).
- `-wp-smoke-tests` — detects unsatisfiable preconditions.
- `-wp-no-simpl` — show raw VCs; `-wp-prover alt-ergo,z3,cvc5`; `-wp-timeout N`.
- `why3 config detect` — re-run after installing any prover.

## ACSL cheat sheet

`requires` / `ensures` / `assigns` / `\nothing` / `\old` / `\at(e,Pre|Here|LoopEntry|LoopCurrent|Label)` / `\valid` / `\valid_read` / `\separated` / `behavior` + `assumes` + `complete|disjoint behaviors` / `loop invariant` / `loop assigns` / `loop variant` / `\forall T x; range ==> P` / `\exists T x; range && P` (use `==>` with forall, `&&` with exists).

Rules of thumb: postconditions must pin the result exactly (`max` needs `== a || == b`); after a loop WP knows only the invariant, so link it to the postcondition (`a == \at(a,Pre) + i`); the invariant plus `¬guard` must imply the post (bounds both sides); give `\valid(p + (0..n-1))` for arrays.

Install on Windows: [[learning/frama-c-wsl-install-gotchas]]. Worked labs: [[examples/ict3112-frama-c-labs-0-2]].
