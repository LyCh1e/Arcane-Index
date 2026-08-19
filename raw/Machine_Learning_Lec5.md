# International Summer School: Trustworthy AI – Machine Learning Meets Blockchain

**Microcredential 2: Machine Learning**
**Part 5: Convolutional Neural Networks**

Tobias Rueckert, M. Sc.
OTH Regensburg
TU Munich
AKTORmed Robotic Surgery

*International Summer School 2026 | Machine Learning*

---

## Slide 2: Convolutional Neural Networks — Four questions, in order

1. **Why convolution at all?** — What goes wrong when a fully connected network meets an image, and which two properties of images repair it.
2. **What happens inside one layer?** — Kernels with depth, many kernels at once, padding, stride, ReLU, pooling, normalisation — and the receptive field.
3. **How is a network built from that?** — The anatomy of a CNN from pixels to class scores, the classification head, and how the kernel numbers are found.
4. **Which networks changed the field?** — AlexNet, VGG, GoogLeNet, ResNet and U-Net — one central idea each, and what we still use from them.

**Colour code:** image data · kernel / weights · feature map · classifier · pitfall

---

## Slide 3: You already know the operation

*A kernel slides over the image and produces a map of responses*

*(Figure: an input fundus image (one channel, 300×300 pixels) convolved with a 3×3 kernel [[-1,0,1],[-2,0,2],[-1,0,1]] — "9 numbers, chosen by hand (Sobel, horizontal derivative)" — producing a feature map showing vessel edges, captioned "where are the edges?".)*

> **Key idea:** Nothing about the arithmetic will change today. Only the question of who picks the numbers.

---

## Slide 4: The one thing that changes

*A convolutional layer is a convolution whose kernel entries are unknown*

*(Figure: side-by-side comparison — "Image processing": a fixed 3×3 kernel [[-1,0,1],[-2,0,2],[-1,0,1]], "You decide what to look for. The numbers are fixed." vs. "Convolutional layer": a 3×3 kernel of unknowns [w1..w9] found via gradient descent, "The data decides. The numbers are learned.")*

> **Key idea:** A convolutional layer has no new mathematics in it. It has nine unknowns per kernel.

---

## Slide 5: Why convolution?

*Part 1 of 4*

In this part:
1. The naive approach: flatten the image and use a fully connected layer
2. Problem 1: a dense layer does not know that pixels have neighbours
3. Problem 2: it has to learn the same pattern once per position
4. The repair: local receptive fields and shared weights

---

## Slide 6: The naive approach

*Flatten the image, connect everything to everything*

*(Figure: a 224×224×3 input image flattened to 150,528 values, fully connected to 1,000 units. Box: "weights in this single layer: 150 million — and it has not seen a second layer yet".)*

> **Key idea:** One dense layer on a small image already needs more weights than an entire well-known CNN.

---

## Slide 7: No sense of neighbourhood

*Permute the pixels and the learning problem is unchanged*

*(Figure: an original fundus photo (same 202,800 numbers) next to a version with pixels randomly permuted (same 202,800 numbers, reordered). Callout: "For a fully connected layer these two inputs are equally hard. It never learns that pixels have neighbours.")*

> **Key idea:** Structure in an image lives in the neighbourhood relations. A dense layer throws exactly that away.

---

## Slide 8: The same pattern, over and over

*In a dense layer every position owns its own weights*

*(Figure: two small pixel grids, each highlighting a different local patch — "81 weights of the dense layer, these weights see the lesion" vs. "81 weights of the dense layer, a completely different set". Callout: "The same pattern has to be learned again for every position it can appear in — and every position needs its own training examples.")*

> **Key idea:** Position-dependent weights mean position-dependent training data — an amount nobody has.

---

## Slide 9: Two properties, two decisions

*Locality and weight sharing are the whole idea behind convolution*

*(Figure: "Fully connected" network diagram — every input node connected to every output node, "63 weights, every one different, 9×7 connections" — vs. "Local + shared" — each output connected only to a local group of inputs, using the same 3 weights (w1, w2, w3) reused at every position, "3 weights, reused at every position".)*

