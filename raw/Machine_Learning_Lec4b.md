# International Summer School: Trustworthy AI – Machine Learning Meets Blockchain

**Microcredential 2: Machine Learning**
**Part 4b: Operations on Images**

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

*International Summer School 2026 | Machine Learning*

---

## Slide 2: Where we are going

*Two families of operations — and where they lead*

**Part I · Point operations** — The new value of a pixel depends only on its own old value.
- Histogram — what is in the image
- Linear scaling — brightness and contrast
- Stretching — use the whole range
- Equalisation — redistribute the levels
- Look-up tables — do it in one pass

**Part II · Neighbourhood operations** — The new value of a pixel depends on its neighbours as well.
- Derivatives — where does intensity change
- Gradient — how much, and in which direction
- Convolution — the machinery behind all of it
- Smoothing — mean, Gaussian, median
- Edge filters — Roberts, Prewitt, Sobel

> The punchline of Part II: a convolutional layer performs exactly the operation we build by hand today. The only difference is that we choose the numbers in the kernel and the network learns them.

---

## Slide 3: Why we start here

*Where these operations sit in a learning pipeline*

```
Acquire (sensor, optics, quantisation)
  → Part I: Enhance (make the signal visible and comparable)
  → Part II: Extract features (edges, textures, regions)
  → the model: Decide (classify, segment, track)
```

> A convolutional network replaces step 3 by something it learns from data — but it does not replace the question.
> — If the contrast operation in step 2 destroys information, no network can recover it.
> — If you know what a hand-designed edge filter responds to, you can read what a first conv layer has learned.

---

## Slide 4: Part I — Histograms and point operations

*One pixel at a time*

Six steps — each one a decision you will have to defend later.

01. The grey-value image
02. The histogram
03. Linear scaling
04. Stretching
05. Equalisation
06. Look-up tables

Goal: given an image, know which operation to apply — and what each one costs you.

---

## Slide 5: A grey-value image is a matrix

*Everything that follows is arithmetic on these numbers*

*(Figure: a grey-value fundus photograph, a zoomed 72×72 pixel detail box, and the raw pixel data shown as a grid of integer values (e.g. row of values like 81, 93, 87, 92, 80, 89, 79, 75, 73, 72 ...). One region annotated: "81 → 115 over four pixels — that is an edge".)*

```
f(m, n)  with m = 0 … M−1, n = 0 … N−1  ·  grey values g ∈ {0, …, G−1}  ·  8 bit → G = 256 levels
```

Fundus photograph: M. Häggström, WikiJournal of Medicine (2014), CC0 · via scikit-image

---

## Slide 6: The histogram

*How often does each grey value occur?*

```
a_g = number of pixels with grey value g
p_f(g) = a_g / (M · N)   — the relative histogram
```

- 0 ≤ p(g) ≤ 1 and Σ p(g) = 1 — a probability distribution
- cost: one pass over the image, one array of 256 counters

---

## Slide 7: Reading a histogram

*Four acquisitions of the same scene — four diagnoses*

*(Figure: four grayscale fundus images with their histograms beneath —*
- **under-exposed**: mass at the left end
- **over-exposed**: mass at the right end
- **low contrast**: narrow peak, range unused
- **over-driven**: clipped at both ends)

> Read it as a checklist: where is the mass, how wide is it, and is anything piled up against 0 or 255? Piles at the ends mean clipping — that information is already lost.

---

## Slide 8: What the histogram cannot know

*It counts grey values and forgets where they were*

**Same histogram, different image**
Image B contains exactly the pixels of image A in a random order. Their histograms are bit-for-bit identical.

- Consequence: any operation that looks only at the histogram cannot tell A from B.
- Consequence: such an operation can never blur, sharpen or find an edge.
- Therefore: spatial structure needs neighbourhood operations — Part II.

---

## Slide 9: Point operations

*One transfer function, applied to every pixel independently*

```
f_transformed(m, n) = T_g( f(m, n) ) = g★
```

- Position never enters the formula. The same input value always gives the same output value.
- T maps the range onto itself. G → G★, both {0, …, G−1}.
- The histogram changes, the geometry does not. No pixel moves.
- Only 256 possible inputs. Compute the answers once, store them in a table.

