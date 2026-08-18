---
type: concept
title: "ML Classification Models — kNN and SVM"
domain: machine-learning
complexity: medium
maturity: established
tags: [machine-learning, classification, kNN, k-nearest-neighbours, SVM, support-vector-machine, kernel-trick, kernel, margin, hyperplane, supervised]
created: 2026-08-17
updated: 2026-08-17
status: established
related:
  - "[[concepts/ml-foundations]]"
  - "[[concepts/ml-model-training-evaluation]]"
  - "[[concepts/decision-trees-and-ensembles]]"
  - "[[concepts/neural-networks-linear-models]]"
  - "[[sources/ml-summer-school-lec2b]]"
---

# ML Classification Models — kNN and SVM

Two classical supervised classification algorithms: k-Nearest Neighbours (kNN) and Support Vector Machines (SVM). Both produce decision boundaries without the gradient-descent training loop required by neural networks.

---

## 1. k-Nearest Neighbours (kNN)

### How It Works

kNN is a **lazy learner** — it has no explicit training phase. The entire training set is stored in memory. At prediction time, for a new input x:

1. Compute the distance between x and every training point (typically Euclidean distance)
2. Select the **k** nearest points
3. **Classification:** predict the majority class among those k neighbours
4. **Regression:** predict the average of those k neighbours' target values

The value of k is a hyperparameter:
- **k = 1:** Extremely sensitive to noise; produces a very jagged boundary
- **Large k:** Smoother boundary; less sensitive to individual points; may miss local structure

### Geometric Intuition

kNN draws a **Voronoi-like boundary**: each region of the input space belongs to the class of the nearest training points. Unlike SVMs or neural networks, the boundary is not parametric — it has no formula, only the stored data.

### Advantages and Disadvantages

| | Detail |
|--|--------|
| ✓ Simple | No training — the model is the data |
| ✓ No assumptions | Makes no assumptions about the data distribution |
| ✓ Flexible | Adapts to complex, non-linear boundaries naturally |
| ✗ Slow prediction | Must compute distance to every training point: O(n · d) per query |
| ✗ Feature scaling | Features must be normalised — unscaled features with large ranges dominate the distance |
| ✗ Curse of dimensionality | In high-dimensional spaces, all points become equidistant; nearest neighbours stop being meaningful |
| ✗ Memory | Entire training set must be stored |

### Practical Notes

- Always standardise features (zero mean, unit variance) before kNN — or at minimum, normalise to [0, 1]
- k is chosen by cross-validation; common starting values are k = 3, 5, or √n
- For images, pixel-level Euclidean distance is a poor similarity measure; learned embeddings are typically needed

---

## 2. Support Vector Machines (SVM)

### Core Idea

An SVM finds the **maximum-margin hyperplane** separating two classes. A hyperplane in d-dimensional space is defined by:

```
w · x + b = 0
```

where **w** is the normal vector to the hyperplane and b is the bias.

The margin is the distance between the hyperplane and the nearest training points from each class. SVM maximises this margin.

### Support Vectors

**Support vectors** are the training points that lie exactly on the margin boundary — they are the critical points that define the hyperplane. If any other training point were removed, the hyperplane would not change. If a support vector were removed, it would.

```
Margin = 2 / ||w||
```

Maximising the margin is equivalent to minimising ||w||, subject to all points being correctly classified (or within the soft-margin tolerance).

### Hard vs Soft Margin (C Parameter)

A **hard-margin SVM** requires perfect separation — not possible when classes overlap or contain noise.

A **soft-margin SVM** introduces slack variables ξᵢ ≥ 0 that allow points to be within the margin or on the wrong side:

| C value | Effect |
|---------|--------|
| Large C | Fewer margin violations, smaller margin → **low bias, high variance** |
| Small C | More tolerance for violations, larger margin → **high bias, low variance** |

C is a regularisation hyperparameter chosen by cross-validation.

### The Kernel Trick

