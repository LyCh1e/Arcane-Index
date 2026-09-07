---
type: source
title: "INF2005 Cyber Security Fundamentals — Steganography"
source: "raw/INF2005 Cyber Security Fundamentals - Steganography.md"
domain: cryptography
tags: [inf2005, steganography, LSB, BPCS, steganalysis, information-hiding, image-processing]
created: 2026-09-07
lecturer: "Dr Tan Kheng Leong"
---

# Source Index — INF2005 CSF: Steganography

**Module:** INF2005 Cyber Security Fundamentals  
**Lecturer:** Dr Tan Kheng Leong  
**Topic:** Steganography  
**Raw file:** `raw/INF2005 Cyber Security Fundamentals - Steganography.md`

---

## Coverage

### Definition and Contrast

| | Cryptography | Steganography |
|---|---|---|
| Goal | Makes message *unreadable* | Hides *existence* of the message |
| Visibility | Ciphertext obviously looks encrypted | Stego object looks like a normal file |

### Core Process

`Payload + Cover Object → Stego Object`

Exploits **redundancy** in cover data (the parts that can be changed without perceptible effect).

### LSB (Least Significant Bit) Algorithm

- Changing the LSB of a pixel byte changes its value by only ±1 — visually imperceptible
- Requires **lossless** image formats (PNG, BMP, TIFF) — lossy formats (JPEG) destroy the payload during compression
- **LSB Replacement:** payload bits directly replace cover LSBs (only ~50% of bits actually change)
- **LSB Matching:** if the LSB doesn't already match, randomly adjust pixel value ±1 (harder to detect statistically)
- Capacity: ~1 bit per pixel channel; larger payloads require modifying additional bits and become detectable

### Bit Planes

Each colour channel can be decomposed into 8 bit planes (one per bit position, 0=LSB to 7=MSB):
- Higher planes (7, 6) retain the visible image structure
- Lower planes (0, 1) appear as random noise — ideal for hiding data

### BPCS (Bit Plane Complexity Segmentation)

- Hides payload in **complex (noisy) regions** of any bit plane, not just the LSB plane
- Complexity: `c = actual changes / 112` for an 8-byte block (max 112 horizontal + vertical transitions)
- Threshold **T ≈ 0.3**: segments with `c > T` are complex (usable)
- **Conjugation:** payload blocks that are not naturally complex enough are XOR'd with a chequerboard pattern before hiding; a flag bit records this for reversal
- Much higher capacity than LSB (~50% vs ~12% of image); lower detectability

### Steganalysis

- **Primary objective:** detect presence of a hidden payload
- **Secondary objective:** extract the payload

Techniques:
- **Visual:** even/odd pixel filtering (even=black, odd=white) reveals LSB patterns
- **Statistical:** analyse pixel value distribution for anomalies introduced by embedding
- **Difference imaging:** compare original vs suspected stego to find altered pixels
- **Tool-based:** automated tools (StegExpose, Stegdetect, QuickStego)

### Implementation Note

Typically implemented in Python using `cv2` (OpenCV) for image I/O and `numpy` for bit-level array manipulation.

---

## Linked Concepts

- [[concepts/steganography]] — full concept page: LSB (Replacement/Matching), BPCS, steganalysis, historical use, OpenCV implementation notes
- [[concepts/opencv-core]] — cv2 image handling used in steganography implementations
