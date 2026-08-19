---
type: concept
status: established
title: "Convolutional Neural Networks"
domain: machine-learning
source: [[sources/ml-summer-school-lec5]]
updated: 2026-08-19
tags: [concept, machine-learning, deep-learning, cnn, computer-vision]
---

# Convolutional Neural Networks

> "A convolutional layer is a fully connected layer with two constraints added — and those constraints are true statements about images."

CNNs are the dominant architecture for any task where the input has spatial structure (images, video, volumetric scans). The same operation first built by hand in [[concepts/digital-image-processing|image processing]] — sliding a kernel over an image — becomes a learned transformation when the kernel values are treated as free parameters.

---

## 1. Why Convolution?

### Problem 1 — No Sense of Neighbourhood

A fully connected (dense) layer receives a flat vector. Two images that are identical except for a random permutation of their pixels are equally hard for a dense layer — it never learns that pixels have neighbours. Yet the meaningful information in an image lives precisely in those neighbourhood relations.

### Problem 2 — Position-Dependent Weights

In a dense layer, every spatial position owns its own weights. The same pattern (a lesion, a vessel edge) at a different location requires an entirely different set of weights to detect — and entirely different training examples to support those weights. An amount of data nobody has.

### The Repair: Locality + Weight Sharing

| Property | What it does |
|----------|-------------|
| **Locality** | Each output connects only to a small patch of the input |
| **Weight sharing** | The same kernel is reused at every position |

These two constraints are not approximations of a dense layer. They are a better model of what an image is.

### The Payoff in Parameters

| Layer type | Setup | Weights |
|-----------|-------|---------|
| Dense | 224×224×3 inputs → 1,000 units | **150,529,000** |
| Convolutional | 64 kernels of 3×3×3 + 64 biases | **1,792** |

**General formula for a convolutional layer:**
```
parameters = (k × k × C_in + 1) × C_out
```
Kernel height/width × input channels, plus one bias, per output channel. The count depends on kernel size and channels — never on image size. The same network happily handles 512×512 endoscopic frames and 224×224 thumbnails.

---

## 2. Inside One Convolutional Layer

### Kernel Depth (the Most Misunderstood Point)

A kernel spans **every channel of its input**. On an RGB image a "3×3 kernel" is really 3×3×3 = 27 weights. The three per-channel results are summed, a bias is added, and one 2-D feature map emerges. In the next layer, if this layer outputs 64 channels, every kernel of the next layer is 3×3×64.

```
Depth of kernel  = channels in
Number of kernels = channels out
```

One window's output: sum of element-wise products across all input channels, plus bias.

### Output Size, Padding, and Stride

```
o = ⌊(n + 2p − k) / s⌋ + 1
```

- **n** = input size, **k** = kernel size, **p** = padding, **s** = stride
- With k=3, p=1, s=1: output size equals input size — the de-facto default in modern architectures
- **Stride 2** halves the spatial resolution: simpler and now more common than max pooling; the layer can learn how to downsample

### Convolution Variants

| Variant | Mechanism | Use case |
|---------|-----------|---------|
| Standard | kernel slides at stride 1 | feature extraction |
| Stride 2 | kernel jumps 2 pixels | downsampling without explicit pooling |
| Dilated | gaps inserted between kernel elements | larger receptive field, same parameter count |
| Transposed | reverse: small input → large output | upsampling in decoder (U-Net) |

### Non-linearity — ReLU

Without a non-linearity between layers, any stack of convolutions collapses into a single larger convolution. Depth buys nothing. ReLU (max(0, z)) sets ~47% of activations to zero after each layer, which is exactly what forces later layers to learn non-linear combinations of earlier features.

### Pooling

**Max pooling 2×2:** keeps the maximum value in each 2×2 block; discards 75% of the values.

*Why it helps:* a small input shift changes ~46% of activations without pooling; after pooling, only ~16% change. Small translations stop mattering.

*The trade-off:* pooling buys shift robustness by discarding location precision. For classification this is good; for segmentation it is a problem — which is why U-Net skips exist.

### Receptive Field

Each layer sees a little more of the image than the one before:

- 1 layer of 3×3 → sees 3×3 of the input
- 2 layers of 3×3 → sees 5×5 of the input
- 3 layers of 3×3 → sees 7×7 of the input

