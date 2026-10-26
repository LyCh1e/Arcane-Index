---
type: concept
title: "Loop Invariants"
domain: formal-verification
status: established
created: 2026-10-15
updated: 2026-10-26
sources: [ict3112-loop-invariants, ict3112-hoare-logic-core, ict3112-hoare-exercises, hoare-logic-workbench]
tags: [loop-invariants, hoare-logic, formal-verification, weakest-precondition, termination, variant, invariant-discovery]
---

# Loop Invariants

A **loop invariant** is a predicate *I* on the programme state that holds:
1. Before the first iteration (established by the precondition).
2. After every iteration (preserved by the loop body).
3. When the loop terminates (combined with the negated guard to give the postcondition).

Invariants are the core tool for verifying loops in Hoare Logic. Without one, the WHILE rule cannot be applied.

---

## What an Invariant Captures

An invariant is a *snapshot predicate* — it describes what is true at every loop-head, regardless of how many iterations have run.

```
{ I ∧ X = x₀ }
while (x > 0)
    x := x − 1;
{ I ∧ x ≤ 0 }
```

With `I ≡ x ≥ 0`:
- Before: x = 37 (satisfies x ≥ 0) ✓
- After iteration 1: x = 36 ✓ … After last: x = 0 ✓
- At exit: x ≥ 0 ∧ x ≤ 0 → x = 0

Invariants also describe what the loop **does not change**: if a variable *y* is not modified by the body, adding `y = Y` to *I* records that *y* keeps its initial value.

Invariants are **not unique**: `x ≥ 0` and `x ≥ 0 ∧ x ≤ X` are both valid invariants for the above loop; the second carries more information.

---

## The Four Proof Obligations

To prove `{P} WHILE B DO c {Q}` using invariant *I* and variant *E*:

| # | Obligation | Formula | How to prove |
|---|---|---|---|
| 1 | **Establishment** | P ⇒ I | Show the given precondition implies I; or if there is initialisation, compute wp(init, I) and show P ⇒ wp(init, I) |
| 2 | **Preservation** | {I ∧ B} c {I} | Compute wp(body, I) and prove I ∧ B ⇒ wp(body, I) |
| 3 | **Exit** | I ∧ ¬B ⇒ Q | The guard being false, combined with I, must give Q |
| 4a | **Variant non-negative** | I ∧ B ⇒ E ≥ 0 | The variant is non-negative whenever the loop runs |
| 4b | **Variant decreases** | {I ∧ B ∧ E = E₀} c {I ∧ E < E₀} | Each iteration strictly reduces E |

Obligations 1 and 3 use the Consequence Rule. Obligation 2 is the core loop check. Obligations 4a–4b give total correctness (termination).

---

## The Five-Step Recipe for Discovering Invariants

Finding an invariant is a *heuristic* process. Checking it is mechanical.

### Step 1 — Start from the Postcondition (Q)

- Identify the **progress variable** (counter that moves from initial to final value during the loop).
- Identify the **result variable** (constrained by Q at loop exit).
- The postcondition is the raw material for the invariant.

### Step 2 — Trace the Loop Head

Construct a small table showing the values of the key variables each time execution reaches the loop head:

| At the loop head | i | s |
|---|---|---|
| before pass 1 | 0 | 0 |
| before pass 2 | 1 | 1 |
| before pass 3 | 2 | 3 |
| before pass 4 | 3 | 6 |

Look for a formula that holds on every row.

### Step 3 — Generalise the Postcondition

Replace the *final value* of the progress variable in Q with the progress variable itself. This transforms "result at the end" into "result so far".

**Sanity check:** substituting the final value back must recover Q exactly.

**Example:** `Q: s = n(n+1)/2`. At exit `i = n`. Generalise: `I_candidate = s = i(i+1)/2`.

If Q mentions the progress variable in multiple roles, the trace (Step 2) and the preservation check (Step 5) determine which occurrences to replace.

### Step 4 — Add Bounds for the Counter

Append the range of the progress variable: typically `0 ≤ i ≤ n` or `1 ≤ i ≤ n+1` depending on whether the counter starts at 0 or 1.

**Full invariant example:** `I ≡ s = i(i+1)/2  ∧  0 ≤ i ≤ n`

### Step 5 — Check All Obligations

Verify Establishment, Preservation, and Exit mechanically:

**Preservation for the triangular-sum example:**
- Body: `i := i + 1; s := s + i`
- wp(body, I): substitute backwards → `s + (i+1) = (i+1)(i+2)/2 ∧ 0 ≤ i+1 ≤ n`
- Check `I ∧ B ⇒ wp(body, I)`:
  - From `s = i(i+1)/2` and adding `(i+1)`: `s + (i+1) = i(i+1)/2 + (i+1) = (i+1)(i+2)/2` ✓
  - From guard `i < n`: `i+1 ≤ n` ✓

If a check fails, the failure tells you what to add or fix in the invariant.

---

## Common Invariant Patterns

