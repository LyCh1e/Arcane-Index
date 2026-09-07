# Cryptography 2: Asymmetric Cryptography, Hashing & Cryptanalysis

*Cyber Security Fundamentals — Dr Tan Kheng Leong*

## 1. The Symmetric Key Problem

- Symmetric cryptography requires the key to be **shared** between sender and receiver beforehand.
- Secure key **distribution** is a major challenge — how do you get the key to the other party without an eavesdropper intercepting it?
- **Asymmetric (public key) cryptography** offers a solution.

## 2. Asymmetric Cryptography Basics

- Uses a **key pair**: mathematically related keys, one chosen as **private**, one as **public**.
- The key-generation algorithm is a **one-way function** — given the public key, it's computationally infeasible to derive the private key.
- The public key is distributed openly to anyone who needs to send you messages.

**Default roles:**
- **Private key** → decrypts
- **Public key** → encrypts

These roles can be reversed depending on the goal (confidentiality vs. authentication).

## 3. Confidentiality vs. Authentication

| Goal | Encrypt with | Decrypt with | Meaning |
|---|---|---|---|
| **Confidentiality** | Recipient's **public** key | Recipient's **private** key | Only the recipient can read it |
| **Authentication** | Sender's **private** key | Sender's **public** key | Proves the message came from that sender (anyone with the public key can verify it, but only the sender could have created it) |

### Combined Authentication + Confidentiality
To get both at once (e.g. Alice sending a secure, authenticated message to Bob):
1. Alice encrypts the message with **her own private key**: `A_PrivKey(msg)` — this "signs" it.
2. Alice encrypts that result with **Bob's public key**: `B_PubKey[A_PrivKey(msg)]`.
3. Bob decrypts with **his private key** to undo step 2.
4. Bob decrypts the result with **Alice's public key** to undo step 1 — successfully decrypting a second time proves Alice sent it.

## 4. One-Way Functions Behind Key Generation

Asymmetric crypto relies on math problems that are easy to compute one way but computationally infeasible to reverse.

### 4.1 Modular Arithmetic
- `a ≡ b mod n` if `a % n = b % n` (like a clock: 14 ≡ 2 mod 12)
- **One-way-ness**: given only the *result* of `a mod b`, you cannot feasibly recover the original `a` and `b` — too many possibilities.

### 4.2 Prime Factorisation
- Multiplying two large primes is easy; factoring the product back into its two primes is extremely hard for sufficiently large numbers.
- e.g. `77 = 7 × 11`, `391 = 17 × 23`

## 5. RSA (Rivest–Shamir–Adleman)

**Key generation steps:**
1. Pick two large, distinct random primes `p` and `q`.
2. Compute `n = p × q`.
3. Compute Euler's totient `φ(n) = (p-1)(q-1)`.
4. Pick `e`, a number less than `φ(n)` that is **co-prime** to `φ(n)` (shares no common factor except 1, i.e. GCD = 1).
5. Compute `d` such that `d × e mod φ(n) = 1`.
6. **Public key** = `(e, n)`; **Private key** = `(d, n)`.

- It is computationally infeasible to derive `d` from `e` and `n` alone — only `e` and `n` are published.
- Note: encryption/decryption use modulus `n`, but key generation uses modulus `φ(n)` — a common point of confusion.

## 6. Diffie–Hellman Key Exchange

Solves: *how do two parties agree on a shared secret key over an insecure channel, without ever transmitting the key itself?*

**Setup:** Alice and Bob publicly agree on a large prime modulus `p` and a generator `G`.

**Steps:**
1. Alice picks private random number `a`, computes `A = Gᵃ mod p`.
2. Bob picks private random number `b`, computes `B = Gᵇ mod p`.
3. Alice and Bob exchange `A` and `B` (publicly — this is safe to observe).
4. Alice computes `K = Bᵃ mod p`; Bob computes `K = Aᵇ mod p`.
5. Both arrive at the same shared secret: `K = G^(ab) mod p`.

> Important: Diffie–Hellman is **not** encryption/decryption — it's a method for two parties to derive a **shared key**, which can then be used with a symmetric cipher.

**Worked example:** `g = 5`, `p = 13`, Alice's secret = 314, Bob's secret = 69 — each computes `g^secret mod p`, exchanges results, then raises the received value to their own secret to arrive at the same shared key.

## 7. Hashing and Hash Functions

