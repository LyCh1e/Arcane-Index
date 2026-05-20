---
type: concept
title: "Database Normalisation"
domain: database-systems
course: INF2003
complexity: high
tags: [normalisation, functional-dependency, bcnf, 1nf, armstrong-axioms, closure, decomposition, anomalies, redundancy]
updated: 2026-05-12
status: established
created: 2026-05-12
---

# Database Normalisation

Normalisation is the process of designing a consistent database schema with *minimum redundancy*. It is Stage 4 (Schema Refinement) of the six-stage database design process — applied after the initial relational schema has been derived from an ER diagram.

> **Goal**: capture all necessary information with as little stored redundancy as possible.

---

## Why Normalise? — Data Anomalies

A poorly designed table that stores unrelated information together introduces **anomalies** — problems that arise when the data is modified.

**Example poorly designed table:**

| SID | Sname | ModuleID | ModuleName | Fee |
|-----|-------|----------|------------|-----|
| S1  | A     | M1       | C++        | 500 |
| S2  | B     | M1       | C++        | 500 |
| S3  | C     | M2       | Java       | 400 |

| Anomaly | Symptom |
|---------|---------|
| **Insertion anomaly** | Cannot record a new module (e.g., Python) without first enrolling a student |
| **Redundancy anomaly** | Module name and fee are repeated for every enrolled student |
| **Update anomaly** | Changing the fee for M1 requires updating *every* tuple where M1 appears — inconsistency if any row is missed |
| **Deletion anomaly** | Deleting student S3 also destroys all information about module M2 |

**Solution: decomposition** — split the table into smaller, non-redundant relations.

---

## Functional Dependencies (FDs)

A **functional dependency** X → Y means: knowing the value of X is sufficient to determine the value of Y.

> For any two tuples t1 and t2 in relation R: if t1[X] = t2[X] then t1[Y] = t2[Y].

**Notation**: `EmpID → Name, Phone, Position` (EmpID determines Name, Phone, and Position)

**Key distinctions:**
- An FD is a *constraint on all possible legal instances* of the relation — not just the current one
- Looking at one instance can show that an FD *does not* hold; it cannot prove that an FD *does* hold
- FDs generalise key constraints: if `K → all attributes`, then K is a superkey; the reverse is not necessarily true

---

## Armstrong's Axioms

A **sound and complete** set of inference rules for deriving all FDs from a given set F.

Let X, Y, Z denote sets of attributes.

| Rule | Statement |
|------|-----------|
| **Reflexivity** | If X ⊆ Y, then Y → X |
| **Augmentation** | If X → Y, then XZ → YZ for any Z |
| **Transitivity** | If X → Y and Y → Z, then X → Z |

**Derived rules** (provable from the three axioms):

| Rule | Statement | Proof sketch |
|------|-----------|-------------|
| **Union** | If X → Y and X → Z, then X → YZ | Augmentation + Transitivity |
| **Decomposition** | If X → YZ, then X → Y and X → Z | Reflexivity + Transitivity |
| **Pseudo-transitivity** | If X → Y and YZ → U, then XZ → U | Augmentation + Transitivity |

---

## Attribute Closure (X⁺)

The **closure of a set of attributes X** with respect to a set of FDs F is the complete set of attributes functionally determined by X.

**Algorithm:**

```
Input:  attribute set X, FD set F
Output: X⁺

1. Split all FDs so each has a single attribute on the right-hand side.
2. Result := X
3. Repeat until no change:
       for each FD B → Y in F:
           if B ⊆ Result then Result := Result ∪ {Y}
4. X⁺ := Result
```

**Example:**

FDs: `name → color`, `category → department`, `{color, category} → price`  
Compute `{name, category}⁺`:

1. X = {name, category}
2. `name → color` → add color → X = {name, category, color}
3. `category → department` → add department → X = {name, category, color, department}
4. `{color, category} → price` → both in X → add price → X = {name, category, color, department, price}

`{name, category}⁺` = {name, category, color, department, price}

### Uses of Closure

| Question | How to Answer |
|----------|--------------|
| Is X → Y derivable from F? | Compute X⁺; check whether Y ⊆ X⁺ |
| What are the keys of R? | Find subsets K where K⁺ = all attributes of R |
| Are FD sets F and G equivalent? | Check every FD in F is derivable from G, and vice versa |

---

## Normal Forms

Normal forms are benchmarks that characterise how well-designed a schema is. Each higher form eliminates a further class of anomaly.

```
Unnormalised  →  1NF  →  2NF  →  3NF  →  BCNF  →  4NF  →  5NF
Most redundancy                                          Least redundancy
```

For most practical purposes, **BCNF is the target**.

### 1NF — First Normal Form

> All attribute values are **atomic** (indivisible). No multi-valued cells, no lists.

