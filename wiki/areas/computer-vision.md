---
type: area
title: "Computer Vision"
domain: computer-vision
status: active
created: 2026-09-04
updated: 2026-09-04
tags: [computer-vision, opencv, image-processing, deep-learning, object-detection, feature-detection, camera-calibration, dnn]
---

# Computer Vision

Computer vision is the field of enabling machines to interpret and understand visual information from the world. It spans classical image processing, geometric vision, statistical pattern recognition, and modern deep learning–based approaches. OpenCV is the dominant practical library for all layers of this stack.

---

## Core Concept Pages

| Page | Description |
|------|-------------|
| [[concepts/opencv-core]] | cv::Mat class, data type system, coordinate conventions, I/O functions, drawing, arithmetic, OpenCV 5.0 changes, and module architecture |
| [[concepts/opencv-image-processing]] | imgproc (filtering, morphology, colour conversion, geometric transforms, histograms, thresholding, contours, edges), features2d (SIFT, ORB, FLANN, homography), calib3d (camera calibration, pose estimation, stereo), dnn (ONNX inference workflow, backends), video analysis (optical flow, background subtraction, tracking) |

---

## Source Pages

| Page | Description |
|------|-------------|
| [[sources/opencv-docs]] | OpenCV official documentation index — module listing, contrib module listing, package variants, Python install, OpenCV 4.13.0 and 5.0.0.93 |

---

## Key Concepts Summary

### Classical Image Processing
- **Spatial filtering**: Gaussian blur, Sobel, Laplacian, Canny edge detection
- **Morphological operations**: erosion, dilation, opening, closing, gradient, top/black-hat
- **Colour spaces**: BGR (OpenCV default), HSV (colour segmentation), greyscale, Lab, YUV
- **Geometric transforms**: affine, perspective (homography), resize, rotate, flip
- **Histograms**: equalisation, CLAHE, colour histogram comparison

### Feature-Based Vision
- **Detectors and descriptors**: SIFT (scale/rotation invariant), ORB (fast, binary), AKAZE, BRISK
- **Matching**: BFMatcher (brute-force exact), FLANN (approximate, fast); Lowe's ratio test
- **Homography**: findHomography with RANSAC — maps one planar surface to another

### Camera Geometry
- **Intrinsic calibration**: chessboard pattern → camera matrix K, distortion coefficients
- **Pose estimation**: solvePnP → rotation (rvec) and translation (tvec) vectors
- **Stereo vision**: stereoCalibrate → stereoRectify → disparity map → 3D depth

### Deep Learning Inference (dnn module)
- **Workflow**: blobFromImage → setInput → forward → post-process
- **Formats**: ONNX (preferred), TF frozen graph, Caffe, Darknet (YOLO)
- **Backends**: CPU (default), CUDA (NVIDIA), OpenCL (integrated GPU)
- **OpenCV 5 DNN engine**: >80% ONNX coverage; LLM/VLM support with tokenisers and KV-cache

### Video Analysis
- **Background subtraction**: MOG2 (Gaussian mixture), KNN
- **Optical flow**: Lucas-Kanade sparse (feature points), Farneback dense (every pixel)
- **Tracking**: CSRT (accurate), KCF (fast), MOSSE (fastest) — from contrib `tracking` module

### Object Detection
- **Classical**: Haar cascades (face, eyes, body), HOG + SVM (pedestrians)
- **Modern**: YOLO (v5/v8/v10), RTDETR — load via dnn module (ONNX)

---

## Planned Topics

| Topic | Area |
|-------|------|
| Convolutional neural networks | Architecture (ResNet, VGG, EfficientNet, ViT) |
| Instance segmentation | Mask R-CNN, YOLOv8-seg via ONNX |
| 3D reconstruction / SfM | opencv_contrib `sfm` module |
| Super-resolution | `dnn_superres` contrib module |
| Optical Character Recognition | `text` contrib module + Tesseract |
| ArUco marker detection | `aruco` contrib module |

---

## Related Areas

- [[areas/performance-optimisation-design]] — measuring and optimising computer vision pipeline throughput
- [[areas/machine-learning]] — statistical learning underpinning classical CV
- [[areas/software-engineering]] — testing and validation of CV systems
