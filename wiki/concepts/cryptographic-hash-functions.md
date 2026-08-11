---
type: concept
title: "Cryptographic Hash Functions"
aliases: ["hash function", "SHA-256", "hashing", "message digest", "digest function"]
tags: [cryptography, hash-functions, SHA-256, MD5, data-integrity, blockchain, Java, security]
created: 2026-08-11
updated: 2026-08-11
status: established
domain: cryptography
address: c-000075
---

# Cryptographic Hash Functions

## 1. Overview

A **hash function** is a mathematical function that maps an input of arbitrary length to a fixed-length output (the *hash*, *digest*, or *message digest*). Hash functions underpin a wide range of security mechanisms: data integrity verification, password storage, digital signatures, blockchain block chaining, and hash-table data structures.

The critical distinction is between **general hash functions** (used in data structures, optimised for speed and distribution) and **cryptographic hash functions** (used in security contexts, optimised for one-wayness and collision resistance).

> **One-line definition:** A cryptographic hash function is a one-way, deterministic function that produces a fixed-length fingerprint of arbitrary data such that any change to the input produces a completely different fingerprint.

---

## 2. Specification Properties

Any hash function — cryptographic or otherwise — should satisfy five core specification properties:

| Property | Description | Why it matters |
|---|---|---|
| **Uniformity** | Output values are evenly distributed across the output space | Prevents output clustering; ensures hash-table performance and prevents statistical leakage |
| **Efficiency** | The hash is fast to compute for any input size | Practical requirement — used in high-throughput verification |
| **Deterministic** | Same input always produces the same output | Without determinism the hash cannot be used for verification |
| **Surjection** | Every possible output value is reachable by some input | Ensures no outputs are "wasted"; important for uniform distribution |
| **One-way function** | Given the output, it is computationally infeasible to recover the input | Core security property — passwords, blockchain, and signatures all depend on this |

The first four properties are shared with non-cryptographic hash functions (e.g., `Object.hashCode()` in Java). The **one-way** property is what elevates a function to *cryptographic* status.

---

## 3. Secure Hash Function Properties

Cryptographic hash functions add four additional security-specific requirements on top of the specification properties:

| Property | Formal name | Description |
|---|---|---|
| **Data Integrity** | Avalanche effect | A change of even 1 bit in the input produces a completely different output — no partial correlation between input-change and output-change |
| **One-Way** | Pre-image resistance | Given hash `H`, it is computationally infeasible to find any input `m` such that `hash(m) = H` |
| **Collision Resistance** | Collision resistance | It is computationally infeasible to find two different inputs `m₁ ≠ m₂` such that `hash(m₁) = hash(m₂)` |
| **Fixed Output Length** | Output uniformity | The output is always the same bit-length regardless of input length (SHA-256 always outputs 256 bits whether the input is 1 byte or 1 GB) |

### 3.1 The Avalanche Effect

The avalanche effect is what makes cryptographic hashes useful for integrity verification. A hash that produced similar outputs for similar inputs would leak information about the input. Instead, a 1-character change in a sentence produces a hash that bears no resemblance to the original:

```
"The red fox jumps over the blue dog"
→ 4a7b2e8c...  (256 bits)

"The red fox jumps over the blue dog."   ← added a period
→ 9f3c1a4d...  (256 bits — completely different)
```

This property means hash functions are reliable detectors of *any* modification, however small.

---

## 4. Common Use Cases

| Use case | How hashing is applied |
|---|---|
| **Checksum / file integrity** | Hash the file before and after download; if hashes match, the file is unaltered |
| **Password storage** | Store `hash(password + salt)`, never the plaintext; on login, hash the input and compare |
| **Hash table / dictionary** | `key → hash(key) mod table_size` gives the bucket index; O(1) average lookup |
| **Digital signatures** | Sign `hash(message)` rather than the full message — faster and protects the signing key from length-extension attacks |
| **Blockchain block chaining** | Each block stores `hash(previous_block)` — altering any block invalidates all subsequent blocks |
| **Merkle trees** | Tree of hashes over a dataset; efficiently prove membership or detect changes in large datasets |
| **Deduplication** | Hash content to detect duplicate files or database entries without comparing bytes |

---

## 5. Hash Function Taxonomy

### 5.1 Digit Sum — Simplest Possible Hash

The **digit sum** function is the most elementary hash: sum the decimal digits of the input.

`F(n) = sum of digits of n`

**Example:** `F(84001) = 8 + 4 + 0 + 0 + 1 = 13`

