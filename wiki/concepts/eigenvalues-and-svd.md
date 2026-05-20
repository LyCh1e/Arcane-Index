---
type: concept
title: "Eigenvalues, Diagonalisation & SVD"
domain: mathematics
course: INF1004
complexity: high
address: c-000023
tags: [linear-algebra, eigenvalues, eigenvectors, diagonalisation, SVD, PCA]
updated: 2026-05-11
status: established
created: 2026-05-11
---

# Eigenvalues, Diagonalisation & Singular Value Decomposition

Eigenvalues and eigenvectors reveal the **intrinsic geometry** of a linear transformation. Singular Value Decomposition (SVD) generalises this idea to any matrix and is one of the most powerful tools in applied mathematics.

---

## Eigenvalues and Eigenvectors

Let A be an n × n matrix. A scalar **λ** is an **eigenvalue** of A if there exists a non-zero vector **e** (the **eigenvector**) such that:

$$A\mathbf{e} = \lambda\mathbf{e}$$

**Geometric interpretation:** An eigenvector is a special direction that the transformation A only *scales* (by factor λ), without rotating it.

### Verification Example

$$A = \begin{pmatrix} 1 & 6 \\ 5 & 2 \end{pmatrix}, \quad \mathbf{u} = \begin{pmatrix} 6 \\ -5 \end{pmatrix}$$

$$A\mathbf{u} = \begin{pmatrix} -24 \\ 20 \end{pmatrix} = -4\begin{pmatrix} 6 \\ -5 \end{pmatrix} = -4\mathbf{u}$$

→ **u** is an eigenvector with eigenvalue **λ = −4**.

---

## Finding Eigenvalues — Characteristic Equation

For a non-trivial solution (e ≠ 0) to $(A - \lambda I)\mathbf{e} = \mathbf{0}$, the matrix $(A - \lambda I)$ must be singular:

$$\det(A - \lambda I) = 0$$

This **characteristic polynomial** is solved for λ to give all eigenvalues.

**Example (3 × 3):**

$$A = \begin{pmatrix} -1 & -1 & 2 \\ 1 & 2 & -1 \\ 0 & 1 & -1 \end{pmatrix}$$

$$\det(A - \lambda I) = 0 \implies (\lambda - 1)(\lambda + 1)^2 = 0 \implies \lambda_1 = 1,\; \lambda_2 = \lambda_3 = -1$$

A repeated eigenvalue (like λ = −1 here) is said to have **algebraic multiplicity** 2.

---

## Finding Eigenvectors

Substitute each eigenvalue back into $(A - \lambda I)\mathbf{e} = \mathbf{0}$ and solve the homogeneous system via row reduction.

**Example:** For λ = −1 in the above, solving gives:

$$e_2 = 0,\quad e_1 = e_3 \implies \mathbf{e} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \text{ (set } e_3 = 1\text{)}$$

---

## Eigendecomposition / Diagonalisation

A matrix A is **diagonalisable** if it has n linearly independent eigenvectors. Then:

$$A = PDP^{-1}$$

where:
- **P** = matrix whose columns are the eigenvectors of A
- **D** = diagonal matrix whose diagonal entries are the corresponding eigenvalues

### Key Benefit — Powers of A

$$A^n = PD^nP^{-1}$$

Since D is diagonal, $D^n$ is simply each diagonal element raised to the power n. This makes computing matrix powers — common in Markov chains, recurrences, and dynamic systems — efficient.

---

## Singular Value Decomposition (SVD)

SVD generalises eigendecomposition to **any m × n matrix** (not just square, symmetric ones):

$$A_{m \times n} = U_{m \times m}\;\Sigma_{m \times n}\;V^T_{n \times n}$$

| Factor | Description |
|--------|-------------|
| **U** | m × m matrix; columns are left singular vectors (orthonormal) |
| **Σ** | m × n diagonal matrix; diagonal entries are singular values $\sigma_i \geq 0$, in descending order |
| **V^T** | n × n matrix; rows are right singular vectors (orthonormal eigenvectors of $A^TA$) |

**Relationship:** $\sigma_i = \sqrt{\lambda_i(A^TA)}$

---

## Computing SVD — Step-by-Step

1. Compute $A^TA$ (n × n symmetric positive semi-definite matrix).
2. Find eigenvalues $\lambda_1 \geq \lambda_2 \geq \ldots \geq 0$ of $A^TA$.
3. Compute singular values $\sigma_i = \sqrt{\lambda_i}$.
4. Find **normalised** eigenvectors of $A^TA$ — these form the **columns of V**.
5. Compute left singular vectors: $\mathbf{u}_i = \frac{1}{\sigma_i} A\mathbf{v}_i$ for each $\sigma_i \neq 0$.
6. Assemble U, Σ, and $V^T$.

> **Critical:** Always normalise eigenvectors when constructing V and U; failing to do so means $U\Sigma V^T \neq A$.

### Non-Uniqueness of U

Columns of U corresponding to zero singular values (i.e., beyond rank(A)) do not affect the product — any orthonormal vector can fill those positions.

---

## Applications of SVD

### 1. Image (Data) Compression — Rank-k Approximation

$$A \approx \sum_{i=1}^{k} \sigma_i\, \mathbf{u}_i\, \mathbf{v}_i^T, \quad k < \text{rank}(A)$$

The first k singular values capture the most information. Using only the top-k terms gives a good approximation with far less data stored.

### 2. Dimensionality Reduction / PCA

SVD is the backbone of Principal Component Analysis. The columns of V are the principal components; the magnitude of each $\sigma_i$ indicates the variance explained by that component.

### 3. Recommender Systems

Decomposes a user–item rating matrix into latent feature representations of users and items (collaborative filtering).

### 4. Pseudoinverse and Least Squares

When A is not square or not invertible, the **Moore-Penrose pseudoinverse** is:
$$A^+ = V\Sigma^+ U^T$$

Least-squares solution: $\hat{\mathbf{x}} = A^+\mathbf{b}$

### 5. Machine Learning

- Weight matrix decomposition for model compression
- Data whitening and pre-processing
- Noise reduction

---

## Key Formulas

| Concept | Formula |
|---------|---------|
| Eigenvalue equation | $\det(A - \lambda I) = 0$ |
| Diagonalisation | $A = PDP^{-1}$ |
| Matrix power | $A^n = PD^nP^{-1}$ |
| SVD | $A = U\Sigma V^T$ |
| Singular values | $\sigma_i = \sqrt{\lambda_i(A^TA)}$ |
| Left singular vectors | $\mathbf{u}_i = \frac{1}{\sigma_i}A\mathbf{v}_i$ |
| Pseudoinverse | $A^+ = V\Sigma^+ U^T$ |

---

## Related Concepts

- [[linear-algebra-matrices]] — matrix operations, determinants, and inverses that eigenanalysis depends on
- [[discrete-mathematics-foundations]] — recurrence relations solved via eigendecomposition
- [[sets-functions-relations]] — vector spaces and linear maps as functions
