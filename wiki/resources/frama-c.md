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

## Purpose: proof, not debugging

A debugger runs one input and shows what happened; Frama-C never runs the code and reasons symbolically, so a proved goal holds for every input (it found the `INT_MIN` overflow in `abs` with no test). It needs a contract from you, and a proof is only as strong as that contract: a wrong or weak spec proves the wrong thing. `Timeout`/`Unknown` is not a disproof. Best spent on small, critical code; testing and proof complement each other.

## Verified option notes (Frama-C 33.0)

- `-wp-rte` (slide option) skips the unsupported alignment/function-pointer guards; plain `-rte` adds `rte_pointer_alignment` goals that time out on `size_t*` array code.
- `-wp-no-simpl` (in the lab text) is a **deprecated alias of `-wp-no-subst`**; it still runs but warns. `-wp-no-qed` disables Qed simplification so raw VCs show in the GUI.
- `-wp-fct f` proves one function; `-wp-cache none` avoids the `.frama-c/` proof-cache folder; `-wp-timeout` defaults to 2 s.
- Several files each defining `main` (or the same function) cannot be loaded into one GUI session.
- Full list kept in `Labs/Frama-C-Commands.md` (CLAUDE.md requires updating it whenever a new command is verified).

## ACSL cheat sheet

`requires` / `ensures` / `assigns` / `\nothing` / `\old` / `\at(e,Pre|Here|LoopEntry|LoopCurrent|Label)` / `\valid` / `\valid_read` / `\separated` / `behavior` + `assumes` + `complete|disjoint behaviors` / `loop invariant` / `loop assigns` / `loop variant` / `\forall T x; range ==> P` / `\exists T x; range && P` (use `==>` with forall, `&&` with exists).

Rules of thumb: postconditions must pin the result exactly (`max` needs `== a || == b`); after a loop WP knows only the invariant, so link it to the postcondition (`a == \at(a,Pre) + i`); the invariant plus `¬guard` must imply the post (bounds both sides); give `\valid(p + (0..n-1))` for arrays.

Install on Windows: [[learning/frama-c-wsl-install-gotchas]]. Worked labs: [[examples/ict3112-frama-c-labs-0-2]].
