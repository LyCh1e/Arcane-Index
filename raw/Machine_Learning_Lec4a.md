# International Summer School: Trustworthy AI – Machine Learning Meets Blockchain

**Microcredential 2: Machine Learning**
**Part 4a: Digital Images**

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

*International Summer School 2026 | Machine Learning*

---

## Slide 2: Digital Images — Table of Contents

1. **Scope and Objectives**
   1.1 Scope
   1.2 Objectives
2. **Digital Images**
   2.1 Grayscale Images
   2.2 Color Images

---

## Slide 3: Digital Images — Scope and Objectives - Scope

*(Figure: a laparoscopic surgery image shown transformed six ways in a 3×2 grid: original colour image, a denoised/grey version, a frequency-domain (Fourier magnitude) view, a version with tracked/highlighted surgical tool trajectories overlaid, an intensity histogram plot, and two further grayscale/noisy variants.)*

- **Image Editing** (Photoshop, threshold segmentation, …)
  vs.
- **Image Processing** (Data analysis, what can be seen in the image)
  vs.
- **Computer Vision** (Use data, make decisions)

---

## Slide 4: Digital Images — Scope and Objectives - Objectives

*(Figure: one endoscopic frame linked by arrows to three downstream tasks:*
- **Segmentation** — coloured overlays (orange, pink, green) marking anatomical/instrument regions
- **Keypoint Estimation** — coloured points and connecting lines marking landmark locations
- **Phase Recognition** — a coloured timeline/status bar labelled with surgical phase abbreviations (e.g. "P", "CTD", "CX", "GP", "CIC", "GR") and current phase "Preparation")

---

## Slide 5: Digital Images — Scope and Objectives - Objectives

*(Figure: pipeline diagram — an Image feeds into "Feature Extraction", which branches into three downstream tasks: Classification, Object Detection, Segmentation.)*

---

## Slide 6: Digital Images — Grayscale Images

**Ideal image**

A continuous function f : D → ℝ, mapping from a spatial domain into an intensity range (set of real numbers):

```
f : D_2D → ℝ,  (x, y) ↦ f(x, y)
```

*(Figure: a grayscale gradient square plotted against x and y axes, and a corresponding 3D surface plot of f(x,y) showing intensity as height over the (x,y) plane.)*

**Origin: bottom left**

---

## Slide 7: Digital Images — Digital Image (Discrete Function)

**Digital image**

A 2D discrete function f : M × N → G, with:

```
M = {0, 1, …, M − 1}
N = {0, 1, …, N − 1}
G = {0, 1, …, G − 1}
```

*(Figure: a pixelated grayscale grid plotted against m (horizontal) and n (vertical) axes, and a corresponding 3D surface/mesh plot of f(m,n).)*

**Origin: upper left**

---

## Slide 8: Digital Images — Example: Laparoscopy

*(Figure: a laparoscopic image showing surgical instruments, with three bullet points listing the RGB colour channels.)*

- Red
- Green
- Blue

---

## Slide 9: Digital Images — Example: Laparoscopy (Grayscale)

*(Figure: the same laparoscopic image shown alongside its grayscale conversion, with an arrow between them.)*

- Red
- Green → **Grayscale** → How?
- Blue

---

## Slide 10: Digital Images — Color images – RGB space

- A colour image is a vector-valued function f: D → ℝ³ obtained by stacking the three channel images f_R, f_G, f_B.
- The perceived colour results from additive mixing of three primaries.

*(Figure: the laparoscopic image decomposed into its three colour channels shown as tinted images — Red (shown in red tint), Green (shown in green tint), Blue (shown in blue tint).)*

---

## Slide 11: Digital Images — Color images – RGB space (grayscale channels)

- A colour image is a vector-valued function f: D → ℝ³ obtained by stacking the three channel images f_R, f_G, f_B.
- The perceived colour results from additive mixing of three primaries.

*(Figure: the same three RGB channels, this time shown as plain grayscale intensity images — Red, Green, Blue — showing the raw channel intensities without colour tint.)*

---

## Slide 12: Digital Images — Color images – HSV space

**HSV: three coordinates**

*(Figure: an HSV colour cone/cylinder diagram, with H as the angular position around the cone, S as the radial distance from the centre axis, and V as the vertical height.)*

- **Hue:** angle on the colour wheel: 0° red, 120° green, 240° blue
- **Saturation:** 0% neutral grey, 100% pure colour
- **Value:** 0% black, 100% full brightness

---

## Slide 13: Digital Images — Color images – HSV space (Why HSV?)

**Why HSV?**
- RGB axes are entangled: changing brightness changes all three channels
- HSV separates color value (H, S) from intensity (V)
- Under multiplicative illumination change: H, S invariant, only V scales → robust colour-based thresholding on H
- Intuitive axes: colour pickers, selective hue/saturation editing

**Limitations**
- Distances in HSV do not reflect perceived colour
- V is not perceived brightness, but strictly calculated (yellow and blue both give V = 100%)
- H is an angle: 0° = 360°, so no straightforward averaging or filtering
- For grey or dark pixels H is essentially meaningless → always check an S/V threshold

---

## Slide 14: Contact

**www.re-mic.de**

**OTH REGENSBURG**
- Phone: +49 941 943 1314
- Address: Galgenbergstraße 32, 93053 Regensburg
- Email: tobias.rueckert@oth-regensburg.de

**Tobias Rueckert, M. Sc.**
- Regensburg Medical Image Computing (ReMIC)
- Regensburg Center for Artificial Intelligence (RCAI)
- Regensburg Center of Health Sciences and Technology (RCHST)
- Regensburg Center of Biomedical Engineering (RCBE)
