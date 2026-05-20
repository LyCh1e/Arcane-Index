---
type: concept
title: "Neural Networks & Linear Models"
domain: machine-learning
course: INF2008
complexity: high
address: c-000030
tags: [machine-learning, linear-regression, gradient-descent, backpropagation, neural-networks, activation-functions, encoding]
updated: 2026-05-11
status: established
created: 2026-05-11
---

# Neural Networks & Linear Models

Linear models are the foundation of modern neural networks. Understanding the progression from simple linear regression → multiple linear regression → the perceptron → deep networks clarifies both the mathematics and the design decisions.

---

## Categorical Encoding

Computers process only numbers. Categorical features must be converted before model training.

### Label Encoding

Assigns a unique integer to each category.

| Category | Encoded |
|----------|---------|
| Red | 0 |
| Green | 1 |
| Blue | 2 |

**Advantage:** Memory efficient; single column; natural for ordinal data.

**Danger:** Imposes artificial ordinality — the model may assume Red < Green < Blue and compute meaningless averages or distances between categories.

**When to use:** Only for genuinely **ordinal** variables (e.g., Low=0, Medium=1, High=2).

### One-Hot Encoding (OHE)

Creates a new binary column per unique category.

| Category | Red | Green | Blue |
|----------|-----|-------|------|
| Red | 1 | 0 | 0 |
| Green | 0 | 1 | 0 |
| Blue | 0 | 0 | 1 |

**Advantage:** No false ordinality; correct for nominal variables.

**Danger:** **Curse of Dimensionality** — 500 zip codes → 500 new columns; sparse, slow, memory-intensive.

**When to use:** Nominal categorical variables with a manageable number of unique values.

---

## Linear Regression

Models a continuous target as a linear function of one or more inputs.

### Simple Linear Regression

$$\hat{y} = m x + c$$

**Residual error:**
$$e_i = y_i - \hat{y}_i$$

**Mean Squared Error (MSE) and RMSE:**
$$MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2 \qquad RMSE = \sqrt{MSE}$$

- Squaring ensures all errors are positive and penalises large errors more.
- RMSE returns the error in the same units as the target.
- **Learning = finding m and c that minimise RMSE.**

### Multiple Linear Regression

$$\hat{y} = \sum_{k=1}^{d} m_k x_k + c$$

Extends to d features. The model learns one weight per feature. Features with small weights contribute little; features with large weights drive predictions.

---

## Gradient Descent — How Learning Works

### Four-Step Training Loop

#### Step 1 — Forward Pass

$$\hat{y}_i = w^T x_i + b$$

Compute predicted output using current weights w and bias b.

#### Step 2 — Loss Calculation

$$L(w, b) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

*(The ½ simplifies the gradient computation.)*

#### Step 3 — Backpropagation (Compute Gradients)

$$\frac{\partial L}{\partial w} = -\frac{1}{n} \sum e_i x_i \qquad \frac{\partial L}{\partial b} = -\frac{1}{n} \sum e_i$$

Where $e_i = y_i - \hat{y}_i$ (residual).

#### Step 4 — Gradient Descent Update

$$w \leftarrow w - \alpha \frac{\partial L}{\partial w} \qquad b \leftarrow b - \alpha \frac{\partial L}{\partial b}$$

α (alpha) is the **learning rate** — controls the step size.

### Worked Example

Data: (x=2, y=3), (x=3, y=4), (x=4, y=5). Initialise: w=1, b=0, α=0.1.

| i | x | y | ŷ=wx+b | e=y−ŷ |
|---|---|---|--------|-------|
| 0 | 2 | 3 | 2 | 1 |
| 1 | 3 | 4 | 3 | 1 |
| 2 | 4 | 5 | 4 | 1 |

L = ½ × ⅓ × 3 = 0.5 | ∂L/∂w = −3 | ∂L/∂b = −1

Updated: **w = 1.3**, **b = 0.1**

### Vectorised Form (Multiple Regression)

