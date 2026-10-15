---
type: source
title: "ICT3112 Formal Verification — Reasoning about Arrays (Module 8)"
domain: formal-verification
source-type: lecture-notes
course: ICT3112
status: ingested
created: 2026-10-15
updated: 2026-10-15
tags: [ict3112, hoare-logic, arrays, array-read, array-assign, bounds-checking, formal-verification, dr-david-sanan]
---

# Source: ICT3112 Formal Verification — Reasoning about Arrays (Module 8)

**Files (7 parts):**
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 8 - Reasoning about Arrays - 1a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 8 - Reasoning about Arrays - 1b.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 8 - Reasoning about Arrays - 2a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 8 - Reasoning about Arrays - 2b.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 8 - Reasoning about Arrays - 3a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 8 - Reasoning about Arrays - 3b.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 8 - Reasoning about Arrays - 3c.md`

**Presenter:** Dr. David Sanan, Singapore Institute of Technology

---

## Summary

Module 8 extends Hoare Logic to handle array reads and array writes. Ordinary variable rules break down for arrays because:
- **Reads** may be out-of-bounds (undefined cell).
- **Writes** update one cell but leave all others unchanged — the postcondition must reason about the entire updated array, not just the written cell.

Two new rules, [ARRAY-READ] and [ARRAY-ASSIGN], are derived step by step.

---

## Why the Simple Assignment Rule Is Insufficient for Arrays

**Problem with reads:**
Naïvely applying [ASSIGN] to `x := a[i]` gives precondition `a[i] > 0` for postcondition `x > 0`. But if `i` is out of bounds the read is undefined, and no postcondition is guaranteed.

**Fix — [ARRAY-READ]:**
The precondition must include both the value condition *and* a definedness guard.

Notation: `def(a[i]) ≡ 0 ≤ i < sizeof(a)`

Rule: `{Q[x ← a[i]]  ∧  def(a[i])}  x := a[i]  {Q}`

**Problem with writes:**
Array assignment `a[i] := E` does not behave like scalar assignment. After `a[i] := v`, cell `a[i]` has value `v`, but `a[j]` for `j ≠ i` is unchanged. Standard `Q[a ← E]` would substitute the whole array name, losing information about the other cells.

**Fix — [ARRAY-ASSIGN]:**
Introduce the *array update* expression `a[i ← E]`, meaning "the array equal to `a` everywhere except at index `i`, where it has value `E`".

Rule: `{Q[a ← a[i ← E]]  ∧  def(a[i])}  a[i] := E  {Q}`

After `a[i] := v`, any assertion about `a[j]` must be expressed using `a[i ← v][j]`:
- If `j = i`: `(a[i ← v])[i] = v` ✓
- If `j ≠ i`: `(a[i ← v])[j] = a[j]` ✓

---

## Key Notation

| Symbol | Meaning |
|---|---|
| `sizeof(a)` | Number of elements in array *a* |
| `def(a[i])` | `0 ≤ i < sizeof(a)` — index *i* is within bounds |
| `a[i ← v]` | Array update: same as *a* except cell *i* holds *v* |
| `(a[i ← v])[j]` | Read cell *j* after updating cell *i* |

---

## Worked Exercises

### Exercise 1 — Read and Check

```
{ ? }
x := a[i];
{ x > 0 }
```

Applying [ARRAY-READ]: `Q[x ← a[i]] ∧ def(a[i]) = (a[i] > 0) ∧ def(a[i])`

**Precondition:** `{a[i] > 0 ∧ 0 ≤ i < sizeof(a)}`

### Exercise 2 — Write and Preserve Other Cells

```
{ ? }
a[i] := v;
{ a[i] = v ∧ a[j] = a[j] }
```

After applying [ARRAY-ASSIGN] with the array update notation, the precondition must encode the updated state and include `def(a[i])`.

### Exercise 3 — Loop over an Array

For loops that iterate over arrays (e.g., find maximum, copy, sum), the invariant must describe:
- The portion of the array examined so far (range `0 ≤ k < i`).
- The definedness of every accessed index within the loop body.
- Bounds on the progress variable *i*.

---

## Concept Pages Updated

- [[concepts/hoare-logic]] — array rules section