> **Key idea:** Locality plus weight sharing is not an approximation of a dense layer. It is a better model of what an image is.

---

## Slide 10: What that buys you

*The same job, done with four orders of magnitude fewer weights*

| | Fully connected layer | Convolutional layer |
|---|---|---|
| Weights | **150,529,000** | **1,792** |
| Setup | 224 × 224 × 3 inputs → 1,000 units | 64 kernels of size 3 × 3 × 3, plus 64 biases |
| Scaling | grows with the image size | independent of the image size |

**Parameters of a convolutional layer:**
```
( k × k × C_in + 1 ) × C_out
```
kernel size × input channels, plus one bias, per output channel

The count depends on the kernel size and on how many channels go in and out — never on how large the image is. That is why the same network happily takes a 512 × 512 endoscopic frame and a 224 × 224 thumbnail.

> **Remember:** A convolutional layer is a fully connected layer with two constraints added — and those constraints are true statements about images.

---

## Slide 11: Inside one convolutional layer

*Part 2 of 4*

In this part:
1. Depth: a kernel always spans all input channels
2. Width: many kernels in one layer, one feature map each
3. Geometry: padding, stride and the output size
4. Non-linearity, pooling, normalisation
5. The receptive field, and why depth beats width

---

## Slide 12: One window, one number

*The kernel visits every position and writes down a single value each time*

*(Figure: a 6×6 input grid of numbers, a highlighted 3×3 patch [[0,3,0],[9,0,4],[1,4,8]] element-wise multiplied by a 3×3 kernel [[0,1,0],[1,-4,1],[0,1,0]], summed to give -21, then placed into a 4×4 feature map. "One window → one number: 1·3 + 1·4 − 4·8 + 1·1 + 1·3 = -21 — slide the window over every position, and the numbers form the feature map.")*

The kernel here is a discrete Laplacian; in a CNN the same nine slots would hold learned values.

---

## Slide 13: A kernel always has depth

*This is the single most misunderstood point about convolutional layers*

**Depth is not optional**
A kernel spans every channel of its input. On an RGB image a "3 × 3 kernel" is really 3 × 3 × 3 = 27 weights.

**One kernel, one map**
The three per-channel results are summed, the bias is added, and what leaves the kernel is a single 2-D feature map.

**And in the next layer?**
If this layer outputs 64 channels, every kernel of the layer after it is 3 × 3 × 64.

---

## Slide 14: Many kernels, many feature maps

*The number of kernels in a layer is the number of channels it outputs*

*(Figure: one input channel (a fundus image) run through 6 different hand-built kernels (vertical edge, horizontal edge, diagonal edge, fine texture, bright blob, dark blob), each producing its own feature map (map 1–map 6), forming a 6-channel output volume.)*

The kernels shown are hand-built prototypes. Trained first layers reliably converge to very similar filters.

> **Key idea:** Depth of the kernel = channels in. Number of kernels = channels out.

---

## Slide 15: Convolution Operation - General

*(Figure: a diagram showing an image being run through a convolution operation, tapering down into progressively smaller feature maps.)*

- **CNNs:** From fixed filter entries to iteratively learned values
- **Function:** Slides a filter over the input to extract local patterns
- **Effect:** Produces a feature map, usually smaller than the input
- **Goal:** Capture important features while reducing spatial size

Source: https://towardsdatascience.com/computer-vision-convolution-basics-2d0ae3b79346/

---

## Slide 16: Convolution Operation – Padding (1 Pixel)

*(Figure: a 3-D diagram showing an input grid with a 1-pixel border of padding added (shown as a dashed/grey outer ring) before the kernel slides across it, producing an output feature map.)*

- **Function:** Adds extra pixels (usually zeros) around the image before convolution
- **Purpose:** Allows filters to include edge information during convolution
- **Goal:** Controls the output size and prevents feature maps from shrinking

Source: https://towardsdatascience.com/computer-vision-convolution-basics-2d0ae3b79346/