| Property | Passes? | Reason |
|---|---|---|
| One-directional | ✓ | Cannot reverse digit sum to original number |
| Fast computation | ✓ | Linear in number of digits |
| Uniformity | ✗ | Small numbers cluster at small outputs; output space underutilised |
| Surjection | ✗ | Most large output values are unreachable |
| Collision Resistance | ✗ | Many inputs share the same digit sum |

The digit sum is used pedagogically to illustrate the *concept* of a hash and the distinction between a trivial hash and a secure one.

**Exercise pattern:** Compute digit sum of an input; output as a zero-padded 8-digit string. This exercise establishes the habit of fixed-length output before introducing cryptographic functions.

---

### 5.2 MD5

| Attribute | Detail |
|---|---|
| Output size | 128 bits |
| Status | **Broken — deprecated** |
| Design | Ron Rivest, 1991 |
| Previous use | SSL/TLS certificate signing (VeriSign and others) |

**Compromise:** In December 2008, security researchers demonstrated at the **Chaos Communication Congress (CCC)** that MD5-signed SSL certificates could be forged using a cluster of 200 PlayStation 3 consoles. The attack exploited a known collision vulnerability — two different certificate requests could be crafted to produce the same MD5 digest, allowing a CA to inadvertently sign a fraudulent certificate.

Following this demonstration, VeriSign and major certificate authorities abandoned MD5 for certificate signing. MD5 is now explicitly prohibited for new security applications. It remains in use for non-security purposes (file checksums in non-adversarial contexts) but should not be used where integrity guarantees matter.

---

### 5.3 SHA Family

The Secure Hash Algorithm (SHA) family is maintained by NIST (National Institute of Standards and Technology).

| Version | Status | Output size | Notes |
|---|---|---|---|
| **SHA-0** | Deprecated | 160 bits | Original (1993); withdrawn almost immediately due to undisclosed flaw |
| **SHA-1** | Deprecated | 160 bits | Successor to SHA-0; collision attacks demonstrated (2017, Google/CWI SHAttered project); no longer acceptable for security use |
| **SHA-2** | **Active** | 224/256/384/512 bits | Family of four variants; SHA-256 is the de facto standard for blockchain; SHA-512 used where higher security margin is required |
| **SHA-3** | Active | 224/256/384/512 bits | Won NIST public competition (2015); structurally different from SHA-2 (Keccak sponge construction vs Merkle–Damgård); designed as a hedge if SHA-2 is broken |

**SHA-2 / SHA-256 properties:**
- Fixed 256-bit (32-byte) output
- Fast computation on modern hardware
- Strong avalanche effect — small input change completely changes all 256 output bits
- No known practical collision attacks as of 2026
- Used in Bitcoin, Ethereum (Keccak variant), and most enterprise blockchain systems

**SHA-3 note:** SHA-3 uses a fundamentally different internal construction (the *Keccak sponge* rather than the Merkle–Damgård compression chain used by SHA-1 and SHA-2). This means a hypothetical attack on SHA-2's construction would not automatically apply to SHA-3. In practice, SHA-2 remains secure and SHA-3 adoption in blockchain is limited.

---

## 6. Hashing in Java

### 6.1 Available APIs

| API | Type | Use case |
|---|---|---|
| `Object.hashCode()` | Non-cryptographic | Java collection bucketing; identity-based or value-based |
| `java.util.Hashtable` | Non-cryptographic | Legacy thread-safe map; uses `hashCode()` |
| `java.util.HashMap` / `HashSet` | Non-cryptographic | Modern collections; uses `hashCode()` |
| **`java.security.MessageDigest`** | **Cryptographic** | SHA-256, SHA-3, MD5 computation; the correct API for blockchain applications |

### 6.2 MessageDigest Supported Algorithms

Standard Java (OpenJDK 17+) `MessageDigest` supports:

```
MD2    MD5
SHA-224   SHA-256   SHA-384   SHA-512
SHA-512/224   SHA-512/256
SHA3-224   SHA3-256   SHA3-384   SHA3-512
```

### 6.3 Computing a Block Hash

```java
public byte[] calculateHash(final Block block) {
    // Concatenate the fields to be hashed
    final String value = block.data() + block.previousHash();

    // Encode as UTF-8 bytes
    final byte[] message = value.getBytes(StandardCharsets.UTF_8);

    // Obtain a SHA-256 MessageDigest instance
    final MessageDigest md = MessageDigest.getInstance("SHA-256");

    // Compute and return the digest
    final byte[] hash = md.digest(message);
    return hash;
}
```

**Key points:**
- `MessageDigest.getInstance("SHA-256")` — the algorithm string must exactly match a supported name
- The input is the *concatenation* of all fields that must be tamper-evident; including both `data` and `previousHash` ensures altering either invalidates the hash
- `md.digest(message)` is the single-call API; for streaming input, use `md.update(chunk)` repeatedly then call `md.digest()`
- The returned `byte[]` is typically hex-encoded for display: `String.format("%02x", b)` for each byte

