---
type: concept
title: "OpenCV — Image Processing and Computer Vision Techniques"
domain: computer-vision
complexity: high
status: established
created: 2026-09-04
updated: 2026-09-04
tags: [opencv, image-processing, imgproc, features2d, calib3d, dnn, inference, object-detection, feature-matching, camera-calibration, optical-flow, morphology, filtering]
---

# OpenCV — Image Processing and Computer Vision Techniques

This page covers OpenCV's practical computer vision toolkit: image filtering, morphology, colour processing, geometric transforms, feature detection and matching, camera calibration, deep neural network inference, and video analysis.

---

## imgproc — Image Processing Module

The most-used module after `core`. Covers per-pixel operations, spatial filtering, morphological processing, colour conversion, geometric warping, contour analysis, and histograms.

### Colour Space Conversion

```python
grey  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv   = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb   = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    # for matplotlib
lab   = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
yuv   = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
```

**Key insight**: HSV is preferred for colour-based segmentation (Hue is colour, Saturation is vividness, Value is brightness). BGR splits colour across all three channels, making range-based masking harder.

### Thresholding

```python
# Simple global threshold
ret, thresh = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)

# Otsu's method — automatically finds optimal threshold
ret, otsu = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Adaptive thresholding — local neighbourhood threshold
adapt = cv2.adaptiveThreshold(grey, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
```

### Filtering (Smoothing and Sharpening)

| Function | Description | Key parameter |
|----------|-------------|---------------|
| `cv2.GaussianBlur(src, ksize, sigmaX)` | Gaussian smoothing — reduces noise | `ksize` must be odd (e.g. `(5,5)`) |
| `cv2.blur(src, ksize)` | Simple box/mean filter | Faster but less quality than Gaussian |
| `cv2.medianBlur(src, ksize)` | Median filter — removes salt-and-pepper noise | Integer ksize only |
| `cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)` | Edge-preserving smoothing | Slow but keeps sharp edges |
| `cv2.filter2D(src, ddepth, kernel)` | Custom convolution kernel | Any kernel matrix |

```python
# Sharpen with a custom kernel
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharp = cv2.filter2D(img, -1, kernel)
```

### Morphological Operations

All morphological operations require a **structuring element** (kernel):

```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# Also: MORPH_ELLIPSE, MORPH_CROSS
```

| Operation | Function / flag | Effect |
|-----------|----------------|--------|
| **Erosion** | `cv2.erode(src, kernel)` | Shrinks bright regions; removes small white noise |
| **Dilation** | `cv2.dilate(src, kernel)` | Expands bright regions; fills small holes |
| **Opening** | `MORPH_OPEN` | Erosion then dilation — removes small objects |
| **Closing** | `MORPH_CLOSE` | Dilation then erosion — fills small gaps |
| **Gradient** | `MORPH_GRADIENT` | Dilation minus erosion — detects edges |
| **Top-hat** | `MORPH_TOPHAT` | Source minus opening — bright features on dark bg |
| **Black-hat** | `MORPH_BLACKHAT` | Closing minus source — dark features on bright bg |

```python
opened  = cv2.morphologyEx(binary, cv2.MORPH_OPEN,  kernel)
closed  = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
```

### Edge Detection

```python
# Sobel gradient (x and y separately, then combine)
sobelx = cv2.Sobel(grey, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(grey, cv2.CV_64F, 0, 1, ksize=3)
mag    = np.sqrt(sobelx**2 + sobely**2)

# Canny — multi-stage: Gaussian → Sobel → non-max suppression → hysteresis
edges = cv2.Canny(grey, threshold1=100, threshold2=200)
# threshold1: lower hysteresis; threshold2: upper hysteresis
```

### Geometric Transformations