---

## Slide 17: Convolution Operation – Padding (2 Pixels)

*(Figure: similar diagram to the previous slide but with a thicker, 2-pixel padding border shown around the input grid.)*

- **Function:** Adds a 2-pixel border (usually zeros) around the input image
- **Purpose:** Lets the filter cover edge regions more
- **Goal:** Increases feature map size to retain more spatial information and capture border features better

Source: https://towardsdatascience.com/computer-vision-convolution-basics-2d0ae3b79346/

---

## Slide 18: Convolution Operation – Strides

*(Figure: a 3-D diagram of the kernel sliding across the input grid in larger jumps, producing a smaller output feature map than a stride-1 convolution.)*

- **Function:** Moves the convolutional filter across the input in steps larger than 1
- **Purpose:** Reduces the spatial size of the feature map and controls sampling density
- **Goal:** Speeds up computation and summarizes regions while keeping important features

Source: https://towardsdatascience.com/computer-vision-convolution-basics-2d0ae3b79346/

---

## Slide 19: Convolution Operation – Padding (1 Pixel) + Strides

*(Figure: a 3-D diagram combining 1-pixel padding and stride > 1, showing an intermediate-sized output feature map.)*

- **Function:** Adds a 1-pixel border and moves the filter across the input in steps
- **Purpose:** Allows edge coverage while controlling how much the feature map is downsampled
- **Goal:** Preserves most spatial information and reduces feature map size moderately

Source: https://towardsdatascience.com/computer-vision-convolution-basics-2d0ae3b79346/

---

## Slide 20: Convolution Operation – Dilation

*(Figure: a 3-D diagram showing a kernel with gaps inserted between its elements (dilated), covering a larger area of the input grid than a standard kernel of the same size.)*

- **Function:** Expands the convolutional filter by inserting gaps between its elements
- **Purpose:** Increases the receptive field without increasing the number of parameters
- **Goal:** Captures more context and larger patterns in the input while keeping computation efficient

Source: https://towardsdatascience.com/computer-vision-convolution-basics-2d0ae3b79346/

---

## Slide 21: Convolution Operation – Transposed

*(Figure: a 3-D diagram showing the reverse operation — a small input grid expanding into a larger output grid via transposed convolution ("upsampling").)*

- **Function:** Applies a convolution in reverse to upsample feature maps
- **Purpose:** Increases spatial resolution of the output
- **Goal:** Reconstructs larger feature maps, useful for tasks like image segmentation or generative models

Source: https://towardsdatascience.com/computer-vision-convolution-basics-2d0ae3b79346/

---

## Slide 22: Padding and stride

*Two dials that decide how large the output is*

**Output size:**
```
o = ⌊ ( n + 2p − k ) / s ⌋ + 1
```

With k = 3, padding p = 1 and stride s = 1 the output has exactly the input size — which is why "3 × 3, padding 1" is the default convolution in almost every modern architecture.

> **In practice:** Halving the resolution with stride 2 is today more common than pooling — same effect, and the layer can learn how to do it.

---

## Slide 23: Convolutional Neural Networks — Convolution Operation (Output Dimensions)

*Determining the output dimensions:*

```
w_o = ( w_i + 2·p_w − w_k ) / s_w + 1
h_o = ( h_i + 2·p_h − h_k ) / s_h + 1
```

If padding, stride, and kernel are symmetric:
```
o = ( n + 2p − k ) / s + 1
```

Where:
- w_i → width of the input image
- h_i → height of the input image
- w_k → width of the kernel
- h_k → height of the kernel
- s_w → stride for width
- s_h → stride for height
- p_w → padding along the width of the image
- p_h → padding along the height of the image

Source: https://towardsdatascience.com/computer-vision-convolution-basics-2d0ae3b79346/

---

## Slide 24: The non-linearity

*Without it, any stack of convolutions collapses into one convolution*

*(Figure: ReLU curve plot (negative → 0, positive → unchanged); a histology image "Before ReLU" (blue = negative, red = positive) and "After ReLU" (black and white, 47% of the values are set to zero). Callout box "Without it: two stacked convolutions are just one bigger convolution — depth would buy nothing.")*

