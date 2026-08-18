---
type: concept
status: established
title: "Digital Image Processing"
domain: machine-learning
source: [[sources/ml-summer-school-lec4a]], [[sources/ml-summer-school-lec4b]]
updated: 2026-08-18
tags: [concept, machine-learning, image-processing, computer-vision, convolution]
---

# Digital Image Processing

> "A convolutional layer performs exactly the operation we build by hand. The only difference is that we choose the numbers in the kernel and the network learns them."

This page covers the mathematical foundations of digital images (Lecture 4a) and the two families of image operations — point operations and neighbourhood operations (Lecture 4b). It closes with the bridge from classical image processing to convolutional neural networks.

---

## 1. Three Levels of Image Understanding

```
Image editing     →  pixel-level changes, display-only (Photoshop)
Image processing  →  analysis of what the image contains (data)
Computer vision   →  use the data to make decisions (classify, detect, segment)
```

A CNN sits at the third level — but if the processing in level 2 destroys information, no network can recover it.

---

## 2. Digital Image Representations

### Ideal (Continuous) Image

A continuous function over a 2D spatial domain:

```
f : D_2D → ℝ,   (x, y) ↦ f(x, y)
```

- Origin at **bottom-left** (mathematical convention)
- Intensity is a real number — unlimited precision

### Digital (Discrete) Image

Sampled onto a pixel grid:

```
f : M × N → G

M = {0, 1, …, M−1}    (columns)
N = {0, 1, …, N−1}    (rows)
G = {0, 1, …, G−1}    (grey levels)
```

- Origin at **upper-left** (image/screen convention)
- 8-bit image: G = 256 levels

### RGB Colour Space

A colour image is a **vector-valued** function:

```
f : D → ℝ³    given by    (f_R, f_G, f_B)
```

- Additive mixing: three primary channels combine to produce perceived colour
- Limitation: changing brightness affects all three channels simultaneously — they are entangled

### HSV Colour Space

Separates colour from intensity into three orthogonal axes:

| Component | Meaning | Key values |
|-----------|---------|------------|
| **Hue** | angle on the colour wheel | 0°=red, 120°=green, 240°=blue |
| **Saturation** | purity | 0%=neutral grey, 100%=pure colour |
| **Value** | brightness | 0%=black, 100%=full brightness |

**Why use HSV?**
- Under multiplicative illumination change (e.g., dimmer lighting): H and S remain invariant; only V scales
- Enables robust colour-based thresholding on H alone, ignoring brightness variation
- Intuitive for colour pickers and selective hue/saturation editing

**Limitations:**
- Euclidean distances in HSV do not reflect perceived colour differences
- V is not perceived brightness — yellow and blue can both give V = 100%
- H is circular (0° = 360°) — no straightforward averaging or filtering
- H is meaningless for grey or dark pixels — always verify an S/V threshold before using H

---

## 3. Part I — Point Operations

A **point operation** maps each pixel through a transfer function independently of its neighbours:

```
f_transformed(m, n) = T_g( f(m, n) )
```

- Position never enters the formula — same input always → same output
- The histogram changes; the spatial geometry does not
- Only 256 possible inputs (8-bit) → compute T once, store as a look-up table

### The Histogram

```
a_g    = number of pixels with grey value g
p_f(g) = a_g / (M · N)     (relative histogram — a probability distribution)
```

**Reading the histogram:**

| Pattern | Diagnosis |
|---------|-----------|
| Mass at left end | Under-exposed |
| Mass at right end | Over-exposed |
| Narrow peak, range unused | Low contrast |
| Spikes piled at 0 or 255 | Clipping — information already lost |

**What the histogram cannot know:** it counts grey values and forgets their positions. Two images with identical histograms can look completely different. Spatial questions require neighbourhood operations.

### Clipping

Clipping is **irreversible and silent** — the image still looks plausible; only the histogram reveals the spike at the boundary. Practical rule: compute in float, clip **once** at the very end, then check the histogram.

### Linear Scaling

```
f_scale(m, n) = ( f(m, n) + c₁ ) · c₂
```

- **c₁** = offset — shifts the histogram left/right; perceived as brightness
- **c₂** = gain — scales distances between grey values; perceived as contrast; values far from the origin move most

### Histogram Stretching (Min–Max Normalisation)

```
T(g) = (g − g_min) / (g_max − g_min) × (G − 1)
```

