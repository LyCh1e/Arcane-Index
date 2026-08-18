---
type: source
status: ingested
title: "ML Summer School — Lecture 4b: Operations on Images"
source_file: raw/Machine_Learning_Lec4b.md
ingested: 2026-08-18
tags: [source, machine-learning, image-processing, convolution, edge-detection]
---

# Source: ML Summer School — Lecture 4b

**File:** `raw/Machine_Learning_Lec4b.md`
**Lecturer:** Tobias Rueckert, M.Sc. — OTH Regensburg / TU Munich / AKTORmed
**Course:** International Summer School 2026 — Trustworthy AI: ML Meets Blockchain
**Topic:** Operations on Images (48 slides)

---

## What This Lecture Covers

Two families of image operations: **point operations** (histogram, linear scaling, stretching, equalisation, LUTs) and **neighbourhood operations** (derivatives, gradient, convolution, smoothing, edge filters). The lecture closes with the connection between classical designed kernels and learned CNN kernels.

---

## Key Ideas Extracted

### Part I — Point Operations

- `f_transformed(m,n) = T_g(f(m,n))` — position never enters; same input always → same output
- **Histogram:** `a_g = pixel count; p_f(g) = a_g/(M·N)` — diagnoses: under-exposed, over-exposed, low-contrast, clipped
- **Clipping:** irreversible; silent; practical rule: compute in float, clip once at the end
- **Linear scaling:** `f_scale = (f + c₁)·c₂` — c₁=brightness offset, c₂=contrast gain
- **Histogram stretching:** `T(g) = (g−g_min)/(g_max−g_min)×(G−1)` — use 1%–99% percentiles, not extreme values; equivalent to min-max normalisation on network inputs
- **Histogram equalisation:** `T_equal(g) = round((G−1)·h_f(g))` where h_f = cumulative histogram; amplifies noise; global only → CLAHE fixes both
- **LUTs:** only 256 possible inputs; evaluate T once, store 256 values, replace every pixel in one pass
- **Critical ML pipeline rule:** fix transform parameters on the training set; apply identical transform at inference — per-image transforms make images incomparable

### Part II — Neighbourhood Operations

- **Four edge types:** step (sharp jump), ramp (blurred step), line (thin spike), roof (triangular peak)
- **Forward difference:** `f′(m) = f(m+1) − f(m)` — answer sits half a pixel to the right
- **Central difference:** `f′(m) = (f(m+1) − f(m−1)) / 2` — sits exactly on the pixel; preferred
- **Gradient:** `∇f = (∂f/∂m, ∂f/∂n)`; magnitude `|∇f| = √(f_m² + f_n²)`; direction `∠∇f = arctan(f_m/f_n)`
- **Why smooth first:** differentiation is a high-pass operation; it amplifies noise as much as signal

### Convolution

```
convolution:   g(m,n) = ΣΣ f(m−i, n−j) · h(i, j)
correlation:   g(m,n) = ΣΣ f(m+i, n+j) · h(i, j)
```

- Convolution flips the kernel 180° before sliding — only convolution is commutative and associative
- Deep learning says "convolution" but implements correlation; for symmetric kernels: identical
- **Border strategies:** zero padding (DL standard; dark edge artefact), replicate/mirror (best for CV), wrap (Fourier-consistent), crop (smaller output)
- **Properties:** commutative, associative (cascading!), distributive, neutral element (δ)
- **Cascading Gaussians:** `σ = √(σ₁² + σ₂²)` — smoothing twice = smoothing once with combined σ
- **Separability:** k²→2k multiplications; 3×3 kernel: 9 → 6 per pixel

### Smoothing Filters

| Filter | Kernel | Type | Good for | Watch out for |
|--------|--------|------|----------|---------------|
| Mean | [[1,1,1],[1,1,1],[1,1,1]]×1/9 | linear, separable | additive noise, speed | blurs edges; square artefacts |
| Gaussian | [[1,2,1],[2,4,2],[1,2,1]]×1/16 | linear, separable, cascadable | additive noise — the default | blurs edges |
| Median | sort, take middle | rank filter (non-linear) | impulse/salt-and-pepper noise | cannot cascade; erases thin lines |

### Edge Filters

| Filter | Kernel | Properties |
|--------|--------|------------|
| Roberts (1965) | 2×2 diagonal | asymmetric; half-pixel shift; extremely noise-sensitive |
| Prewitt | [−1,0,1] columns × 3 rows | symmetric 3×3; averages without weighting |
| Sobel | [1,2,1]ᵀ × [−1,0,1] | smoother ⊗ derivative; no half-pixel shift; rotation invariant magnitude |

- Sobel `∂f/∂n` → responds to vertical edges; `∂f/∂m` → responds to horizontal edges; `|∇f|` combines both
- **Canny:** two thresholds + non-maximum suppression → thin, connected edges; the standard answer

### Designed vs Learned Kernels

The key insight: **a CNN convolutional layer performs exactly this operation**. Classical CV chooses the kernel numbers by hand (from calculus). Backpropagation chooses them from a loss function. Same operation — different source of numbers.

---

## Concept Pages Generated

- [[concepts/digital-image-processing|Digital Image Processing]] — covers both Lec 4a and Lec 4b content