The kernel trick allows SVM to find non-linear boundaries without explicitly computing a transformation into a high-dimensional feature space.

**The problem:** Some data that is not linearly separable in 2D becomes separable when lifted to a higher-dimensional space via a mapping φ(x). But computing φ(x) explicitly is expensive.

**The trick:** The SVM's decision function only ever requires **inner products** of the form φ(xᵢ) · φ(xⱼ). A **kernel function** K(xᵢ, xⱼ) computes this inner product directly in the original space — without computing φ at all.

This makes working in million-dimensional spaces computationally feasible.

#### Kernel Examples

**Example 1 — Quadratic transformation (1D → 2D):**

Data points on a number line that are not linearly separable. After squaring: x → x², the classes separate by a horizontal threshold.

**Example 2 — Modulo transformation:**

φ(x) = x mod 2 separates even values from odd values in 2D — not achievable with any line in 1D.

**Example 3 — Second-degree polynomial mapping (2D → 3D):**

```
φ([x₁, x₂]) = [x₁², √2·x₁x₂, x₂²]
```

Concentric circular classes (not separable in 2D) become separated by a plane in 3D. Visualising this:

```
Inner class (orange) maps to low z values
Outer class (blue) maps to high z values
→ linearly separable by a horizontal plane
```

#### Common Kernel Functions

| Kernel | Formula | Use case |
|--------|---------|----------|
| Linear | K(x, z) = xᵀz | When data is already linearly separable |
| Polynomial | K(x, z) = (xᵀz + c)^d | Moderate non-linearity |
| RBF (Gaussian) | K(x, z) = exp(−γ‖x − z‖²) | General purpose; default choice |

The **RBF kernel** is the most widely used default because it can represent arbitrarily complex boundaries and has only one hyperparameter (γ).

### High-Dimensional Space Trade-offs

Explicitly transforming data into high-dimensional space (without the kernel trick) has costs:
- High computational cost — storing and operating on large feature vectors
- Memory-intensive
- Numerical instability with very large or sparse feature vectors

The kernel trick avoids all of these by staying in the original feature space for computation.

### Advantages and Disadvantages

| | Detail |
|--|--------|
| ✓ High-dimensional spaces | Works well when features > samples |
| ✓ Robust to overfitting | Margin maximisation acts as regularisation |
| ✓ Non-linear | Kernel trick handles complex decision boundaries |
| ✗ Slow on large datasets | O(n²) to O(n³) training; O(n_sv · d) prediction |
| ✗ Kernel selection | RBF is a good default but requires tuning γ |
| ✗ Less interpretable | Decision function is a weighted sum over support vectors |

---

## Comparison: kNN vs SVM

| Property | kNN | SVM |
|----------|-----|-----|
| Training cost | None | O(n²) to O(n³) |
| Prediction cost | O(n · d) per query | O(n_sv · d) per query |
| Decision boundary | Non-parametric (Voronoi) | Parametric (hyperplane) |
| Requires feature scaling | Yes — critical | Yes — for most kernels |
| High-dimensional performance | Degrades (curse of dimensionality) | Works well |
| Non-linear boundaries | Yes (implicitly) | Yes (via kernel) |
| Interpretability | High (nearest neighbours) | Low (support vectors) |
| Hyperparameters | k | C, kernel type, γ (for RBF) |

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/ml-foundations]] | Supervised learning context; classification vs regression |
| [[concepts/ml-model-training-evaluation]] | Cross-validation for choosing k and C; bias-variance tradeoff |
| [[concepts/decision-trees-and-ensembles]] | Alternative classical classifiers; often compared with SVM on tabular data |
| [[concepts/neural-networks-linear-models]] | Deep learning replaces hand-designed features; SVM is equivalent to a single-layer network with a specific loss |
| [[concepts/medmnist-v2-datasets]] | These classifiers applied to medical imaging benchmarks |
| [[sources/ml-summer-school-lec2b]] | Primary source for this concept page |
