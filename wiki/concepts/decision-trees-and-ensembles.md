---
type: concept
title: "Decision Trees & Ensemble Methods"
domain: machine-learning
course: INF2008
complexity: high
address: c-000029
tags: [machine-learning, decision-trees, random-forest, boosting, bagging, ensemble, Gini, gradient-boosting]
updated: 2026-05-11
---

# Decision Trees & Ensemble Methods

Decision trees are the foundational supervised algorithm for classification and regression. Ensemble methods combine many such trees to overcome individual tree weaknesses — particularly high variance.

---

## Decision Trees

### Structure

A decision tree is a directed acyclic graph where:
- The **root** is the first splitting condition (the most informative feature).
- **Internal nodes** represent feature conditions.
- **Leaves** hold class labels or predicted values.
- **Depth** = number of decision steps from root to leaf.
- A **decision stump** has depth 1 (one split, two leaves, three nodes total).

### What Makes a Good Split?

A good split makes the resulting child nodes **more uniform (purer)** — fewer mixed classes within each node.

**Analogy:** Sorting clothes by type (shirts/pants/socks) creates uniform piles — good split. Sorting by colour creates mixed piles — bad split.

---

### Entropy

$$H = -\sum_i p_i \log_2 p_i$$

A measure of disorder. Maximum at equal class proportions (fair coin = 1.0 bits); zero when all samples belong to one class.

---

### Gini Impurity

$$Gini = 1 - \sum_i p_i^2$$

The probability of misclassifying a randomly chosen point if labelled according to class proportions.

- **Lower Gini = purer node**; Gini = 0 when all samples are one class.
- Faster to compute than entropy (no logarithms) → preferred in practice (sklearn default).

**Worked example:** 10 samples — 7 Bus, 3 MRT:
$$Gini = 1 - (0.7^2 + 0.3^2) = 1 - (0.49 + 0.09) = 0.42$$

### Gini After a Split

**Parent** (5 Bus, 3 MRT): Gini = 1 − (0.625² + 0.375²) = **0.469**

**After split:**
- Left child (2 Bus, 3 MRT): Gini = 1 − (0.16 + 0.36) = **0.48**
- Right child (3 Bus, 0 MRT): Gini = **0**
- Weighted Gini = (5/8) × 0.48 + (3/8) × 0 = **0.30** → improvement of 0.169

---

### Building a Decision Tree (Greedy Algorithm)

```
1. Compute Gini (or entropy) for all possible splits on all features.
2. Select the split with the lowest weighted Gini (highest information gain).
3. Assign that feature as the current node.
4. Recursively repeat on each child branch using only samples in that branch.
5. Continue until stopping criteria are met.
```

Decision trees are **greedy** — they choose the locally best split at each step, without backtracking to find a globally optimal tree.

---

### Stopping Criteria

Without stopping, trees grow until every leaf is pure → memorises training data → **overfitting**.

| Hyperparameter | Effect |
|----------------|--------|
| `max_depth` | Limits how many sequential decisions a tree can make; prevents overly specific rules |
| `min_samples_split` | Requires a node to have enough samples before it can split |
| `min_samples_leaf` | Ensures each leaf is supported by a minimum number of samples; prevents rare-case memorisation |

---

## Ensemble Methods

Ensembles combine multiple base learners to produce a better combined prediction.

> **Nasi Lemak analogy:** One restaurant review = one opinionated uncle. Thousands of reviews average out personal bias.

### Core Requirement

Base learners must be both **accurate** (better than random) and **diverse** (making uncorrelated errors). If all learners make the same mistakes, averaging adds nothing.

**Failure modes:**
- **Correlated errors** — all models see the same data in the same way; they all get the same things wrong.
- **Bad data / no signal** — ensembling cannot recover from fundamentally wrong inputs.

---

### Bagging (Bootstrap Aggregation)

- Train many models on different **bootstrap samples** of the training data (sampled with replacement).
- Aggregate predictions by voting (classification) or averaging (regression).
- Targets **variance reduction**; does not fix systematic bias.

