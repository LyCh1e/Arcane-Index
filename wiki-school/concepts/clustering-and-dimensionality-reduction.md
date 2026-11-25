---
type: concept
title: "Clustering & Dimensionality Reduction"
domain: machine-learning
course: INF2008
complexity: high
address: c-000031
tags: [machine-learning, unsupervised, k-means, DBSCAN, PCA, t-SNE, clustering, dimensionality-reduction]
updated: 2026-05-11
status: established
created: 2026-05-11
---

# Clustering & Dimensionality Reduction

Unsupervised learning discovers structure in data without labels. The two primary families are **clustering** (group similar points) and **dimensionality reduction** (compress the feature space while preserving information).

---

## Distance Measures

All clustering algorithms depend on a notion of similarity, typically expressed as distance.

| Measure | Formula | Intuition |
|---------|---------|-----------|
| **Euclidean (L2)** | $\sqrt{\sum_i (x_i - y_i)^2}$ | Straight-line distance |
| **Manhattan (L1)** | $\sum_i |x_i - y_i|$ | City-block distance (grid walking) |
| **Chebyshev (L∞)** | $\max_i |x_i - y_i|$ | Chess king: max single-axis move |

**Worked example:** A=(3,5,7), B=(9,5,9)

| Metric | Calculation | Result |
|--------|-------------|--------|
| Manhattan | 6 + 0 + 2 | **8** |
| Euclidean | √(36 + 0 + 4) | **√40** |
| Chebyshev | max(6, 0, 2) | **6** |

> **Important:** Features with larger numeric ranges dominate distance calculations. Always **scale / normalise** features before clustering.

---

## k-Nearest Neighbours (k-NN)

Classify a new point by finding the k closest training points and taking a majority vote.

**Issues:**
- Prone to overfitting; common heuristic: k = √(number of training samples).
- Performance degrades with large N or large feature dimension.
- Requires feature scaling.

---

## K-Means Clustering

### Objective Function

$$J = \sum_{j=1}^{k} \sum_{x_i \in C_j} ||x_i - \mu_j||^2$$

Minimise the total within-cluster sum of squared distances. The centroid that minimises this for a given cluster is the **mean**:

$$\mu_j = \frac{1}{|C_j|} \sum_{x_i \in C_j} x_i$$

*Proof sketch:* Differentiate Jⱼ w.r.t. μⱼ, set to zero → μ = (1/n)Σxᵢ. Second derivative = 2n > 0 → global minimum.

### Algorithm

```
1. Initialise k centroids (e.g., random points from the dataset).
2. REPEAT:
   a. Assign each point to the nearest centroid.
   b. Recompute each centroid as the mean of its assigned points.
3. UNTIL centroids stop moving (or loss < threshold, or max iterations reached).
```

### Choosing K

| Method | Description | Limitation |
|--------|-------------|-----------|
| **Elbow Method** | Plot J vs k; look for the "elbow" where gain diminishes | Subjective; may be unclear in high dimensions |
| **Silhouette Score** | Measures cluster cohesion vs. separation (see below) | Computationally expensive for large datasets |

**Silhouette Score:**
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

- a(i) = average distance from xᵢ to points in **its own cluster**
- b(i) = average distance from xᵢ to points in the **nearest other cluster**
- Score ≈ 1: well separated | ≈ 0: on boundary | Negative: likely wrong cluster

### K-Means Limitations

- Assumes **spherical / convex** clusters — fails on irregular shapes (spirals, crescents).
- Sensitive to initialisation.
- Must specify k in advance.

### K-Means++ Initialisation

Reduces sensitivity to initialisation by spreading initial centroids:

1. Choose first centroid randomly from the data.
2. Choose each subsequent centroid with probability ∝ squared distance to the nearest existing centroid:
$$P(x_i) \propto D(x_i)^2$$

Points far from existing centroids are more likely to become new centroids.

---

## DBSCAN

**Density-Based Spatial Clustering of Applications with Noise**

### Parameters

| Parameter | Meaning |
|-----------|---------|
| **ε (epsilon)** | Neighbourhood radius — how far can a point be and still count as a "neighbour"? |
| **MinPts** | Minimum number of points required within ε to form a dense region |

### Point Types

| Type | Definition |
|------|-----------|
| **Core Point** | Has ≥ MinPts points within ε (including itself) |
| **Border Point** | Has < MinPts within ε, but is within ε of at least one core point |
| **Noise / Outlier** | Has < MinPts within ε AND is not within ε of any core point |

### Algorithm

```
1. Pick a random unvisited point.
2. If it has ≥ MinPts neighbours within ε → it is a core point → start a new cluster.
3. Expand cluster recursively: add all points within ε of the core point;
   if any of those are also core points, expand from them too.
4. If a point has < MinPts neighbours and no core-point neighbour → mark as noise.
5. Repeat until all points are visited.
```

### Effects of Parameter Choices

| Parameter | Too Large | Too Small |
|-----------|-----------|-----------|
| **ε** | Over-merging — many distinct clusters merge into one | Fragmentation — real clusters split |
| **MinPts** | High bias — misses small clusters; more points labelled noise | High variance — sensitive to noise; many tiny clusters |