Two stacked 3×3 layers cover the same window as one 5×5 layer, using 18 weights plus a non-linearity vs. 25 weights with no non-linearity. **Depth is the cheap way to see more.** This is the argument VGG is built on.

| Layer depth | Receptive field | What one position sees |
|-------------|----------------|----------------------|
| 1 | 3×3 px | edges, single vessel walls |
| 2 | ~20×20 px | vessel segments, curvature |
| 3 | ~90×90 px | branchings, optic disc |
| 4 | whole image | "this is a retina" |

### Batch Normalisation

Re-centres each layer's pre-activations to mean 0 and standard deviation 1 before the non-linearity. Effects:
- Every layer receives inputs on the same scale → gradients remain usable even with many layers
- Much larger learning rates become stable
- Networks deeper than approximately twenty layers became practical to train because of BatchNorm

> **Critical pitfall:** Freezing a BatchNorm layer freezes somebody else's statistics (computed on the source domain). In transfer learning and domain adaptation, this is a silent failure — no error, just worse numbers.

---

## 3. CNN Anatomy

### The Block Template

Almost every modern CNN repeats the same block:

```
Convolution → Batch Normalisation → ReLU → Pooling or Stride 2
     ↑                                                    ↓
 "learn what                                     "shrink spatial
  to look for"                                         size"
```

Stack four to five of these and you have a CNN.

### Feature Extractor + Classifier Head

```
Input (224²×3)
  → Stage 1 (112²×64)     edges, in 64 flavours
  → Stage 2 (56²×128)     textures, short curves
  → Stage 3 (28²×256)     vessel branchings, lesions
  → Stage 4 (14²×512)     regions of the retina
  → Stage 5 (7²×512)      most of the image at once
  → Pooling + Head         class scores
```

**Resolution decreases; channels increase.** Fewer positions, richer descriptions at each position.

### Classification Head: Flatten vs Global Average Pooling

| Head type | Mechanism | Parameters |
|-----------|-----------|------------|
| Flatten + FC | 7²×512 → 25,088 → FC 4096 | 102,760,448 |
| **Global average pooling** | one average per channel → 512 → FC 4096 | **no extra weights in the pooling itself** |

Global average pooling removed 89% of VGG-16's 138M parameters and makes the network independent of input image size. It is the default in all modern architectures.

### Augmentation as a Modelling Decision

Every augmentation is a statement: "images transformed this way should have the same label." Ask of each:

> *"Could this image plausibly have come out of the clinic with the same label?"*

- **Allowed:** horizontal flip, rotation, random crop, mild brightness, elastic warp, Gaussian noise — all are plausible clinical variants
- **Not allowed (on retinal images):** strong colour shift — haemorrhages are red, exudates are yellow; shifting hue erases the diagnostic signal

---

## 4. Architecture History

```
ILSVRC top-5 error
15.3% → AlexNet (2012)
 7.3% → VGG-16  (2014)
 6.7% → GoogLeNet (2014)
 3.57%→ ResNet-152 (2015)
~5%   ← human performance
```

"Two of the three big jumps came from architecture, not from more data."

### LeNet-5 (1998) — The Template

Local receptive fields, shared weights, alternating convolution + subsampling, fully connected classifier on top. 0.06M parameters. What was missing: ReLU, normalisation, dropout, GPUs, and a million-image dataset. The layout has not changed since. Only its scale has.

*LeCun, Bottou, Bengio & Haffner, Proc. IEEE 1998*

### AlexNet (2012) — The Breakthrough

8 weighted layers, 60M parameters, 15.3% top-5 error. What was new: ReLU instead of tanh, dropout in the FC head, aggressive augmentation, split across two GPUs. The runner-up (hand-designed features) scored 26.2%. This result started the field.

> "Not a new idea — LeNet at scale, with ReLU, dropout and GPUs. Sometimes that is the whole contribution."

*Krizhevsky, Sutskever & Hinton, NeurIPS 2012*

### VGG-16 (2014) — Uniformity

Every convolution is 3×3, every pooling is 2×2. The only variable is depth. 138M parameters (most in the FC head), 7.3% error. Proved that 3×3 is enough — nearly every network since uses only small kernels. Depth alone took error from 11.7% (2013) to 7.3%.

> "VGG is the proof that 3×3 is enough."

