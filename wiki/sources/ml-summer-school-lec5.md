---
type: source
status: ingested
title: "ML Summer School — Lecture 5: Convolutional Neural Networks"
source_file: raw/Machine_Learning_Lec5.md
ingested: 2026-08-19
tags: [source, machine-learning, deep-learning, cnn, computer-vision]
---

# Source: ML Summer School — Lecture 5

**File:** `raw/Machine_Learning_Lec5.md`
**Lecturer:** Tobias Rueckert, M.Sc. — OTH Regensburg / TU Munich / AKTORmed
**Course:** International Summer School 2026 — Trustworthy AI: ML Meets Blockchain
**Topic:** Convolutional Neural Networks (55 slides)

---

## What This Lecture Covers

Four sequential questions: Why convolution at all? → What happens inside one layer? → How is a network built? → Which networks changed the field?

---

## Key Ideas Extracted

### Why Convolution?

- **FC layer problem 1:** no neighbourhood — a permuted image is equally easy; the spatial structure is thrown away
- **FC layer problem 2:** position-dependent weights — the same pattern must be learned at every position separately
- **Two repairs:** locality (connect each output only to a small patch) + weight sharing (reuse the same kernel at every position)
- **Parameter comparison:** 224×224×3 → 1000 FC layer needs 150,529,000 weights; 64 3×3×3 kernels + biases need 1,792
- **Formula:** `(k × k × C_in + 1) × C_out`
- **Key insight:** "A convolutional layer is a fully connected layer with two constraints added — and those constraints are true statements about images."

### Inside One Convolutional Layer

- **Depth:** a kernel spans ALL input channels (most misunderstood point). A 3×3 kernel on RGB is really 3×3×3 = 27 weights. One kernel → one 2D feature map (the per-channel results are summed)
- **Width:** number of kernels = number of output channels
- **Output size:** `o = ⌊(n + 2p − k)/s⌋ + 1`; with k=3, p=1, s=1: output size = input size (the default)
- **Padding types:** standard (p=1, preserves size), dilation (inserts gaps into kernel, enlarges receptive field without more parameters), transposed/upsampling convolution
- **Stride 2 vs pooling:** stride 2 is more common today; the layer learns how to downsample
- **ReLU:** without it, stacked convolutions collapse into one larger convolution — depth buys nothing
- **Max pooling 2×2:** drops 75% of values; small input shift → 46% change without pooling, 16% after (shift robustness); bad for segmentation (spatial precision lost → U-Net skips fix this)
- **Receptive field:** 2 × 3×3 layers cover the same 5×5 window as one 5×5 layer, using 18 + non-linearity vs 25 weights and no non-linearity; depth is the cheap way to see more
- **Batch normalisation:** re-centres pre-activations to mean 0, std 1; makes learning rates much larger practical; why networks deeper than ~20 layers became trainable; FREEZING IT FREEZES SOMEBODY ELSE'S STATISTICS

### CNN Anatomy

- **Block template (repeated 4–5×):** Conv → Normalisation → ReLU → Pooling/Stride
- **Feature extractor:** spatial resolution decreases, channel count increases (example: 224²×3 → 112²×64 → 56²×128 → 28²×256 → 14²×512 → 7²×512)
- **Classifier head:** global average pooling (one average per channel → 512 values; no weights; flexible input size) or flatten + FC; GAP removed 89% of VGG-16's 138M parameters
- **Augmentation as a modelling decision:** "Ask of every augmentation: could this image plausibly have come out of the clinic with the same label?" — a colour shift is not allowed if colour carries diagnostic meaning

### Architecture History

| Network | Year | Params | One-line idea | Still used |
|---------|------|--------|--------------|------------|
| LeNet-5 | 1998 | 0.06 M | conv+pool alternating, then classify | the overall layout |
| AlexNet | 2012 | 60 M | LeNet at scale on GPUs, ReLU, dropout | ReLU, dropout, heavy augmentation |
| VGG-16 | 2014 | 138 M | only 3×3 kernels, stack deep | small kernels everywhere |
| GoogLeNet | 2014 | 5 M | parallel kernel sizes, 1×1 bottlenecks | 1×1 convolutions for cheap channel mixing |
| ResNet-50 | 2015 | 25.6 M | add input back to block output (F(x)+x) | residual connections, in everything |
| U-Net | 2015 | 31 M | encoder + decoder + skip connections | reference for segmentation |

Post-2015: DenseNet (every layer receives all earlier outputs), MobileNet (depthwise separable conv, 8× cheaper), EfficientNet (scale depth/width/resolution together), ConvNeXt (ResNet with ViT training recipe — competitive without attention).

"Two of the three big jumps came from architecture, not from more data."

---

## Concept Pages Generated

- [[concepts/convolutional-neural-networks|Convolutional Neural Networks]] — full CNN concept page