> **Key idea:** Depth is only worth something if something non-linear sits between the layers.

---

## Slide 25: Pooling

*Fewer numbers to carry, and small shifts stop mattering*

*(Figure: a 4×4 feature map max-pooled (2×2) down to a 2×2 map, keeping the largest value of each block, "75% of the numbers are dropped". Second panel: original vs. shifted-by-2px vessel image, each max-pooled, showing "mean change: 46% before pooling, 16% after pooling" — "a small shift of the input barely changes the pooled map".)*

> **Key idea:** Pooling buys robustness with location precision. For classification that is a good trade; for segmentation it is a problem we will have to fix.

---

## Slide 26: The receptive field

*Each layer sees a little more of the image than the one before*

*(Figure: left — a small network diagram showing "7 input pixels reach this one unit" after 3 stacked layers. Right — comparison: "Two 3×3 layers cover the same 5×5 window" as "one 5×5 layer" — two 3×3 layers use 18 weights plus a non-linearity; one 5×5 layer uses 25 weights, no non-linearity.)*

> **Key idea:** Depth is the cheap way to see more. This is the argument VGG is built on.

---

## Slide 27: What the deeper layers can see

*Larger receptive fields make more abstract features possible*

*(Figure: the same fundus photograph shown four times with progressively larger highlighted squares — Layer 1: receptive field 3×3 px ("edges, single vessel walls"); Layer 2: 20×20 px ("vessel segments, curvature"); Layer 3: 90×90 px ("branchings, optic disc"); Layer 4: whole image ("this is a retina").)*

Squares are drawn to scale on the same photograph. Only the receptive field grows — the image does not change.

---

## Slide 28: Normalisation inside the network

*Keep every layer's inputs on a comparable scale*

*(Figure: two histograms — "Raw pre-activations" (mean +0.83, std 0.37, skewed) vs. "After normalisation" (mean +0.00, std 1.00, centred bell curve). One randomly initialised 5×5 kernel applied to 24 real image patches; green band = ±1 standard deviation. Callout: "Why it helps: Every layer receives inputs on the same scale, so gradients stay usable and much larger learning rates work.")*

> **Key idea:** Batch normalisation is why networks deeper than about twenty layers became practical to train.

---

## Slide 29: The block that CNNs repeat

*Four operations, stacked four or five times*

*(Figure: a pipeline diagram — Convolution ("learn what to look for") → Normalisation ("keep the scale under control") → ReLU ("make it non-linear") → Pooling/stride ("shrink the spatial size", optional). "one stage — stack four to five of these and you have a CNN".)*

> **Key idea:** If you can read this block, you can read almost any convolutional architecture published since 2015.

---

## Slide 30: From layers to a network

*Part 3 of 4*

In this part:
1. The anatomy: from pixels to class scores
2. The pattern: resolution down, channels up
3. The head: flatten, or global average pooling
4. Training: the kernel entries are ordinary weights
5. Augmentation: which transformations are honest

---

## Slide 31: Convolutional Neural Networks — Architecture

*(Figure: flow of four concept boxes — "Processing of image data" → "Images have special matrix properties" → "Naiv approach: Transform pixel values in vector and classify it" → "CNNs use matrix-properties for better processing" — followed by a full CNN pipeline diagram: RGB input → Convolution → Feature Maps → Pooling Function → (repeated) → Flattening → fully connected layers → output classes Dog/Cat.)*

Source: J. Frochte: *Maschinelles Lernen - Grundlagen und Algorithmen in Python*, 2018.

---

## Slide 32: Convolutional Neural Networks — Convolution Operation

*(Figure: a large, detailed matrix I (input) with a small kernel K sliding across it, producing an output feature map S = I∗K, all rendered as grids of numeric values.)*

- Central element of CNNs
- Extract features from input image
- Move kernel K over input I
- Sum the products of the respective entries
- The result is a feature map S
- S contains discriminating features

