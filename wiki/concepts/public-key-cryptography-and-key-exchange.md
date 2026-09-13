---
type: concept
title: "Public-Key Cryptography and Key Exchange"
aliases: ["asymmetric cryptography", "symmetric vs asymmetric", "RSA", "Diffie-Hellman", "key exchange", "digital signature", "public key infrastructure", "key distribution problem", "textbook RSA"]
tags: [cryptography, rsa, diffie-hellman, asymmetric, symmetric, key-exchange, digital-signatures, authentication, pki, inf2005]
created: 2026-09-03
updated: 2026-09-03
status: established
domain: cryptography
address: c-000124
---

# Public-Key Cryptography and Key Exchange

## 1. Overview

| | **Symmetric** | **Asymmetric (public-key)** |
|---|---|---|
| Keys | one shared secret `K` | a linked **pair** `(pub, priv)` per party |
| `E`/`D` relationship | `D(K, E(K, P)) = P` — same key both ways | `D(priv, E(pub, P)) = P` **and** `D(pub, E(priv, P)) = P` — opposite key |
| Speed | fast (AES, ChaCha20, DES, Blowfish) | 100–1000× slower (RSA, ECC) |
| Main problem | how to **share `K`** securely first | how to **trust that a public key belongs to who it claims** |
| Typical use | bulk data encryption | key exchange, digital signatures, small payloads |

In practice the two are combined: asymmetric crypto establishes a symmetric **session key**, then symmetric crypto encrypts the actual traffic (TLS, PGP, SSH all work this way).

> **One-line definition:** Public-key cryptography gives every party a freely publishable key and a secret key such that one reverses the other, enabling confidential messaging and digital signatures without any pre-shared secret — provided public keys can be authenticated.

---

## 2. Symmetric Key Cryptography

* One key `K` performs both encryption and decryption.
* Both parties must already hold `K` — so it must travel over a **separate secure channel** before secure communication can begin (chicken-and-egg).
* `n` mutually-communicating users need `n(n−1)/2` distinct keys.
* Wrong key / wrong mode / wrong IV ⇒ output is unrelated noise or a padding error (no graceful degradation).
* Examples exercised in the INF2005 lab: a generic web crypto tool (AES/DES/RC4), Blowfish-CBC (`SIT-UOG` key), and a toy shared-secret cryptosystem.

---

## 3. Asymmetric Key Cryptography

The key pair is mathematically linked: **whatever one key of the pair locks, only the other key unlocks.** A key can never reverse its own operation, so you cannot use the same key to encrypt and decrypt.

### 3.1 The two services

| Direction | Provides | How |
|---|---|---|
| Encrypt with **recipient's public** key → decrypt with their **private** key | **Confidentiality** | anyone can send; only the owner can read |
| Encrypt (sign) with **sender's private** key → decrypt (verify) with their **public** key | **Authentication + integrity + non-repudiation** | only the owner could have produced it; *not* secret — anyone can verify |

**Authentication ≠ confidentiality.** They are independent goals. Successfully decrypting a message with someone's *public* key tells you *who wrote it* and *that it is unaltered* — it tells you nothing about secrecy, because the public key is public.

### 3.2 Combining both (Alice ↔ Bob)

Private key `privX` is held **only** by `X`; public keys are distributed openly.

* Bob → Alice, secret: encrypt with `pubA`; Alice decrypts with `privA`.
* Bob → Alice, authenticated: Bob signs with `privB`; Alice verifies with `pubB`.
* Bob → Alice, secret **and** authenticated: Bob signs with `privB`, then encrypts with `pubA`; Alice decrypts with `privA`, then verifies with `pubB`.

---

## 4. RSA

### 4.1 Key generation
1. Choose two large primes `p`, `q`; compute `n = p·q` (the **modulus**).
2. Compute `φ(n) = (p−1)(q−1)`.
3. Choose public exponent `e` coprime to `φ(n)` (commonly `65537`).
4. Private exponent `d = e⁻¹ mod φ(n)`.
5. Public key `(n, e)`; private key `(n, d)` (or `p, q, d`).

### 4.2 Operations
* Encrypt / verify: `c = mᵉ mod n`
* Decrypt / sign: `m = cᵈ mod n`

Correctness rests on Euler's theorem; security rests on the **integer factorisation problem** — recovering `d` requires `φ(n)`, which requires factoring `n`.

### 4.3 Why key size is everything — the INF2005 team challenge

`public_key.pem` held a **64-bit** modulus:
```
n = 16513720463601767803,  e = 65537
```
64 bits factors in milliseconds:
```
n = 3917781347 × 4215069449 = p × q
φ(n) = (p−1)(q−1) = 16513720455468917008
d = 65537⁻¹ mod φ(n) = 9440767265896423601
```
With `d` recovered, `m = cᵈ mod n` decrypts the file block by block. Real RSA needs **≥ 2048-bit** moduli.

### 4.4 "Textbook" RSA is not enough even at large sizes
Raw `mᵉ mod n` with no padding is deterministic (same plaintext → same ciphertext), malleable, and leaks structure (small-`m` attacks, common-modulus, Håstad broadcast). Production RSA uses **OAEP** padding for encryption and **PSS** for signatures.

---

## 5. The Key-Distribution Problem and Diffie–Hellman

**The weakness common to §2 and §3:** key management.
* Symmetric — the secret key must somehow be shared before any secure comms.
* Asymmetric — no shared secret, but a **man-in-the-middle** who swaps in their own public key defeats everything unless keys are authenticated.

