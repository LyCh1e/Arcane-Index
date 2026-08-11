---
type: example
title: "Hedera Local Ledger — Hash-Chained Audit Trail + Testnet Transactions (JavaScript)"
tags: [Hedera, HBAR, blockchain, hash-chaining, SHA-256, JavaScript, Node.js, Hiero, SDK, Testnet, ECDSA, transfer, audit-trail]
domain: blockchain
concept: "[[concepts/hedera-network]]"
related-concepts:
  - "[[concepts/cryptographic-hash-functions]]"
  - "[[concepts/blockchain-technology]]"
created: 2026-08-11
updated: 2026-08-11
status: working
sdk-version: "@hiero-ledger/sdk v2.85.0"
network: Hedera Testnet
---

# Hedera Local Ledger — Hash-Chained Audit Trail + Testnet Transactions

## Overview

This program combines two concepts in a single working example:

1. **A local hash-chained ledger** (`Ledger` class) — a JavaScript implementation of the block-and-chain pattern from [[sources/hedera-lecture-2-blockchain-hashing]], using Node.js `crypto.createHash("sha256")` instead of Java's `MessageDigest`. Each block stores the hash of the previous block; the chain is tamper-evident via `isValid()`.

2. **Real Hedera Testnet operations** — account creation and HBAR transfers using `@hiero-ledger/sdk` (the Hiero-rebranded successor to `@hashgraph/sdk`). Each Testnet transaction is recorded as a block in the local ledger, complete with the Hedera transaction ID and a HashScan URL.

The design reflects a real architectural pattern: **Hedera is the distributed ledger providing consensus and mathematical finality; the local chain is an application-level audit trail** that references Hedera's transaction IDs for verifiability. The local chain is tamper-evident but not distributed — it is a structured log, not a replacement for Hedera itself.

---

## Full Source

```javascript
const crypto = require("crypto");
const {
  AccountId,
  PrivateKey,
  Client,
  TransferTransaction,
  Hbar,
  AccountCreateTransaction,
} = require("@hiero-ledger/sdk"); // v2.85.0

// ============================================================================
// Local hash-chained ledger — app-level audit trail referencing Hedera tx IDs
// ============================================================================

class Ledger {
  constructor() {
    this.chain = [this.createGenesisBlock()];
  }

  createGenesisBlock() {
    const block = {
      index: 0,
      timestamp: new Date().toISOString(),
      type: "GENESIS",
      data: {},
      prevHash: "0",
    };
    block.hash = this.computeHash(block);
    return block;
  }

  computeHash(block) {
    const { hash, ...rest } = block; // never hash the hash field itself
    return crypto.createHash("sha256").update(JSON.stringify(rest)).digest("hex");
  }

  addBlock(type, data) {
    const prevBlock = this.chain[this.chain.length - 1];
    const block = {
      index: prevBlock.index + 1,
      timestamp: new Date().toISOString(),
      type,
      data,
      prevHash: prevBlock.hash,
    };
    block.hash = this.computeHash(block);
    this.chain.push(block);
    return block;
  }

  isValid() {
    for (let i = 1; i < this.chain.length; i++) {
      const current = this.chain[i];
      const prev    = this.chain[i - 1];
      if (current.prevHash !== prev.hash) return false;
      if (current.hash !== this.computeHash(current)) return false;
    }
    return true;
  }

  print() {
    console.log("\n================= LEDGER =================");
    for (const block of this.chain) {
      console.log(`#${block.index} [${block.type}] ${block.timestamp}`);
      if (block.type !== "GENESIS") console.log("  data     :", block.data);
      console.log("  prevHash :", block.prevHash.slice(0, 16) + "...");
      console.log("  hash     :", block.hash.slice(0, 16) + "...");
    }
    console.log(`Chain valid: ${this.isValid()}`);
    console.log("============================================\n");
  }
}

// ============================================================================
// Hedera helpers
// ============================================================================