$$\nabla_w L = -\frac{1}{n} X^T e \qquad \frac{\partial L}{\partial b} = -\frac{1}{n} \mathbf{1}^T e$$

$$w \leftarrow w - \alpha \nabla_w L \qquad b \leftarrow b - \alpha \frac{\partial L}{\partial b}$$

---

## Neurons and Neural Networks

### The Neuron

A neuron generalises linear regression with a **non-linear activation function**:

$$z = W^T x + b \qquad a = \sigma(z)$$

| Symbol | Meaning |
|--------|---------|
| x | Input features |
| W | Weights |
| z | Linear combination (pre-activation) |
| σ | Activation function |
| a | Activated output |

**Without activation:** Stacking layers collapses to a single linear transformation: $W_2(W_1 x)$ = $W' x$.

**With activation:** The network becomes non-linear and can approximate arbitrarily complex functions.

### Hidden Layer Activation Functions

| Function | Formula | Range | Best Use |
|----------|---------|-------|----------|
| **ReLU** | $\max(0, z)$ | [0, ∞) | Default for hidden layers; fast, no saturation for positives |
| **Leaky ReLU** | $\max(\alpha z, z)$ | (−∞, ∞) | Fixes the "dead neuron" problem in deep CNNs / GANs |
| **tanh** | $\frac{e^z - e^{-z}}{e^z + e^{-z}}$ | (−1, 1) | Zero-centred; useful in RNNs / LSTMs |

> **Dead neuron:** A ReLU neuron that always receives negative input outputs zero, receives zero gradient, and never updates. Leaky ReLU mitigates this by allowing small negative outputs.

### Output Activation Functions

| Task | Output Activation | Notes |
|------|------------------|-------|
| Regression | Identity: f(z) = z | Raw numeric output |
| Binary classification | Sigmoid: $\frac{1}{1+e^{-z}}$ | Output ∈ (0,1) → probability |
| Multi-label classification | Sigmoid per class | Each class independently |
| Multi-class classification | Softmax: $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | Outputs sum to 1 |

**Softmax example:** Logits [2.0, 1.0, 0.1] → [0.659, 0.242, 0.099]

---

## Backpropagation in a Neuron

### Chain Rule

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}$$

### Loss Functions

| Task | Loss |
|------|------|
| Regression | Half MSE: $\frac{1}{2n} \sum (y_i - \hat{y}_i)^2$ |
| Classification | Cross-Entropy: $-\sum t_i \log(p_i)$ |

### Worked Backprop Example

Setup: x=2, w=0.5, b=1, identity activation, y=4, λ=0.1

**Forward pass:** z = 0.5×2 + 1 = 2; a = 2; L = ½(4−2)² = **2**

**Backpropagation:**
1. ∂L/∂a = a − y = 2 − 4 = **−2**
2. ∂a/∂z = 1 (identity)
3. ∂z/∂w = x = 2; ∂z/∂b = 1
4. ∂L/∂w = (−2)(1)(2) = **−4**; ∂L/∂b = (−2)(1)(1) = **−2**

**Update:** w = 0.5 − 0.1×(−4) = **0.9**; b = 1 − 0.1×(−2) = **1.2**

---

## Complexity Progression

| Model | Formula |
|-------|---------|
| Simple Linear Regression | $y = mx + c$ |
| Multiple Linear Regression | $y = \sum_k m_k x_k + c$ |
| Single Perceptron | $y = f\!\left(\sum_k m_k x_k + c\right)$ |
| Deep Neural Network | Multiple stacked nonlinear layers |

---

## Related Concepts

- [[ml-model-training-evaluation]] — RMSE and MSE as evaluation metrics; bias-variance diagnosis
- [[linear-algebra-matrices]] — vectorised gradient descent uses matrix calculus; the OLS solution $(X^TX)^{-1}X^Ty$ is the closed-form alternative to gradient descent
- [[eigenvalues-and-svd]] — SVD underpins weight decomposition in model compression
- [[ml-foundations]] — supervised learning context; regression vs classification framing