**Violation:**

| Name | GPA | Courses |
|------|-----|---------|
| Alice | 3.8 | Math; DB; OS |

**Fix:** Split multi-valued attribute into a separate linking table.

| Name | GPA | | Name | Course |
|------|-----|-|------|--------|
| Alice | 3.8 | | Alice | Math |
| Bob | 3.7 | | Alice | DB |
| | | | Alice | OS |

### BCNF — Boyce-Codd Normal Form

> For every non-trivial FD X → Y in relation R, X must be a **superkey** of R.

**A trivial FD** is one where Y ⊆ X (e.g., `{A, B} → A`).

**Test:** Compute X⁺ for each non-trivial FD. If X⁺ ≠ all attributes of R, the FD violates BCNF.

**Example violation:**

```
Product(name, price, category, color)
FDs: {name, category} → price, category → color

(name, category)⁺ = {name, category, price, color}  ← superkey ✓
category⁺         = {category, color}               ← NOT a superkey ✗
```

`Product` is NOT in BCNF because `category → color` has a non-superkey left-hand side.

---

## BCNF Decomposition Algorithm

**Cannot** arbitrarily split relations — must use the violating FD to guide decomposition.

```
Normalise(R):
    Find FD X → A in R where A ∉ X and X⁺ ≠ all attributes (violates BCNF)
    If none found: R is in BCNF. Return.
    Else:
        Y = X⁺ − X       (attributes determined by X, excluding X itself)
        Z = R − X⁺       (remaining attributes not determined by X)
        Decompose R into R1(X⁺) and R2(X ∪ Z)
        Recursively Normalise(R1) and Normalise(R2)
```

**Example 1:**

```
Person(Name, SSN, Age, HairColour, PhoneNo)
FDs: SSN → Name, Age, HairColour
     Age → HairColour

Iteration 1: SSN⁺ = {SSN, Name, Age, HairColour} ← bad FD
  → Decompose: P(SSN, Name, Age, HairColour) and Phone(SSN, PhoneNo)

Iteration 2: check P — Age⁺ = {Age, HairColour} ← bad FD
  → Decompose P: People(SSN, Name, Age) and Hair(Age, HairColour)

Final: People(SSN, Name, Age), Hair(Age, HairColour), Phone(SSN, PhoneNo)
```

---

## Properties of Decomposition

After decomposing R into R1 and R2, two properties must be evaluated:

### Lossless Join (BCNF guarantees this ✓)

A decomposition of R into S and T is **lossless** if and only if:

```
S ∩ T ≠ ∅   AND   R = S ⋈ T
```

The original relation can be perfectly reconstructed by natural-joining the decomposed relations. BCNF decomposition always produces a lossless join.

**Lossy example:** Decomposing `Person(Name, Power, Category)` into `{Name, Power}` and `{Name, Category}` loses the `Power–Category` association — the join produces spurious tuples.

### Dependency Preservation (BCNF does NOT guarantee this ✗)

A decomposition **preserves all FDs** if every original FD can be enforced by checking constraints on individual decomposed relations (without joining).

BCNF can violate this:

```
R(C, P, S, J, D, Q)
FDs: C → PSJDQ, JP → C, SD → P, J → S
Decompose into: R1(CJDQ), R2(JS), R3(SDP)

JP → C spans R1 and R2 — cannot be enforced without joining.
```

**Trade-off:** If dependency preservation is critical, add a relation `(J, P, C)` solely to enforce `JP → C` — accepting some redundancy.

---

## Normalisation vs. Performance

Normalisation reduces redundancy but can *increase* query cost — joins are expensive.

| Approach | Benefit | Cost |
|----------|---------|------|
| Fully normalised | No redundancy, easy updates | More joins required for queries |
| Intentionally denormalised | Faster reads (one table, no join) | Redundancy; update anomalies |

> **Design principle**: normalise first; denormalise selectively based on measured query performance.

A database designer may deliberately keep a "bad" (denormalised) relation for performance-critical read paths — but the trade-off must be consciously accepted.

---

## Summary: The Normalisation Story

```
Bad design → anomalies
Anomalies  → redundancy
Redundancy → decomposition guided by FDs
FDs        → Armstrong's axioms → closure → BCNF check
BCNF       → lossless decomposition (but may sacrifice dependency preservation)
Resulting schema: minimal redundancy, no update/insert/delete anomalies
```

---

## See Also

- [[concepts/relational-database-fundamentals]] — Keys and integrity constraints (FDs generalise key constraints)
- [[concepts/er-diagrams]] — S2–S3 of design; normalisation is S4
- [[concepts/relational-algebra-and-sql]] — SQL used to implement and query normalised schemas
- [[sources/INF2003-database-systems]] — Source course