Source: J. Frochte: *Maschinelles Lernen - Grundlagen und Algorithmen in Python*, 2018.

---

## Slide 33: Convolutional Neural Networks — Pooling

*(Figure: a 4×4 numeric grid [[2,2,1,2],[9,0,6,0],[0,0,0,1],[5,6,3,1]] max-pooled (2×2) into a 2×2 grid [[9,6],[6,3]], with the max value of each quadrant highlighted.)*

- Extract the most meaningful features from a feature map
- Keep only these values and discard all others
- Reduces the number of parameters and thus the complexity of the network
- Different types: min pooling, average pooling, max pooling, etc.
  - Here: max pooling

Source: [4, S. 370]

---

## Slide 34: Convolutional Neural Networks — Flattening & Classification

*(Figure: continuation of the CNN pipeline diagram from slide 31 — Convolution → Pooling Function → Flattening → multi-layer perceptron → softmax output (Dog / Cat).)*

- Transfer values from the last convolutional layer to vector
- Process values in multi-layer perceptron
- Convert values to probabilities using softmax function
- Perform classification
  - This MLP is used as the classifier of the CNN

Source: [4, S. 352]

---

## Slide 35: The anatomy of a CNN

*A feature extractor that shrinks the image, then a classifier that reads it*

*(Figure: a full CNN diagram — input (224²×3) → stage 1 (112²×64) → stage 2 (56²×128) → stage 3 (28²×256) → stage 4 (14²×512) → stage 5 (7²×512) → global average pooling ("features", 512) → FC → softmax output (healthy, mild DR, moderate [highlighted], severe). Labelled "feature extractor — convolution, normalisation, ReLU, downsampling" (spatial size shrinks, number of channels grows) and "classifier" (one score per class).)*

> **Key idea:** Everything left of the vector is reusable across tasks. Everything right of it is task-specific.

---

## Slide 36: Resolution down, channels up

*The one design pattern that all of these networks share*

| Stage | Resolution | Positions | Channels | What one position describes |
|---|---|---|---|---|
| input | 224 × 224 | 50,176 | 3 | one pixel, RGB |
| 1 | 112 × 112 | 12,544 | 64 | an edge, in one of 64 flavours |
| 2 | 56 × 56 | 3,136 | 128 | a texture, a short curve |
| 3 | 28 × 28 | 784 | 256 | a vessel branching, a lesion |
| 4 | 14 × 14 | 196 | 512 | a region of the retina |
| 5 | 7 × 7 | 49 | 512 | most of the image at once |

**Fewer positions** — Each stage keeps a quarter of the positions of the one before it — there is simply less to carry.
**Richer positions** — Each remaining position is described by twice as many numbers, so it can encode something more specific.

Dimensions follow the VGG-style layout used throughout this session.

---

## Slide 37: The classification head

*Flatten was the original answer; global average pooling is today's*

*(Figure: comparing two heads on a 7²×512 feature map — "Flatten + fully connected": flatten to 25,088 → dense to 4096, "every value keeps its own weight, 102,760,448 weights"; vs. "Global average pooling": one average per channel → 512 → dense to 4096, "no weights at all". Callout: "89% of VGG-16's 138 million parameters sit in the flatten head — pooling removes almost all of them.")*

> **Key idea:** Global average pooling removed most of the parameters of the classical CNN and made the input size flexible.

---

## Slide 38: How the numbers are found

*Exactly the same loop as for any other neural network*

*(Figure: "Training a CNN" cycle — Image (one training example) → Network (convolutions with the current weights) → Prediction (one score per class) → Loss (distance to the correct label) → loops back to Network. Caption: "Backpropagation nudges every kernel entry in the direction that lowers the loss, and the update is repeated over millions of examples." Nothing here is special to convolution — the nine numbers in a kernel are ordinary weights.)*

> **Key idea:** Weight sharing means one kernel entry collects gradient from every position it was used at.

---

## Slide 39: Augmentation is a modelling decision

*Every transformation states what you believe should not change the label*

