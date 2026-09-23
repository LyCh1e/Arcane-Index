---
type: study-notes
title: "INF2005 Cyber Security Fundamentals — Formula Sheet"
module: INF2005
tags: [study-notes, inf2005, cyber-security, formula-sheet, cheat-sheet, exam-prep]
created: 2026-09-21
updated: 2026-09-21
---

# INF2005 CSF — Formula & Quick-Reference Sheet

→ Full notes: [[INF2005 - Cyber Security Fundamentals Exam Notes]]

---

## CIA Triad

| C | I | A |
|---|---|---|
| Confidentiality | Integrity | Availability |
| Encryption | Hashing / Signatures | Backups / Redundancy |

---

## Cryptography Types

| Symmetric | Asymmetric | Hashing |
|-----------|-----------|---------|
| 1 shared key | Key pair (pub + priv) | No keys |
| Fast | Slow | One-way only |
| DES / 3DES / AES / OTP | RSA / DH | MD5 / SHA-1 (broken) · SHA-2 (secure) |

---

## Key Lengths & Status

| Algorithm | Key | Block | Status |
|-----------|-----|-------|--------|
| DES | 56-bit | 64-bit | ❌ Broken |
| 3DES | 168-bit | 64-bit | ⚠️ Deprecated 2024 |
| AES | 128/192/256-bit | 128-bit | ✅ Current |
| MD5 | — | 128-bit digest | ❌ Broken |
| SHA-1 | — | 160-bit digest | ❌ Broken |
| SHA-256 | — | 256-bit digest | ✅ Secure |

---

## Kerckhoffs's Principle

> Security rests on the **key** alone — never on secrecy of the algorithm.

---

## RSA Key Generation (6 Steps)

```
1. Pick two large primes p, q
2. n = p × q
3. φ(n) = (p−1)(q−1)
4. Pick e: 1 < e < φ(n), gcd(e, φ(n)) = 1
5. d × e ≡ 1 mod φ(n)
6. Public key = (e, n)   Private key = (d, n)
```

Encrypt/decrypt use mod **n**. Generation uses mod **φ(n)**.

---

## Diffie–Hellman

```
Public: prime p, generator G
Alice: a → A = G^a mod p
Bob:   b → B = G^b mod p
Exchange A and B
Shared secret K = B^a mod p = A^b mod p = G^(ab) mod p
```

DH ≠ encryption. It establishes a **shared key**.

---

## Digital Signature Flow

```
Sign:    Hash(doc) → Encrypt with sender's PRIVATE key → Signature
Verify:  Decrypt signature with sender's PUBLIC key
         Hash received doc
         Compare hashes → match = authentic + intact
```

---

## Asymmetric Role Rules

```
Confidentiality → encrypt with RECIPIENT's public key
Authentication  → encrypt with SENDER's private key
Both            → sign (priv) then seal (recipient's pub) — two passes
```

---

## Birthday Attack

> Collision resistance ≈ 2^(n/2) operations for an n-bit digest.
> Short digests (MD5 128-bit → effectively 2^64 work) are too easy to collide.

---

## Steganography Formula

```
Core process: Payload + Cover Object → Stego Object
```

**BPCS complexity:**
```
c = (bit transitions in segment) / 112
    where 112 = 2 × 8 bytes × 7 max transitions/byte
c > T (T ≈ 0.3) → segment is "complex" → usable for hiding
```

**LSB variants:**
- **Replacement** — directly overwrite LSB with payload bit → statistically detectable
- **Matching** — ±1 pixel value to match payload bit → harder to detect

**LSB constraint:** lossless formats only (PNG, TIFF, BMP). JPEG destroys embedded bits.

---

## Password Storage (Best → Worst)

```
✅ Hash(password + salt)   ← Salt defeats rainbow tables
⚠️ Hash(password)          ← Vulnerable to precomputed tables
⚠️ Encrypt(password)       ← Reversible if key is compromised
❌ Plaintext               ← Immediate total exposure
```

---

## Authentication Factors

| Factor | Basis | Examples |
|--------|-------|---------|
| Knowledge | Know | Password, PIN, graphical |
| Token | Have | Smart card, eToken, RFID |
| Biometrics | Are | Fingerprint, iris, face, gait |

---

## Biometric Accuracy Metrics

- **FAR** — False Accept Rate → impostors granted access (→ 0 ideally)
- **TAR** — True Accept Rate → legitimate users granted access (→ 1 ideally)
- **ROC curve** — TAR vs FAR tradeoff; higher TAR = higher FAR

---

## Access Control Models

| Model | Who controls | Mechanism | Pitfall |
|-------|-------------|-----------|---------|
| DAC | Resource owner | ACLs | Over-sharing |
| RBAC | Admin (by role) | Role assignment | Role Creep |
| MAC | OS (labels) | Classification + Category | High overhead |

---

## BPCS Algorithm (Pseudocode)

```
While payload remains:
    Get next bit plane
    While space in bit plane:
        Get next complex segment
        Get next payload block
        If payload block is complex → hide directly
        Else → conjugate (XOR) payload, then hide
```

---

## Pen Testing Stages

```
1. Reconnaissance  → Whois, Google Dorking, OSINT (passive or active)
2. Scanning        → Nmap/Zenmap, ping sweep, banner grabbing, Nessus
3. Enumeration     → Services, accounts, CVE/NVD/Exploit-DB
4. Gaining Access  → Metasploit, EternalBlue, Wireshark, Hydra
5. Maintaining     → Backdoors (Netcat), rootkits, hidden accounts, startup scripts
6. Covering Tracks → Log cleanup; ethical = restore target to original state
```

---

## Hacker Hats

| White ⚪ | Gray 🩶 | Black ⚫ |
|---------|---------|---------|
| Authorised | Partially | Unauthorised |
| Reports findings | Crosses ethical lines | Malicious intent |

**Key word in Singapore CMA:** *"unauthorised"* — this is what makes it a crime.

---

## Graphical Password Space

```
Recognition-based: (images per challenge set)^(rounds)
e.g. 1 of 9 images × 5 rounds = 9^5 = 59,049 combinations
```

---

## Common Exam Mistakes (10-point checklist)

- [ ] Transposition ciphers ARE vulnerable to frequency analysis
- [ ] DH is key exchange — NOT encryption
- [ ] RSA generation uses φ(n); encrypt/decrypt use n
- [ ] Signature = hash + private-key encryption (hash alone is NOT a signature)
- [ ] MD5 and SHA-1 are broken
- [ ] Salt defeats rainbow tables; encryption alone does not
- [ ] LSB steganography requires lossless format (not JPEG)
- [ ] Authentication ≠ Authorisation (different stages)
- [ ] RBAC requires ongoing review to prevent Role Creep
- [ ] Ethical hacking requires **legal authorisation**, not just good intentions
