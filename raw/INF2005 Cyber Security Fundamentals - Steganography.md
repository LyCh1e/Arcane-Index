# Steganography

*Cyber Security Fundamentals — Dr Tan Kheng Leong*

## 1. Hiding in Plain Sight

- To be unnoticeable or inconspicuous by **staying visible** in a setting that masks your presence (like camouflage gear blending into a natural environment).
- **Steganography** — the practice of concealing messages or information within other non-secret text or multimedia data.

## 2. Steganography vs. Cryptography

| | Cryptography | Steganography |
|---|---|---|
| Goal | Makes a message unreadable | Hides the **existence** of the message |
| Visibility | Ciphertext is visible (obviously "encrypted-looking") | The stego object looks like an ordinary file — nothing appears hidden |

> Stego attempts to hide the **presence** of a message; crypto doesn't — it just hides the *content*.

## 3. Historical Example: Acrostics

- An **acrostic** is a poem with a "hidden word" formed from the first letter of each line.
- Example: in *Through the Looking-Glass* (1871), the closing poem "A boat, beneath a sunny sky" is an acrostic spelling out **Alice Pleasance Liddell** — the real girl Alice was based on.

## 4. The Steganography Process

```
Payload + Cover Object → Stego Object
```

- **Payload** — the secret data you want to hide
- **Cover Object** — the carrier used to hide the payload (e.g. image, audio/video, text file — suitability varies)
- **Stego Object** — the resulting file, containing the hidden payload, that looks like an ordinary cover object

Steganography's underlying principle is **security by obscurity**: it exploits redundancy in the cover data (i.e. parts of the file that can be altered without a noticeable change) to hide information.

## 5. Least Significant Bit (LSB) Algorithm

- In a digital image, each pixel channel (R, G, B) is stored as a byte, with a **Most Significant Bit (MSB)** and a **Least Significant Bit (LSB)**.
- **LSB algorithm**: hides the payload by replacing the *least significant bit(s)* of each cover-image pixel byte with payload bits.
  - Changing only the rightmost bit of a byte causes a minimal, usually unnoticeable, change to the pixel's value/color.
  - If the payload is too large, the algorithm has to modify further bits (2nd LSB, 3rd LSB...), and eventually the changes may become noticeable to an attacker.

### Constraints
- LSB only works reliably on **lossless-compression** image formats (PNG, TIFF, BMP) — compression here does not discard or alter pixel data. Lossy formats (like JPEG) can destroy the hidden LSB data.
- Two main variants: **LSB Replacement** and **LSB Matching**.

### LSB Replacement
- The payload's bits (read from MSB onward) directly **replace** the LSBs of the cover image's pixel bytes.
- Example: hiding the letter `G` (`01000111`) — on average, only **50%** of the cover image's LSB bits actually change (since roughly half the time the LSB already matches the payload bit).

### LSB Matching
- Instead of a direct bit replacement, if a pixel's LSB doesn't already match the required payload bit, the pixel value is randomly adjusted by **+1 or −1** until the LSB matches.
- This produces a statistically less detectable result than straight replacement, since it avoids a hard "flip" pattern.

*(Implementation in Python uses `cv2` (OpenCV) for image handling and `numpy` for array/bit-level manipulation — converting data to binary, then embedding/extracting the payload bit by bit.)*

**Example tool:** QuickStego (freely available application demonstrating basic image-based steganography).

## 6. Bit Planes

- Each color channel (R, G, B) of an image can be decomposed into **8 individual bit planes** — one for each bit position (0 = LSB, 7 = MSB) across all pixels.
- The **0th bit plane** of a channel = all the LSBs of that channel's bytes across the image.
- Lower-order bit planes (closer to the LSB) tend to look like random noise, while higher-order bit planes (closer to the MSB) retain the recognizable structure/shape of the image — this is why LSB changes are visually unnoticeable.
- Grayscale bit planes store intensity information; note that grayscale images can sometimes yield **higher classification accuracy** than RGB images in certain analysis contexts.

## 7. Bit Plane Complexity Segmentation (BPCS) Algorithm

- **Idea:** rather than always hiding data in the LSB plane, hide payload data in the **"complex" (noisy)** regions of *any* bit plane — since the human eye can't distinguish changes within already rapidly-varying (noisy) bit patterns.

**Process:**
1. Split the cover image into 8 bit planes.
2. Divide each bit plane into segments/blocks, and classify each as **complex** or **non-complex** (based on how "noisy" it looks).
3. Hide the payload in complex segments — this avoids visible image deterioration.
4. If a chunk of payload data itself is *not* complex enough to blend into a complex segment, perform **conjugation** (an XOR operation) to make it appear complex before hiding it.

**Algorithm (pseudocode):**
```
While there is more payload to hide:
    Get the next bit plane
    While there is more space in the current bit plane:
        Get the next complex segment
        Get the next block of payload
        If the payload block is complex:
            hide it in the current segment
        Else:
            conjugate (XOR) the payload block, then hide it in the current segment
```

### Measuring Complexity
- Complexity measures how often neighboring bits in a segment **change value**.
- For an 8-byte segment/block:
  - Count bit-value changes within each byte (max possible = 7 changes per byte, e.g. `10101010`).
  - Total maximum possible changes across the block = `2 × 8 × 7 = 112` (the factor of 2 accounts for both horizontal and vertical variations).
  - **Complexity** `c = actual changes / 112`.
- A **threshold T** (a tunable algorithm parameter, typically around **0.3**) determines the cutoff: if `c > T`, the segment is classified as **complex** (and can be used to hide payload).

## 8. Steganalysis (Attacking Steganography)

- **Steganalysis** is the attack/counter-discipline aimed at steganography.
  - **Primary objective:** detect the presence of a hidden payload.
  - **Secondary objective:** extract the hidden payload.
- Rationale: hiding information in digital media inevitably alters some content, which may introduce visual degradation or other unusual statistical characteristics.

### Techniques
- **Visual Steganalysis** — e.g. black-and-white filtering (even pixel values shown as black, odd as white) makes otherwise indistinguishable LSB changes visible; comparing an original image against a suspected stego-image can reveal a "difference image" highlighting altered pixels.
- **Statistical Steganalysis** — analyzes statistical irregularities in pixel-value distributions that stego-embedding tends to introduce.
- **Tool-based Steganalysis** — using dedicated software to automate detection.

## 9. Applied / Real-World Steganography

- Steganography has been used in real espionage and criminal cases (e.g. cases referenced involving hidden data used for covert communication).
- Further reading: Bruce Schneier's writing on steganography (schneier.com).

## Key Takeaways
- Steganography hides the **existence** of a message; cryptography hides its **content**. The two can be combined for layered protection.
- The core process is **Payload + Cover Object → Stego Object**.
- **LSB algorithms** (Replacement and Matching) exploit the fact that changing an image's least significant bits is visually imperceptible — but are limited to lossless formats and vulnerable if too much payload is embedded.
- **Bit planes** decompose an image into 8 layers of "significance"; higher bit planes hold the visible structure, lower ones look like noise — which is why noisy regions are ideal hiding spots.
- **BPCS** improves on simple LSB by hiding data in genuinely *complex* (noisy) image regions across any bit plane, using a complexity threshold (commonly ~0.3) and conjugation (XOR) when payload isn't naturally complex enough.
- **Steganalysis** is the attacking discipline — detecting and extracting hidden payloads via visual, statistical, or tool-based methods.
