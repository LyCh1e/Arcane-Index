---
type: source
title: "OpenCV Official Documentation — docs.opencv.org"
source_url: "https://docs.opencv.org/"
domain: computer-vision
tags: [opencv, computer-vision, image-processing, deep-learning, python, cpp]
created: 2026-09-04
note: "docs.opencv.org returns 403 to automated fetchers. Content sourced from docs.opencv.org (via search cache), PyPI, GitHub (opencv/opencv, opencv/opencv_contrib), and community resources (learnopencv.com, pyimagesearch.com, geeksforgeeks.org)."
---

# Source Index — OpenCV Official Documentation

**URL**: https://docs.opencv.org  
**Current stable 4.x**: 4.13.0 — https://docs.opencv.org/4.13.0/  
**Current stable 5.x**: 5.0.0.93 (released July 2, 2026) — https://docs.opencv.org/5.0/  
**GitHub**: https://github.com/opencv/opencv  
**Contrib modules**: https://github.com/opencv/opencv_contrib

---

## What OpenCV Is

OpenCV (Open Source Computer Vision Library) is a cross-platform, open-source library for real-time computer vision, image processing, and machine learning. Originally developed by Intel in 1999, it has over 2,500 optimised algorithms covering the full computer vision stack — from basic image I/O to deep neural network inference.

**Languages**: C++ (primary API), Python (`cv2`), Java, MATLAB  
**Platforms**: Windows, Linux, macOS, Android, iOS  
**License**: Apache 2.0

---

## Python Packages (PyPI)

Four variants — **do not install multiple packages in the same environment** (all share the `cv2` namespace):

| Package | Contents | Use case |
|---------|----------|----------|
| `opencv-python` | Main modules only | Desktop/GUI applications |
| `opencv-contrib-python` | Main + contrib/extra modules | Full feature set |
| `opencv-python-headless` | Main modules, no GUI | Servers, Docker |
| `opencv-contrib-python-headless` | Main + contrib, no GUI | Servers with extra algorithms |

**Note**: Non-free patented algorithms (e.g. SURF) are excluded from all PyPI packages. SIFT is included since 4.3.0 (patent expired).

```bash
pip install opencv-python          # standard
pip install opencv-contrib-python  # with extras
```

---

## Main Modules (OpenCV 4.x / 5.x)

| Module | Name | Description |
|--------|------|-------------|
| `core` | Core functionality | Basic data structures (cv::Mat), math operations, memory management |
| `imgproc` | Image Processing | Filtering, morphology, colour conversion, geometric transforms, histograms, drawing |
| `imgcodecs` | Image I/O | Reading and writing image files (imread, imwrite) |
| `videoio` | Video I/O | Capturing from cameras, reading/writing video files |
| `highgui` | High-level GUI | Windows, trackbars, mouse events (imshow, waitKey) |
| `video` | Video Analysis | Motion estimation, background subtraction, optical flow, object tracking |
| `calib3d` | Calibration & 3D | Camera calibration, stereo, pose estimation, homography, 3D reconstruction |
| `features2d` | 2D Features | Feature detectors (SIFT, ORB), descriptors, matchers (BFMatcher, FLANN) |
| `objdetect` | Object Detection | Haar cascades, HOG+SVM people detector, QR/barcode detection |
| `dnn` | Deep Neural Networks | Model loading and inference (ONNX, TF, Caffe); see OpenCV 5 for major upgrades |
| `ml` | Machine Learning | SVM, k-NN, decision trees, random forests, Bayes — classical ML |
| `flann` | FLANN | Fast approximate nearest-neighbour search for feature matching |
| `photo` | Computational Photography | Denoising, inpainting, HDR, deblurring |
| `stitching` | Image Stitching | Panorama pipeline |
| `gapi` | Graph API | Graph-based image pipeline for heterogeneous acceleration |

---

## Contrib / Extra Modules (opencv_contrib)

Selected highlights — full list at https://github.com/opencv/opencv_contrib/tree/master/modules:

| Module | Description |
|--------|-------------|
| `aruco` | ArUco and ChArUco marker detection for AR |
| `face` | Face recognition (Eigenfaces, Fisherfaces, LBPH) |
| `tracking` | Visual object tracking algorithms (KCF, CSRT, MOSSE, etc.) |
| `xfeatures2d` | Extra feature detectors/descriptors (SURF, BRIEF, FREAK) — some non-free |
| `ximgproc` | Extended image processing (structured forests, guided filter, domain transform) |
| `xphoto` | Extra computational photography (white balance, denoising, inpainting variants) |
| `dnn_superres` | Super-resolution via CNN (EDSR, ESPCN, FSRCNN, LapSRN) |
| `dnn_objdetect` | Compact CNN object detection models |
| `sfm` | Structure from Motion — 3D reconstruction from 2D images |
| `optflow` | Optical flow: DeepFlow, SimpleFlow, SparseToDenseFlow |
| `bgsegm` | Background segmentation (GMG, CNT, GSOC methods) |
| `text` | Scene text detection and recognition (EAST, Tesseract integration) |
| `saliency` | Visual attention / saliency maps |
| `stereo` | Advanced stereo correspondence |
| `rgbd` | RGB-D processing: surface normals, 3D planes, 3D object recognition |
| `img_hash` | Perceptual image hashing (pHash, average hash, Marr–Hildreth) |
| `mcc` | Macbeth Color Chart detection for colour calibration |
| `videostab` | Video stabilisation |
| `viz` | 3D visualisation (Viz window) |
| `wechat_qrcode` | WeChat-based QR code detection and parsing |
| `quality` | Image quality analysis (BRISQUE, PSNR, SSIM, MSE) |
| `freetype` | Text rendering with FreeType + HarfBuzz |
| `hdf` | Hierarchical Data Format (HDF5) I/O |

---

## Linked Concepts

- [[concepts/opencv-core]] — Mat, data types, module architecture, OpenCV 5 changes, Python API
- [[concepts/opencv-image-processing]] — imgproc, features2d, calib3d, dnn inference, video analysis
