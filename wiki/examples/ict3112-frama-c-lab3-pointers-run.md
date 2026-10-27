---
type: example
title: "ICT3112 Frama-C Lab 3 Folder — Pointer Examples and Exercises, Run Results"
domain: formal-verification
course: ICT3112
created: 2026-10-27
updated: 2026-10-27
tags: [frama-c, acsl, wp, pointers, valid, assigns, separated, lab, ivette]
---

# Lab 3 folder run (Frama-C 33.0, Alt-Ergo 2.6.4, Z3 4.8.12, WSL Ubuntu)

Files: `Labs/lab3/*.c` (19 files). Slides: [[sources/ict3112-frama-c-lab1-lab2-pointers-slides]]. Concepts: [[concepts/acsl-contract-strength-and-pointer-memory]]. Command per file: `frama-c -wp -wp-rte -wp-cache none file.c`, one session per file, run from a script because of the quoting issues in [[learning/frama-c-wsl-install-gotchas]].

## Lecture examples — all match the slides

| File | Proved | What it shows |
|---|---|---|
| swap1.c | 3/7 | no `\valid`: 4 `rte,mem_access` timeouts |
| swap2.c | 7/7 | `requires \valid(a) && \valid(b)` |
| valid.c | 7/10 | `write_pointer` write needs `\valid`, `missing_return`, `unref(&value)` precondition false for `const` |
| side1.c | 13/13 | `ensures h == \old(h)` |
| side2.c | 11/12 | no `assigns`: second `h == 42` unproved |
| side3.c | 14/14 | `assigns *a, *b` |
| sep1.c | 6/10 | alias: both `ensures` + both overflow goals fail |
| sep2.c | 8/10 | `\separated`: only the 2 overflow goals left |
| sep3.c | 10/10 | plus `INT_MIN <= *a + *b <= INT_MAX` |
| sumsq.c | 8/9 (Alt-Ergo), **9/9 with `-wp-prover z3`** | true-but-hard goal |
| sumsq_assert.c | 10/10 | helper `assert (x-y)*(x-y) >= 0` |
| take.c | 7/8 (Z3: *Unknown*) | false goal |
| take_fix.c | 8/8 | `requires 0 <= n <= *stock` |

## Exercises — completed 2026-10-27, all proved with `frama-c -wp -wp-rte`

Started uncontracted (4/7, 4/9, 4/12, 5/11, 7/8, 10/11). Contracts written directly (English first, then ACSL), files in `Labs/lab3/` edited in place.

| File | Before | After | Contract |
|---|---|---|---|
| ex1_copy.c | 4/7 | **10/10** | `requires \valid(dst) && \valid_read(src)` (`limit` is `const`, so `src` cannot need `\valid`); `assigns *dst`; `ensures *dst == \old(*src)` |
| ex2_reset.c | 4/9 | **16/16** | `\valid(p)`, `\separated(p, &resets)` (else `p == &resets` breaks `*p == 0`), `resets < INT_MAX`; `assigns *p, resets`; `*p == 0`, `resets == \old(resets) + 1`. WP still prints the memory-model hypothesis `requires \separated(p, &resets)` for `reset`; every goal incl. the call in `main` is proved |
| ex3_zero3.c | 4/12 | **19/19** | `\valid(a + (0 .. 2))`; `assigns a[0 .. 2]` (this is what keeps `t[3]` and `other`); three `ensures a[k] == 0` |
| ex4_transfer.c | 5/11 | **18/18** | both `\valid`, `\separated(from, to)`, `INT_MIN <= *to + *from <= INT_MAX`; `assigns *from, *to`; `*to == \old(*to) + \old(*from)`, `*from == 0`. Answer to "from == to?": it would destroy the money (`*to = 2x`, then `*from = 0`), so the contract forbids it |
| ex5_volume.c | 7/8 | **8/8** | **code fixed**: `if(*volume <= 10)` to `< 10` (at 10 the guard passed and the volume became 11). Spec unchanged |
| ex6_next.c | 10/11 | **11/11** | **spec fixed**: `0 <= i <= 3` to `0 <= i <= 2` (`t[i+1]` reads index 4 at `i == 3`). `main` was already proved because it calls `next(t, 2)`; the postcondition bullet was half-green because it relied on the unproved `mem_access` goal |

## Traps found while running

- **All 19 files cannot share one session.** 9 define `main`, several define `swap`/`incr_a_by_b`/`sumsq`/`take`. Frama-C only emits `def'n of func main ... conflicts ... keeping the one at ...` and drops the later definition, so a combined run silently reports on the wrong code.
- GUI: 9 conflict-free groups opened as 9 Ivette windows, one per group: `{valid, swap1, sep1, sumsq, take, ex5}`, `{side1, sep2, sumsq_assert, take_fix}`, `{side2, sep3}`, `{side3}`, `{ex1, swap2}`, `{ex2}`, `{ex3}`, `{ex4}`, `{ex6}`. The `dbus ... systemd1.Manager.StartTransientUnit` lines in the GUI log are harmless WSL noise.
- Ivette windows read the **WSL copy** of the folder (`~/ICT3112-Software-Verification-and-Validation`); re-run `copy_to_wsl.sh` after editing the Windows files.
