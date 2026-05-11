---
type: concept
title: "Linear Algebra & Matrices"
domain: mathematics
course: INF1004
complexity: high
address: c-000022
tags: [linear-algebra, matrices, vectors, SLE, determinants, transformations]
updated: 2026-05-11
---

# Linear Algebra & Matrices

Linear algebra is the branch of mathematics that studies **vectors, matrices, and systems of linear equations**. It is the foundational language of machine learning, computer graphics, data science, and engineering.

---

## Matrices — Fundamentals

An **m × n matrix** has m rows and n columns:

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$

### Special Matrix Types

| Type | Definition |
|------|------------|
| Square matrix | m = n |
| Column vector | m × 1 |
| Row vector | 1 × n |
| Identity matrix I | Square; 1s on diagonal, 0s elsewhere |
| Zero matrix | All entries 0 |
| Diagonal matrix | Non-zero entries only on main diagonal |
| Symmetric matrix | $A = A^T$ |

---

## Matrix Operations

### Addition and Subtraction

Requires **same dimensions**:
$$(A + B)_{ij} = a_{ij} + b_{ij}$$

Properties: commutative ($A + B = B + A$), associative, $A + 0 = A$.

### Scalar Multiplication

$$kA = \begin{pmatrix} ka_{11} & \cdots \\ \vdots & \ddots \end{pmatrix}$$

### Transpose

$(A^T)_{ij} = a_{ji}$ — swaps rows and columns.

Key properties:
- $(A^T)^T = A$
- $(AB)^T = B^T A^T$
- $(A + B)^T = A^T + B^T$

### Matrix Multiplication

**AB** is defined only when cols(A) = rows(B).

If A is m × n and B is n × p, then AB is **m × p**:
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik}\, b_{kj}$$

Properties:
- **Not commutative:** AB ≠ BA in general
- Associative: (AB)C = A(BC)
- Distributive: A(B + C) = AB + AC
- $AI = IA = A$

---

## Determinants

The determinant encodes whether a matrix is invertible.

### 2 × 2

$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

### 3 × 3 (Cofactor Expansion along first row)

$$\det(A) = a_{11} M_{11} - a_{12} M_{12} + a_{13} M_{13}$$

where $M_{ij}$ is the minor (determinant of the 2×2 matrix obtained by deleting row i and column j).

### Key Properties

| Property | Detail |
|----------|--------|
| $\det(AB) = \det(A)\det(B)$ | Product rule |
| $\det(A^T) = \det(A)$ | Transpose invariant |
| $\det(kA) = k^n \det(A)$ | For n × n matrix |
| Row/col of zeros | det = 0 |
| Two identical rows/cols | det = 0 |
| Singular matrix | $\det(A) = 0$ |

---

## Inverse Matrix

$$AA^{-1} = A^{-1}A = I$$

**A is invertible if and only if det(A) ≠ 0.**

### 2 × 2 Inverse

$$A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

### Gauss-Jordan Method (General)

Set up augmented matrix $[A \mid I]$ and apply row operations until it becomes $[I \mid A^{-1}]$.

**Three elementary row operations:**
1. Swap rows: $R_i \leftrightarrow R_j$
2. Scale: $R_i \leftarrow k R_i$
3. Add multiple: $R_i \leftarrow R_i + k R_j$

Properties: $(AB)^{-1} = B^{-1}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$, $\det(A^{-1}) = \frac{1}{\det(A)}$.

---

## Systems of Linear Equations (SLE)

A system **Ax = b** where A is the coefficient matrix, x is the unknown vector, and b is the constants vector.

### Types of Solutions

| Condition | Outcome |
|-----------|---------|
| $\det(A) \neq 0$ | Unique solution: $\mathbf{x} = A^{-1}\mathbf{b}$ |
| Underdetermined (redundant equations) | Infinitely many solutions |
| Inconsistent (contradiction) | No solution (e.g., $0 = 5$) |

### Gauss-Jordan Elimination

Form the augmented matrix $[A \mid b]$ and row-reduce to obtain the solution.

---

## Vectors

A **vector** has both magnitude and direction.

$$\mathbf{v} = (v_1, v_2, \ldots, v_n)$$

**Magnitude:** $|\mathbf{v}| = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}$

**Unit vector (normalisation):** $\hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|}$

### Dot Product (Inner Product)

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i} u_i v_i = |\mathbf{u}||\mathbf{v}|\cos\theta$$

| Condition | Meaning |
|-----------|---------|
| $\mathbf{u} \cdot \mathbf{v} = 0$ | Orthogonal (perpendicular) |
| $\mathbf{u} \cdot \mathbf{u} = |\mathbf{u}|^2$ | Self dot-product = squared magnitude |

Properties: commutative, distributive, scalar multiplication.

### Parametric Line Equations

**In ℝ²:**
$$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x_0 \\ y_0 \end{pmatrix} + t \begin{pmatrix} d_1 \\ d_2 \end{pmatrix}$$

**In ℝ³ (symmetric form):**
$$\frac{x - x_0}{d_1} = \frac{y - y_0}{d_2} = \frac{z - z_0}{d_3}$$

---

## Linear Transformations

Matrices represent geometric transformations applied by multiplication:
$$\text{transformed} = B \cdot A \quad \text{(B = transformation matrix, A = vertices)}$$

### Common 2D Transformation Matrices

| Transformation | Matrix |
|----------------|--------|
| Reflect about x-axis | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ |
| Reflect about y-axis | $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ |
| Rotate by θ | $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ |
| Scale by factor k | $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ |
| Shear along x | $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ |

---

## Linear Regression (Matrix Form)

$$\mathbf{y} = X\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

**Ordinary Least Squares solution** (minimises $\sum (y_i - \hat{y}_i)^2$):

$$\hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y}$$

---

## Key Formulas Summary

| Operation | Formula |
|-----------|---------|
| 2×2 determinant | $ad - bc$ |
| 2×2 inverse | $\frac{1}{|A|}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ |
| Solve SLE | $\mathbf{x} = A^{-1}\mathbf{b}$ |
| Dot product | $\mathbf{u}\cdot\mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos\theta$ |
| Least squares | $\hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y}$ |

---

## Related Concepts

- [[eigenvalues-and-svd]] — builds directly on matrix foundations
- [[discrete-mathematics-foundations]] — number theory underlying integer arithmetic in linear systems
- [[sets-functions-relations]] — functions as linear maps; injection/surjection in the context of SLE uniqueness