async function createAccount(client, operatorId, label, initialBalance = 10) {
  const privateKey = PrivateKey.generateECDSA();
  const publicKey  = privateKey.publicKey;

  const tx = new AccountCreateTransaction()
    .setECDSAKeyWithAlias(publicKey)
    .setInitialBalance(new Hbar(initialBalance));

  const response  = await tx.execute(client);
  const receipt   = await response.getReceipt(client);
  const accountId = receipt.accountId;

  console.log(`Created ${label}: ${accountId.toString()}`);
  return { label, accountId, privateKey, publicKey };
}

async function transfer(client, ledger, sender, receiverAccountId, amount) {
  let tx = new TransferTransaction()
    .addHbarTransfer(sender.accountId, new Hbar(-amount))
    .addHbarTransfer(receiverAccountId, new Hbar(amount))
    .freezeWith(client);

  if (sender.privateKey) {
    tx = await tx.sign(sender.privateKey);
  }

  const response = await tx.execute(client);
  const receipt  = await response.getReceipt(client);
  const txId     = response.transactionId.toString();

  ledger.addBlock("TRANSFER", {
    from: sender.accountId.toString(),
    to: receiverAccountId.toString(),
    amountHbar: amount,
    status: receipt.status.toString(),
    hederaTxId: txId,
    hashscanUrl: `https://hashscan.io/testnet/transaction/${txId}`,
  });

  console.log(
    `Transfer ${amount} HBAR: ${sender.accountId} -> ${receiverAccountId} [${receipt.status}]`
  );
}

// ============================================================================
// Main
// ============================================================================

async function main() {
  let client;
  const ledger = new Ledger();

  try {
    const MY_ACCOUNT_ID  = AccountId.fromString(process.env.HEDERA_ACCOUNT_ID);
    const MY_PRIVATE_KEY = PrivateKey.fromStringECDSA(process.env.HEDERA_PRIVATE_KEY);

    client = Client.forTestnet();
    client.setOperator(MY_ACCOUNT_ID, MY_PRIVATE_KEY);

    const operator = { label: "Operator", accountId: MY_ACCOUNT_ID, privateKey: null };

    // 1. Create Alice and Bob
    const alice = await createAccount(client, MY_ACCOUNT_ID, "Alice", 10);
    ledger.addBlock("ACCOUNT_CREATED", { label: "Alice", accountId: alice.accountId.toString() });

    const bob = await createAccount(client, MY_ACCOUNT_ID, "Bob", 5);
    ledger.addBlock("ACCOUNT_CREATED", { label: "Bob", accountId: bob.accountId.toString() });

    // 2. Operator → Alice
    await transfer(client, ledger, operator, alice.accountId, 2);

    // 3. Alice → Bob  (Alice's own key must sign)
    await transfer(client, ledger, alice, bob.accountId, 1);

    // 4. Bob → Operator  (Bob's own key must sign)
    await transfer(client, ledger, bob, MY_ACCOUNT_ID, 0.5);

    ledger.print();
  } catch (error) {
    console.error(error);
  } finally {
    if (client) client.close();
  }
}

main();
```

---

## Setup

```bash
npm install @hiero-ledger/sdk dotenv