*(Figure: a fundus image shown in 7 augmented variants — original, horizontal flip, rotation 20°, random crop, brightness, elastic warp, noise, and colour shift (marked in red as not allowed).)*

**Which transformations are allowed?**
A retina can be photographed mirrored or rotated, so flips, rotations, crops and mild noise produce images that could have come from the clinic.

**A strong colour shift cannot.**
Colour carries diagnostic meaning here: haemorrhages are red, exudates are yellow. Shifting it trains the network to ignore the very signal you need.

**Augmentation is a modelling decision, not a checkbox.**

> **Key idea:** Ask of every augmentation: could this image plausibly have come out of the clinic with the same label?

---

## Slide 40: Architectures that changed the field

*Part 4 of 4*

In this part:
1. LeNet-5 and AlexNet: the template, and the breakthrough
2. VGG: uniformity and depth
3. GoogLeNet: several scales in parallel
4. ResNet: shortcuts, and why depth became possible
5. U-Net: the same ideas, for segmentation

---

## Slide 41: Fourteen years in one picture

*Depth, uniformity and shortcuts — three ideas, three jumps*

*(Figure: a timeline bar chart of ILSVRC top-5 classification error by year: LeNet-5 (1998, not comparable, digits/5 layers), AlexNet (2012, 15.3%, ReLU/dropout/GPUs), VGG-16 (2014, 7.3%, only 3×3 very deep), GoogLeNet (2014, 6.7%, parallel scales 1×1), ResNet-152 (2015, 3.57%, skip connections), U-Net (2015, not comparable, segmentation/medical).)*

bars: ILSVRC top-5 classification error reported by each network — human performance on this task is about 5%
LeNet-5 predates the benchmark; U-Net addresses a different task

> **Key idea:** Two of the three big jumps came from architecture, not from more data.

---

## Slide 42: Bigger did not stay the trend

*Accuracy went up while parameter counts came back down*

*(Figure: bar chart of parameter counts in millions: AlexNet 60.0M, VGG-16 138.4M, GoogLeNet 5.0M, ResNet-50 25.6M, U-Net 31.0M.)*

Parameters in millions, for the original published models. LeNet-5 (1998) had 0.06 M.
Architectural ideas — 1×1 bottlenecks, global average pooling, residual connections — bought more than size ever did.

- **VGG-16 — 138 M:** Depth by brute force. Almost 90% of the weights sit in the fully connected head.
- **GoogLeNet — 5 M:** A lower error than VGG with one twenty-eighth of the weights, thanks to 1×1 bottlenecks.
- **ResNet-50 — 25.6 M:** Deeper than VGG, five times smaller, and still the default backbone in medical imaging.

---

## Slide 43 (footer 44): LeNet-5, 1998

*The template: alternate convolution and pooling, then classify*

**What is already here**
Local receptive fields, shared weights, alternating convolution and subsampling, a fully connected classifier on top.

**What was missing**
ReLU, normalisation, dropout, GPUs — and above all a dataset with a million labelled images.

**Why it matters**
The layout has not changed since. Only its scale has.

LeCun, Bottou, Bengio & Haffner, *Proceedings of the IEEE*, 1998

---

## Slide 44 (footer 45): AlexNet, 2012

*The result that turned computer vision into a deep learning field*

*(Figure: the AlexNet architecture diagram — a 227×227×3 input passing through Conv1→Pool1→Conv2→Pool2→Conv3→Conv4→Conv5→Pool3, then fully connected layers FC6, FC7, softmax output (1000 classes). Box: "8 weighted layers, 60M parameters, 15.3% top-5 error".)*

What was new: ReLU instead of tanh, dropout in the fully connected head, aggressive augmentation, and a network split across two GPUs because a single card had too little memory.

The runner-up that year, built on hand-designed features, scored 26.2%. This result is what started the field.

Krizhevsky, Sutskever & Hinton, NeurIPS 2012

> **Key idea:** Not a new idea — LeNet at scale, with ReLU, dropout and GPUs. Sometimes that is the whole contribution.