---

## Slide 10: The two edges of the range

*What happens when the result leaves [0, G−1]*

**Clipping is not an error — it is a decision**
Values below 0 are stored as 0, values above G−1 as G−1. Different inputs collapse onto the same output.

- Irreversible. Once clipped, the original value is gone.
- Silent. The image still looks plausible; only the histogram shows the spike at the end.
- Practical rule. Compute in float, clip once at the very end, and check the histogram afterwards.

---

## Slide 11: Linear scaling

*The simplest useful transfer function*

```
f_scale(m, n) = ( f(m, n) + c1 ) · c2
```

- **c₁ · offset** — Shifts the whole histogram left or right. Perceived as brightness. Distances between grey values are unchanged.
- **c₂ · gain** — Scales the distances between grey values. Perceived as contrast. Values far from the origin move most.

---

## Slide 12: Linear scaling in practice

*Shape survives, position and width do not*

*(Figure: a fundus photograph with histogram shown three ways — original; c₁=+55, c₂=1 (histogram shifted); c₁=0, c₂=2.2 (histogram widened + clipped).)*

> Watch the right-hand histogram: raising the gain pushes values past 255. The peak at the right edge is clipped contrast, not detail.

---

## Slide 13: Histogram stretching

*Map the occupied range onto the full range*

```
for g < g_min:            → 0
for g_min ≤ g ≤ g_max:    → (g − g_min) · (G−1) / (g_max − g_min)
for g > g_max:             → G − 1
```

- It is linear scaling. With c₁ = −g_min and c₂ = (G−1)/(g_max − g_min).
- Two numbers decide everything. How you estimate g_min and g_max is the whole design question.
- Also called min–max normalisation. The same operation you apply to network inputs.

---

## Slide 14: Stretching: what you gain

*Visibility — not information*

**61 levels before, 61 levels after**
The transformation is one-to-one, so nothing is added and nothing is destroyed. The differences simply become large enough for the eye — and for a fixed threshold — to notice.

- Invertible up to rounding: the gaps between used levels stay empty.
- Comparable across acquisitions — provided you use the same g_min and g_max.
- Careful with per-image parameters: two images then receive two different transformations.

---

## Slide 15: Why min and max are a bad choice

*One hot pixel decides the whole transformation*

*(Figure: a fundus photograph shown three ways with histograms —*
- **original**: range [30, 231], but 99% of pixels in [49, 128]
- **min-max stretch**: outliers eat most of the range
- **1% – 99% stretch**: clip 1% per side → real contrast gain)

> Use percentiles instead: estimate g_min and g_max as the 1% and 99% quantiles. A few saturated pixels or a specular highlight then no longer control the result.

---

## Slide 16: When stretching is not enough

*The range is fully used, yet the values crowd together*

**The idea**
Pull crowded grey levels apart and squeeze empty ones together, so that every level carries roughly the same number of pixels.

**The tool**
The cumulative histogram already measures the crowding: it is steep where pixels pile up. So use it as the transfer function.

---

## Slide 17: Histogram equalisation

*The cumulative histogram becomes the transfer function*

```
T_equal(g) = round( (G − 1) · h_f(g) )    with    h_f(g) = Σ_{k ≤ g} p_f(k)
```

**Worked example — a tiny 10-pixel image with G = 10 grey levels**

| g | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| a_g counts | 0 | 0 | 0 | 2 | 0 | 1 | 6 | 1 | 0 | 0 |
| p_f(g) relative | 0 | 0 | 0 | .2 | 0 | .1 | .6 | .1 | 0 | 0 |
| h_f(g) cumulative | 0 | 0 | 0 | .2 | .2 | .3 | .9 | 1.0 | 1.0 | 1.0 |
| T_equal(g) → new value | 0 | 0 | 0 | 2 | 2 | 3 | 8 | 9 | 9 | 9 |

> Read the last two rows together: level 6 holds 60% of the pixels, so it is moved far (6 → 8); the empty levels 0–2 are mapped onto each other and stay empty.

---

## Slide 18: Equalisation: result

*Orange curve: the cumulative histogram after the transform*

