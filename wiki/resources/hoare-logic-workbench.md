---
type: resource
title: "Hoare Logic Workbench — davidsanan.github.io/Hoare-Logic"
domain: formal-verification
url: https://davidsanan.github.io/Hoare-Logic/
author: "David Sanan (SIT / ICT3112)"
status: active
created: 2026-10-26
updated: 2026-10-26
tags: [hoare-logic, formal-verification, ict3112, weakest-precondition, loop-invariants, interactive-tool, exercises]
---

# Hoare Logic Workbench

An interactive website by Dr David Sanan for learning and practising Hoare Logic, designed to accompany ICT3112. No server required; runs entirely in the browser.

**URL:** https://davidsanan.github.io/Hoare-Logic/  
**Source:** https://github.com/davidsanan/Hoare-Logic  
**Reference PDF:** *Hoare Logic for the Verification of Software* (HoareLogic.pdf) — D. Sanan

---

## Sections

| Section | What it covers |
|---|---|
| **Introduction** | What Hoare triples say; states and assertions; logical variables; proving with rules; WP calculus; frequent mistakes |
| **Language** | The five commands; specification language (fib, fact, sum, forall, …); ASCII notation input table |
| **Rules** | Interactive display of all 10 rules: each shows premises, conclusion, wp formula, mechanism, what to check, and a worked example |
| **Loop invariants** | 5-step recipe; other strategies; what to do when a check fails |
| **Exercises** | 40+ exercises, browsable and searchable by topic |
| **WP calculator** | Enter a programme + postcondition + invariants; the tool computes weakest preconditions backwards and shows each step |
| **Exercise editor** | Create `.hl` exercise files in plain text; preview and test them |

---

## All Exercises

### Skip
| File | Topic |
|---|---|
| `10-skip-consequence.hl` | Consequence rule applied to skip |
| `11-skip-not-valid.hl` | Invalid skip triple |

### Assignment
| File | Topic |
|---|---|
| `20-assign-double.hl` | Doubling a variable |
| `21-assign-minus-three.hl` | Subtract three |
| `22-assign-constant.hl` | Assign a constant |
| `23-assign-consequence-range.hl` | Consequence with assignment |

### Sequential Composition / Swap
| File | Topic |
|---|---|
| `30-swap-temp.hl` | Swap using a temporary |
| `31-swap-no-temp.hl` | Swap without a temporary |
| `32-series-of-assignments.hl` | Series of assignments |
| `33-fill-precondition-true.hl` | Fill in a true precondition |
| `34-fill-precondition-false.hl` | Fill in a false precondition |
| `35-37-prove-sequence-*.hl` | Prove a sequence triple (a, b, c) |
| `38-swap-arithmetic.hl` | Arithmetic swap |
| `39-square-36.hl` | Square a value |

### Conditionals
| File | Topic |
|---|---|
| `40-maximum.hl` | Maximum of two values |
| `41-44-conditional-*.hl` | Min, even, two conditionals, absolute value |
| `45-conditional-slides.hl` | Example from lectures |
| `46-empty-else.hl` | Conditional with empty else branch |

### Loops
| File | Topic |
|---|---|
| `50-countdown.hl` | Countdown to zero |
| `51-adds-two.hl` | Add 2 each iteration |
| `52-transfer-y-to-x.hl` | Transfer a value via a loop |
| `53-multiply-by-adding.hl` | Multiplication by repeated addition |
| `54-minus-two.hl` | Decrement by two each iteration |
| `55-sum-up-to-n.hl` | Triangular sum |
| `56-fibonacci.hl` | Fibonacci sequence |
| `57-factorial-wrong.hl` | Incorrect factorial (invariant fails) |
| `58-integer-division.hl` | Integer division |
| `60-powers-of-two.hl` | Powers of two |
| `61-factorial.hl` | Correct factorial |
| `62-sum-of-odd-numbers.hl` | Sum of odd numbers |
| `63-integer-square-root.hl` | Integer square root |
| `64-egyptian-multiplication.hl` | Egyptian (Russian peasant) multiplication |

### Arrays
| File | Topic |
|---|---|
| `70-array-read.hl` | Array read with definedness |
| `71-array-increment.hl` | Increment all array elements |
| `72-array-aliasing.hl` | Aliasing scenario |
| `73-naive-write-rule.hl` | Why the naïve write rule is wrong |
| `74-array-sum.hl` | Sum of array elements |

---

## Key JavaScript Modules

| Module | Purpose |
|---|---|
| `logic.js` | Parser, printer, substitution, wp calculation, evaluator/interpreter |
| `format.js` | Reads the `.hl` exercise file format |
| `checker.js` | Tests solutions against sample states |
| `content.js` | All educational text and rule definitions |
| `app.js` | UI implementation |

---

## Exercise File Format (`.hl`)

A plain-text file. Key fields:

```
id: my-exercise
title: Increment twice
topic: Sequential composition
level: 1            # 1–3
pre: x = 0
post: x = 3
program:
  {P}
  x := x + 1;  // i1
  {R1}
  x := x + 2   // i2
  {Q}
verdict: valid
step: The last statement
rule: ASSIGN, WP
focus: i2
calc:
  wp(x := x + 2, Q)
  = (x = 3)[x <- x + 2]
  = x = 1
set: R1 = x = 1
```

`{R1}` is a named slot — shown as unknown until a `set:` step fills it. Steps can use `rule:`, `calc:`, `vc:`, `instance:`, and `text:` fields. Loop exercises use `part: Establishment / Preservation / Conclusion`.

---

## WP Prover

The `test/` folder contains a prover that calls the **Z3 SMT solver** to prove verification conditions formally rather than by testing on small states. The standard testing tool evaluates claims on integers in `[-range, range]` — a passing test is not a proof.

---

## Related Pages

- [[concepts/hoare-logic]] — full rule reference and frequent mistakes
- [[concepts/loop-invariants]] — 5-step recipe, what to do when a check fails
- [[sources/ict3112-hoare-logic-core]] — lecture notes source
- [[examples/ict3112-hoare-exercises-worked]] — worked proofs