- Maps the occupied range onto the full [0, G−1] range
- Equivalent to **min-max normalisation** applied to network inputs
- **Do not use the extreme values** for g_min and g_max — a single hot pixel controls the entire transform
- Use the **1%–99% percentiles** instead

### Histogram Equalisation

Uses the cumulative histogram as the transfer function:

```
T_equal(g) = round( (G − 1) · h_f(g) )    where    h_f(g) = Σ_{k ≤ g} p_f(k)
```

**Worked example — 10-pixel image, G = 10:**

| g | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| a_g counts | 0 | 0 | 0 | 2 | 0 | 1 | 6 | 1 | 0 | 0 |
| p_f(g) | 0 | 0 | 0 | .2 | 0 | .1 | .6 | .1 | 0 | 0 |
| h_f(g) cumulative | 0 | 0 | 0 | .2 | .2 | .3 | .9 | 1.0 | 1.0 | 1.0 |
| T_equal(g) | 0 | 0 | 0 | 2 | 2 | 3 | 8 | 9 | 9 | 9 |

Level 6 holds 60% of pixels, so it is moved far (6 → 8). Empty levels 0–2 stay empty.

**Problems:** amplifies noise (stretches flat regions most); global — one transfer function for the whole image. **CLAHE** fixes both: equalise in local tiles, limit the slope of the transfer function, interpolate between tiles.

### Look-Up Tables (LUTs)

Only 256 possible inputs for an 8-bit image. Evaluate T once per grey level → store 256 values → replace every pixel via one table look-up. Any point operation, regardless of formula complexity, costs one pass. Also enables pseudo-colour by mapping each grey value to (r, g, b).

### Critical ML Pipeline Rule

> **Fix transform parameters on the training set. Apply the identical transform at inference time.**

A per-image normalisation (e.g., stretch each image to [0, 1] based on its own min/max) makes two images incomparable — this is a subtle but serious bug that will not appear in the loss curve.

---

## 4. Part II — Neighbourhood Operations

A **neighbourhood operation** computes the new pixel value from the pixel and its surrounding neighbours. This is where spatial structure enters.

### Edge Types in Images

| Edge type | Profile | Physical cause |
|-----------|---------|----------------|
| Step | sharp jump | ideal boundary |
| Ramp | gradual rise | blurred/diffracted boundary |
| Line | thin spike | thin structure: vessel, wire |
| Roof | triangular peak | thin structure, blurred |

Optics and sampling turn every step into a ramp — which is good news: a ramp has a well-defined slope that can be measured.

### Discrete Derivatives

**Forward difference:**
```
f′(m) = f(m+1) − f(m)       ← answer sits half a pixel right of position m
```

**Central difference (preferred):**
```
f′(m) = ( f(m+1) − f(m−1) ) / 2    ← answer sits exactly on position m
```

Use central difference for real filters: no half-pixel shift.

### The Gradient

```
∇f = ( ∂f/∂m , ∂f/∂n )             — one partial derivative per axis
|∇f| = √( f_m² + f_n² )            — edge strength (rotation invariant)
∠∇f = arctan( f_m / f_n )          — edge direction (perpendicular to the edge)
```

### Why Smooth Before Differentiating

Differentiation is a **high-pass operation** — it amplifies noise as much as edges. Always smooth first.

```
Acquire → Smooth (Gaussian, σ controls smallest structure) → Differentiate → Combine → Threshold
```

---

## 5. Convolution

The fundamental operation underlying all neighbourhood filters:

```
convolution:   g(m,n) = ΣΣ f(m−i, n−j) · h(i, j)    ← flips kernel 180°
correlation:   g(m,n) = ΣΣ f(m+i, n+j) · h(i, j)    ← no flip
```

- Only convolution is commutative and associative — theory uses it for this reason
- For **symmetric kernels**, convolution and correlation give identical results
- Deep learning says "convolution" but implements correlation — for learned weights it makes no difference

### Border Strategies

When the kernel window hangs over the image edge, the missing pixels must be invented:

| Strategy | Advantage | Cost |
|----------|-----------|------|
| **Zero padding** | Fast; the DL standard | Creates an artificial dark border artefact |
| **Replicate / mirror** | No artificial edge; usually best for CV | Invents structure that was not measured |
| **Wrap around** | Consistent with Fourier transform | Connects opposite edges of the image |
| **Crop** | No invented data at all | Output is smaller than input |

