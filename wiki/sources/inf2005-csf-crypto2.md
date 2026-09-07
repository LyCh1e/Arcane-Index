---
type: source
title: "INF2005 Cyber Security Fundamentals — Cryptography 2: Asymmetric Cryptography, Hashing & Cryptanalysis"
source: "raw/INF2005 Cyber Security Fundamentals - Crypto2 PK Attacks.md"
domain: cryptography
tags: [inf2005, cryptography, asymmetric, RSA, diffie-hellman, hashing, digital-signatures, birthday-attack, cryptanalysis]
created: 2026-09-07
lecturer: "Dr Tan Kheng Leong"
---

# Source Index — INF2005 CSF: Cryptography 2

**Module:** INF2005 Cyber Security Fundamentals  
**Lecturer:** Dr Tan Kheng Leong  
**Topic:** Asymmetric Cryptography, Hashing, and Cryptanalysis  
**Raw file:** `raw/INF2005 Cyber Security Fundamentals - Crypto2 PK Attacks.md`

---

## Coverage

### The Symmetric Key Distribution Problem

- Symmetric crypto requires the key to be shared before any secure communication — the chicken-and-egg problem.
- Asymmetric crypto solves this by using a mathematically linked key pair.

### Asymmetric Cryptography

| Goal | Encrypt with | Decrypt with |
|------|-------------|-------------|
| Confidentiality | Recipient's **public** key | Recipient's **private** key |
| Authentication | Sender's **private** key | Sender's **public** key |
| Both combined | Step 1: sender's private key; Step 2: recipient's public key | Step 1: recipient's private key; Step 2: sender's public key |

### Mathematical Foundations

- **Modular arithmetic:** `a ≡ b mod n` — easy to compute, hard to invert
- **Prime factorisation:** multiplying two large primes is trivial; factoring the product is computationally infeasible (basis of RSA)
- **Discrete logarithm problem:** basis of Diffie–Hellman

### RSA Key Generation

1. Choose large primes `p`, `q`; compute `n = p × q`
2. Compute `φ(n) = (p−1)(q−1)`
3. Choose `e` coprime to `φ(n)`; compute `d = e⁻¹ mod φ(n)`
4. Public key: `(e, n)`; Private key: `(d, n)`
5. Encrypt: `c = mᵉ mod n`; Decrypt: `m = cᵈ mod n`

Note: encryption/decryption use modulus `n`; key generation uses modulus `φ(n)`.

### Diffie–Hellman Key Exchange

Public parameters `p` (prime), `G` (generator):

1. Alice: `A = Gᵃ mod p`; Bob: `B = Gᵇ mod p`
2. Exchange `A` and `B` publicly
3. Alice: `K = Bᵃ mod p`; Bob: `K = Aᵇ mod p`
4. Both reach the same shared secret `K = G^(ab) mod p`

DH is **not encryption** — it establishes a shared symmetric key which can then encrypt actual data.

### Hashing

| Algorithm | Digest size | Status |
|-----------|------------|--------|
| MD5 | 128 bits | Broken (collision 2004) |
| SHA-1 | 160 bits | Broken (practical collision demonstrated) |
| SHA-2 (256/384/512) | 256/384/512 bits | Secure |

Properties: one-way, deterministic, strong collision resistance. Supports **Integrity**.

### Digital Signatures

1. Hash the document
2. Encrypt hash with sender's **private key** (= the signature)
3. Recipient decrypts with sender's **public key** → recovers original hash
4. Recipient independently hashes received document → compare; match = authentic and unaltered

Provides: Authenticity + Integrity.

### Birthday Attack

- Birthday paradox: with 23 people, >50% chance two share a birthday — because all pairs are checked.
- Applied to hashing: finding two inputs that collide is easier than expected, motivating large digest sizes and why MD5/SHA-1 are broken.

### Cryptanalysis

| Attack | Input needed | Target |
|--------|-------------|--------|
| Brute Force | Computing power | Small key spaces; average ½ space required |
| Frequency Analysis | Statistical knowledge of language | Monoalphabetic substitution/transposition ciphers |
| Known Plaintext | Matched plaintext + ciphertext pair | Any cipher where such pairs exist |

---

## Linked Concepts

- [[concepts/public-key-cryptography-and-key-exchange]] — RSA, DH, digital signatures, key roles, PKI
- [[concepts/cryptographic-hash-functions]] — one-way properties, SHA family, birthday attack
- [[concepts/classical-ciphers-and-cryptanalysis]] — cryptanalysis techniques (brute force, frequency analysis)
