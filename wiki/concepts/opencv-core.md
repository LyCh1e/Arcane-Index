---
type: concept
title: "OpenCV — Core Library and Architecture"
domain: computer-vision
complexity: high
status: established
created: 2026-09-04
updated: 2026-09-04
tags: [opencv, computer-vision, cv2, mat, image-processing, python, cpp, dnn, opencv5]
---

# OpenCV — Core Library and Architecture

OpenCV (Open Source Computer Vision Library) is the dominant open-source library for real-time computer vision, image processing, and neural network inference. The primary data structure is `cv::Mat` — an n-dimensional dense array — and virtually every OpenCV operation reads from and writes to a Mat.

---

## The cv::Mat Class

`cv::Mat` is the foundation of OpenCV. It represents any n-dimensional dense numerical array: a greyscale image, an RGB frame, a depth map, a point cloud, a feature descriptor, a histogram, or a tensor.

### Structure

A Mat object has two parts:

1. **Header** — contains size (rows × cols), type, number of channels, step (bytes per row), and a reference counter
2. **Data pointer** — points to the actual pixel/value buffer in memory

### Reference Counting and Shallow Copies

OpenCV uses **reference counting** — copying a Mat copies the header and increments the reference count; it does NOT copy the pixel data. Both Mat objects share the same buffer.

```python
import cv2
import numpy as np

img = cv2.imread('image.jpg')  # Mat with its own buffer
copy = img                     # shallow copy — same buffer, ref count = 2
deep = img.copy()              # deep copy — new buffer
```

To get an independent copy: `mat.copy()` or `mat.clone()`.

### Creating Mat Objects

```python
# From file
img = cv2.imread('photo.jpg')              # BGR, CV_8UC3
grey = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)  # CV_8UC1

# From NumPy array (Python — Mat and ndarray share memory)
arr = np.zeros((480, 640, 3), dtype=np.uint8)
mat = cv2.UMat(arr)   # UMat for GPU-accelerated paths

# Blank images
blank = np.zeros((height, width, 3), dtype=np.uint8)
white = np.full((height, width, 3), 255, dtype=np.uint8)
```

---

## Data Types — The CV_Type System

Every Mat has a **type** encoding: `CV_<depth><S|U|F>C<channels>`

| Part | Meaning | Examples |
|------|---------|---------|
| Depth (bits) | Bit depth per channel value | 8, 16, 32, 64 |
| S / U / F | Signed int / Unsigned int / Float | `U` = `uint`, `S` = `int`, `F` = `float` |
| C\<n\> | Number of channels | C1, C2, C3, C4 |

### Common Types

| Type constant | Bit depth | Signed? | Channels | Typical use |
|---------------|----------|---------|---------|-------------|
| `CV_8UC1` | 8-bit | Unsigned | 1 | Greyscale image |
| `CV_8UC3` | 8-bit | Unsigned | 3 | BGR colour image |
| `CV_8UC4` | 8-bit | Unsigned | 4 | BGRA image (with alpha) |
| `CV_16UC1` | 16-bit | Unsigned | 1 | Depth image (e.g. RealSense) |
| `CV_16SC1` | 16-bit | Signed | 1 | Sobel output, intermediate gradients |
| `CV_32FC1` | 32-bit | Float | 1 | Floating-point greyscale, DFT output |
| `CV_32FC3` | 32-bit | Float | 3 | HDR image, optical flow field |
| `CV_64FC1` | 64-bit | Double | 1 | High-precision computation |

**New in OpenCV 5**: `CV_16F` (FP16 / `cv::hfloat`) and `CV_16BF` (BF16 / `cv::bfloat`) types added for neural network weights and inference.

### Pixel Value Ranges

| Type | Range |
|------|-------|
| CV_8U | 0–255 |
| CV_16U | 0–65,535 |
| CV_16S | −32,768 to 32,767 |
| CV_32F | −∞ to +∞ (float) |

### Checking and Converting Types

```python
print(img.dtype)    # e.g. uint8
print(img.shape)    # (height, width, channels) — note rows × cols × ch
print(img.ndim)     # 2 for greyscale, 3 for colour

# Convert type
img_float = img.astype(np.float32) / 255.0   # normalise to [0, 1]
img_back = (img_float * 255).astype(np.uint8)
```

---

## Coordinate System and Image Layout

- **Axes**: (row, col) = (y, x) — row 0 is the **top** of the image
- **Colour channel order**: OpenCV stores colour images as **BGR** (not RGB). This catches many beginners.
- **Shape**: `img.shape` returns `(height, width, channels)` — height first

```python
# Accessing a pixel
pixel = img[y, x]         # returns [B, G, R] for CV_8UC3
b, g, r = img[y, x]       # unpack channels

# Region of interest (ROI) — also a shallow copy
roi = img[y1:y2, x1:x2]

# Convert BGR → RGB for matplotlib
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

---

## Essential I/O Functions

| Function | Description |
|----------|-------------|
| `cv2.imread(path, flag)` | Read image from file. Flags: `IMREAD_COLOR` (BGR, default), `IMREAD_GRAYSCALE`, `IMREAD_UNCHANGED` (preserves alpha) |
| `cv2.imwrite(path, img)` | Save image to file |
| `cv2.imshow(name, img)` | Display in a window |
| `cv2.waitKey(ms)` | Wait for key press (0 = wait indefinitely) |
| `cv2.destroyAllWindows()` | Close all display windows |
| `cv2.VideoCapture(src)` | Open camera (int) or video file (str) |
| `cv2.VideoWriter(...)` | Write video to file |

```python
cap = cv2.VideoCapture(0)          # webcam
while True:
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

