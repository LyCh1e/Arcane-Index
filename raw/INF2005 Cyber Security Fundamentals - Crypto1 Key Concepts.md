# Cryptography 1: Key Concepts (Symmetric Cryptography)

*Cyber Security Fundamentals — Dr Tan Kheng Leong*

## 1. Basic Concepts

- **Plaintext** — the original, readable message
- **Ciphertext** — the encrypted, unreadable form of the message
- **Key** — the secret value that controls encryption/decryption
- A **cipher** transforms plaintext into ciphertext using a key, and back again

## 2. Why Cryptography?

Cryptography underpins:
- Digital currency transactions
- Data protection
- Safe business processes

It primarily supports **Confidentiality** (of the CIA triad — Confidentiality, Integrity, Availability), though certain schemes (hashing, digital signatures) also support Integrity and Authentication.

## 3. The Threat Model

- **Alice** sends a message to **Bob**
- **Eve** (the eavesdropper) can intercept traffic on an insecure communications channel
- Encryption means Eve can still *see* the transmitted data, but cannot understand it without the key

## 4. Types of Cryptography

| Type | How it works | Example use |
|---|---|---|
| **Symmetric key** | Same key used for encryption and decryption (private key known only to sender & receiver) | Private Key Cryptography |
| **Asymmetric key** | Different keys for encryption and decryption (public key encrypts, private key decrypts) | Public Key Cryptography |
| **Hashing** | No keys; one-way function maps data to a fixed-length "digest" | Password storage, integrity checks |

## 5. Symmetric Cryptography

**Process:** `ENCRYPT(plaintext, key) → ciphertext` and `DECRYPT(ciphertext, key) → plaintext`, using the *same* key both times.

### 5.1 Substitution Ciphers
Replace each plaintext character with another, following a fixed pattern.

- **Monoalphabetic** (one fixed substitution) — e.g. **Caesar Cipher**
  - Shift every letter along the alphabet by a fixed amount to encrypt; shift back to decrypt.
  - Example: shift of 3 → `HELLO WORLD` → `KHOOR ZRUOG`
- **Polyalphabetic** (substitution varies by position) — e.g. **Vigenère Cipher**
  - A repeating keyword determines a different shift for each letter (using a Vigenère table).
  - Example: keyword `ALICE`, plaintext `HELLO` → ciphertext `HPTNS`

### 5.2 Transposition Ciphers
Keep the same characters but shift their *positions* according to a pattern (rather than substituting them).

- **Simple transposition** — reverse the order of characters
  - `UNIVERSITY` → `YTISREVINU`
- **Rail Fence Cipher** — write the message in a zig-zag across a number of "rails," then read off row by row
  - `HELLOBOB` with rail key 2 → `HLOOELBB`
- **Columnar Transposition Cipher** — write plaintext into a grid (row by row), then read out column by column in an order set by a keyword/key
  - Key `RED`, plaintext `HELLOWORLD`, padding `X` → `LWLX EORX HLOD`

## 6. Kerckhoffs's Principle

> "The security of a cryptosystem must not depend on the secrecy of the algorithm; it should only depend on the secrecy of the **key**."

This addresses the vulnerability of "security through obscurity": if an attacker learns *how* an algorithm works (e.g. Caesar cipher, rail fence), they can decrypt messages unless the *key* itself remains secret.

## 7. Modern Symmetric Algorithms

| Algorithm | Key length | Block size | Notes |
|---|---|---|---|
| **DES** (Data Encryption Standard) | 56-bit effective (64-bit with parity bits discarded) | 64-bit | 16 rounds of substitution, transposition, XOR with per-round 48-bit sub-keys; published by NIST; cracked in <24 hrs in 2002 by networked computing |
| **3DES** (Triple DES) | 168-bit (3×56) | 64-bit | Encrypt–Decrypt–Encrypt using keys K1, K2, K3 (`Ek1 → Dk2 → Ek3`); decrypt reverses the steps. Being deprecated from 2024 due to small 64-bit block size (vulnerable to birthday attacks) |
| **AES** (Advanced Encryption Standard) | 128 / 192 / 256-bit (AES-128/192/256) | 128-bit | Number of rounds depends on key size; each round does substitution, transposition, and XOR; theoretically crackable with quantum computing |

## 8. One-Time Pad (OTP)

- Key must be **at least as long as the plaintext**
- Each symmetric key is used **only once**, then discarded
- Key should ideally be **truly random**
- Real-world analogues: 2FA codes, OTP dongles
- Example: `Plain: H A T` with key `6 12 17` → `Cipher: N M K`

## 9. Random Number Generators (RNG)

- **True randomness** comes from observing unpredictable physical/environmental data (mouse movement, electrical/fan noise) — this is **entropy**.
- Computer-generated "random" numbers are usually **pseudo-random**: generated predictably via a mathematical formula/seed, which can be a security weakness if used where true randomness (e.g. OTP keys) is required.

## Key Takeaways
- Symmetric crypto uses **one shared key** for both directions — fast, but the key must somehow be securely distributed.
- Substitution ciphers change *what* the characters are; transposition ciphers change *where* they are.
- Security should rest entirely on **key secrecy**, never on hiding the algorithm (Kerckhoffs's Principle).
- DES → 3DES → AES represents the historical progression as computing power made shorter keys/blocks insecure.
- OTPs are theoretically unbreakable but impractical at scale because the key must be as long as the message and truly random.
