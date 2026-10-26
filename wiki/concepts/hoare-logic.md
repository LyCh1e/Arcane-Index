---
type: concept
title: "Hoare Logic"
domain: formal-verification
status: established
created: 2026-10-15
updated: 2026-10-26
sources: [ict3112-hoare-logic-core, ict3112-hoare-arrays, hoare-logic-workbench]
tags: [hoare-logic, formal-verification, axiomatic-semantics, weakest-precondition, inference-rules, partial-correctness, total-correctness]
---

# Hoare Logic

Hoare Logic (also called *axiomatic semantics*) is a formal proof system for reasoning about the correctness of imperative programmes. It was introduced by Sir Tony Hoare in 1969.

**Key property:** Hoare Logic proves *partial correctness* — if the programme terminates, the postcondition holds. Termination is proved separately using *variants*.

---

## Hoare Triples

The central object is the **Hoare triple:**

```
{P}  C  {Q}
```

- **P** (precondition): a predicate on the programme state *before* C executes.
- **C**: the programme (or statement).
- **Q** (postcondition): a predicate the state must satisfy *after* C terminates.

Formally: if P holds in state σ and C executed from σ terminates in state σ′, then Q holds in σ′.

Assertions denote *sets of states*: `{x ≥ 0 ∧ y ≥ 1}` denotes every state where x is non-negative and y is at least 1.

---

## The Six Inference Rules

### [SKIP]

```
{Q}  SKIP  {Q}
```

SKIP does nothing. The state is unchanged, so any postcondition that held before still holds after. SKIP also fills a missing ELSE branch: `IF B THEN c` desugars to `IF B THEN c ELSE SKIP`.

---

### [ASSIGN]

```
{Q[x ← E]}  x := E  {Q}
```

The precondition is the postcondition *Q* with every free occurrence of *x* replaced by the expression *E*.

**Intuition:** after `x := E`, the name *x* holds the value *E* had before. So any property that *Q* requires of *x* must already hold of *E*.

**Examples:**
- `{y + 1 = 2}  y := y + 1  {y = 2}` — simplifies to `{y = 1}  y := y + 1  {y = 2}` ✓
- `{y + z = c}  x := y + z  {x = c}` ✓
- `{y * z > 0}  x := y * z  {x > 0}` ✓

---

### [CONSEQUENCE]

```
P → P′    {P′}  c  {Q′}    Q′ → Q
─────────────────────────────────────
            {P}  c  {Q}
```

Allows *weakening* the precondition (using a stronger P than needed) and *strengthening* the postcondition (accepting a weaker Q than proved).

**Use cases:**
- Bridging the gap between a given precondition and the weakest precondition produced by [ASSIGN].
- Simplifying a complex postcondition before passing it to [WHILE].

**Example:** to verify `{x > 120}  x := x + 1  {x > 101}`:
1. [ASSIGN] gives `{x > 100}  x := x + 1  {x > 101}`.
2. Show `x > 120 → x > 100`. ✓

---

### [SEQ]

```
{P}  c₁  {R}    {R}  c₂  {Q}
──────────────────────────────
      {P}  c₁ ; c₂  {Q}
```

An intermediate assertion *R* serves as both the postcondition of c₁ and the precondition of c₂.

**WP for sequences (compute right to left):**
```
wp(c₁ ; c₂, Q) = wp(c₁, wp(c₂, Q))
wp(c₁ ; c₂ ; … ; cₙ, Q) = wp(c₁, wp(c₂, … wp(cₙ, Q)…))
```

---

### [IF]

```
{P ∧ B}  c₁  {Q}    {P ∧ ¬B}  c₂  {Q}
─────────────────────────────────────────
     {P}  IF B THEN c₁ ELSE c₂  {Q}
```

Each branch sees the precondition *P* together with the truth-value of the guard *B*.

**WP for conditionals:**
```
wp(IF B THEN c₁ ELSE c₂, Q) = (B ⇒ wp(c₁, Q))  ∧  (¬B ⇒ wp(c₂, Q))
```

---

### [WHILE]