**Bootstrap algorithm:**
1. From original dataset D₀ of size N, draw N samples **with replacement** → new dataset D₁.
2. Repeat for each tree (can be parallelised).

**Statistical property:** Sampling N with replacement from N preserves the expected empirical distribution. On average, ~63.2% of samples appear in each bootstrap dataset; ~36.8% are left out.

---

### Random Forests (Bagging + Feature Subsampling)

Random Forests extend bagging with an additional randomisation step:

1. **Bootstrap sampling** of data (standard bagging).
2. At each node split, consider only a **random subset of features** (`max_features`, default = √num_features).

**Why feature subsampling?** Without it, strong features dominate all trees → trees are correlated → ensemble gain is lost. Forcing each tree to use different feature subsets creates diversity.

#### Out-of-Bag (OOB) Estimation

Each tree is trained on ~63.2% of samples. The remaining **~36.8%** are "out-of-bag" for that tree.

$$P(\text{sample not selected}) = \left(1 - \frac{1}{N}\right)^N \approx e^{-1} \approx 0.368$$

**OOB accuracy:** For each training sample, gather predictions from all trees that did NOT see it, then compare to the true label. This provides a free validation estimate without a separate validation set.

#### Key Hyperparameters

| Parameter | Meaning | Default |
|-----------|---------|---------|
| `n_estimators` | Number of trees | 100 |
| `max_depth` | Max depth per tree | None |
| `max_features` | Features considered per split | sqrt(n_features) |
| `min_samples_leaf` | Min samples per leaf | 1 |
| `bootstrap` | Enable bootstrap sampling | True |
| `random_state` | Random seed | None |

---

### Boosting

Boosting trains base learners **sequentially**, with each new learner focusing on the errors of the previous ensemble.

- Targets **bias reduction**.
- Builds an increasingly complex decision boundary over iterations.

**Food recommendation analogy:**
- Round 1: "Where to eat?" → McDonald's.
- Round 2: "Not fast food?" → PS Cafe.
- Round 3: "Not fast food, not expensive?" → Japanese ramen.

#### AdaBoost

1. Train first model.
2. Identify misclassified points; **increase their sample weights**.
3. Train next model on the weighted data.
4. Repeat until convergence.
5. Combine all models weighted by their accuracy.

#### Gradient Boosting (GBM)

1. Train a weak regression tree on the data.
2. Compute the **loss gradient** (residuals) of the current ensemble.
3. Train the next tree to **predict the gradients**.
4. Update the ensemble: $\hat{y}_{new} = \hat{y}_{old} - \eta \times \text{tree output}$
5. Repeat.

**Loss gradient intuition:** If y_actual = 10, ŷ = 7:
- Residual = 3; MSE loss gradient = −6
- Negative gradient → prediction is too low → next tree pushes it up
- Scaled by learning rate η (e.g., 0.1): ŷ₁ = 7.6 → ŷ₂ = 8.08 → … → 10

**When boosting stops:**
1. Early stopping — adding a tree no longer improves validation performance
2. Fixed number of iterations
3. Minimum improvement threshold

---

### Stacking

- Train diverse models (different algorithm types) on the same data.
- Train a **meta-model** that learns how to optimally combine their predictions.
- Targets both bias and variance reduction.

---

### Ensemble Method Comparison

| Method | Error Reduced | Training | Aggregation |
|--------|---------------|----------|-------------|
| **Bagging** | Variance | Parallel | Voting / Averaging |
| **Boosting** | Bias | Sequential | Weighted sum |
| **Stacking** | Both | Parallel | Meta-learner |

---

## Related Concepts

- [[ml-model-training-evaluation]] — bias-variance trade-off; random forests directly address high variance
- [[ml-foundations]] — supervised learning context; classification vs regression
- [[eigenvalues-and-svd]] — feature importance in random forests can be related to SVD concepts
