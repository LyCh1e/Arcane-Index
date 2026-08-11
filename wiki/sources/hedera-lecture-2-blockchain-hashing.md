---
type: source
title: "Hedera Developer Course — Lecture 2: Blockchain & Hash Functions"
source-type: lecture-slides
author: "Hendrik Ebbers (OpenElements / Swirlds Labs / Hedera)"
date-ingested: 2026-08-11
tags: [blockchain, hash-functions, SHA-256, MD5, Java, cryptography, Hedera, DLT, distributed-consensus]
domain: blockchain
status: ingested
file: "raw/Lecture 2.pdf"
---

# Source: Hedera Developer Course — Lecture 2

**File:** `raw/Lecture 2.pdf`
**Presenter:** Hendrik Ebbers — OpenElements, Swirlds Labs, Hedera
**Slides:** ~49 slides
**Topics:** Blockchain basics · Hash functions · Hashing in Java · Creating a blockchain in Java · Why distributed consensus is required

---

## Source Summary

Lecture 2 of a blockchain developer course delivered by Hendrik Ebbers, a core contributor to the Hedera ecosystem. The lecture is structured in four parts:

1. **Blockchain Basics** — block structure (`data`, `timestamp`, `prev_hash`); the "WAIT" question (why not a database?); hash chaining as the answer; the immutability argument
2. **Hash Functions** — formal specification properties; secure hash requirements; use cases; worked example (Digit Sum); MD5 history and compromise; SHA family evolution
3. **Hashing in Java** — OpenJDK hash APIs; `MessageDigest` class; SHA-256 in practice
4. **Creating a Blockchain in Java** — `Block` class design; `Chain` class design; `isChainValid()` logic; the single-chain attack; why distributed consensus is the required next step

The lecture is a strong introductory-to-intermediate resource: mathematically accurate without being proof-heavy, with directly runnable Java code examples.

---

## Key Concepts Covered

### Part 1 — Blockchain Basics

The core insight of the lecture is the "WAIT" moment: a block consists of `data`, a `timestamp`, and a `previousHash`. At first glance, this data could be stored in a SQL database, a Java object, JSON, MongoDB, or Redis. The question "what makes blockchain *special*?" is answered by hash chaining.

**Block structure (simplified):**

| Field | Description |
|---|---|
| `data` | Payload — transaction records, events, or any string |
| `timestamp` | UNIX epoch of block creation |
| `previousHash` | SHA-256 digest of the entire previous block |

**Chain integrity argument:** Each block's `previousHash` field is the SHA-256 digest of the previous block's full content. If any block's `data` is altered, its hash changes — which invalidates the `previousHash` field of the next block, cascading through the entire chain. "Each block defines the validity of all previous blocks."

**Why a database is insufficient:** A traditional database is mutable. An attacker who gains write access can silently alter any row. A blockchain's hash chain makes silent mutation computationally infeasible: altering one block forces recomputation of all subsequent blocks, which is detectable.

---

### Part 2 — Hash Functions

#### Specification Properties (5)

| Property | Description |
|---|---|
| **Uniformity** | Output values are distributed evenly across the output space; no output is disproportionately common |
| **Efficiency** | Hash is fast to compute for any input |
| **Deterministic** | Same input always produces the same output |
| **Surjection** | Every possible output value can be reached by some input (no unused output values) |
| **One-way function** | Given the output, it is computationally infeasible to recover the input |

#### Secure Hash Function Properties (4)

| Property | Description |
|---|---|
| **Data Integrity** | Even a 1-bit change in input produces a completely different output (avalanche effect) |
| **One-Way** | Cannot reverse the hash to the original input |
| **Collision Resistance** | Computationally infeasible to find two different inputs producing the same hash |
| **Fixed Output Length** | Output is always the same bit-length regardless of input size |

#### Use Cases

- **Checksum** — verify file integrity during download or transfer
- **Password storage** — store hash of password, never the plaintext
- **Hash table** — key → index mapping for O(1) lookup (Java `HashMap`, `HashSet`)

#### Digit Sum — Simplest Possible Hash

`F_b(n)` = sum of decimal digits of `n`

**Example:** `F(84001) = 8 + 4 + 0 + 0 + 1 = 13`

| Property | Passes? |
|---|---|
| One-directional | ✓ |
| Fast computation | ✓ |
| Uniformity | ✗ (small numbers cluster at small outputs) |
| Surjection | ✗ (many output values unreachable) |

The Digit Sum illustrates the idea of a hash but fails as a *secure* hash. Used as a worked example and basis for a hands-on exercise: write a program computing the digit sum and outputting it as an 8-digit string.

#### MD5

- 128-bit output
- Previously used in SSL certificate signing (VeriSign)
- **Broken:** December 2008, the Chaos Communication Congress (CCC), using a cluster of 200 PlayStation 3 consoles, demonstrated practical MD5 collision attacks sufficient to forge a CA certificate
- VeriSign and major CAs subsequently deprecated MD5; it is no longer acceptable for security use

