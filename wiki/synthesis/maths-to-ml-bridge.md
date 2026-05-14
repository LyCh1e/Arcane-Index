---
type: synthesis
title: "Mathematics Foundations → Machine Learning: The Hidden Curriculum"
domain: mathematics × machine-learning
sources:
  - concepts/linear-algebra-matrices
  - concepts/eigenvalues-and-svd
  - concepts/probability-distributions
  - concepts/ml-foundations
  - concepts/neural-networks-linear-models
  - concepts/clustering-and-dimensionality-reduction
complexity: high
updated: 2026-05-14
tags: [synthesis, mathematics, machine-learning, linear-algebra, probability, PCA, neural-networks, gradient-descent, INF1003, INF1004, INF2008]
---

# Mathematics Foundations → Machine Learning: The Hidden Curriculum

Students who take the SIT maths modules (INF1003/INF1004) before machine learning (INF2008) often experience them as disconnected courses. They are not. INF2008 assumes fluency in the entire vocabulary of INF1003 and INF1004, but the connection is never made explicit in class. This page documents it precisely.

---

## 1. Linear Algebra → Neural Networks

### Weight matrices and the forward pass

A neural network layer is, at its most fundamental, a matrix-vector multiplication followed by a non-linear activation function. From [[concepts/neural-networks-linear-models|Neural Networks & Linear Models]]:

$$z = W^T x + b \qquad a = \sigma(z)$$

Here W is the weight matrix, x is the input vector, and b is the bias vector — all concepts defined in full in [[concepts/linear-algebra-matrices|Linear Algebra & Matrices]]. The dot product $W^T x$ is exactly the matrix multiplication rule:

$$(AB)_{ij} = \sum_k a_{ik} b_{kj}$$

applied to the case where B is a column vector. Every forward pass through a fully-connected network is a sequence of matrix multiplications. The vectorised gradient descent update for multiple-regression:

$$\nabla_w L = -\frac{1}{n} X^T e$$

is also pure matrix calculus: X is the design matrix, e is the residual vector, and $X^T e$ is a matrix-vector product.

### Closed-form vs iterative solutions

The ordinary least-squares solution from INF1004:

$$\hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y}$$

is the exact, closed-form alternative to gradient descent for linear regression. INF2008 reaches the same parameter values via iteration; INF1004 reaches them via matrix inversion. Understanding both reveals that gradient descent is a workaround for when the matrix inverse is too expensive to compute — which is always true for deep networks.

---

## 2. Eigenvalues and SVD → PCA

This is the most direct and underappreciated connection in the curriculum.

### PCA via eigendecomposition

[[concepts/clustering-and-dimensionality-reduction|Clustering & Dimensionality Reduction]] presents PCA as finding the eigenvectors of the covariance matrix:

$$C = \frac{1}{m} X_{scaled}^T X_{scaled} \qquad CW = \lambda W$$

The eigenvectors W are the principal component directions; the eigenvalues λ quantify the variance each component captures. This is literally the eigendecomposition covered in [[concepts/eigenvalues-and-svd|Eigenvalues, Diagonalisation & SVD]]:

$$A = PDP^{-1}$$

where P holds the eigenvectors and D holds the eigenvalues on its diagonal.

### PCA via SVD (the practical route)

In practice, computing the covariance matrix explicitly can be numerically unstable for large datasets. SVD provides a superior path:

$$X_{scaled} = U\Sigma V^T$$

The columns of V are the right singular vectors — and these are identical to the eigenvectors of $X^T X$, which is proportional to the covariance matrix. The singular values $\sigma_i = \sqrt{\lambda_i(X^TX)}$ give the same variance ordering as the eigenvalues. This is why scikit-learn's PCA implementation uses SVD internally, never the covariance matrix directly.

The INF2008 PCA algorithm (standardise → covariance → eigendecompose → project) and the SVD route arrive at the same principal components. SVD is simply more numerically stable and works on any m × n matrix, not just square covariance matrices.

### Rank-k approximation and dimensionality reduction

The SVD low-rank approximation:

$$A \approx \sum_{i=1}^{k} \sigma_i\, \mathbf{u}_i\, \mathbf{v}_i^T$$

is the mathematical statement of what PCA does when you select k principal components: you retain the k directions of greatest variance and discard the rest.

---

## 3. Probability Distributions → Bayesian Classifiers and Model Evaluation

### Gaussian Naive Bayes

Naive Bayes classifies by computing the posterior $P(class \mid features)$ via Bayes' theorem:

$$P(class \mid x) \propto P(class) \cdot P(x \mid class)$$