---

## Drawing on Images

All drawing functions operate **in-place** on the Mat:

```python
cv2.line(img, pt1, pt2, color, thickness)
cv2.rectangle(img, pt1, pt2, color, thickness)  # thickness=-1 fills
cv2.circle(img, center, radius, color, thickness)
cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)
cv2.putText(img, text, org, fontFace, fontScale, color, thickness)
cv2.polylines(img, pts, isClosed, color, thickness)
```

Colors are BGR tuples: `(255, 0, 0)` = blue, `(0, 255, 0)` = green, `(0, 0, 255)` = red.

---

## Arithmetic and Logic Operations

```python
# Per-pixel arithmetic (clips at type bounds)
cv2.add(a, b)          # saturated add
cv2.subtract(a, b)
cv2.multiply(a, b)
cv2.divide(a, b)
cv2.addWeighted(a, alpha, b, beta, gamma)   # alpha*a + beta*b + gamma (blend)

# Bitwise operations (useful for masking)
cv2.bitwise_and(a, b, mask=mask)
cv2.bitwise_or(a, b)
cv2.bitwise_xor(a, b)
cv2.bitwise_not(a)
```

---

## OpenCV 5.0 — Major Changes (June 2026)

OpenCV 5.0 is the first new major version since OpenCV 4.0 (2018). Key changes:

### 1. Rewritten DNN Engine

- New graph engine with **shape inference, constant folding, and operator fusion**
- ONNX coverage: **>80%** of the ONNX spec (vs <23% in 4.x)
- Modern YOLO detectors (v5, v8, v10, RTDETR) now load without manual graph editing
- CUDA and OpenCL backends maintained; new RISC-V and ARM acceleration paths

### 2. LLM and VLM Support

- Built-in **tokeniser** classes and **KV-cache** management
- Autoregressive decoding support (Qwen, Gemma, GPT-family variants)
- Vision-Language Models runnable through the DNN module

### 3. New Data Types

| Type | Description | Use case |
|------|-------------|----------|
| `CV_16F` / `cv::hfloat` | 16-bit float (FP16) | Neural network weights, faster GPU inference |
| `CV_16BF` / `cv::bfloat` | Brain float 16 (BF16) | Modern ML hardware (TPU, AVX-512 BF16) |
| `CV_Bool` | Boolean | Mask operations |
| `CV_64S` | 64-bit signed integer | Large index arrays |

### 4. N-Dimensional Mat Improvements

- `cv::Mat` can now represent **0D (scalar)** and **1D arrays**
- **Broadcasting** support for element-wise operations across mismatched shapes
- N-D operations run across CPUs and accelerators without code changes
- Up to 2× improvement on mathematical workloads

### 5. C API Removal

The legacy C API (OpenCV 1.x era functions like `cvLoadImage`, `IplImage`, `CvMat`) has been **fully removed**. Use the C++ API or Python `cv2` bindings exclusively.

### 6. Hardware Acceleration

Tuned paths for:
- Intel IPP (SSE/AVX/AVX-512)
- Arm KleidiCV
- Qualcomm FastCV
- RISC-V Vector (RVV)

---

## Module Architecture Overview

```
opencv-python (cv2 namespace)
│
├── Core
│   ├── core        — Mat, arithmetic, drawing, random numbers
│   ├── imgcodecs   — imread / imwrite
│   ├── highgui     — imshow / VideoCapture / GUI
│   └── videoio     — VideoCapture / VideoWriter
│
├── Image Analysis
│   ├── imgproc     — filtering, morphology, colour, geometry, histograms
│   ├── photo       — denoising, inpainting, HDR
│   └── stitching   — panorama
│
├── Feature Analysis
│   ├── features2d  — SIFT, ORB, BFMatcher, FLANN descriptor matchers
│   ├── flann       — Fast approximate NN search
│   └── objdetect   — Haar, HOG, QR code, barcode
│
├── 3D Vision
│   ├── calib3d     — camera calibration, stereo, pose estimation
│   └── video       — optical flow, background subtraction, tracking
│
└── AI / ML
    ├── dnn         — ONNX/TF/Caffe inference (rewritten in v5)
    └── ml          — classical ML (SVM, kNN, decision trees)
```

---

## Key Connections

- [[concepts/opencv-image-processing]] — imgproc, features2d, calib3d, dnn inference details
- [[concepts/digital-image-processing]] — theory: convolution, Fourier transform, colour spaces
- [[concepts/convolutional-neural-networks]] — CNNs that the dnn module executes
- [[sources/opencv-docs]] — source reference with full module and contrib listing
