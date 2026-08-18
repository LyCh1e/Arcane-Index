---
type: source
status: ingested
title: "ML Summer School — Lecture 4a: Digital Images"
source_file: raw/Machine_Learning_Lec4a.md
ingested: 2026-08-18
tags: [source, machine-learning, image-processing, computer-vision]
---

# Source: ML Summer School — Lecture 4a

**File:** `raw/Machine_Learning_Lec4a.md`
**Lecturer:** Tobias Rueckert, M.Sc. — OTH Regensburg / TU Munich / AKTORmed
**Course:** International Summer School 2026 — Trustworthy AI: ML Meets Blockchain
**Topic:** Digital Images (14 slides)

---

## What This Lecture Covers

Foundations of digital image representation: the three levels of image understanding, grayscale and colour image models, and the HSV colour space with its practical advantages over RGB.

---

## Key Ideas Extracted

### Three Levels of Image Understanding
- **Image editing** — Photoshop-style manipulation
- **Image processing** — data analysis; what can be seen in the image
- **Computer vision** — use data to make decisions (classify, detect, segment)

### Grayscale Image Models
- **Ideal image:** continuous function f: D_2D → ℝ, (x,y) ↦ f(x,y); origin **bottom-left**
- **Digital image:** discrete function f: M×N → G where M={0,…,M−1}, N={0,…,N−1}, G={0,…,G−1}; origin **upper-left**
- 8-bit image: G = 256 levels

### RGB Colour Space
- Colour image: vector-valued function f: D → ℝ³ — stacking three channel images (f_R, f_G, f_B)
- Additive mixing: red + green + blue → perceived colour
- Limitation: brightness changes affect all three channels simultaneously

### HSV Colour Space
| Component | Meaning | Range |
|-----------|---------|-------|
| Hue | angle on the colour wheel | 0°=red, 120°=green, 240°=blue |
| Saturation | purity of colour | 0%=neutral grey, 100%=pure colour |
| Value | brightness | 0%=black, 100%=full brightness |

**Advantages:**
- Separates colour identity (H, S) from intensity (V)
- Under multiplicative illumination change: H and S are invariant, only V scales
- Enables robust colour-based thresholding on H channel alone

**Limitations:**
- Distances in HSV ≠ perceived colour differences
- V is not perceived brightness (yellow and blue can both give V = 100%)
- H is an angle (0° = 360°) — no straightforward averaging or filtering
- H is meaningless for grey or dark pixels — always check S/V threshold first

---

## Concept Pages Generated

- [[concepts/digital-image-processing|Digital Image Processing]] — covers Lec 4a (image representations) and Lec 4b (operations)