# .env
HEDERA_ACCOUNT_ID=0.0.XXXXXX
HEDERA_PRIVATE_KEY=<ECDSA hex private key from Hedera Portal>
```

Run on Testnet:

```bash
node index.js
```

---

## Architecture — Two Layers

```
┌──────────────────────────────────────────────────────┐
│  Application layer                                   │
│  ┌───────────────────────────────────────────────┐  │
│  │  Local Ledger  (Ledger class)                 │  │
│  │  SHA-256 hash-chained blocks                  │  │
│  │  Block types: GENESIS | ACCOUNT_CREATED |     │  │
│  │               TRANSFER                        │  │
│  │  Each TRANSFER block stores hederaTxId +      │  │
│  │  hashscanUrl → anchors audit trail to Hedera  │  │
│  └───────────────────────────────────────────────┘  │
│                         │ references                 │
└─────────────────────────┼────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────┐
│  Hedera Testnet layer                                │
│  Real distributed ledger — Hashgraph ABFT consensus  │
│  AccountCreateTransaction, TransferTransaction       │
│  Transaction IDs, receipts, status codes             │
│  Verifiable on HashScan                              │
└──────────────────────────────────────────────────────┘
```

---

## Key Patterns Explained

### 1. The `computeHash` Destructuring Trick

```javascript
computeHash(block) {
  const { hash, ...rest } = block; // exclude the hash field itself
  return crypto.createHash("sha256").update(JSON.stringify(rest)).digest("hex");
}
```

The block object includes a `hash` field, but you cannot include `hash` in the input to `computeHash` — that would be circular. The object rest-spread `{ hash, ...rest }` extracts `hash` into its own binding and passes only `rest` to the hasher. This is the JavaScript equivalent of the Lecture 2 Java pattern where only `data + previousHash` (not the stored hash) are passed to `MessageDigest`.

**Stability caveat:** `JSON.stringify` does not guarantee stable field ordering across JavaScript engines or after property mutations. For a production system, either sort the keys before serialising or use a canonical encoding library.

### 2. ECDSA Account Creation with Alias

```javascript
const privateKey = PrivateKey.generateECDSA();
const publicKey  = privateKey.publicKey;

const tx = new AccountCreateTransaction()
  .setECDSAKeyWithAlias(publicKey)
  .setInitialBalance(new Hbar(initialBalance));
```

`setECDSAKeyWithAlias` creates a Hedera account whose **EVM alias** (the `0x...` Ethereum-style address) is derived from the ECDSA public key. This makes the account accessible from both the native Hedera API (using the `0.0.XXXX` account ID) and from EVM-compatible tools (MetaMask, Ethers.js) using the derived `0x` alias. This is the standard pattern for EVM-compatible Hedera accounts.

The alternative, `setKey(publicKey)`, creates an account with no EVM alias — accessible only via the native API.

### 3. The `freezeWith` + `sign` Pattern

```javascript
let tx = new TransferTransaction()
  .addHbarTransfer(sender.accountId, new Hbar(-amount))
  .addHbarTransfer(receiverAccountId, new Hbar(amount))
  .freezeWith(client);          // locks transaction bytes

if (sender.privateKey) {
  tx = await tx.sign(sender.privateKey);   // explicit signature
}

const response = await tx.execute(client); // operator auto-signs on execute
```

| Step | Purpose |
|---|---|
| `.freezeWith(client)` | Fixes the transaction bytes (node ID, valid duration, transaction ID). Nothing can change after this. Required before explicit signing. |
| `.sign(privateKey)` | Attaches a cryptographic signature from the given key. Returns a new transaction object (immutable; must reassign). |
| `.execute(client)` | Submits to the network. The **client's operator key signs automatically** at this step — so the operator never needs an explicit `.sign()` call. |

**Why the `if (sender.privateKey)` branch?** The `operator` object is constructed with `privateKey: null` because the SDK auto-signs as the operator on `execute()`. If a non-operator account (Alice or Bob) sends a transaction, their private key must be attached explicitly after freezing. Without it, the network rejects the transaction because the required authorisation signature is missing.

### 4. Transaction ID and HashScan

```javascript
const txId = response.transactionId.toString();
// format: "0.0.XXXXX@1234567890.000000000"
//          account   seconds  nanoseconds

