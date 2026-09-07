---
type: source
title: "INF2005 Cyber Security Fundamentals — Cryptography 1: Key Concepts (Symmetric Cryptography)"
source: "raw/INF2005 Cyber Security Fundamentals - Crypto1 Key Concepts.md"
domain: cryptography
tags: [inf2005, cryptography, symmetric, DES, AES, OTP, kerckhoffs, substitution, transposition]
created: 2026-09-07
lecturer: "Dr Tan Kheng Leong"
---

# Source Index — INF2005 CSF: Cryptography 1

**Module:** INF2005 Cyber Security Fundamentals  
**Lecturer:** Dr Tan Kheng Leong  
**Topic:** Key Concepts — Symmetric Cryptography  
**Raw file:** `raw/INF2005 Cyber Security Fundamentals - Crypto1 Key Concepts.md`

---

## Coverage

### Basic Model

- Plaintext → cipher with key → ciphertext → decipher with same key → plaintext
- Cryptography primarily supports **Confidentiality** (CIA triad); hashing/signatures extend to Integrity and Authentication
- Threat model: Alice → Eve (eavesdropper on channel) → Bob

### Types of Cryptography

| Type | Key mechanism | Example |
|------|--------------|---------|
| Symmetric | Same key both directions | AES, DES |
| Asymmetric | Public key encrypts, private key decrypts | RSA |
| Hashing | No key; one-way | SHA-256, MD5 |

### Classical Ciphers

- **Substitution — monoalphabetic:** Caesar cipher (shift of 3: `HELLO` → `KHOOR`)
- **Substitution — polyalphabetic:** Vigenère cipher (repeating keyword, e.g. `ALICE` + `HELLO` → `HPTNS`)
- **Transposition — simple:** reverse (`UNIVERSITY` → `YTISREVINU`)
- **Transposition — Rail Fence:** zig-zag rails (`HELLOBOB`, rail=2 → `HLOOELBB`)
- **Transposition — Columnar:** grid write, column-order read by keyword (`RED` key: `HELLOWORLD` → `LWLX EORX HLOD`)

### Kerckhoffs's Principle

Security rests on key secrecy, not algorithm secrecy. Even if an attacker knows the algorithm (Caesar, AES), they cannot decrypt without the key.

### Modern Symmetric Algorithms

| Algorithm | Key | Block | Rounds | Status |
|-----------|-----|-------|--------|--------|
| DES | 56-bit eff. | 64-bit | 16 | Broken 2002 |
| 3DES | 168-bit (K1, K2, K3) | 64-bit | 48 | Deprecated 2024 |
| AES-128/192/256 | 128/192/256-bit | 128-bit | 10/12/14 | Current |

### One-Time Pad (OTP)

- Key ≥ length of plaintext; used only once; must be truly random
- Theoretically unbreakable; impractical at scale
- Real-world OTP analogues: 2FA codes, OTP dongles

### Randomness

- **True randomness (entropy):** physical unpredictability (mouse movement, electrical/fan noise)
- **Pseudo-random:** deterministic formula + seed — security weakness if used for crypto keys

---

## Linked Concepts

- [[concepts/classical-ciphers-and-cryptanalysis]] — detailed treatment of substitution, transposition, frequency analysis, encodings
- [[concepts/symmetric-encryption]] — DES, 3DES, AES architecture, OTP, Kerckhoffs, block cipher modes