---

## Slide 45 (footer 46): VGGNet, 2014

*One kernel size, one pooling size, and a decision about depth*

*(Figure: the VGG-16 architecture diagram — a stack of 3×3 conv+ReLU blocks and 2×2 max-pooling layers progressing from 224×224×3 down to 7×7×512, then flattened to 1×1×4096, 1×1×4096, 1×1×1000 (softmax).)*

Every convolution is 3×3 and every pooling is 2×2. The only remaining decision is how many layers to stack.
Depth alone took the ILSVRC top-5 error from 11.7% in 2013 down to 7.3%.
The price: 138 million parameters, most of them in the fully connected head, and slow inference.

Simonyan & Zisserman, ICLR 2015

> **Key idea:** VGG is the proof that 3 × 3 is enough. Nearly every network since uses only small kernels.

---

## Slide 46 (footer 47): GoogLeNet, 2014

*Instead of choosing one kernel size, use several and let the network decide*

**Several scales at once**
Small and large kernels run in parallel and their outputs are concatenated — no need to pick one.

**The 1 × 1 convolution**
It ignores neighbours completely and only mixes channels. Used as a bottleneck it makes the large kernels affordable — and it is still used everywhere.

**The result**
22 layers, 5 M parameters, 6.7% top-5 error — and it won.

Szegedy et al., CVPR 2015

---

## Slide 47 (footer 48): ResNet, 2015

*Let each block learn a correction instead of a whole transformation*

*(Figure: comparison of "Plain block" (F(x), a stack of 3×3 conv, BN, ReLU, 3×3 conv, BN with no shortcut) vs. "Residual block" (F(x) + x, the same stack but with an identity shortcut adding x back to the output). Callout: "Why it works: The block only has to learn the difference. If the best thing to do is nothing, it outputs zero and passes x through unchanged — so extra layers can no longer make the network worse.")*

Before residuals, a plain 34-layer network reached a higher training error than a plain 18-layer one.
With them, 152 layers trained and won ILSVRC-2015 at 3.57% top-5 error.

> **Key idea:** Residual connections turned depth from a liability into an asset. Every large vision model since uses them — including the Transformer.

---

## Slide 48 (footer 49): U-Net, 2015

*The same components, rearranged for a task that needs the resolution back*

*(Figure: the classic U-Net "U"-shaped architecture diagram — a contracting encoder path (downsampling via conv 3×3/ReLU and max pool 2×2) on the left, a symmetric expanding decoder path (up-conv 2×2) on the right, with skip connections ("copy and crop") linking corresponding encoder/decoder resolutions, ending in a 1×1 conv producing the output segmentation map.)*

> **Key idea:** ResNet's shortcuts add, U-Net's shortcuts concatenate. Both exist because information gets lost on the way down.

---

## Slide 49 (footer 50): Why segmentation is different

*Classification returns one number, segmentation returns one label per pixel*

*(Figure: a fundus photograph ("Input") → a version with vessels traced in green ("Segmentation") → a black-and-white vessel mask ("Output mask"), captioned "one image" / "one label for every pixel" / "same resolution as the input". Callout: "What changes: Classification throws the spatial layout away. Segmentation must give it back — which is exactly what the decoder is for.")*

Illustration of the task. The vessel mask was computed with a classical ridge filter, not produced by a network.

> **Key idea:** Every architecture in this part is the same block, arranged to fit the shape of the output the task needs.

---

## Slide 50 (footer 51): What happened after 2015

*The block stayed; the bookkeeping around it got better*

1. **DenseNet, 2017** — Every layer receives the outputs of all earlier layers in its block. Skip connections taken to the limit; very parameter-efficient.
2. **MobileNet, 2017** — A convolution split into a per-channel spatial filter plus a 1×1 channel mix. Roughly eight times cheaper — this is how CNNs run on embedded hardware.
3. **EfficientNet, 2019** — Depth, width and input resolution scaled together in a fixed ratio rather than one at a time.
4. **ConvNeXt, 2022** — A ResNet modernised with the training recipe of Vision Transformers, and competitive with them — evidence that much of the gap was the recipe, not the architecture.