*Simonyan & Zisserman, ICLR 2015*

### GoogLeNet / Inception (2014) — Multi-Scale

Several kernel sizes (1×1, 3×3, 5×5) run in parallel within each Inception block; outputs are concatenated. The **1×1 convolution** acts as a bottleneck (channel mixing, no spatial context), making the large kernels affordable. Result: 22 layers, 5M parameters, 6.7% error — fewer parameters than AlexNet with better accuracy. 1×1 convolutions for cheap channel mixing are now used everywhere.

*Szegedy et al., CVPR 2015*

### ResNet (2015) — Residual Connections

**The problem:** a plain 34-layer network had higher training error than a plain 18-layer one — adding depth hurt. The cause: gradients vanish by the time they reach the early layers.

**The fix:**
```
Residual block: output = F(x) + x
```
The block only learns the **correction** (residual) relative to the identity. If the best action is "do nothing," the block outputs zero and x passes through unchanged — extra layers can never make the network worse.

```
Plain block:    x → [3×3 conv → BN → ReLU → 3×3 conv → BN] → F(x)
Residual block: x → [3×3 conv → BN → ReLU → 3×3 conv → BN] → F(x) + x  ← skip
```

With residual connections, 152 layers trained and won ILSVRC-2015 at 3.57%. ResNet-50 (25.6M params) remains the default backbone in medical imaging.

> "Residual connections turned depth from a liability into an asset. Every large vision model since uses them — including the Transformer."

*He, Zhang, Ren & Sun, CVPR 2016*

### U-Net (2015) — Segmentation

**The problem:** classification destroys spatial layout; segmentation must give it back.

```
Encoder (contracting path): 
  input → [conv, BN, ReLU] → max pool → deeper features (resolution ↓, channels ↑)

Decoder (expanding path):
  features → [upsample] → [conv, BN, ReLU] → output mask (resolution ↑, channels ↓)

Skip connections: fine-detail feature maps from the encoder are concatenated into the decoder at matching resolutions
```

ResNet's shortcuts **add** (F(x) + x); U-Net's shortcuts **concatenate** (F(x) cat x). Both exist because information gets lost on the downsampling path.

> "Every architecture in Part 4 is the same block, arranged to fit the shape of the output the task needs."

*Ronneberger, Fischer & Brox, MICCAI 2015*

### Post-2015 Developments

| Network | Year | Key idea | Practical gain |
|---------|------|---------|---------------|
| DenseNet | 2017 | every layer receives outputs of all earlier layers | very parameter-efficient |
| MobileNet | 2017 | depthwise separable conv (per-channel spatial + 1×1 channel mix) | ~8× cheaper; runs on embedded hardware |
| EfficientNet | 2019 | scale depth, width, resolution together in a fixed ratio | Pareto-optimal |
| ConvNeXt | 2022 | ResNet modernised with ViT training recipe | competitive without attention |

The pattern: none of these replaces the convolutional block — they change how it is connected, scaled, or trained.

---

## 5. The Five Take-Aways

1. **A convolutional layer is a constrained dense layer.** Locality and weight sharing are true statements about images — and cost four orders of magnitude fewer weights.
2. **A kernel spans all input channels.** One kernel → one feature map, whatever the input depth. Number of kernels = channels out.
3. **Depth buys view, not magic.** Stacked 3×3 layers cover a large window cheaply and add non-linearity on the way.
4. **Resolution goes down, channels go up.** Every architecture follows this pattern.
5. **The task decides the shape.** Classification may destroy spatial layout. Segmentation must give it back — hence encoders, decoders, and skips.

---

## Related Concepts

- [[concepts/digital-image-processing|Digital Image Processing]] — convolution by hand; Sobel kernel; the mathematical operation CNNs use
- [[concepts/neural-networks-linear-models|Neural Networks & Linear Models]] — MLP, backpropagation, ReLU; CNNs apply backprop to kernel weights
- [[concepts/transfer-learning-and-domain-adaptation|Transfer Learning and Domain Adaptation]] — how CNN encoders are reused across tasks
- [[concepts/ml-evaluation-metrics|ML Evaluation Metrics]] — segmentation: DSC + boundary metrics; classification: AUROC + AP
- [[concepts/medmnist-v2-datasets|MedMNIST v2 Datasets]] — practical benchmarks for CNN evaluation