*(Figure: a fundus photograph and histogram shown three ways — original; stretched (1–99%); equalised — with the equalised version's cumulative histogram plotted as a near-straight orange line.)*

> A straight cumulative histogram means a uniform distribution. Exactly uniform is impossible: whole levels are merged, never split.

---

## Slide 19: Where equalisation goes wrong

*It maximises contrast — including the contrast of the noise*

- **Noise is amplified.** Flat regions get stretched the most, because that is where most pixels sit.
- **It is global.** One transfer function for the whole image, so a locally dark region stays dark.
- **CLAHE fixes both.** Equalise in tiles, limit the slope of the transfer function, interpolate between tiles.

---

## Slide 20: Look-up tables

*Any point operation costs one table and one pass*

**Why it is fast**
There are only G possible inputs. Evaluate T once per level, store 256 bytes, then replace every pixel by a table look-up.

**Same mechanism, colour output**
Map each grey value to an (r, g, b) triple and you have pseudo-colour. The data never changes — only the table.

---

## Slide 21: Part I — which operation, when?

*Three tools, three different jobs*

| Operation | Use it when | Typical purpose | Watch out for |
|---|---|---|---|
| Linear scaling | you know how much to shift or scale | brightness / contrast by a fixed amount | clipping at both ends |
| Stretching | the image uses only part of the range | make acquisitions comparable | outliers decide g_min and g_max — use percentiles |
| Equalisation | the range is used but values crowd together | reveal detail in a dense region | amplifies noise; global by nature — consider CLAHE |

> One rule for all three: in a machine-learning pipeline, fix the parameters on the training set and apply the identical transform at inference time. A per-image transform makes two images incomparable — and that is a bug you will not see in the loss curve.

---

## Slide 22: Part II — Convolution and edge detection

*A pixel and its neighbours*

From "what is an edge" to a working edge detector — in six steps.

01. What is an edge?
02. Derivatives
03. The gradient
04. Convolution
05. Smoothing
06. Edge filters

> Everything in this half is one operation with different numbers in the kernel.

---

## Slide 23: What is an edge?

*Four idealised shapes — real images mix them*

*(Figure: four idealised 1-D intensity profiles plotted against position — step edge (sharp jump), ramp edge (gradual rise, "boundary after blurring"), line (thin spike, "thin structure: vessel, wire"), roof (triangular peak, "thin structure, blurred").)*

> Optics and sampling turn every step into a ramp. That is good news: a ramp has a well-defined slope, and a slope is something we can measure. A perfect step would have an infinite derivative.

---

## Slide 24: Edges in two dimensions

*An edge now has a strength and a direction*

**Two questions now**
In 1-D we only asked "where". In 2-D we must also ask "which way does the intensity change".

- **Object boundary** — the slope we want
- **Specular highlight** — a steep slope that is not a boundary
- **Shadow** — a boundary that is not an object
- **Noise** — steep everywhere, meaningful nowhere

---

## Slide 25: One line through the image

*An image row is a 1-D signal, so 1-D reasoning applies*

*(Figure: a fundus image with a horizontal scan line drawn across it, and the corresponding 1-D intensity signal plotted below, with markers at each vessel crossing.)*

**What we are looking for**
Positions where the signal changes quickly — not positions where it is bright or dark.

**Why that is useful**
Brightness depends on illumination. A change in brightness depends on the object.

---

## Slide 26: Derivatives locate the edge

*Extremum, or zero crossing*

**First derivative f′**
Large where the intensity changes. The edge sits at the extremum — so we look for maxima of |f′|.

**Second derivative f″**
Zero exactly at the edge. Sub-pixel accurate, but it differentiates twice and therefore doubles the noise problem.

> In practice: first derivative for detection, second derivative when you need precise localisation.

---

## Slide 27: The discrete derivative

*There is no limit to take — the pixel grid is the smallest step*

```
f′(m) = [ f(m+1) − f(m) ] / 1 = f(m+1) − f(m)     because Δm = 1
```

- **Forward difference** — Two pixels, one subtraction — but the answer belongs half a pixel to the right of where we stored it.
- **Central difference** — Three pixels, still one subtraction. The answer sits exactly on the pixel — which is why real filters use it.

---

## Slide 28: The gradient

*Two derivatives per pixel — strength and direction*

*(Figure: an image detail of a vessel, its gradient magnitude |∇f| (shown as bright edges), and gradient direction ∠∇f (shown as arrows perpendicular to the edges).)*

```
∇f = ( ∂f/∂m , ∂f/∂n )              — one partial derivative per axis
|∇f| = √( f_m² + f_n² )             — how strong is the edge
∠∇f = arctan( f_m / f_n )           — perpendicular to the edge
```

---

## Slide 29: Why we smooth before we differentiate

*Differentiation is a high-pass operation — and so is noise*

*(Figure: three signals — clean signal, +little noise (σ=4), +much noise (σ=14) — each with its 1st derivative plotted below, showing the derivative becoming progressively noisier.)*

> the derivative amplifies noise — smooth first, then differentiate

**How much smoothing?** σ sets the smallest structure that survives. Too little and noise wins; too much and the edge you are looking for disappears with it.

---

## Slide 30: Convolution

*One weighted sum per pixel, then move the window*

- **The kernel is the algorithm.** Change the nine numbers and the same code smooths or finds edges.
- **Pixels are independent.** Which is why this maps perfectly onto a GPU.
- **You need a second buffer.** Writing results back into the input would corrupt the neighbourhood of the next pixel.

---

## Slide 31: Correlation or convolution?

*The difference is one sign — and one piece of vocabulary*

```
correlation:   g(m,n) = ΣΣ f(m+i, n+j) · h(i, j)
convolution:   g(m,n) = ΣΣ f(m−i, n−j) · h(i, j)
```

- Convolution flips the kernel by 180° before it slides.
- Only convolution is associative and commutative — that is why the theory uses it.
- For symmetric kernels the two give identical results.
- Deep learning says "convolution" but implements correlation. It makes no difference: the weights are learned either way.

---

## Slide 32: The border problem

*The window hangs over the edge — you must invent data*

| Strategy | Advantage | Cost |
|---|---|---|
| Zero padding | fast, and standard in deep learning | creates an artificial dark edge |
| Replicate / mirror | no artificial edge, usually the best choice | invents structure that was never measured |
| Wrap around | consistent with the Fourier transform | connects opposite sides of the image |
| Crop the result | no invented data at all | the output is smaller than the input |

---

## Slide 33: Properties of convolution

*Four identities that buy you real speed*

```
Commutative:      f∗h = h∗f
Associative:      (f∗h₁)∗h₂ = f∗(h₁∗h₂)
Distributive:     f∗h₁ + f∗h₂ = f∗(h₁+h₂)
Neutral element:  f∗δ = f
```

**Why this is not just algebra**
- Cascading. Two Gaussians with σ₁ and σ₂ equal one Gaussian with σ = √(σ₁² + σ₂²). Smoothing twice is smoothing once.
- Pre-combining. Smoothing then differentiating equals convolving with one kernel — that is exactly what Sobel is.
- Separability. A 2-D kernel that factorises into two 1-D kernels turns k² multiplications into 2k per pixel.

---

## Slide 34: Smoothing 1 — the mean filter

*Replace every pixel by the average of its neighbourhood*

```
1  1  1
1  1  1    × 1/9
1  1  1
```

- Keeps the mean of the image and reduces the variance of additive noise by a factor of k².
- Blurs edges as much as noise — it cannot tell them apart.
- Cheap and separable but leaves visible square artefacts on point-like structures.

---

## Slide 35: Smoothing 2 — the Gaussian filter

*Weight the neighbours by distance instead of equally*

```
1  2  1
2  4  2    × 1/16
1  2  1
```

- One parameter, σ. The kernel size follows from it — about 6σ, rounded up to an odd number.
- Optimal for additive white noise and the only kernel that introduces no new structure at any scale.
- Separable and cascadable — see the previous slide.

---

## Slide 36: Binomial kernels and separability

*Where 1 2 1 comes from, and why it is cheap*

*(Figure: Pascal's triangle showing rows 1; 1,1; 1,2,1 (3×1); 1,3,3,1; 1,4,6,4,1 (5×1); and a diagram showing the 2-D 3×3 binomial kernel built as the outer product of two 1-D [1,2,1] kernels: [1,2,1]ᵀ × [1,2,1] = [[1,2,1],[2,4,2],[1,2,1]].)*

**Integer arithmetic**
Binomial coefficients approximate the Gaussian and divide by a power of two — a bit shift instead of a division.

**Two passes, one result**
Filter every row with 1 2 1, then every column. Identical output, a fraction of the work.

*separable: two 1-D passes instead of one 2-D pass — k² multiplications per pixel → 2k (for k=9: 81 → 18)*

---

## Slide 37: Smoothing 3 — the median filter

*Sort the neighbourhood and take the middle value*

**Not a convolution**
There are no weights and no sum, so none of the four identities from before apply. It is a rank filter.

- Removes outliers completely — salt-and-pepper noise, dead pixels, cosmic rays.
- Preserves step edges because a majority decides, not an average.
- More expensive (sorting) and it can erase thin lines that are in the minority.

---

## Slide 38: Three filters, one noisy image

*Gaussian noise and salt-and-pepper noise at the same time*

| Filter | Use it for | Nature | Cost |
|---|---|---|---|
| Mean | additive noise, when speed matters | linear, separable | blurs edges, square artefacts |
| Gaussian | additive noise — the default choice | linear, separable, cascadable | blurs edges |
| Median | outliers and impulse noise | non-linear, edge preserving | no algebra, slower, erases thin lines |

---

## Slide 39: Edge filters 1 — asymmetric differences

*The smallest possible derivative kernels (Roberts, 1965)*

```
forward, along n:    0  -1        diag 1:  -1   0        diag 2:   0  -1
                      1   0                  0   1                -1   0
```

- Two pixels are enough to estimate a derivative — and that is the problem.
- The answer lands between the pixels, so every edge is shifted by half a pixel.
- Extremely noise sensitive: no averaging happens at all.

---

## Slide 40: Edge filters 2 — symmetric differences

*Prewitt averages, Sobel weights the average*

```
Prewitt:          Sobel:
-1  0  1          -1  0  1
-1  0  1          -2  0  2
-1  0  1          -1  0  1
```

**Sobel = smoothing ⊗ derivative**
The column [1 2 1]ᵀ is a binomial smoother, the row [−1 0 1] is a central difference. Their outer product is the Sobel kernel — one convolution instead of two.

- Central difference: the answer sits on the pixel, no half-pixel shift.
- Averaging across the edge makes it far more robust than Roberts — at the price of slightly thicker edges.

> Rotate the kernel by 90° and you get the other partial derivative.
> ∂f/∂n responds to vertical edges · ∂f/∂m responds to horizontal edges · |∇f| combines both and is rotation invariant

---

## Slide 41: Sobel on a real image

*Two directions, one invariant magnitude*

*(Figure: a fundus photograph shown four ways — original; ∂f/∂n (vertical edges); ∂f/∂m (horizontal edges); |∇f| (all edges, combined magnitude).)*

Fundus photograph: M. Häggström, WikiJournal of Medicine (2014), CC0 · via scikit-image

> Mid-grey means zero. Derivatives are signed, so the two middle images are shown with 0 mapped to 128 — bright is a rise, dark is a fall.

---

## Slide 42: From magnitude to an edge map

*One threshold — and no value is the right one everywhere*

*(Figure: a vessel gradient-magnitude image |∇f| thresholded at three levels — T=0.04 (too low: noise survives), T=0.14 (balanced), T=0.4 (too high: edges break up).)*

**The dilemma**
Lower the threshold and you keep noise; raise it and edges fall apart.

**The standard answer: Canny**
Two thresholds plus non-maximum suppression — thin, connected edges.

---

## Slide 43: The complete pipeline

*Five steps, all of them convolutions except the last*

1. **Smooth** — Gaussian, σ chosen by the scale of the structures you care about
2. **Differentiate** — Sobel in both directions
3. **Combine** — gradient magnitude — rotation invariant
4. **Decide** — threshold, ideally with hysteresis

---

## Slide 44: Designed kernels, learned kernels

*Same operation, different source of numbers*

**Classical computer vision** — You choose the nine numbers
```
-1  0  1
-2  0  2
-1  0  1
```
- derived from calculus
- you can say what it responds to
- one kernel, one purpose
- Works immediately, needs no data — and never adapts to your images.

**Convolutional network** — Back-propagation chooses them
```
w₁  w₂  w₃
w₄  w₅  w₆
w₇  w₈  w₉
```
- derived from a loss function
- many kernels per layer
- purpose emerges from the data
- Adapts to your images — and needs enough of them to do so.

*(same operation)*

> So when you inspect the first layer of a trained network and find edge- and blob-like kernels: you have already built those by hand today.

---

## Slide 45: What to take away

*Six sentences worth remembering*

1. **The histogram tells you what, never where.** Spatial questions need neighbourhood operations.
2. **Contrast moves information around,** it never creates it — and clipping destroys it for good.
3. **Estimate the range from percentiles,** not from the extreme values.
4. **Smooth before you differentiate.** The derivative amplifies noise more than signal.
5. **One operation, many faces.** The kernel decides whether the convolution smooths or finds edges.
6. **A conv layer is the same operation.** Its weights are learned; everything you know about kernels transfers.

---

## Slide 46: Hands-on in Fiji — Part I

*Where to click for every operation we discussed*

| Task | Menu path |
|---|---|
| Work on a copy | Image ▸ Duplicate… (Ctrl+Shift+D) |
| Convert to 8-bit grey | Image ▸ Type ▸ 8-bit |
| Histogram | Analyze ▸ Histogram (Ctrl+H) · tick Live · List / Copy for the raw counts |
| Brightness & contrast, interactive | Image ▸ Adjust ▸ Brightness/Contrast (Ctrl+Shift+C) — changes the display only until you press Apply |
| Linear scaling, exact | Process ▸ Math ▸ Add… then Process ▸ Math ▸ Multiply… |
| Min–max stretch | Process ▸ Enhance Contrast… · Saturated = 0.0 · tick Normalize |
| Robust 1% stretch | Process ▸ Enhance Contrast… · Saturated = 1.0 · tick Normalize |
| Histogram equalisation | Process ▸ Enhance Contrast… · tick Equalize histogram (hold Alt to use the raw counts instead of their square root) |
| CLAHE | Process ▸ Enhance Local Contrast (CLAHE)… |
| Inversion LUT | Edit ▸ Invert (Ctrl+Shift+I) |
| Pseudo-colour LUT | Image ▸ Lookup Tables ▸ Fire / Spectrum / … |
| Avoid clipping in a chain | Image ▸ Type ▸ 32-bit → do the maths → Image ▸ Type ▸ 8-bit |
| Record what you clicked | Plugins ▸ Macros ▸ Record… |

---

## Slide 47: Hands-on in Fiji — Part II

*Convolution, smoothing and edges*

| Task | Menu path |
|---|---|
| Intensity profile | draw a line, then Analyze ▸ Plot Profile (Ctrl+K) |
| Intensities as a surface | Analyze ▸ Surface Plot… |
| Add noise | Process ▸ Noise ▸ Add Specified Noise… · Process ▸ Noise ▸ Salt and Pepper |
| Mean filter | Process ▸ Filters ▸ Mean… (parameter is a radius: 1 ≈ 3×3) |
| Gaussian filter | Process ▸ Filters ▸ Gaussian Blur… (parameter is σ) |
| Median filter | Process ▸ Filters ▸ Median… (radius) |
| Your own kernel | Process ▸ Filters ▸ Convolve… — type the matrix, row by row |
| Kernels with negative weights | Image ▸ Type ▸ 32-bit first, otherwise negative results are clipped to 0 |
| Sobel magnitude | Process ▸ Find Edges |
| One directional derivative | Convolve… with -1 0 1 / -2 0 2 / -1 0 1 |
| Binary edge map | Image ▸ Adjust ▸ Threshold… (Ctrl+Shift+T) |
| Canny | Plugins ▸ Feature Extraction ▸ Canny Edge Detector |
| Compare two results | Process ▸ Image Calculator… (Difference) |

---

## Slide 48: Contact

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
