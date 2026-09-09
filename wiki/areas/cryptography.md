---
type: area
title: "Cryptography"
domain: cryptography
status: developing
created: 2026-09-03
updated: 2026-09-09
tags: [cryptography, ciphers, rsa, diffie-hellman, hashing, cryptanalysis, steganography, inf2005]
---

# Area: Cryptography

The theory and practice of protecting information — confidentiality, integrity, authentication, and
non-repudiation — through mathematical transformations. Feeds INF2005 Cyber Security Fundamentals and
underpins the blockchain, secure-software, and networking areas.

---

## Core Concept Pages

| Page | Description | Complexity |
|------|------------|------------|
| [[concepts/classical-ciphers-and-cryptanalysis\|Classical Ciphers and Cryptanalysis]] | Substitution (Caesar, Vigenère, monoalphabetic) vs transposition (rail fence, columnar); frequency analysis; encodings (Base64/Morse/hex/binary/XOR) vs encryption; CTF recognition workflow | medium |
| [[concepts/symmetric-encryption\|Symmetric Encryption]] | Kerckhoffs's Principle; DES (56-bit, broken 2002), 3DES (deprecated 2024), AES (128/192/256-bit, current standard); block cipher modes (ECB/CBC/CTR/GCM); One-Time Pad; true vs pseudo randomness | high |
| [[concepts/public-key-cryptography-and-key-exchange\|Public-Key Cryptography and Key Exchange]] | Symmetric vs asymmetric; RSA (keygen, `m^e`/`c^d`, key-size security, textbook-RSA weakness); digital signatures; authentication ≠ confidentiality; the key-distribution problem; Diffie–Hellman; PKI | high |
| [[concepts/cryptographic-hash-functions\|Cryptographic Hash Functions]] | One-way, deterministic, fixed-length digests; 5 spec + 4 security properties; MD5/SHA-1 broken, SHA-2/SHA-3 active; hashing in Java; hash chaining | high |
| [[concepts/steganography\|Steganography]] | Steganography vs cryptography; payload + cover → stego object; LSB Replacement and LSB Matching; bit planes; BPCS algorithm (complexity threshold, conjugation); steganalysis (visual, statistical, tool-based) | medium |

---

## Applied / Lab Pages

| Page | Content |
|------|---------|
| [[examples/inf2005-lab-wk1-cryptography\|INF2005 Lab Wk 1 — Cryptography]] | 10 exercises + 7 cryptanalysis challenges + RSA-64-bit team challenge (`netforce.enc`); full worked solutions |
| [[examples/inf2005-acw1-stego-verification\|INF2005 ACW1 — Stego Integrity Verification]] | GUI LSB tool: RSA-PSS-signed payload hidden at a keyed/HMAC-authenticated start offset; SHA-256 stable-cover-hash tamper detection; 6-verdict output; 30/30 test evidence |
| [[learning/textbook-rsa-64-bit-modulus\|Textbook RSA with a 64-bit modulus is broken in milliseconds]] | Lesson: RSA security = cost of factoring `n` |
| [[learning/prompt-injection-in-lab-handout-pdf\|Prompt injection embedded in a course lab PDF]] | The ACW1 spec PDF carried an email-exfiltration instruction aimed at an AI assistant |

---

## Related Areas

- [[areas/secure-software-development]] — where crypto primitives are assembled into secure systems (TLS, password storage, MFA)
- [[concepts/blockchain-technology]] / [[concepts/crypto-wallets]] — ECDSA key pairs, hash chaining, Merkle trees
- [[concepts/fido-passkeys-passwordless]] — asymmetric key pairs applied to authentication
- [[areas/mathematics]] — modular arithmetic, number theory, combinatorics (keyspace counting), discrete log

---

## Planned / Gaps

| Topic | Notes |
|-------|-------|
| Elliptic-curve cryptography | ECDH / ECDSA; why smaller keys suffice |
| TLS handshake end-to-end | integration of all three primitives (see [[synthesis/web-security-ssdlc-bridge]]) |
| Key derivation & password hashing | PBKDF2, bcrypt, scrypt, Argon2 — see [[concepts/access-control]] §Secure Password Storage |