| Function | Description |
|----------|-------------|
| `cv2.resize(src, dsize, interpolation)` | Resize image; `INTER_AREA` for downscaling, `INTER_CUBIC`/`INTER_LINEAR` for upscaling |
| `cv2.rotate(src, rotateCode)` | 90°/180°/270° rotation |
| `cv2.getRotationMatrix2D(center, angle, scale)` + `warpAffine` | Arbitrary rotation |
| `cv2.flip(src, flipCode)` | 0=vertical, 1=horizontal, -1=both |
| `cv2.warpAffine(src, M, dsize)` | Apply 2×3 affine matrix (rotation, translation, scale, shear) |
| `cv2.warpPerspective(src, M, dsize)` | Apply 3×3 homography (for perspective correction) |
| `cv2.getPerspectiveTransform(src_pts, dst_pts)` | Compute homography from 4 point pairs |

### Contours

```python
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area   = cv2.contourArea(cnt)
    perim  = cv2.arcLength(cnt, closed=True)
    approx = cv2.approxPolyDP(cnt, 0.02 * perim, True)   # polygon approximation
    x,y,w,h = cv2.boundingRect(cnt)
    (cx,cy), r = cv2.minEnclosingCircle(cnt)

cv2.drawContours(img, contours, -1, (0,255,0), 2)   # -1 = all contours
```

### Histograms

```python
hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])

# Histogram equalisation (contrast enhancement)
eq = cv2.equalizeHist(grey)

# CLAHE — contrast limited adaptive histogram equalisation
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1   = clahe.apply(grey)
```

---

## features2d — 2D Feature Detection and Matching

### Feature Detectors and Descriptors

| Algorithm | Class | Free? | Good for |
|-----------|-------|-------|---------|
| **SIFT** | `cv2.SIFT_create()` | ✅ (since 4.3) | Scale- and rotation-invariant; gold standard |
| **ORB** | `cv2.ORB_create()` | ✅ | Fast binary descriptor; real-time matching |
| **AKAZE** | `cv2.AKAZE_create()` | ✅ | Non-linear scale space; good for planar scenes |
| **BRISK** | `cv2.BRISK_create()` | ✅ | Binary, scale-invariant |
| **SURF** | `cv2.xfeatures2d.SURF_create()` | ❌ (patent) | Faster than SIFT (contrib only) |

```python
sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(grey, mask=None)
# kp: list of KeyPoint (pt, size, angle, response, octave)
# des: ndarray (N, 128) float32 descriptor matrix
```

### Feature Matching

```python
# Brute-force matcher (exact)
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)      # for SIFT/SURF
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) # for ORB/BRISK/AKAZE

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda m: m.distance)   # sort by quality

# FLANN matcher (approximate, much faster for large descriptor sets)
FLANN_INDEX_KDTREE = 1
index_params  = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann   = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# Lowe's ratio test — filter poor matches
good = [m for m, n in matches if m.distance < 0.75 * n.distance]
```

### Homography and Object Finding

```python
# Find transformation between matched point sets
src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
# H: 3×3 perspective transformation matrix
# RANSAC removes outlier matches

# Warp scene image to template perspective
warped = cv2.warpPerspective(scene, H, (template.shape[1], template.shape[0]))
```

---

## Hough Transforms (in imgproc)

```python
# Line detection
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180,
                         threshold=100, minLineLength=50, maxLineGap=10)

# Circle detection
circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT,
                            dp=1, minDist=20, param1=50, param2=30,
                            minRadius=10, maxRadius=100)
```

---

## calib3d — Camera Calibration and 3D Reconstruction

### Camera Model

A camera is described by:
- **Intrinsic matrix K** (3×3): focal lengths fx, fy and principal point cx, cy
- **Distortion coefficients** (5–14 values): radial (k1,k2,k3) and tangential (p1,p2) distortion

```
K = [[fx,  0, cx],
     [ 0, fy, cy],
     [ 0,  0,  1]]
```

### Camera Calibration