```
{I ∧ B}  c  {I}
──────────────────────────────────────────
{I}  WHILE B DO c  {I ∧ ¬B}
```

*I* is the **loop invariant** — a predicate that is preserved by every iteration of the body.

**Extended rule (with Consequence):**
```
P ⇒ I       {I ∧ B}  c  {I}       I ∧ ¬B ⇒ Q
──────────────────────────────────────────────────
            {P}  WHILE B DO c  {Q}
```

**WP formulation:** precondition = I, with two side conditions that must hold in every state:
- `(B ∧ I) ⇒ wp(c, I)` — preservation
- `(¬B ∧ I) ⇒ Q` — exit condition

See [[concepts/loop-invariants]] for how to find and verify invariants.

---

### [ARRAY-READ]

Standard [ASSIGN] is insufficient for array reads because the index may be out of bounds.

Notation: `def(a[i]) ≡ 0 ≤ i < sizeof(a)`

```
{Q[x ← a[i]]  ∧  def(a[i])}  x := a[i]  {Q}
```

The precondition must include both the value property and a definedness guard.

---

### [ARRAY-ASSIGN]

Array assignment `a[i] := E` is more complex than scalar assignment because only one cell changes; all other cells are unmodified.

Notation: `a[i ← E]` denotes the array equal to *a* except at index *i*, where it holds *E*.
- `(a[i ← v])[i] = v`
- `(a[i ← v])[j] = a[j]` for `j ≠ i`

```
{Q[a ← a[i ← E]]  ∧  def(a[i])}  a[i] := E  {Q}
```

---

## Dijkstra's Weakest Precondition Calculus

`wp(C, Q)` is the *largest* (weakest) set of states from which executing C is guaranteed to terminate in a state satisfying Q.

```
∀P. (P ⇒ wp(C, Q))  ⇒  {P} C {Q}
```

**Summary of wp rules:**

| Statement | wp(C, Q) |
|---|---|
| `SKIP` | Q |
| `x := E` | Q[x ← E] |
| `c₁ ; c₂` | wp(c₁, wp(c₂, Q)) |
| `IF B THEN c₁ ELSE c₂` | (B ⇒ wp(c₁, Q)) ∧ (¬B ⇒ wp(c₂, Q)) |
| `WHILE B DO c` | I, with side conditions (B∧I)⇒wp(c,I) and (¬B∧I)⇒Q |
| `x := a[i]` | Q[x ← a[i]] ∧ def(a[i]) |
| `a[i] := E` | Q[a ← a[i ← E]] ∧ def(a[i]) |

---

## Partial vs. Total Correctness

| | Partial correctness | Total correctness |
|---|---|---|
| **Claim** | If C terminates, Q holds | C terminates AND Q holds |
| **Tool** | Hoare Logic (WHILE rule) | Hoare Logic + variant |
| **Notation** | {P} C {Q} | [P] C [Q] (some textbooks) |

Hoare Logic as presented here proves partial correctness. Termination is added via a *variant* (see [[concepts/loop-invariants]]).

---

## Proof Outline Format

A proof outline annotates a programme with intermediate assertions:

```
{P}           // precondition
stmt₁;
{R₁}          // intermediate assertion
stmt₂;
{R₂}
…
{Q}           // postcondition
```

Each consecutive pair `{Rₖ} stmtₖ₊₁ {Rₖ₊₁}` must be a valid Hoare triple.

---

## Logical Variables

Specifications often need to refer to the value a variable had at the start. **Logical variables** are names (such as `x'`, `A`, or `n`) that the programme never assigns. The precondition `x = x' && y = y'` names the initial values; the postcondition `x = y' && y = x'` says the values were swapped.

> **Critical:** `x` and `x'` are two *different* variables. When the [ASSIGN] rule substitutes `x ← E`, the variable `x'` is unchanged. Confusing them is one of the most common mistakes in assessments.

---

## Notation — ASCII Input Reference

The WP calculator and `.hl` exercise files accept plain ASCII. The workbench renders it as the slide notation.