### K-Means vs DBSCAN

| Feature | K-Means | DBSCAN |
|---------|---------|--------|
| Requires k in advance? | Yes | No |
| Shape assumption | Spherical / Convex | Arbitrary |
| Handles noise/outliers | No | Yes |
| Sensitive to feature scaling | Yes | Yes |
| Sensitive to initialisation | Yes | No |
| Fails with | Irregular shapes | Varying cluster densities |

---

## Principal Component Analysis (PCA)

PCA finds the directions of **maximum variance** in the data and projects points onto a lower-dimensional subspace while losing as little information as possible.

**Intuition:** Food nutritional labels have many correlated features (calories, carbs, sugar, fat, sodium, protein). PCA identifies three underlying factors: *energy density*, *protein vs carbs*, and *heart health* — compressing 6 features into 2–3 components.

### PCA — Step by Step

#### Step 1: Standardise

$$X_{scaled} = \frac{X - \bar{X}}{\sigma}$$

Required because PCA maximises variance — unscaled features with large numeric ranges would otherwise dominate.

#### Step 2: Compute the Covariance Matrix

$$C = \frac{1}{m} X_{scaled}^T X_{scaled}$$

C is n×n (n = number of features). Positive entries → positive correlation; negative → inverse relationship.

#### Step 3: Eigendecomposition

$$CW = \lambda W$$

- **Eigenvectors (W):** The principal component directions (new coordinate axes).
- **Eigenvalues (λ):** How much variance each PC captures.

**Food example:**

| PC | Eigenvalue | Variance Explained |
|----|------------|-------------------|
| PC1 (energy density) | 4.530 | 75.49% |
| PC2 (protein contrast) | 1.470 | 24.50% |
| PC3 | 0 | 0% |

**Why only 2 non-zero eigenvalues?** Rank ≤ min(samples − 1, features) = min(2, 6) = 2. Centering (subtracting the mean) removes one degree of freedom.

#### Step 4: Project Data

$$\text{PCs} = X_{scaled} \times W$$

Each original observation is now represented as coordinates along the principal component axes.

#### Step 5: Interpret

- **PC score magnitude:** How strongly a sample aligns with that component.
- **Feature loadings:** How much each original feature contributes to each PC.

---

## t-SNE (t-Distributed Stochastic Neighbor Embedding)

t-SNE reduces high-dimensional data to 2D or 3D for **visualisation**. Unlike PCA, it is non-linear and preserves **local** structure.

### Algorithm — Marble Bag Intuition

1. **High-D probabilities:** Convert pairwise distances to probabilities using a Gaussian:
$$P_{j|i} = \frac{\exp(-d_{ij}^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-d_{ik}^2 / 2\sigma_i^2)}$$
2. **Random 2D init:** Place points randomly in 2D.
3. **Low-D probabilities (Q):** Compute similarities in 2D using Student's t-distribution (heavier tails prevent the crowding problem):
$$Q_{ij} = \frac{(1 + ||Y_i - Y_j||^2)^{-1}}{\sum_{k \neq l} (1 + ||Y_k - Y_l||^2)^{-1}}$$
4. **Gradient descent:** Minimise KL divergence between P and Q:
$$\frac{dX_i}{dt} = 4 \sum_{j \neq i} (P_{ij} - Q_{ij})\, Q_{ij}\, (x_i - x_j)$$
   - Pᵢⱼ > Qᵢⱼ → **pull together** (close in high-D but far in 2D)
   - Pᵢⱼ < Qᵢⱼ → **push apart** (far in high-D but close in 2D)

### Perplexity Parameter

| Perplexity | Effect | Dataset Size |
|-----------|--------|-------------|
| Low (~5–10) | Very local; may fragment global structure | Small (~100 points) |
| Medium (~30–50) | Balanced local + global | Medium (~1,000 points) |
| High (~100+) | Global focus; fine detail lost | Large (~10,000+ points) |

### PCA vs t-SNE

| Feature | PCA | t-SNE |
|---------|-----|-------|
| Approach | Linear | Non-linear |
| Goal | Maximise global variance | Preserve local similarity |
| Deterministic? | Yes | No (stochastic) |
| Axes interpretable? | Yes (feature loadings) | No |
| Use case | Compression, preprocessing | Visualisation |

---

## Unsupervised Learning Taxonomy

| Category | Methods |
|----------|---------|
| **Partitional Clustering** | K-Means, DBSCAN |
| **Hierarchical Clustering** | HDBSCAN, DIANA |
| **Dimensionality Reduction (Linear)** | PCA |
| **Dimensionality Reduction (Non-linear)** | t-SNE, UMAP |
| **Feature Selection** | RFE, Mutual Information |
| **Association Rule Mining** | Apriori, FP-Growth, GSP, PrefixSpan |

---

## Related Concepts

- [[ml-foundations]] — unsupervised learning framing; CRISP-DM context
- [[eigenvalues-and-svd]] — PCA is computed via eigendecomposition; SVD is an equivalent formulation
- [[probability-distributions]] — Gaussian and t-distributions underpin t-SNE probability conversions
- [[descriptive-statistics]] — mean, variance, and standardisation are core PCA prerequisites