> **The pattern:** None of these replaces the convolutional block. They change how it is connected, scaled or trained.

---

## Slide 51 (footer 52): The five architectures side by side

*One sentence each, for your notes*

| Network | Year | Params | The one idea | What we still use |
|---|---|---|---|---|
| LeNet-5 | 1998 | 0.06 M | conv and pooling alternating, then a classifier | the overall layout |
| AlexNet | 2012 | 60 M | the same at scale, on GPUs | ReLU, dropout, heavy augmentation |
| VGG-16 | 2014 | 138 M | only 3 × 3 kernels, stacked deep | small kernels everywhere |
| GoogLeNet | 2014 | 5 M | parallel kernel sizes, 1 × 1 bottlenecks | 1 × 1 convolutions for cheap channel mixing |
| ResNet-50 | 2015 | 25.6 M | add the input back to the block output | residual connections, in everything |
| U-Net | 2015 | 31 M | encoder, decoder, and skips between them | the reference for segmentation |

Parameter counts are the commonly cited figures for the original published models and vary slightly between reimplementations.

---

## Slide 52 (footer 53): What to take away

*Five sentences that carry the whole session*

1. **A convolutional layer is a constrained dense layer.** Locality and weight sharing are not tricks — they are true statements about images, and they cost four orders of magnitude fewer weights.
2. **A kernel spans all input channels.** One kernel produces exactly one feature map, whatever the input depth. The number of kernels is the number of output channels.
3. **Depth buys view, not magic.** Stacked 3 × 3 layers cover a large window cheaply and add non-linearity on the way. That is why small kernels won.
4. **Resolution goes down, channels go up.** Every architecture in Part 4 follows this pattern. What differs is only how the blocks are wired.
5. **The task decides the shape.** Classification may destroy the spatial layout. Segmentation must give it back — hence encoders, decoders and skips.

---

## Slide 53 (footer 54): Where this goes next

*Three threads that start here*

1. **Transfer learning** *(next session)* — Nobody trains from scratch on 500 images. Keep the feature extractor, replace the head — exactly at the seam we found on the anatomy slide.
2. **Vision Transformers** *(later this week)* — Attention over image patches instead of a local kernel. The receptive field picture from Part 2 is the right thing to compare it against.
3. **Your team project** *(Friday)* — A CNN on a MedMNIST subset. Kernel size, depth, pooling, normalisation, augmentation — every one of those is now your decision.

**One question to take with you**
A convolutional layer assumes that the same pattern is worth detecting everywhere in the image. For which of your own images is that assumption false — and what would you do about it?

---

## Slide 54 (footer 55): References and image credits

- LeCun, Bottou, Bengio & Haffner: *Gradient-based learning applied to document recognition.* Proceedings of the IEEE, 1998.
- Krizhevsky, Sutskever & Hinton: *ImageNet classification with deep convolutional neural networks.* NeurIPS 2012.
- Simonyan & Zisserman: *Very deep convolutional networks for large-scale image recognition.* ICLR 2015.
- Szegedy et al.: *Going deeper with convolutions.* CVPR 2015.
- He, Zhang, Ren & Sun: *Deep residual learning for image recognition.* CVPR 2016.
- Ronneberger, Fischer & Brox: *U-Net — convolutional networks for biomedical image segmentation.* MICCAI 2015.
- Ioffe & Szegedy: *Batch normalization.* ICML 2015.
- Dumoulin & Visin: *A guide to convolution arithmetic for deep learning.* arXiv:1603.07285, 2016.
- Liu et al.: *A ConvNet for the 2020s.* CVPR 2022.

**Image credits**
Colour fundus photograph: Mikael Häggström, WikiJournal of Medicine, CC0, via the scikit-image sample data. All schematic figures were generated for this session in Matplotlib; every convolution, pooling and normalisation result shown was computed on the images displayed.

---

## Slide 55 (footer 56): Contact

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
