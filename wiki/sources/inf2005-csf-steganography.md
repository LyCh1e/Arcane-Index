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

---

## Transcript Additions (Live Lecture — Lec02)

*Source: `raw/INF2005 CSF - Lec02 Steganography_transcript.md`*

The live lecture opened with a cryptography recap before covering steganography. Key additions not fully captured in the slide deck:

### Cryptography Recap — TLS/HTTPS: All Three Primitives in Practice

Dr Tan demonstrated live certificate inspection in the browser (SIT website + generic HTTPS sites) to show how all three cryptographic types combine in everyday browsing:

| TLS Component | Primitive | Example observed |
|---------------|-----------|-----------------|
| Key exchange (server's public key) | Asymmetric (RSA 2048) | Certificate from Amazon CA |
| Bulk data encryption | Symmetric (AES-128) | Visible in the connection security details |
| Certificate signature + integrity | Hashing (SHA-256) | Shown on all inspected certificates |

**Why both asymmetric and symmetric?** Asymmetric (RSA/ECC) is much slower than symmetric (AES). Using asymmetric to encrypt bulk page content would be prohibitively slow. So:
1. Browser verifies certificate → gets server's **public key**.
2. Browser generates a random **session key** → encrypts it with the server's public key → sends it.
3. Server decrypts the session key with its **private key**.
4. All subsequent content is encrypted with AES using the session key (symmetric).

> "If you are using a symmetric key, the time taken will be much longer than symmetric key [asymmetric key]... that's why we have both."

**SSL → TLS:** The original protocol (SSL, Secure Socket Layer) had critical flaws (Heartbleed). It has been replaced by TLS (Transport Layer Security). "SSL certificate" remains colloquial for what is now a TLS certificate.

**Hashing for download integrity (concrete application):**

> "If you go to any download site, the proper one, they also provide you a hash string. To ensure that when you download it, it's not tampered with. You can actually hash this downloaded file and see whether the hash value matches."

This is the CIA "Integrity" pillar in practice: the publisher provides a reference hash; the user recomputes it on the downloaded file; a match gives high confidence the file was not altered in transit or on the server.

### LSB Matching — Boundary Conditions

When randomly choosing ±1, edge cases at the byte extremes must be handled:

| Pixel value | Problem | Rule |
|-------------|---------|------|
| **0** | Subtracting 1 borrows into higher bits → many bits change → anomaly obvious to steganalyst | **Always add 1** |
| **255** | Adding 1 overflows (wraps to 0) → many bits change | **Always subtract 1** |
| 1–254 | No overflow/underflow risk | Choose +1 or −1 randomly |

> "If you say the zero, you cannot do minus. Imagine if you do a minus, a lot of bits will be changed — you're creating a more obvious sign to the observer that something has been changed. Same for 255 — once you have 255, of course you do a minus 1."

### Terminator String

Because the payload is typically much smaller than the cover object, extraction must know when to stop without reading every pixel:

- The **terminator string** (e.g., `====`, or any agreed-upon short sentinel sequence) is embedded immediately after the payload's last bit.
- During decoding, the program reads bits and reconstructs characters until it encounters the terminator, then stops.
- **Why not read everything?** For a large cover image the performance cost of extracting and interpreting every bit is significant. The terminator allows early exit.
- **Marker selection:** avoid characters that could legitimately appear in the payload; a short unique sequence (2–4 characters) is sufficient. The marker must be agreed between encoder and decoder.

### File Size and Hash After LSB Embedding

**File size:** LSB steganography *replaces* bits that are already part of the cover file — no bytes are added. The stego object has exactly the same file size as the cover object.

> "You are just changing a bit. The bit is originally there, so you're just doing a replacement. The size capacity is already there."

Demonstrated live with a hex editor: original vs stego images — file size identical.

**Hash changes:** despite the same file size, the file hash changes completely even if only a single bit differs.

> "The best hashing algorithm — even you have a slight change, even one bit of change, your output will look totally different. As long as content has changed, the hashing will definitely change."

This is an important property: size equality does not imply content equality. A forensic analyst who only checks file size will miss LSB embedding.

### Real-World Espionage Case — JPEG EOF Injection

Dr Tan shared a documented espionage case (agent spying for China) that used a non-LSB steganographic technique:

**Method:**
1. A JPEG image was converted to its binary representation.
2. The payload was appended **after the JPEG EOF marker** (byte sequence `0xFF 0xD9`).
3. A start marker and an end marker (`88` in the transcript) framed the payload within the extra bytes.
4. Any image viewer reads from the file header to the EOF marker and renders the image normally; bytes beyond the marker are silently ignored.

**Why it appeared innocent:** the image rendered correctly; no visible changes; even a casual security review would just see a valid image file.

**Detection vector — file size anomaly:**

> "The image is only, say, 1024 × 1034. Why is the file size so large? You can do a rough estimation. If the size doesn't quite match the resolution, it gives you an alert."

File size ≈ width × height × bytes_per_pixel (for lossless formats). If actual size >> calculated expected size, extra data exists somewhere in the file.

**Why LSB is superior:** an LSB-embedded image has the same file size as the cover, and all data occupies byte positions already expected by the format — there is no "extra bytes after EOF" anomaly. The operative apparently did not know about LSB.

### Steganalysis — Histogram Analysis

When comparing a cover object to a stego object, pixel-value histograms show characteristic spikes at certain values. A preliminary steganalysis workflow:

1. Compute the pixel-value histogram of the suspected stego image.
2. If spikes are present at values that would not arise naturally (e.g., even/odd clustering in LSB Replacement), this is a hint that embedding occurred.
3. Limitation: a spike in isolation is inconclusive — some natural images also have histogram spikes. Confirmation requires either the original cover or a more sophisticated statistical test.

> "Before, there's already some spikes, and after, the spikes go higher. Without the stego object — if you are only given one object — there's actually no way of telling."

---

## Linked Concepts

- [[concepts/steganography]] — full concept page: LSB (Replacement/Matching), BPCS, steganalysis, historical use, OpenCV implementation notes
- [[concepts/public-key-cryptography-and-key-exchange]] — TLS hybrid cryptography; RSA key exchange; session keys
- [[concepts/opencv-core]] — cv2 image handling used in steganography implementations