#### SHA Family

| Version | Status | Notes |
|---|---|---|
| SHA-0 | Deprecated | Quickly replaced; collision vulnerability |
| SHA-1 | Deprecated | Collision attacks demonstrated; no longer acceptable |
| SHA-2 | **Active** | Variants: SHA-224, SHA-256, SHA-384, SHA-512; SHA-256 used in Bitcoin and most blockchain systems |
| SHA-3 | Active | Won NIST public competition (2015); structurally different internal construction from SHA-2; similar security level; not yet widely used in blockchain |

**SHA properties:**
- Fixed-size output (SHA-256 → always 256 bits)
- Fast computation
- Avalanche effect — small input change produces completely different output
- Collision resistant

---

### Part 3 — Hashing in Java

OpenJDK exposes hashing through several APIs:

| API | Purpose |
|---|---|
| `Object.hashCode()` | Identity-based hash for use in collections |
| `Hashtable` | Legacy thread-safe hash map |
| `HashMap` / `HashSet` | Modern non-thread-safe collections |
| **`MessageDigest`** | Cryptographic hash computation — the relevant API for blockchain |

**`MessageDigest` supported algorithms** (Java standard library):
MD2, MD5, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256, SHA3-224, SHA3-256, SHA3-384, SHA3-512

**Computing a block hash in Java:**

```java
public byte[] calculateHash(final Block block) {
    final String value = block.data() + block.previousHash();
    final byte[] message = value.getBytes(StandardCharsets.UTF_8);
    final MessageDigest md = MessageDigest.getInstance("SHA-256");
    final byte[] hash = md.digest(message);
    return hash;
}
```

Key observations:
- The hash input concatenates `data` and `previousHash` — both fields are included so altering either invalidates the hash
- `MessageDigest.getInstance("SHA-256")` — algorithm string must match a supported name exactly
- `md.digest(message)` — single-call API; returns raw bytes
- Output is a `byte[]`, typically hex-encoded for storage and display

---

### Part 4 — Creating a Blockchain in Java

#### Design: Separation of Concerns

The lecture enforces a clean separation:

| Class | Responsibility |
|---|---|
| `Block` | Immutable data object; knows nothing about the chain |
| `Chain` | Holds the sequence of blocks; provides validation and append operations |
| `HashUtils` | Static utility for hash computation |

#### Block Class

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

Notes:
- All fields are `final` — Block is immutable by design
- The constructor accepts a `previousBlock` reference and immediately computes and stores its hash
- `Block` has no reference back to the chain; it is purely a data container

#### Simple Chain Construction

```java
ArrayList<Block> blockchain = new ArrayList<Block>();
Block block1 = new Block("Hi im the first block");
Block block2 = new Block("Hi im the second block", block1);
Block block3 = new Block("Hi im the third block", block2);
blockchain.add(block1);
blockchain.add(block2);
blockchain.add(block3);
```

#### Chain Validation

```java
boolean isChainValid() {
    for (int i = 1; i < blockchain.size(); i++) {
        Block currentBlock = blockchain.get(i);
        Block previousBlock = blockchain.get(i - 1);
        String hash = HashUtils.calculateHash(previousBlock);
        if (!Objects.equals(previousBlock.hash(), hash)) {
            return false;
        }
    }
    return true;
}
```

Logic: For every block from index 1 onwards, recompute the hash of the previous block and compare it to the stored value. Any discrepancy means the chain has been tampered with.

#### Why This Is Not Enough

Hash chaining prevents *silent* tampering — but an attacker who tampers with block 1 can simply recompute all subsequent hashes to produce a new, internally consistent chain. From the perspective of `isChainValid()` alone, the tampered chain is indistinguishable from the original.

**The answer: distributed consensus.** If the same chain is held by multiple independent nodes (A, B, C), an attacker must simultaneously tamper with and recompute all copies — and must control a majority of nodes to get the tampered version accepted. This is the argument for decentralisation and the motivating question for Lecture 3.

---

## Connections to Wiki Pages

- [[concepts/cryptographic-hash-functions]] — full concept page derived from this lecture's hash function content
- [[concepts/blockchain-technology]] — broader blockchain anatomy and consensus mechanisms
- [[concepts/distributed-ledger-technology]] — DLT taxonomy including blockchain, DAG, Hashgraph
- [[concepts/hedera-network]] — Hedera Hashgraph — the presenter's home organisation

---

## Source Quality Assessment

| Dimension | Assessment |
|---|---|
| Authority | High — presenter is a Hedera core ecosystem contributor (OpenElements / Swirlds Labs) |
| Accuracy | High — hash function properties, SHA family history, and Java code are technically correct |
| Depth | Medium — introductory course; sufficient for concept formation, not sufficient for production implementation guidance |
| Currency | High — SHA-256 and Java `MessageDigest` content is current; MD5 compromise date (2008) confirmed |
| Bias | Low declared bias — course is delivered by a Hedera-affiliated presenter, but the hash function and Java content is neutral and not Hedera-specific |