| You type | Displayed as | Meaning |
|---|---|---|
| `&&` or `/\` | A ∧ B | and |
| `\|\|` or `\/` | A ∨ B | or |
| `!` | ¬A | not |
| `==>` or `=>` | A ⇒ B | implies |
| `<=>` | A ⟺ B | if and only if |
| `=` or `==`, `!=` | x = y, x ≠ y | equality, difference |
| `<=`, `>=` | x ≤ y, x ≥ y | comparisons; chains `0 <= i <= n` allowed |
| `x'` | x′ | logical variable (prime) |
| `A0`, `x_k` | A₀, xₖ | name with subscript |
| `2^n` | 2ⁿ | power |
| `fact(n)` or `n!` | n! | factorial |
| `Q[x <- E]` | Q[x ← E] | substitution |
| `a[i \|-> e]` | a[i ↦ e] | array a updated at i |
| `sum(k, 0, n-1, a[k])` | Σ a[k] | a[0] + … + a[n−1] |
| `forall k. P` | ∀k. P | for every k |
| `exists k. P` | ∃k. P | there exists k |
| `wp(x := E, Q)` | wp(x := E, Q) | weakest precondition |

Unicode symbols from the slides (∧ ∨ ¬ ⇒ ≤ ≥ ≠ ≔ ←) are also accepted.

Multiplication must be written explicitly: `n * (n + 1)`, not `n(n + 1)` (which is parsed as a function call).

### Specification Language Functions

`fib(n)`, `fact(n)` (= n!), `pow(a, b)` (= aᵇ), `abs(x)`, `even(x)`, `odd(x)`, `min`, `max`, `sizeof(a)`, `def(a[i])` (= 0 ≤ i < sizeof(a))  
Sums: `sum(k, lo, hi, e)` = e[k=lo] + … + e[k=hi]  
Products: `prod(k, lo, hi, e)`  
Quantifiers: `forall k. P`, `exists k. P`

---

## Frequent Mistakes

From the Hoare Logic Workbench (source: `content.js`):

1. **Going forwards.** Rules are applied *from the postcondition up to the precondition*. Starting from the precondition and pushing down does not follow the [ASSIGN] rule and will produce wrong results.

2. **Mixing x and x′.** They are *different* variables. The substitution `[x ← x − y]` replaces `x` only. For example, `(x = y' && y = x')[x ← x − y]` is `x − y = y' && y = x'` — the `x'` is untouched.

3. **Inventing conjuncts.** Every intermediate assertion must come from a rule. Adding a conjunct about a variable not in the formula (e.g. `k = k'`) is at best unnecessary and often wrong.

4. **Writing an assertion that no rule produced.** Every assertion in a proof outline must be justified by the rule of the adjacent command, or by an implication in the Consequence rule.

5. **Sign errors when simplifying.** `x − (x − y)` is `y`, not `−y`. Keep parentheses introduced by a substitution until you have simplified them carefully.

---

## Why Formal Verification Matters

Historical software failures caused by unverified programmes:
- **Therac-25** (1985–87): arithmetic overflow in radiation therapy machine → at least 3 deaths.
- **Ariane 5** (1996): 64-bit float to 16-bit int conversion overflow → £370 M rocket destroyed on launch.
- **Patriot Missile** (1991): clock desynchronisation → 28 soldiers killed.
- **Blockchain exploits**: $3.6 billion stolen in 2022 via smart contract bugs.

Testing is *incomplete*: it can find bugs but cannot prove their absence. Formal verification can prove zero errors for the verified properties.

---

## Related Pages

- [[concepts/loop-invariants]] — finding and verifying invariants, the 5-step recipe
- [[sources/ict3112-hoare-logic-core]] — lecture notes source (Modules 0–6)
- [[sources/ict3112-loop-invariants]] — loop invariant discovery lecture notes (Module 7)
- [[sources/ict3112-hoare-arrays]] — array rules lecture notes (Module 8)
- [[sources/ict3112-hoare-exercises]] — solved exercise sheets
- [[examples/ict3112-hoare-exercises-worked]] — key worked proofs