- A **one-way function** (e.g. MD5, SHA) that takes an arbitrary-length input and produces a **fixed-length digest** (message digest / hash).
- The same input always produces the same hash.

**Properties of a secure hash:**
- **One-way property** — infeasible to find a message that produces a given hash.
- **Strong collision resistance** — infeasible to find two *different* messages that hash to the same value.
- Hashing primarily supports **Integrity** (of CIA), and can support authentication when combined with signatures.

### Common Hash Algorithms
| Algorithm | Digest size | Status |
|---|---|---|
| MD5 | 128 bits | Broken — collision shown in 2004 |
| SHA-1 | 160 bits | Broken — practical collision demonstrated |
| SHA-2 (SHA-256 / SHA-384 / SHA-512) | 256 / 384 / 512 bits | Currently considered secure |

## 8. Digital Signatures

1. Sender hashes the document.
2. Sender encrypts the hash with **their own private key** (this is the "signature").
3. Sender sends the encrypted hash along with the original document (which may also be encrypted).
4. Recipient decrypts the signature with the sender's **public key** to recover the original hash.
5. Recipient independently hashes the received document and compares it to the decrypted hash.
6. A match confirms both **authenticity** (came from sender) and **integrity** (not altered).

A secure digital signature system provides **Confidentiality and Integrity**, though overall data security also needs access control, backups, etc.

## 9. Birthday Attack

- Named after the **birthday paradox**: in a group of just 23 people, there's a >50% chance two share a birthday — far higher than intuition suggests.
- This works because we're comparing *every pair* of people/values against each other, not just one fixed target against everyone else.
- Applied to hashing: it becomes easier than expected to find **two different inputs producing the same hash** (a collision), which is why short digest sizes (like DES's 64-bit block, or MD5) become vulnerable as computing power grows.

## 10. Cryptanalysis (Attacking Ciphers)

**Definition:** The study of ciphers to find weaknesses and break them — this drives improvements in cryptographic protocols.

### 10.1 Brute-Force Attack
- Try all possible keys until intelligible plaintext emerges.
- On average, need to try **half** of all possible keys.
- Requires significant computing resources; infeasible if the key space is sufficiently large.

### 10.2 Frequency Analysis
- Exploits the fact that English text has predictable statistical structure:
  - Most frequent letters: **E** (12.51%), T, A, O, I
  - Most frequent words: *the, and, for, of, to, in...*
  - Common digraphs/trigraphs: TH, ND, RE, ...
- **Weakness exploited:** in monoalphabetic substitution/transposition ciphers, letter *positions* change but their *frequencies* don't — so the most common ciphertext symbol likely maps to "E," etc.
- Process: substitute the most frequent letters first, then use short common words to refine guesses (trial and error).

### 10.3 Known Plaintext Attack
- The attacker has access to **both** a plaintext and its corresponding ciphertext.
- By comparing the two (`C = (P + K) mod 26` / `P = (C − K) mod 26` for simple ciphers), the attacker can infer the key or the algorithm's behavior.
- Related technique: **Side Channel Analysis** — injecting known plaintext into a crypto engine and observing the output to infer the protocol.

### Summary Comparison
| Attack | Requires | Best against |
|---|---|---|
| Brute Force | Computing power to try all keys | Small key spaces / weak algorithms |
| Frequency Analysis | Statistical knowledge of the language | Monoalphabetic substitution & transposition ciphers |
| Known Plaintext | Access to matched plaintext/ciphertext pairs | Any cipher where such pairs can be obtained |

## Key Takeaways
- Asymmetric crypto solves the symmetric key-distribution problem using mathematically linked public/private key pairs.
- Key **role** (which key encrypts vs. decrypts) determines whether you get confidentiality or authentication — combining both requires two encryption passes.
- **RSA** relies on the difficulty of prime factorisation; **Diffie–Hellman** relies on the difficulty of the discrete logarithm problem (modular exponentiation) to establish a shared secret without transmitting it.
- **Hashing** provides integrity via one-way, collision-resistant digests; MD5 and SHA-1 are now broken.
- **Digital signatures** combine hashing + private-key encryption for authenticity and integrity.
- The **birthday attack** shows why digest/key length must be generously sized to resist collision-based attacks.
- Cryptanalysis techniques (brute force, frequency analysis, known plaintext) are the classic ways ciphers get broken, and understanding them motivates why modern ciphers use large keys and diffusion/confusion.
