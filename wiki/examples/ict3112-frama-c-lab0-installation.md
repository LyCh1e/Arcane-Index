---
type: example
title: "ICT3112 Frama-C Lab 0 — Proof Environment Installation"
domain: formal-verification
course: ICT3112
created: 2026-10-20
updated: 2026-10-20
tags: [frama-c, wp, installation, wsl, lab]
---

# Lab 0 — Proof Environment Installation

Overview: [[examples/ict3112-frama-c-labs-0-2]]. Tool reference: [[resources/frama-c]]. Problems met: [[learning/frama-c-wsl-install-gotchas]].

## What the lab is about

Frama-C is a C analysis platform (CEA List / Inria). Its **WP** plugin implements the weakest precondition calculus from the lectures: ACSL annotations plus C code become verification conditions (VCs), which SMT solvers (Alt-Ergo, Z3, cvc5) try to prove valid. `-rte` adds assertions for runtime errors (overflow, invalid pointers).

## What I did

1. WSL 2 + Ubuntu 24.04 already present; `apt install opam build-essential libgmp-dev graphviz z3 cvc5 ...`.
2. `opam switch create frama 4.14.2`, then `opam install frama-c alt-ergo` (resolved Frama-C **33.0 Arsenic**, Alt-Ergo 2.6.4, Why3 1.8.2). Slow: everything compiles from source (~30–40 min).
3. `why3 config detect` — listed Alt-Ergo, Z3 4.8.12 and cvc5 1.1.2.
4. Verified with `swap` and `assert a == 37 && b == 42` (`lab0/main.c`): `frama-c -wp -rte main.c` gives **14/14 goals proved**.
5. Not done: GUI first start (`frama-c-gui`, needs Node 24 + yarn). The CLI is enough for the labs.

## Learnings

- Windows users run Frama-C inside WSL, and keep lab files in the Linux filesystem for speed (I ran them from `/mnt/c`, which worked but is slower).
- Since 33.0 the GUI command is `frama-c-gui` (was `ivette`).
- After installing any new prover, re-run `why3 config detect`; WP only sees provers Why3 knows about.
- Pinning versions avoids opam pulling in needless GTK packages.
- Non-interactive installs need care: opam prompts for system packages and layout upgrades (see the gotchas page).