```python
# 1. Prepare object points (e.g. 7×7 chessboard)
objp = np.zeros((7*7, 3), np.float32)
objp[:,:2] = np.mgrid[0:7, 0:7].T.reshape(-1,2)

objpoints, imgpoints = [], []

for img in calibration_images:
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(grey, (7,7), None)
    if ret:
        corners2 = cv2.cornerSubPix(grey, corners, (11,11), (-1,-1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners2)

# 2. Calibrate
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, grey.shape[::-1], None, None)

# 3. Undistort images
undistorted = cv2.undistort(img, K, dist)
```

**Outputs**:
- `K` — camera matrix (intrinsics)
- `dist` — distortion coefficients
- `rvecs`, `tvecs` — rotation and translation vectors for each calibration image

### Pose Estimation

```python
# Find 2D→3D correspondence, compute pose
ret, rvec, tvec = cv2.solvePnP(objpoints, imgpoints, K, dist)
# rvec: rotation vector (Rodrigues), tvec: translation vector

# Reproject to verify
projected, _ = cv2.projectPoints(objpoints, rvec, tvec, K, dist)
```

### Stereo Vision

```python
# Stereo calibration
ret, K1, d1, K2, d2, R, T, E, F = cv2.stereoCalibrate(
    objpoints, imgpoints_left, imgpoints_right, K1, d1, K2, d2, shape)

# Compute rectification maps
R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(K1, d1, K2, d2, shape, R, T)

# Disparity and depth
stereo = cv2.StereoBM_create(numDisparities=64, blockSize=15)
disparity = stereo.compute(grey_left, grey_right)
depth = cv2.reprojectImageTo3D(disparity, Q)  # Q from stereoRectify
```

---

## dnn — Deep Neural Network Inference

### Supported Model Formats

| Format | Load function | Notes |
|--------|--------------|-------|
| **ONNX** | `cv2.dnn.readNetFromONNX(path)` | Preferred; >80% ONNX spec in v5 |
| **TensorFlow** (.pb) | `cv2.dnn.readNetFromTensorflow(path, config)` | Frozen TF1 graphs |
| **Caffe** | `cv2.dnn.readNetFromCaffe(proto, model)` | Legacy models |
| **Darknet** | `cv2.dnn.readNetFromDarknet(cfg, weights)` | YOLO family |
| **TF2/SavedModel** | Via ONNX export → readNetFromONNX | Convert first |
| **PyTorch** | Via `torch.onnx.export()` → ONNX | Convert first |

### Standard Inference Workflow

```python
# 1. Load model
net = cv2.dnn.readNetFromONNX('model.onnx')

# 2. Optional: set backend and target
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)   # GPU
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
# Alternatives: DNN_BACKEND_OPENCV + DNN_TARGET_CPU (default)
#               DNN_BACKEND_OPENCV + DNN_TARGET_OPENCL

# 3. Preprocess image → blob
blob = cv2.dnn.blobFromImage(
    img,
    scalefactor=1/255.0,    # normalise to [0,1]
    size=(640, 640),        # model input size
    mean=(0, 0, 0),         # mean subtraction (BGR order)
    swapRB=True,            # BGR → RGB
    crop=False
)
# blob shape: (1, C, H, W) — NCHW format

# 4. Set input and run forward pass
net.setInput(blob)
outputs = net.forward(net.getUnconnectedOutLayersNames())

# 5. Post-process (model-specific — NMS, decode boxes, etc.)
```

### blobFromImage Parameters

| Parameter | Description |
|-----------|-------------|
| `scalefactor` | Multiply each pixel by this value (e.g. 1/255.0 to normalise) |
| `size` | Target spatial size `(width, height)` |
| `mean` | Mean BGR values to subtract (e.g. `(104, 117, 123)` for VGG/ResNet) |
| `swapRB` | Swap R and B channels (True when model expects RGB) |
| `crop` | If True, centre-crop after resize; if False, stretch |

### Common DNN Backends and Targets

