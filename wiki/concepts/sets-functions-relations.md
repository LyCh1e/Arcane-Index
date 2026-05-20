---
type: concept
title: "Sets, Functions & Relations"
domain: mathematics
course: INF1003
complexity: medium
tags: [sets, functions, relations, equivalence-relations, partial-order, injective, surjective, bijective]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000018
---

# Sets, Functions & Relations

Set theory, functions, and relations form the mathematical language of computer science — from database schemas and type systems to graph theory and algorithm design.

---

## Sets

A **set** is an unordered collection of distinct objects (elements).

| Notation | Meaning |
|----------|---------|
| $\{1, 2, 3\}$ | Roster notation |
| $\{x \mid P(x)\}$ | Set-builder notation |
| $x \in A$ | $x$ is an element of $A$ |
| $\emptyset$ or $\{\}$ | Empty set |

**Standard number sets:** $\mathbb{N}$ (naturals), $\mathbb{Z}$ (integers), $\mathbb{Q}$ (rationals), $\mathbb{R}$ (reals).

### Subsets and Equality

- $A \subseteq B$ — every element of $A$ is in $B$ (subset)
- $A \subset B$ — $A \subseteq B$ and $A \neq B$ (proper subset)
- $A = B$ — iff $A \subseteq B$ and $B \subseteq A$
- $\emptyset \subseteq A$ for every set $A$

### Cardinality

$|A|$ = number of distinct elements.

| Set | $|A|$ |
|-----|-------|
| $\{a, b, c\}$ | 3 |
| $\{\{a\}, b\}$ | 2 |
| $\emptyset$ | 0 |
| $\{\emptyset\}$ | 1 |

### Power Set

$\mathcal{P}(A)$ = the set of all subsets of $A$.

$$|\mathcal{P}(A)| = 2^{|A|}$$

**Example:** $\mathcal{P}(\{a, b\}) = \{\emptyset, \{a\}, \{b\}, \{a,b\}\}$ — four elements for a two-element set.

### Set Operations

| Operation | Symbol | Result |
|-----------|--------|--------|
| Union | $A \cup B$ | elements in $A$ or $B$ (or both) |
| Intersection | $A \cap B$ | elements in both $A$ and $B$ |
| Difference | $A - B$ | elements in $A$ but not $B$ |
| Complement | $\overline{A}$ | elements not in $A$ (relative to universal set $U$) |

**Cartesian product:** $A \times B = \{(a, b) \mid a \in A,\ b \in B\}$, with $|A \times B| = |A| \times |B|$.

### Set Identities

Set identities mirror [[propositional-logic]] equivalences exactly:

| Identity | Set law |
|----------|---------|
| Identity | $A \cup \emptyset = A$; $A \cap U = A$ |
| Domination | $A \cup U = U$; $A \cap \emptyset = \emptyset$ |
| De Morgan's | $\overline{A \cup B} = \overline{A} \cap \overline{B}$; $\overline{A \cap B} = \overline{A} \cup \overline{B}$ |
| Double complement | $\overline{\overline{A}} = A$ |

---

## Functions

A **function** $f: A \to B$ assigns to each element $a \in A$ exactly one element $f(a) \in B$.

- **Domain** = $A$; **codomain** = $B$
- **Range / image** = $\{f(a) \mid a \in A\} \subseteq B$

### Function Types

| Type | Definition | Check |
|------|------------|-------|
| **Injective** (one-to-one) | $f(a) = f(b) \Rightarrow a = b$ | No two inputs share an output |
| **Surjective** (onto) | Range = codomain | Every $b \in B$ is hit |
| **Bijective** | Both injective and surjective | One-to-one correspondence |

### Function Operations

- **Sum:** $(f_1 + f_2)(x) = f_1(x) + f_2(x)$
- **Product:** $(f_1 f_2)(x) = f_1(x) \cdot f_2(x)$
- **Composition:** $(f_1 \circ f_2)(x) = f_1(f_2(x))$ — apply $f_2$ first, then $f_1$

Composition is generally **not commutative**: $f_1 \circ f_2 \neq f_2 \circ f_1$.

### Floor and Ceiling

- $\lfloor x \rfloor$ = greatest integer $\leq x$ (e.g. $\lfloor 2.7 \rfloor = 2$, $\lfloor -2.7 \rfloor = -3$)
- $\lceil x \rceil$ = smallest integer $\geq x$ (e.g. $\lceil 2.1 \rceil = 3$, $\lceil -2.7 \rceil = -2$)

Used in the [[combinatorics#Generalised Form|generalised pigeonhole principle]] and algorithm analysis.

---

## Relations

A **binary relation** $R$ on set $A$ is a subset of $A \times A$. We write $aRb$ or $(a, b) \in R$.

### Properties of Relations

| Property | Definition | Matrix test |
|----------|------------|-------------|
| **Reflexive** | $\forall a,\, (a, a) \in R$ | All diagonal entries = 1 |
| **Symmetric** | $(a,b) \in R \Rightarrow (b,a) \in R$ | $M_R = M_R^T$ |
| **Antisymmetric** | $(a,b) \in R \wedge (b,a) \in R \Rightarrow a = b$ | No off-diagonal symmetric 1-pairs |
| **Transitive** | $(a,b) \in R \wedge (b,c) \in R \Rightarrow (a,c) \in R$ | $M_R^2$ has no 1 where $M_R$ has 0 |

### Equivalence Relations

A relation that is **reflexive, symmetric, and transitive** is an equivalence relation.

**Equivalence class** of $a$: $[a] = \{b \in A \mid aRb\}$ — the set of all elements equivalent to $a$.

**Example:** "Studies in the same programme" on SIT students is an equivalence relation; students partition into equivalence classes by programme.

### Partial Orders

A relation that is **reflexive, antisymmetric, and transitive** is a **partial order** (e.g. $\leq$ on integers).

A **total order** additionally requires every pair to be comparable.

---

## Related Pages

- [[propositional-logic]] — set identities are the direct analogue of logical equivalences
- [[predicate-logic-and-proofs]] — quantifiers are used to state set and relation properties formally
- [[discrete-mathematics-foundations]] — number theory uses divisibility as an example of a relation
- [[graph-algorithms]] — graphs are formally defined as relations (sets of vertex pairs)