| Loop purpose | Typical invariant structure |
|---|---|
| Counter accumulation | `result = f(i)  ∧  0 ≤ i ≤ n` |
| Array scan (max/min/sum) | `property_of_A[0..i-1]  ∧  1 ≤ i ≤ n` |
| Multiplication by repeated addition | `p = i · m  ∧  0 ≤ i ≤ n` |
| Binary algorithm (halving) | `x' · y' = x · y + z  ∧  x ≥ 0` |
| Sorting (partial) | `A[0..i-1] sorted  ∧  0 ≤ i ≤ n` |

---

## Other Ways to Build a Candidate

Replacing a final constant with the progress variable (Step 3) is the most common technique, but there are three others:

| Strategy | When to use | Example |
|---|---|---|
| **Drop a conjunct** | Part of Q is already given by ¬B at exit (search loops) | A search that finds an index: Q says `a[result] = x`; `!B` already gives the position, so the invariant only needs `not found yet` |
| **Use two progress variables** | The loop works on a range from both ends | Reversing an array uses indices `i` (from left) and `j` (from right); invariant covers `A[0..i-1]` and `A[j+1..n-1]` swapped |
| **Add what preservation needs** | Preservation fails because the body uses a variable the candidate says nothing about | Fibonacci loop: candidate `a = fib(i)` fails preservation because the body also uses `b`; add `b = fib(i+1)` to the invariant |

---

## What to Do When a Check Fails

Source: Hoare Logic Workbench (`content.js`).

| Failing check | What the failing state shows | What to do |
|---|---|---|
| **Establishment** | A real start state that the candidate rejects | The candidate is **too strong** — weaken it |
| **Preservation** | A state the candidate accepts, from which one iteration leaves the candidate | The candidate is **too weak** — add the fact that rules out that state |
| **Exit** | A state satisfying I ∧ ¬B but not Q | The candidate is **too weak** — the bounds are usually missing |

**Example:** Candidate `p = a * i` for a multiplication loop `while i < b do (p := p + a; i := i + 1)`.  
The state `a = 2, b = 3, i = 4, p = 8` satisfies `I ∧ ¬B` but `p ≠ a * b`. The missing fact is `0 ≤ i ≤ b`.

---

## Loop Variants (Termination)

A **variant** *E* is an integer expression with two properties:

1. **Non-negative while running:** `I ∧ B ⇒ E ≥ 0`
2. **Strictly decreasing:** `{I ∧ B ∧ E = E₀}  c  {I ∧ E < E₀}` — compute using WP.

**Common variants:**

| Loop type | Typical variant |
|---|---|
| Count up to n | `n − i` |
| Count down to 0 | `i` |
| Halving | `x` (for `while x ≠ 0 do x := x div 2`) |
| Array index | `sizeof(a) − i` |

---

## Worked Example — Triangular Sum

```
{n ≥ 0}
i := 0;
s := 0;
while (i < n) {
    i := i + 1;
    s := s + i;
}
{s = n(n+1)/2}
```

**Invariant:** `I ≡ s = i(i+1)/2  ∧  0 ≤ i ≤ n`
**Variant:** `E = n − i`

| Obligation | Proof sketch |
|---|---|
| Establishment | wp(i:=0; s:=0, I) = `0 = 0 ∧ 0 ≤ 0 ≤ n` = `n ≥ 0` = P ✓ |
| Preservation | wp(body, I) = `s + (i+1) = (i+1)(i+2)/2 ∧ 0 ≤ i+1 ≤ n`; `I ∧ i < n` implies this ✓ |
| Exit | `I ∧ ¬(i < n)` → `i = n` (from bounds); substituting: `s = n(n+1)/2 = Q` ✓ |
| Variant ≥ 0 | `I ∧ i < n ⇒ n − i ≥ 1 ≥ 0` ✓ |
| Variant ↓ | wp(body, `n − i < E₀`) = `n − (i+1) < E₀`; with `n − i = E₀`, `n − i − 1 < n − i = E₀` ✓ |

---

## Worked Example — Russian Peasant Multiplication

```
{x = x' ∧ y = y' ∧ x' ≥ 0 ∧ y' > 0}
z := 0;
while (x ≠ 0) {
    if (x mod 2 = 1) then z := z + y else skip;
    y := y * 2;
    x := x div 2;
}
{z = x' · y'}
```

**Invariant:** `I ≡ x' · y' = x · y + z  ∧  x ≥ 0`
**Variant:** `E = x`

Key insight for preservation: the hint `2 · (x div 2) = x − x mod 2` lets you split into case `x mod 2 = 0` (then `2 · (x div 2) = x`) and case `x mod 2 = 1` (then `2 · (x div 2) = x − 1`).

---

## Related Pages

- [[concepts/hoare-logic]] — all six inference rules and WP calculus
- [[sources/ict3112-loop-invariants]] — source notes (Module 7)
- [[sources/ict3112-hoare-exercises]] — solved exercise sheets
- [[examples/ict3112-hoare-exercises-worked]] — condensed worked examples