### 5.1 Diffie–Hellman key exchange

Public parameters: prime modulus `p`, generator `G`.

1. Alice picks secret `a`, sends `A = Gᵃ mod p`.
2. Bob picks secret `b`, sends `B = Gᵇ mod p`.
3. Alice computes `s = Bᵃ mod p`; Bob computes `s = Aᵇ mod p`. Both equal `G^(ab) mod p`.

An eavesdropper sees `p, G, A, B` but must solve the **discrete logarithm problem** to get `a` or `b`. The shared secret `s` is never transmitted.

**Worked example (INF2005 Q9):** `p = 11`, `G = 2`, `a = 9`, `b = 4`.
`A = 2⁹ mod 11 = 6`; `B = 2⁴ mod 11 = 5`; `s = 5⁹ mod 11 = 6⁴ mod 11 = 9`. **Shared key = 9.**

### 5.2 Remaining gap and the fix
Plain DH has no authentication → still MITM-able. Real protocols use **authenticated** DH (signed with long-term keys) and rely on a **PKI**: Certificate Authorities issue signed certificates binding a public key to an identity, so a swapped key fails validation. Ephemeral DH (DHE/ECDHE) additionally gives **forward secrecy**.

---

## 6. TLS/HTTPS — All Three Primitives in Practice

TLS (Transport Layer Security) is the canonical real-world deployment of all three cryptographic primitives working together. Every HTTPS page load uses this protocol.

### 6.1 What a Browser Certificate Shows

When you open any HTTPS site and inspect the certificate:
- The certificate contains the server's **public key only** — the private key never leaves the server.
- The certificate is issued and signed by a **Certificate Authority (CA)** — the browser verifies this signature to confirm the public key genuinely belongs to the claimed server.
- Typical certificate fields: subject (who it is for), issuer (the CA), key algorithm and size (e.g. RSA 2048), signature hash (e.g. SHA-256).
- Example: SIT website certificate — issued by Amazon CA, RSA 2048, SHA-256.
- The active TLS session additionally shows the symmetric cipher in use (e.g. AES-128-GCM).

### 6.2 The TLS Handshake (Simplified)

| Step | Who acts | Primitive |
|------|----------|-----------|
| 1. Browser requests a secure connection | Browser | — |
| 2. Server sends its certificate (contains public key) | Server | — |
| 3. Browser verifies certificate against trusted CAs | Browser | Hash (SHA-256) |
| 4. Browser generates a random **session key** | Browser | — |
| 5. Browser encrypts session key with server's public key; sends it | Browser | Asymmetric (RSA or ECDH) |
| 6. Server decrypts session key with its private key | Server | Asymmetric |
| 7. Both sides now share the session key | — | — |
| 8. All subsequent content encrypted with AES using session key | Both | Symmetric (AES-128/256) |
| 9. Each record authenticated with HMAC | Both | Hash (SHA-256) |

### 6.3 Why Hybrid: Performance Rationale

Asymmetric encryption (RSA, ECC) is **100–1000× slower** than symmetric encryption (AES). Using RSA to encrypt bulk web page content would be prohibitively slow. The hybrid approach uses:
- **Asymmetric** — for the key exchange only (once per session, small payload: the session key)
- **Symmetric** — for all subsequent data (the bulk of every browsing session)

> "If you are using asymmetric key, the time taken will be much longer than symmetric key. That's why you need to have both."

This principle extends beyond TLS: PGP, SSH, and Signal all use the same hybrid pattern.

### 6.4 SSL → TLS Transition

The original protocol was **SSL (Secure Sockets Layer)**. It was deprecated after critical vulnerabilities were discovered, most notably **Heartbleed** (a buffer over-read in OpenSSL that leaked server memory, including private keys). The current protocol is **TLS** (Transport Layer Security), now at versions 1.2 and 1.3.

"SSL certificate" persists as a colloquial term even when the actual protocol in use is TLS 1.3.

### 6.5 Digital Signing vs Encryption in Certificates

When you authenticate (sign) rather than encrypt, the terminology shifts deliberately:
- You do **not** say "encrypt with private key" — you say **sign** with private key.
- The recipient **verifies** (not "decrypts") using your public key.
- A successful verification proves the message came from the private key holder and was not altered.

This is the basis of digital certificates: the CA **signs** the certificate with its private key; browsers **verify** it with the CA's public key (built into the browser/OS trust store).

---

## 7. Connections

- [[concepts/classical-ciphers-and-cryptanalysis]] — what came before; substitution/transposition and the statistical attacks public-key crypto is immune to
- [[concepts/cryptographic-hash-functions]] — the third primitive; signatures sign a hash, not the message
- [[concepts/fido-passkeys-passwordless]] — passkeys are asymmetric key pairs: device holds the private key, the service stores the public key
- [[concepts/blockchain-technology]] / [[concepts/crypto-wallets]] — ECDSA key pairs; wallet address ≈ public key, seed phrase ≈ private key
- [[concepts/tcp-ip-network-model]] / [[synthesis/web-security-ssdlc-bridge]] — TLS is the production assembly of all three primitives
- [[examples/inf2005-lab-wk1-cryptography]] — full worked lab including the RSA-64-bit break
- [[learning/textbook-rsa-64-bit-modulus]] — the lesson: RSA security = cost of factoring `n`
