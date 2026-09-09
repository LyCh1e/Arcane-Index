---
type: concept
title: "Steganography"
aliases: ["LSB steganography", "BPCS", "steganalysis", "information hiding", "steganography vs cryptography"]
tags: [steganography, information-hiding, LSB, BPCS, steganalysis, image-processing, security, inf2005]
created: 2026-09-07
updated: 2026-09-09
status: established
domain: cryptography
---

# Steganography

**Steganography** is the practice of concealing the *existence* of a message by hiding it within ordinary, non-secret data (a "cover object"). It differs fundamentally from cryptography:

| | **Cryptography** | **Steganography** |
|---|---|---|
| Goal | Make a message *unreadable* | Hide the *existence* of a message |
| Visibility | Ciphertext is obviously "encrypted looking" | The stego object looks like an ordinary file |
| Security model | Assumes the attacker knows something is hidden | Relies on the attacker not noticing anything is there |

The two are complementary, not mutually exclusive. Encrypting a message and then hiding it steganographically provides both confidentiality (content is unreadable) and obscurity (presence is concealed).

> **One-line definition:** Steganography hides a message inside ordinary-looking data so that only the intended recipient knows the message exists at all.

---

## Core Process

```
Payload  +  Cover Object  →  Stego Object
```

| Term | Definition |
|------|-----------|
| **Payload** | The secret data to be hidden |
| **Cover object** | The carrier medium: an image, audio file, video, or text document |
| **Stego object** | The output file — visually/audibly indistinguishable from the cover, but containing the hidden payload |

Steganography exploits **redundancy** in cover data — portions of a file that can be modified without producing a perceptible change. The most commonly used cover medium is digital images.

---

## Least Significant Bit (LSB) Algorithm

### Why it works

A digital image stores each pixel channel (R, G, B) as a byte (0–255). The **most significant bit** (MSB) at position 7 contributes 128 to the channel value; the **least significant bit** (LSB) at position 0 contributes only 1. Flipping the LSB changes the pixel value by just ±1 — a change completely invisible to the human eye.

### Constraint: lossless formats only

LSB steganography requires **lossless compression** formats: **PNG**, **BMP**, **TIFF**. Lossy formats (JPEG) re-quantise pixel values during compression, destroying the embedded LSB bits.

### LSB Replacement

The payload's bits (read from its MSB) directly replace the LSBs of successive cover-image pixel bytes.

```
Payload byte (letter G):  0 1 0 0 0 1 1 1
Cover pixel bytes:        [... various values ...]
→ Replace each pixel's LSB with one payload bit in sequence
```

On average, only ~50% of cover LSBs actually change (half the time they already match the payload bit). This characteristic is detectable by statistical analysis.

### LSB Matching

Instead of a direct bit replacement, if a pixel's LSB does not already match the required payload bit, the pixel value is randomly adjusted by **+1 or −1** until its LSB matches.

- Produces a less detectable result — avoids the asymmetric "flip only" pattern that LSB Replacement creates.
- Still limited to lossless formats.

### Capacity vs Detectability

If the payload is too large, more bits per pixel must be used (2nd LSB, 3rd LSB, …), progressively degrading image quality and increasing statistical detectability. The usable capacity of pure LSB encoding is approximately **1 bit per pixel channel** — or 3 bits per colour pixel.

---

## Bit Planes

An image can be decomposed into **8 bit planes** per colour channel — one for each bit position (0 = LSB through 7 = MSB):

| Bit plane | Visual appearance | Significance |
|-----------|-----------------|--------------|
| 7 (MSB) | Closely resembles the original image | Most perceptually significant |
| 6–4 | Gradually coarser approximation | Medium significance |
| 3–0 (LSB region) | Appears as random noise | Least perceptually significant |

Because lower bit planes look like noise, hiding data in them (or in genuinely noisy regions of higher planes) is visually undetectable.

---

## Bit Plane Complexity Segmentation (BPCS)

BPCS improves on simple LSB by hiding payload data in **complex (noisy) regions of any bit plane**, not just the LSB plane. This dramatically increases capacity while maintaining visual quality.

### Complexity Measure

Complexity `c` of an 8-byte segment = (number of bit-value changes between adjacent pixels) / (maximum possible changes).

- Maximum changes for an 8-byte block = `2 × 8 × 7 = 112` (horizontal and vertical transitions).
- `c = actual_changes / 112`
- A complexity **threshold T ≈ 0.3** classifies segments: `c > T` → complex (usable for hiding).

### Conjugation

If a payload block is not complex enough to blend into a complex segment (it would look out of place), a **conjugation** operation (XOR with a chequerboard-like pattern) transforms it into a complex block, which is then hidden instead. A flag bit records that conjugation was applied, so the receiver can reverse it.

### BPCS Algorithm (pseudocode)

```
While more payload remains:
    Get the next bit plane
    While space remains in the current bit plane:
        Get the next complex segment from the bit plane
        Get the next block of payload
        If payload block is complex (c > T):
            Hide it directly in the segment
        Else:
            Conjugate the payload block, then hide it in the segment
```

### BPCS vs LSB