| Backend | Target | Use case |
|---------|--------|---------|
| `DNN_BACKEND_OPENCV` | `DNN_TARGET_CPU` | Default, cross-platform |
| `DNN_BACKEND_OPENCV` | `DNN_TARGET_OPENCL` | GPU via OpenCL (integrated GPUs) |
| `DNN_BACKEND_CUDA` | `DNN_TARGET_CUDA` | NVIDIA GPU (requires CUDA build) |
| `DNN_BACKEND_CUDA` | `DNN_TARGET_CUDA_FP16` | NVIDIA GPU, half-precision |

---

## video — Video Analysis

### Background Subtraction

```python
# MOG2 — Gaussian Mixture Model (adaptive background)
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16)
fgmask = fgbg.apply(frame)

# KNN — K-Nearest Neighbours
fgbg = cv2.createBackgroundSubtractorKNN()
fgmask = fgbg.apply(frame)
```

### Optical Flow

```python
# Lucas-Kanade sparse (tracks specific feature points)
old_grey = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_grey, maxCorners=100, qualityLevel=0.3, minDistance=7)

p1, status, err = cv2.calcOpticalFlowPyrLK(old_grey, new_grey, p0, None)
good_new = p1[status == 1]
good_old = p0[status == 1]

# Farneback dense (flow vector for every pixel)
flow = cv2.calcOpticalFlowFarneback(old_grey, new_grey, None,
    pyr_scale=0.5, levels=3, winsize=15, iterations=3,
    poly_n=5, poly_sigma=1.2, flags=0)
# flow shape: (H, W, 2) — dx, dy per pixel
```

### Object Tracking (contrib: `tracking` module)

```python
tracker = cv2.TrackerCSRT_create()   # accurate but slower
# Also: TrackerKCF_create(), TrackerMOSSE_create(), TrackerGOTURN_create()

ret = tracker.init(frame, bbox)      # bbox = (x, y, w, h)
ok, bbox = tracker.update(frame)     # returns updated bounding box
```

---

## objdetect — Object Detection

### Haar Cascade (classical)

```python
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1,
                                       minNeighbors=5, minSize=(30,30))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
```

Available cascades (in `cv2.data.haarcascades`): frontal face, eye, full body, upper body, cat face, licence plate, smile, etc.

### HOG + SVM People Detector

```python
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
rects, weights = hog.detectMultiScale(img, winStride=(8,8), padding=(4,4), scale=1.05)
```

### QR Code and Barcode Detection

```python
qr = cv2.QRCodeDetector()
data, points, _ = qr.detectAndDecode(img)

# In OpenCV 5 / contrib: wechat_qrcode for more robust QR detection
```

---

## Common Computer Vision Pipelines

### Image Segmentation (Colour-based)

```python
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([35, 100, 50])    # green lower bound in HSV
upper = np.array([85, 255, 255])   # green upper bound
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)
```

### YOLO Inference (with dnn module)

```python
net  = cv2.dnn.readNetFromONNX('yolov8n.onnx')
blob = cv2.dnn.blobFromImage(img, 1/255.0, (640,640), swapRB=True)
net.setInput(blob)
outputs = net.forward(net.getUnconnectedOutLayersNames())
# Post-process: decode boxes, apply NMS (cv2.dnn.NMSBoxes)
```

### Feature-Based Object Recognition

```python
# 1. Detect + describe template
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(template_grey, None)

# 2. Detect + describe scene
kp2, des2 = sift.detectAndCompute(scene_grey, None)

# 3. Match + Lowe ratio test
flann = cv2.FlannBasedMatcher(...)
matches = [m for m,n in flann.knnMatch(des1,des2,k=2) if m.distance < 0.75*n.distance]

# 4. Find homography + warp
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
```

---

## Key Connections

- [[concepts/opencv-core]] — Mat, data types, I/O, drawing, OpenCV 5 architecture
- [[concepts/digital-image-processing]] — underlying theory (convolution, Fourier, colour spaces)
- [[concepts/convolutional-neural-networks]] — CNNs executed through the dnn module
- [[sources/opencv-docs]] — official documentation reference and full module listing
