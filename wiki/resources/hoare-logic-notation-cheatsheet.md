---
type: resource
title: "Hoare Logic — Notation Cheat Sheet"
domain: formal-verification
course: ICT3112
created: 2026-10-26
updated: 2026-10-26
tags: [hoare-logic, notation, ascii, cheat-sheet, ict3112, workbench]
---

# Notation Cheat Sheet

ASCII input accepted by the [[resources/hoare-logic-workbench\|Hoare Logic Workbench]] WP calculator and `.hl` exercise files.

| You type               | It is displayed as | Meaning                                               |
| ---------------------- | ------------------ | ----------------------------------------------------- |
| `&&` or `/\`           | A ∧ B              | and                                                   |
| `\|\|` or `\/`         | A ∨ B              | or                                                    |
| `!`                    | ¬A                 | not                                                   |
| `​==>` or `​=>`        | A ⇒ B              | implies                                               |
| `<=>`                  | A ⇔ B              | if and only if                                        |
| `​=` or `​==`, `!=`    | x = y, x ≠ y       | equality, difference                                  |
| `<=`, `>=`             | x ≤ y, x ≥ y       | comparisons; chains such as `0 <= i <= n` are allowed |
| `x'`                   | x′                 | a logical variable                                    |
| `A0`, `x_k`            | A₀, x_k            | a name with a subscript                               |
| `2^n`                  | 2ⁿ                 | power                                                 |
| `fact(n)` or `n!`      | n!                 | factorial                                             |
| `Q[x <- E]`            | Q[x ← E]           | substitution                                          |
| `a[i \|-> e]`          | a[i ↦ e]           | array a updated at i                                  |
| `sum(k, 0, n-1, a[k])` | Σ k=0..n−1 a[k]    | a[0] + ... + a[n - 1]                                 |
| `forall k. P`          | ∀k. P              | for every k                                           |
| `wp(x := E, Q)`        | wp(x := E, Q)      | weakest precondition                                  |
| `x := E`               | x := E             | assignment, in programs                               |

Unicode symbols from the slides (∧ ∨ ¬ ⇒ ≤ ≥ ≠ ≔ ←) are also accepted — paste directly from slides.

Multiplication must be written explicitly: `n * (n + 1)`, not `n(n + 1)`.