| Feature | LSB | BPCS |
|---------|-----|------|
| Planes used | LSB plane only | Any plane (complex regions) |
| Capacity | Low (~12% of image) | High (~50%+ of image) |
| Detectability | Higher — LSB statistics are disturbed | Lower — exploits naturally noisy regions |
| Complexity | Simple to implement | More complex; requires complexity measurement and conjugation |

---

## Steganalysis

**Steganalysis** is the discipline of detecting (and extracting) steganographic content — the attacker-side counterpart to steganography.

### Primary vs Secondary Objectives

- **Primary:** detect whether a payload is present.
- **Secondary:** extract the payload.

### Techniques

| Method | Description |
|--------|-------------|
| **Visual steganalysis** | Filtering tricks that make hidden bits visible to the human eye — e.g. showing even-valued pixels as black and odd-valued as white reveals an LSB payload as a pattern that wouldn't appear in a natural image |
| **Difference imaging** | Compare the suspected stego image against the original cover; altered pixels appear in the difference image |
| **Statistical steganalysis** | Compare pixel value distributions against expected natural-image statistics; LSB Replacement creates a characteristic histogram asymmetry (pair-of-values effect) |
| **Structural analysis** | Detect BPCS or other algorithm-specific structural artefacts in complex regions |
| **Tool-based** | Automated steganalysis software (e.g. StegExpose, Stegdetect) |

### Limits

Steganalysis is fundamentally a detection problem. A sufficiently small payload embedded with a well-designed algorithm (e.g. BPCS with a low T threshold and short payload) may be statistically indistinguishable from unmodified cover data.

---

## Historical and Real-World Context

- **Acrostics** — words hidden in the first letters of lines; Lewis Carroll's *Through the Looking-Glass* (1871) contains an acrostic spelling "Alice Pleasance Liddell."
- **Wartime use** — invisible ink, microdots hidden in newspaper full stops.
- **Digital espionage** — real intelligence cases have documented steganography use for covert communications.
- **Tool reference:** QuickStego — a freely available GUI for basic image-based LSB steganography.
- **Further reading:** Bruce Schneier's writing on steganography (schneier.com).

---

## Implementation Note (Python / OpenCV)

LSB steganography implementations typically use:
- `cv2` (OpenCV) for image I/O (`cv2.imread`/`cv2.imwrite` with PNG to preserve LSBs)
- `numpy` for bit-level manipulation (converting text to binary, slicing and replacing LSBs via array indexing)

See also [[concepts/opencv-core]] for `cv::Mat` and the CV type system used in such implementations.

---

## Applied: engineering an LSB stego *verification* tool

Worked build in [[examples/inf2005-acw1-stego-verification]] (INF2005 ACW1) — a stego
tool whose job is not covert messaging but **integrity + authenticity verification** of
image and audio files. Reusable design points beyond the textbook algorithm:

- **Cover → flat "carrier" abstraction.** Reduce any format to a mutable byte array of
  "units": image = every R/G/B[/A] channel byte; 16-bit PCM audio = the **low byte only**
  of each little-endian sample (the high byte carries most perceptual weight — leave it
  alone). All bit-twiddling then works on one array regardless of media.
- **Selectable bit depth (1–8 LSBs).** `mask_clear = (0xFF << n) & 0xFF` clears the low
  `n` bits; capacity in bytes = `available_units * n // 8`; units needed =
  `ceil(payload_bits / n)`. Depth is a GUI control (higher = more capacity, more
  audible/visible, more detectable).
- **Don't embed at unit 0.** A fixed start offset is exactly what a steganalyst checks
  first. Derive a secret per-file offset:
  `offset = HMAC-SHA256(secret_key, salt ‖ "OFFSET") mod range`, XOR-encrypt it with a
  second HMAC keystream, and cover the locator header with an HMAC tag so a wrong key
  fails loudly before any capsule bytes are read.
- **Two independent integrity checks.** An RSA-PSS **signature over the payload** catches
  edits to the *hidden* bytes; a SHA-256 **hash of the carrier with the stego regions
  blanked to 0x00** (computed identically by encoder and verifier) catches edits to the
  *visible/audible* content. Sign a **canonical JSON** serialization (sorted keys, no
  whitespace) so both sides hash byte-identical data.
- **Capacity check first.** Reject an over-large payload (`is payload > cover capacity?`)
  before writing anything.
- **Verdict, not boolean.** `Authentic` / `Tampered` / `Signature Invalid` /
  `Payload Missing` / `Wrong Start Location` / `Cannot Verify` — each maps to a specific
  failed check.

---

## Key Connections

- [[concepts/opencv-core]] — image I/O, pixel access, bit manipulation in OpenCV used for LSB implementation
- [[concepts/digital-image-processing]] — bit planes, pixel value distributions, image statistics
- [[concepts/classical-ciphers-and-cryptanalysis]] — cryptography as the complementary layer (encrypt-then-hide)
- [[concepts/public-key-cryptography-and-key-exchange]] — RSA-PSS signatures used to authenticate a hidden payload
- [[concepts/cryptographic-hash-functions]] — SHA-256 / HMAC for tamper detection and keyed start-location derivation
- [[examples/inf2005-acw1-stego-verification]] — applied build: signed-payload LSB verification tool
- [[areas/cryptography]] — parent area