### Properties of Convolution

```
Commutative:      f∗h = h∗f
Associative:      (f∗h₁)∗h₂ = f∗(h₁∗h₂)    ← cascading
Distributive:     f∗h₁ + f∗h₂ = f∗(h₁+h₂)
Neutral element:  f∗δ = f
```

**Practical consequences:**
- **Cascading Gaussians:** two Gaussians with σ₁ and σ₂ equal one Gaussian with `σ = √(σ₁² + σ₂²)` — smoothing twice costs no more than smoothing once
- **Sobel = one kernel:** smooth-then-differentiate is equivalent to a single convolution
- **Separability:** a 2D kernel that factorises into two 1D kernels → k² multiplications per pixel becomes 2k (3×3: 9 → 6; 9×9: 81 → 18)

---

## 6. Smoothing Filters

| Filter | Kernel | Behaviour | Use it for | Watch out for |
|--------|--------|-----------|------------|---------------|
| **Mean** | [[1,1,1],[1,1,1],[1,1,1]] × 1/9 | linear, separable | additive noise, speed | blurs edges; square artefacts |
| **Gaussian** | [[1,2,1],[2,4,2],[1,2,1]] × 1/16 | linear, separable, cascadable | additive noise — the default | blurs edges |
| **Median** | sort neighbourhood, take middle | rank filter (non-linear) | impulse/salt-and-pepper noise, edge preservation | cannot cascade; erases thin lines |

**Binomial kernels:** the [1,2,1]ᵀ kernel comes from Pascal's triangle (row 3). Outer product of two 1D kernels gives the 2D kernel — integer arithmetic (division by a power of two = bit shift).

---

## 7. Edge Filters

### Roberts (1965)

```
0  -1        -1   0
1   0          0   1
```

2×2, asymmetric; result lands half a pixel off-grid; extremely noise sensitive — no averaging.

### Prewitt

```
-1  0  1
-1  0  1
-1  0  1
```

Symmetric 3×3; central difference along the derivative axis; averages over three rows without weighting.

### Sobel

```
∂f/∂n  (vertical edges):     ∂f/∂m  (horizontal edges):
-1  0  1                      -1  -2  -1
-2  0  2                       0   0   0
-1  0  1                       1   2   1
```

**Sobel = smoother ⊗ derivative:**
- Column `[1, 2, 1]ᵀ` is a binomial smoother
- Row `[−1, 0, 1]` is a central difference
- Their outer product is the Sobel kernel — one convolution instead of two steps

Properties: no half-pixel shift; far more robust than Roberts; `|∇f|` = rotation-invariant edge magnitude.

### From Magnitude to Edge Map — Canny

A single threshold produces either too much noise (low threshold) or broken edges (high threshold). **Canny** solves this with:
1. Gaussian smoothing
2. Sobel gradient magnitude
3. **Non-maximum suppression** — thin the edge to one pixel width
4. **Hysteresis thresholding** — two thresholds: high to start an edge, low to continue it

---

## 8. Designed vs Learned Kernels

This is the key bridge from classical image processing to deep learning:

| Aspect | Classical CV | Convolutional Network |
|--------|-------------|----------------------|
| Source of numbers | Chosen by hand from calculus | Learned by backpropagation from data |
| Number of kernels | One per purpose | Many per layer |
| Interpretability | Explicit — you know what it detects | Emerges from data |
| Data requirement | Works immediately | Needs sufficient training data |
| Adaptability | Fixed | Adapts to your specific images |

**Same operation.** When you inspect the first layer of a trained network and find edge-like and blob-like filters — you have built those by hand.

The convolutional layer is exactly `g(m,n) = ΣΣ f(m−i, n−j) · h(i, j)`, with the only difference being that `h` is learned rather than specified. Everything about kernels, border strategies, separability, and cascading applies equally to CNN layers.

---

## Related Concepts

- [[concepts/neural-networks-linear-models|Neural Networks & Linear Models]] — CNN architecture, backpropagation, ReLU
- [[concepts/ml-evaluation-metrics|ML Evaluation Metrics]] — evaluation of segmentation and detection models
- [[concepts/medmnist-v2-datasets|MedMNIST v2 Datasets]] — practical dataset pre-processing considerations
- [[concepts/ai-in-medicine|AI in Medicine]] — medical image modalities and applications
