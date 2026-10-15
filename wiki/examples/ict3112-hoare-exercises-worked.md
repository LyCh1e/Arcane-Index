---
type: example
title: "ICT3112 Hoare Logic — Key Worked Proofs"
domain: formal-verification
course: ICT3112
created: 2026-10-15
updated: 2026-10-15
tags: [hoare-logic, weakest-precondition, loop-invariants, proof-outline, worked-examples]
---

# ICT3112 Hoare Logic — Key Worked Proofs

Condensed, high-value examples from the three solved exercise sheets.

---

## 1. WP for a Two-Statement Sequence

**Problem:** `{?}  y := x;  y := x + x + y;  {y = 3·x}`

**Method:** compute wp right to left.

| Step | Statement | Postcondition | Substitution | Result |
|---|---|---|---|---|
| 2 | `y := x + x + y` | `y = 3·x` | `[y ← x + x + y]` | `x + x + y = 3·x`, i.e. `y = x` |
| 1 | `y := x` | `y = x` | `[y ← x]` | `x = x` = **True** |

**Weakest precondition:** `True`. Any starting state works.

---

## 2. WP for an If–Else

**Problem:** `{?}  if (x − y > 0) then z := x else z := y  {z ≤ y ∧ z ≤ x}`

| Branch | Guard | Statement | Substitution | WP of branch |
|---|---|---|---|---|
| then | `x − y > 0` | `z := x` | `[z ← x]` | `x ≤ y` |
| else | `x − y ≤ 0` | `z := y` | `[z ← y]` | `y ≤ x` |

Combined: `(x − y > 0 ⇒ x ≤ y) ∧ (x − y ≤ 0 ⇒ y ≤ x) = x ≤ y ∧ y ≤ x = x = y`

**Weakest precondition:** `x = y`.

---

## 3. Proving a Three-Statement Triple

**Problem:** `{x = x′ ∧ y = y′}  k := x + n;  x := y − m;  y := k + y;  {x = y′ − m ∧ y = x′ + n + y′}`

| Step | Statement | Postcondition Q | Substitution | wp = Q after substitution |
|---|---|---|---|---|
| R3 | `y := k + y` | `x = y′ − m ∧ y = x′ + n + y′` | `[y ← k + y]` | `x = y′ − m ∧ k + y = x′ + n + y′` |
| R2 | `x := y − m` | above | `[x ← y − m]` | `y = y′ ∧ k = x′ + n` |
| R1 | `k := x + n` | `y = y′ ∧ k = x′ + n` | `[k ← x + n]` | `y = y′ ∧ x = x′` |

Given precondition = R1 (same conjuncts). ✓

---

## 4. Loop Invariant — Counter and Sum (Exercise 5a)

**Programme:**
```
{x = x′ ∧ y = y′ ∧ y ≥ 0}
while (y > 0) do {
    x := x + 1;
    y := y − 1;
}
{x = x′ + y′}
```

**Derivation:**

| At loop head | x | y | x + y |
|---|---|---|---|
| before pass 1 | 2 | 3 | 5 |
| before pass 2 | 3 | 2 | 5 |
| before pass 3 | 4 | 1 | 5 |
| at exit | 5 | 0 | 5 |

Sum `x + y` is constant = x′ + y′.

**Invariant:** `I ≡ x + y = x′ + y′  ∧  y ≥ 0`  
**Variant:** `E = y`

| Obligation | Proof |
|---|---|
| Establishment | `x = x′ ∧ y = y′ ∧ y ≥ 0 ⇒ x + y = x′ + y′ ∧ y ≥ 0` ✓ |
| Preservation | wp(body, I) = `x + y = x′ + y′ ∧ y ≥ 1`; I ∧ `y > 0` gives `y ≥ 1` ✓ |
| Exit | `y ≥ 0 ∧ y ≤ 0 ⇒ y = 0`; then `x = x′ + y′` ✓ |
| Termination | Variant `y ≥ 0` from I; decreases by 1 each iteration ✓ |

---

## 5. Loop Invariant — Multiplication by Counting (Exercise 5b)

**Programme:**
```
{x = x′ ∧ y = y′ ∧ y ≥ 0}
z := 0; a := 1;
while (a <= y) do {
    z := z + x;
    a := a + 1;
}
{z = x · y}
```

**Invariant:** `I ≡ z = x · (a − 1)  ∧  1 ≤ a ≤ y + 1`  
**Variant:** `E = y + 1 − a`

**Establishment:** wp(z:=0; a:=1, I) = `0 = x · 0 ∧ y ≥ 0` = `y ≥ 0` = P ✓

**Preservation:** wp(body, I) = `z + x = x · a ∧ 1 ≤ a + 1 ≤ y + 1`; from I and guard `a ≤ y` both conjuncts follow ✓

**Exit:** `a > y` and `a ≤ y + 1` together give `a = y + 1`; then `z = x · y` ✓

---

## 6. Russian Peasant Multiplication (Exercise 5c)

**Programme:**
```
{x = x′ ∧ y = y′ ∧ x′ ≥ 0 ∧ y′ > 0}
z := 0;
while (!(x = 0)) do {
    if (x mod 2 = 1) then z := z + y else skip;
    y := y * 2;
    x := x div 2;
}
{z = x′ · y′}
```

**Invariant:** `I ≡ x′ · y′ = x · y + z  ∧  x ≥ 0`  
**Variant:** `E = x`

**Preservation hint:** `2 · (x div 2) = x − x mod 2`

- Case `x mod 2 = 1`: z becomes `z + y`; then `x' · y' = 2(x div 2) · y + y + z = (x−1)·y + y + z = x·y + z` ✓
- Case `x mod 2 = 0`: `x' · y' = 2(x div 2)·y + z = x·y + z` ✓

**Exit:** `x = 0 ⇒ x · y + z = z = x′ · y′` ✓

---

## 7. Simple Partial Correctness — Loop that May Not Terminate

**Programme:**
```
{x = n}
while (x > 0) do { x := x − 2; }
{x ≤ 0}
```

Postcondition is exactly `¬B`. Simplest invariant: `True`.

| Obligation | Proof |
|---|---|
| Establishment | `x = n ⇒ True` ✓ |
| Preservation | wp(x:=x−2, True) = True; `True ∧ x > 0 ⇒ True` ✓ |
| Exit | `True ∧ ¬(x > 0) = x ≤ 0 = Q` ✓ |
| Termination | Variant E = x; `x > 0 ⇒ x ≥ 0` ✓; wp(x:=x−2, x < E₀) = `x − 2 < E₀`; with `x = E₀`, `x − 2 < x` ✓ |

**Note:** this only terminates when the initial *x* is *even and positive* or is 0. If *n* is odd and positive, the loop runs until `x = −1`. The invariant `True` is intentionally weak — it proves partial correctness without constraining the final value to `x = 0`.
