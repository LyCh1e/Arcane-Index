---
type: concept
title: "Symmetric Encryption — Modern Block and Stream Ciphers"
aliases: ["DES", "3DES", "AES", "One-Time Pad", "OTP", "block cipher", "symmetric key", "Kerckhoffs"]
tags: [cryptography, symmetric, DES, AES, 3DES, OTP, block-cipher, kerckhoffs, inf2005]
created: 2026-09-07
updated: 2026-09-07
status: established
domain: cryptography
---

# Symmetric Encryption — Modern Block and Stream Ciphers

**Symmetric encryption** uses a single shared key for both encryption and decryption:

```
ENCRYPT(plaintext, K) → ciphertext
DECRYPT(ciphertext, K) → plaintext
```

Both parties must hold `K`. The fundamental challenge is **key distribution** — how to securely share the key before any secure channel exists. This is the problem that asymmetric cryptography solves (see [[concepts/public-key-cryptography-and-key-exchange]]).

> **One-line definition:** Symmetric encryption uses one secret key to lock and unlock a message — fast and secure for bulk data, but requires a pre-shared key.

---

## Kerckhoffs's Principle

> "The security of a cryptosystem must not depend on the secrecy of the algorithm; it should rest entirely on the secrecy of the **key**."
> — Auguste Kerckhoffs (1883), restated by Claude Shannon as "the enemy knows the system"

**Implication:** A cipher should be open for public scrutiny. If its security depended on secrecy of the algorithm, discovery of that algorithm would instantly compromise all encrypted data. Security through obscurity fails as soon as the algorithm leaks. Only the key is practical to keep secret.

This is why AES and other modern ciphers are publicly specified — but remain secure.

---

## The Threat Model

- **Alice** sends an encrypted message to **Bob** over an insecure channel.
- **Eve** (eavesdropper) can intercept the ciphertext but not the key.
- Goal: Eve sees ciphertext but cannot recover plaintext without `K`.

---

## Modern Symmetric Algorithms

### DES — Data Encryption Standard

| Property | Value |
|----------|-------|
| Key length | 56 bits effective (64-bit key, 8 parity bits discarded) |
| Block size | 64 bits |
| Structure | 16 rounds of substitution, transposition, and XOR with a 48-bit round sub-key |
| Status | **Broken** — cracked in <24 hours by networked computing in 2002; do not use |

DES was published by NIST in 1977. Each of its 16 rounds applies:
1. An **expansion permutation** (32-bit half-block → 48 bits)
2. XOR with the round's 48-bit sub-key
3. Eight **S-box substitutions** (non-linear; primary source of security)
4. A **P-box permutation** (diffuses the bits)

The small 56-bit key space (2⁵⁶ ≈ 72 quadrillion keys) is its fatal weakness.

### 3DES — Triple DES

| Property | Value |
|----------|-------|
| Key length | 168 bits (three independent 56-bit DES keys K1, K2, K3) |
| Block size | 64 bits (inherited from DES) |
| Operation | Encrypt–Decrypt–Encrypt: `EK1 → DK2 → EK3` |
| Decryption | Reverse: `DK3 → EK2 → DK1` |
| Status | **Deprecated** from 2024 (NIST SP 800-131A); 64-bit block size vulnerable to birthday attacks at ≥ 32 GB of data under the same key |

The EDE (Encrypt–Decrypt–Encrypt) structure means that if K1 = K2 = K3, 3DES degrades to single DES — a backwards-compatibility property.

### AES — Advanced Encryption Standard