---

## 7. Blockchain Application — Hash Chaining

### 7.1 Block Class Design

```java
public class Block {
    private final long timestamp;
    private final String data;
    private final String previousHash;

    public Block(final String data, final Block previousBlock) {
        this.timestamp = System.currentTimeMillis();
        this.data = data;
        this.previousHash = HashUtils.calculateHash(previousBlock);
    }
}
```

**Design principles:**
- All fields are `final` — `Block` is immutable; once constructed it cannot be altered
- `Block` has no reference to the chain — it is a pure data container (single responsibility)
- The constructor immediately computes and stores `previousHash`; the value is frozen at construction time

### 7.2 Chain Validation

```java
boolean isChainValid() {
    for (int i = 1; i < blockchain.size(); i++) {
        Block currentBlock  = blockchain.get(i);
        Block previousBlock = blockchain.get(i - 1);

        // Recompute the previous block's hash
        String recomputedHash = HashUtils.calculateHash(previousBlock);

        // Compare with the hash stored in the current block
        if (!Objects.equals(previousBlock.hash(), recomputedHash)) {
            return false;  // Chain has been tampered with
        }
    }
    return true;
}
```

**Logic:** For every consecutive pair of blocks, the current block's stored `previousHash` must match the recomputed hash of the actual previous block. Any discrepancy reveals tampering.

### 7.3 The Single-Chain Attack — Why Hashing Alone Is Insufficient

Hash chaining prevents *silent* tampering — but an adversary who modifies block 1's `data` can then **recompute all subsequent hashes** to produce a new, internally consistent chain. `isChainValid()` would return `true` for this tampered chain because it only checks internal consistency, not authenticity.

```
Original:   [Block 1: data=A, hash=H1] → [Block 2: prev=H1] → [Block 3: prev=H2]
Tampered:   [Block 1: data=A', hash=H1'] → [Block 2: prev=H1'] → [Block 3: prev=H2']
                                            ← recomputed to match ←
```

Both chains pass `isChainValid()`. There is no way to distinguish them from within a single chain.

**Solution: distributed consensus.** If the chain is replicated across multiple independent nodes (A, B, C), an attacker must simultaneously tamper with all copies and recompute all their hashes — and, under Byzantine Fault Tolerant protocols, must control more than one-third of nodes to have the tampered version accepted. This is the fundamental argument for decentralisation in blockchain systems.

---

## 8. Security Considerations

| Concern | Detail |
|---|---|
| **Length-extension attacks** | SHA-2 (except SHA-512/224 and SHA-512/256) is vulnerable to length-extension attacks when used naively with secret-prefix MACs. Use HMAC or SHA-3 for MAC construction. |
| **MD5 and SHA-1** | Must not be used for any new security application. Existing systems using them should migrate. |
| **Rainbow table attacks on passwords** | Hash alone is insufficient for password storage; always use a random salt per password, and prefer dedicated password hashing functions (bcrypt, Argon2, scrypt) over raw SHA-256. |
| **Hash comparison timing attacks** | Compare hashes with constant-time comparison (`MessageDigest.isEqual()` or `Arrays.equals()` is NOT constant-time; use `java.security.MessageDigest.isEqual()`). |
| **Quantum computing** | Grover's algorithm halves the effective bit-security of hash functions (SHA-256 → ~128-bit security under quantum attack). SHA-256 remains considered secure through 2030+; SHA-384/512 provide larger margins. |

---

## 9. Related Pages

- [[concepts/blockchain-technology]] — broader blockchain architecture including Merkle trees, consensus, and PoW/PoS
- [[concepts/distributed-ledger-technology]] — DLT taxonomy; hash functions underpin all DLT variants
- [[concepts/hedera-network]] — Hedera Hashgraph uses SHA-384 for its gossip-about-gossip protocol
- [[sources/hedera-lecture-2-blockchain-hashing]] — primary source for the Java implementation patterns and hash function taxonomy in this page

---

## 10. Key Statistics

| Metric | Value |
|---|---|
| SHA-256 output length | 256 bits (32 bytes) |
| SHA-256 collision resistance | 2¹²⁸ operations (birthday bound) |
| MD5 collision demonstrated | December 2008, CCC, 200 PS3s |
| SHA-1 collision demonstrated | February 2017 (Google/CWI SHAttered) |
| SHA-3 standardised | August 2015 (NIST FIPS 202) |
| Java `MessageDigest` algorithms | 12 standard identifiers (OpenJDK 17+) |