The Gaussian variant assumes features follow a Normal distribution within each class — a direct application of $X \sim N(\mu, \sigma^2)$ from [[concepts/probability-distributions|Probability Distributions]]. The likelihood $P(x_j \mid class)$ is evaluated using the Gaussian PDF:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

The prior $P(class)$ is the class frequency in the training data — the law of large numbers at work.

### Distribution of model errors

When evaluating a regression model, the residuals $e_i = y_i - \hat{y}_i$ are assumed to be normally distributed with mean zero and constant variance (homoscedasticity). This assumption justifies minimising MSE as a loss function: it is the maximum-likelihood estimator under a Gaussian error model. The CLT also explains why large-sample performance metrics (mean accuracy, mean F1 across cross-validation folds) behave predictably — they are sample means of identically distributed random variables.

---

## 4. Descriptive Statistics → Feature Scaling and Data Understanding

### Mean and variance in CRISP-DM phase 2

The CRISP-DM Data Understanding phase asks: what is the distribution of each feature? This is answered directly by the summary statistics from INF1003: mean $\mu$, variance $\sigma^2$, and standard deviation $\sigma$. Outliers are spotted as values beyond $\mu \pm 3\sigma$ (the 99.7% rule for Normal distributions).

### Feature scaling as standardisation

PCA, k-NN, K-Means, and SVMs all require features to be on comparable scales. The standardisation step in PCA:

$$X_{scaled} = \frac{X - \bar{X}}{\sigma}$$

is exactly the Z-score transformation from INF1004:

$$Z = \frac{X - \mu}{\sigma}$$

The reason it is required is stated in [[concepts/clustering-and-dimensionality-reduction|Clustering & Dimensionality Reduction]]: "features with larger numeric ranges dominate distance calculations." Variance, as defined in INF1004, is what PCA maximises — so an unscaled feature with large numeric values would trivially dominate the first principal component.

---

## 5. Where ML Goes Beyond the Maths Modules

The maths modules are necessary but not sufficient. Several INF2008 topics require knowledge that INF1003/INF1004 does not fully provide:

| ML Concept | Mathematical Basis | Coverage in INF1003/INF1004 |
|---|---|---|
| Gradient descent | Multivariate calculus (partial derivatives, chain rule) | Not covered — introduced directly in INF2008 |
| Cross-entropy loss | Information theory; logarithms of probabilities | Logarithms covered; information theory not |
| L1/L2 regularisation | L1 norm (sum of absolute values), L2 norm (Euclidean length) | Vector magnitudes and norms covered partially |
| Backpropagation | Chain rule over a computation graph | Chain rule not covered |
| t-SNE | KL divergence, Student's t-distribution | t-distribution not covered; KL divergence not covered |

The regularisation gap is worth noting explicitly. Ridge regression adds $\lambda \|w\|_2^2$ to the loss, and Lasso adds $\lambda \|w\|_1$ — both norms are defined in terms of vector magnitude, which INF1004 covers (magnitude $|\mathbf{v}| = \sqrt{\sum v_i^2}$), but the norm notation and its role in penalisation are introduced only in INF2008.

---

## 6. Module Dependency Summary

```
INF1004: Linear Algebra & Matrices
  ├── dot products, matrix multiplication  ──→  forward pass in neural networks
  ├── OLS solution (X^TX)^{-1}X^Ty        ──→  closed-form linear regression
  └── determinants, inverses               ──→  matrix operations in data preprocessing

INF1004: Eigenvalues & SVD
  ├── eigendecomposition                   ──→  PCA (covariance matrix route)
  └── SVD (A = UΣV^T)                     ──→  PCA (numerically stable route)

INF1004 / INF1003: Probability & Statistics
  ├── Normal distribution                  ──→  Gaussian Naive Bayes likelihood
  ├── mean, variance                       ──→  feature standardisation, Z-score scaling
  ├── Law of Large Numbers                 ──→  prior probabilities from class frequencies
  └── CLT                                  ──→  confidence in cross-validated metrics
```

---

## See Also

- [[concepts/linear-algebra-matrices|Linear Algebra & Matrices]] — matrix multiplication, dot products, OLS solution
- [[concepts/eigenvalues-and-svd|Eigenvalues, Diagonalisation & SVD]] — eigendecomposition, SVD computation, rank-k approximation
- [[concepts/probability-distributions|Probability Distributions]] — Normal distribution, mean, variance, CLT
- [[concepts/ml-foundations|Machine Learning Foundations]] — CRISP-DM, supervised vs unsupervised framing
- [[concepts/neural-networks-linear-models|Neural Networks & Linear Models]] — forward pass, gradient descent, backpropagation
- [[concepts/clustering-and-dimensionality-reduction|Clustering & Dimensionality Reduction]] — PCA step-by-step, t-SNE, feature scaling requirement