const hashscanUrl = `https://hashscan.io/testnet/transaction/${txId}`;
```

Hedera transaction IDs include the **payer account ID** and the **consensus timestamp** (Unix seconds + nanoseconds), which makes every transaction ID globally unique and self-describing. Pasting the URL into a browser shows the full transaction on HashScan, including fee breakdown, involved accounts, and consensus timestamp.

### 5. Operator Signing Model

The `Client.setOperator(accountId, privateKey)` call designates a single account as the default fee payer and auto-signer. This has two consequences:

- **Every transaction** submitted via `.execute(client)` is automatically signed by the operator's key — even transactions whose `from` account is a different account. The operator pays the Hedera network fee; the `from` account is debited only the explicit HBAR amount.
- **Multi-party transactions** (Alice or Bob sending) still require the `from` account's signature for the debit authorisation. The operator's auto-signature alone is insufficient; both signatures are needed.

---

## Local Ledger — Block Sequence

After a successful run, the local chain contains 7 blocks:

| Index | Type | Key data |
|---|---|---|
| 0 | GENESIS | — |
| 1 | ACCOUNT_CREATED | Alice's accountId |
| 2 | ACCOUNT_CREATED | Bob's accountId |
| 3 | TRANSFER | Operator → Alice, 2 HBAR, hederaTxId |
| 4 | TRANSFER | Alice → Bob, 1 HBAR, hederaTxId |
| 5 | TRANSFER | Bob → Operator, 0.5 HBAR, hederaTxId |

Each `TRANSFER` block's `data.hederaTxId` anchors the local audit trail to the real Hedera ledger, where the transaction is immutably recorded with ABFT finality.

---

## Concepts Demonstrated

| Concept | Demonstrated by |
|---|---|
| Hash chaining | `Ledger.addBlock` stores `prevHash`; `isValid()` recomputes and compares |
| Immutability via hashing | Altering any block's `data` changes its hash, breaking the `prevHash` link in the next block |
| SHA-256 in JavaScript | `crypto.createHash("sha256").update(...).digest("hex")` |
| Hedera account creation | `AccountCreateTransaction().setECDSAKeyWithAlias()` |
| EVM-compatible accounts | `setECDSAKeyWithAlias` vs `setKey` |
| HBAR transfer | `TransferTransaction().addHbarTransfer()` with debit (negative) and credit (positive) entries |
| `freezeWith` + `sign` | Required for non-operator signers; auto-sign applies only to the operator |
| Transaction receipt | `response.getReceipt(client)` → `receipt.status`, `receipt.accountId` |
| HashScan verification | `hashscanUrl` field in each TRANSFER block links to the public block explorer |
| Hiero SDK rebrand | `@hiero-ledger/sdk` is the Linux Foundation successor to `@hashgraph/sdk` |

---

## `@hiero-ledger/sdk` — The Hiero Rebrand

In September 2024, Hedera transferred its source code to the **Linux Foundation Decentralised Trust** project, which operates under the **Hiero** umbrella. The JavaScript SDK was subsequently republished under the new package name:

| Old | New |
|---|---|
| `@hashgraph/sdk` | `@hiero-ledger/sdk` |

The API surface is identical; only the package name changed. Existing code using `@hashgraph/sdk` continues to work; new projects should use `@hiero-ledger/sdk`.

---

## Potential Issues and Improvements

| Issue | Detail | Fix |
|---|---|---|
| `JSON.stringify` key ordering | Object property order in `JSON.stringify` is insertion-order in V8 but not guaranteed across environments | Sort keys before serialising: `JSON.stringify(rest, Object.keys(rest).sort())` |
| No persistence | Local ledger exists only in memory — lost on process exit | Persist to a file (JSON / SQLite) or push blocks to Hedera HCS for durable ordering |
| No Merkle tree | Each block hashes only its own `data`; a Merkle root would allow partial-block proof of inclusion | Implement a Merkle tree over `data` fields if the block data becomes large |
| `initialBalance` in HBAR | `new Hbar(10)` is 10 HBAR; ensure the operator's testnet account has sufficient funds | Fund via the [Hedera Testnet faucet](https://portal.hedera.com) |
| `privateKey: null` for operator | The `operator` object uses `null` to indicate "auto-signed by client" — relies on convention, not type safety | Use TypeScript with a discriminated union type: `{ type: "operator" } | { type: "account", privateKey: PrivateKey }` |

---

## Related Pages

- [[concepts/hedera-network]] — Hedera architecture, native services, governing council, HBAR tokenomics
- [[concepts/cryptographic-hash-functions]] — SHA-256 properties, `MessageDigest` (Java) and `crypto` (Node.js) APIs
- [[sources/hedera-lecture-2-blockchain-hashing]] — the Lecture 2 source that introduced the Block/Chain Java pattern this JavaScript code mirrors
- [[concepts/blockchain-technology]] — broader blockchain architecture including Merkle trees and consensus mechanisms