| Property | Value |
|----------|-------|
| Key length | 128 / 192 / 256 bits (AES-128, AES-192, AES-256) |
| Block size | 128 bits (fixed) |
| Rounds | 10 (128-bit key), 12 (192-bit key), 14 (256-bit key) |
| Status | **Current standard** — no practical attack; theoretically vulnerable to large-scale quantum computing (Grover's algorithm halves effective key length, so AES-256 would have ~128-bit quantum security) |

Each AES round applies four operations to a 4×4 byte state array:
1. **SubBytes** — non-linear byte substitution via an S-box (provides confusion)
2. **ShiftRows** — cyclic row shifts (spreads data across columns)
3. **MixColumns** — linear transformation of each column (provides diffusion) — omitted in the final round
4. **AddRoundKey** — XOR with the round key derived from key expansion

### Comparison Summary

| Algorithm | Key (bits) | Block (bits) | Rounds | Status |
|-----------|-----------|--------------|--------|--------|
| DES | 56 | 64 | 16 | Broken (2002) |
| 3DES | 168 | 64 | 48 (16×3) | Deprecated (2024) |
| AES-128 | 128 | 128 | 10 | Current standard |
| AES-256 | 256 | 128 | 14 | Current standard |

---

## Block Cipher Modes of Operation

A block cipher alone encrypts a single fixed-size block. **Modes** define how to apply the cipher to arbitrary-length messages:

| Mode | Description | Weakness / Notes |
|------|-------------|------------------|
| **ECB** (Electronic Codebook) | Each block encrypted independently | Same plaintext block → same ciphertext block; patterns leak (penguins in ECB) — never use |
| **CBC** (Cipher Block Chaining) | Each block XOR'd with previous ciphertext before encryption; IV needed | Sequential; padding oracle attacks if IV is predictable |
| **CTR** (Counter) | Block cipher encrypts a counter → keystream XOR'd with plaintext | Turns block cipher into a stream cipher; parallelisable; nonce must never repeat |
| **GCM** (Galois/Counter Mode) | CTR + authentication tag (AEAD) | Industry standard for authenticated encryption; used in TLS 1.3, AES-GCM |

---

## One-Time Pad (OTP)

| Property | Requirement |
|----------|------------|
| Key length | At least as long as the plaintext |
| Key reuse | Never — each key used exactly once, then destroyed |
| Randomness | Key must be **truly random** (not pseudorandom) |

The OTP is **theoretically unbreakable** (Shannon's perfect secrecy) — given any ciphertext, there exists a valid key that maps it to every possible plaintext of the same length, so no information is leaked. The cost is practicality: key management at scale is infeasible since each message needs a fresh, truly-random key of equal length.

**Real-world OTP analogues:** hardware OTP tokens (RSA SecurID), TOTP codes in 2FA apps, bank OTP cards.

---

## Randomness and Entropy

| Type | Description | Security |
|------|-------------|---------|
| **True RNG (TRNG)** | Entropy sourced from physical/environmental unpredictability: mouse movement, fan/electrical noise, thermal noise, radioactive decay | Truly random — suitable for cryptographic key generation |
| **Pseudo-RNG (PRNG)** | Deterministic mathematical algorithm seeded by an initial value; output is predictable if the seed is known | Not cryptographically secure unless specifically designed (CSPRNG) |
| **CSPRNG** | Cryptographically Secure PRNG — passes statistical randomness tests and is computationally infeasible to predict without the seed | Acceptable for most crypto use — used in OS entropy pools (e.g. `/dev/random`, CryptGenRandom) |

**Security implication:** Using a PRNG where a TRNG or CSPRNG is required (e.g. generating OTP keys, nonces, session tokens) is a critical vulnerability — an attacker who knows the algorithm and seed can predict all "random" outputs.

---

## Key Connections

- [[concepts/classical-ciphers-and-cryptanalysis]] — historical predecessors (Caesar, Vigenère, transposition), cryptanalysis techniques (brute force, frequency analysis)
- [[concepts/public-key-cryptography-and-key-exchange]] — asymmetric crypto solves the symmetric key distribution problem; in practice both are combined (asymmetric establishes session key, symmetric encrypts bulk data)
- [[concepts/cryptographic-hash-functions]] — one-way functions; distinct from encryption (hash is irreversible)
- [[areas/cryptography]] — area overview
