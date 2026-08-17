---
type: example
title: "Hedera HTS, HCS, and Batch Transactions — JavaScript (@hiero-ledger/sdk)"
domain: blockchain
tags: [hedera, javascript, HTS, HCS, tokens, fungible, TokenCreate, TokenAirdrop, TokenBurn, TopicCreate, BatchTransaction, batchify, HIP-551, HIP-904, hiero-sdk]
created: 2026-08-13
updated: 2026-08-13
status: established
related:
  - "[[concepts/hedera-network]]"
  - "[[concepts/token-standards-erc20-erc721]]"
  - "[[examples/hedera-account-creation-js]]"
  - "[[examples/hedera-local-ledger-js]]"
---

# Hedera HTS, HCS, and Batch Transactions — JavaScript

Five operations from a single script using `@hiero-ledger/sdk` v2.85.0. Builds on the account-creation pattern from [[examples/hedera-account-creation-js]].

**SDK imports used in this script:**
```javascript
const {
  AccountId, PrivateKey, Client, AccountCreateTransaction, Hbar,
  TransferTransaction,
  TokenCreateTransaction, TokenType, TokenUpdateTransaction,
  TokenAirdropTransaction, TokenBurnTransaction,
  TopicCreateTransaction,
  BatchTransaction,
} = require("@hiero-ledger/sdk");
```

---

## 1. HBAR Transfer

```javascript
const txTransfer = new TransferTransaction()
  .addHbarTransfer(MY_ACCOUNT_ID, new Hbar(-1))    // debit operator
  .addHbarTransfer(receiverAccount, new Hbar(1));   // credit receiver

const txTransferResponse = await txTransfer.execute(client);
const receiptTransferTx  = await txTransferResponse.getReceipt(client);
const statusTransferTx   = receiptTransferTx.status;          // "SUCCESS"
const txIdTransfer       = txTransferResponse.transactionId.toString();

console.log("Receipt status :", statusTransferTx.toString());
console.log("Transaction ID :", txIdTransfer);
console.log("Hashscan URL   :", `https://hashscan.io/testnet/transaction/${txIdTransfer}`);
```

**Notes:**
- `addHbarTransfer` amounts must sum to zero — the network enforces this.
- No `.freezeWith()` or `.sign()` needed here because the operator is the only signer (fee payer and sender are the same account). The SDK signs automatically on `.execute()`.
- `receiverAccount` is a placeholder — fill in the target `AccountId`.

---

## 2. Token Creation

### 2a — Basic Token (Immutable — no admin or supply keys)

```javascript
const txTokenCreate = await new TokenCreateTransaction()
  .setTokenName("Your Token Name")
  .setTokenSymbol("F")
  .setTokenType(TokenType.FungibleCommon)  // fungible; use TokenType.NonFungibleUnique for NFTs
  .setTreasuryAccountId(MY_ACCOUNT_ID)     // receives all initial supply
  .setInitialSupply(5000)                  // 5,000 units in smallest denomination
  .freezeWith(client);

// Treasury must sign — it is receiving the initial supply
const signedTxTokenCreate  = await txTokenCreate.sign(MY_PRIVATE_KEY);
const txTokenCreateResponse = await signedTxTokenCreate.execute(client);
const receiptTokenCreateTx  = await txTokenCreateResponse.getReceipt(client);
const tokenId               = receiptTokenCreateTx.tokenId;
const statusTokenCreateTx   = receiptTokenCreateTx.status;
```

**Why treasury must sign:** The treasury receives the initial supply. The network requires the treasury's explicit authorisation to prevent tokens being forced into an account.

**Without admin/supply keys → immutable token:**
- Token name, symbol, and metadata cannot be updated after creation.
- No additional tokens can be minted; no existing tokens can be burned via the protocol.
- The only way to reduce supply is to transfer tokens to a burn address (but the total supply on-chain stays the same).

### 2b — Advanced Token (Mutable — with admin and supply keys)

```javascript
const txTokenCreate = await new TokenCreateTransaction()
  .setTokenName("Your Token Name")
  .setTokenSymbol("F")
  .setTokenType(TokenType.FungibleCommon)
  .setTreasuryAccountId(MY_ACCOUNT_ID)
  .setAdminKey(MY_PRIVATE_KEY.publicKey)   // ← enables TokenUpdateTransaction
  .setSupplyKey(MY_PRIVATE_KEY.publicKey)  // ← enables TokenMintTransaction / TokenBurnTransaction
  .setInitialSupply(5000)
  .freezeWith(client);

const signedTxTokenCreate   = await txTokenCreate.sign(MY_PRIVATE_KEY);
const txTokenCreateResponse = await signedTxTokenCreate.execute(client);
const receiptTokenCreateTx  = await txTokenCreateResponse.getReceipt(client);
const tokenId               = receiptTokenCreateTx.tokenId;
```

### Token Key Reference

| Key | Set with | Enables |
|-----|----------|---------|
| `adminKey` | `.setAdminKey(pubKey)` | `TokenUpdateTransaction` — rename, change keys, etc. |
| `supplyKey` | `.setSupplyKey(pubKey)` | `TokenMintTransaction` / `TokenBurnTransaction` — adjust supply |
| `treasuryKey` | (implicit — treasury account) | Receives initial supply and any minted tokens |
| `freezeKey` | `.setFreezeKey(pubKey)` | `TokenFreezeTransaction` — freeze individual accounts |
| `kycKey` | `.setKycKey(pubKey)` | `TokenGrantKycTransaction` — KYC-gate accounts |
| `wipeKey` | `.setWipeKey(pubKey)` | `TokenWipeTransaction` — forcibly remove tokens from an account |
| `pauseKey` | `.setPauseKey(pubKey)` | `TokenPauseTransaction` — pause all transfers globally |

**Keys not set at creation time cannot be added later** (unless the admin key is set — then the admin can add missing keys via `TokenUpdateTransaction`).

---

## 3. HCS Topic Creation

HCS (Hedera Consensus Service) provides an ordered, timestamped, tamper-evident message log. A **topic** is the channel. Messages are published to a topic; Hedera timestamps and sequences them.

```javascript
// Bare topic — no submit key, no memo, no access controls
const txCreateTopic = new TopicCreateTransaction();

const txCreateTopicResponse = await txCreateTopic.execute(client);
const receiptCreateTopicTx  = await txCreateTopicResponse.getReceipt(client);
const statusCreateTopicTx   = receiptCreateTopicTx.status;
const topicId               = receiptCreateTopicTx.topicId.toString(); // "0.0.XXXXX"

console.log("Topic ID :", topicId);
```

**Advanced topic creation options:**

```javascript
const txCreateTopic = new TopicCreateTransaction()
  .setTopicMemo("My application event log")
  .setSubmitKey(submitPublicKey)     // only this key can publish messages
  .setAdminKey(adminPublicKey);      // only this key can update or delete the topic
```

**Publishing a message to the topic:**
```javascript
const { TopicMessageSubmitTransaction } = require("@hiero-ledger/sdk");

await new TopicMessageSubmitTransaction()
  .setTopicId(topicId)
  .setMessage("{ \"event\": \"user_login\", \"userId\": 42 }")
  .execute(client);
```

**Subscribing to a topic (mirror node):**
```javascript
const { TopicMessageQuery } = require("@hiero-ledger/sdk");

new TopicMessageQuery()
  .setTopicId(topicId)
  .subscribe(client, (message) => {
    console.log(message.contents.toString());
    console.log("Consensus timestamp:", message.consensusTimestamp.toString());
    console.log("Sequence number    :", message.sequenceNumber.toString());
  });
```

---

## 4. Batch Transaction (HIP-551)

A batch transaction atomically executes multiple independent Hedera transactions. If any inner transaction fails, **all are rolled back**. This is the primary mechanism for composing multi-step workflows without distributed transaction risk.

### The `batchify()` Pattern

`batchify(client, batchPublicKey)` converts a normal transaction into an **inner transaction** payload. The `batchPublicKey` is the key that will sign the outer `BatchTransaction` — it acts as the batch's authority key.

**Important:** Each inner transaction still requires all of its own signers. `batchify` does not remove any existing signing requirements.

### Full Batch Example: Create Account + Update Token + Airdrop + Burn

```javascript
// ── Keys ──────────────────────────────────────────────────────────────────────
const recipientAccountPrivateKey = PrivateKey.generateECDSA();
const recipientAccountPublicKey  = recipientAccountPrivateKey.publicKey;

// The batch key signs the OUTER BatchTransaction — not the inner transactions
const batchKey       = PrivateKey.generateECDSA();
const batchPublicKey = batchKey.publicKey;

// ── Inner Tx 1: Create recipient account ─────────────────────────────────────
const txCreateAccount = await new AccountCreateTransaction()
  .setECDSAKeyWithAlias(recipientAccountPublicKey)
  .setInitialBalance(new Hbar(10))
  .batchify(client, batchPublicKey);  // ← converts to inner transaction
const signedTxCreateAccount = await txCreateAccount.sign(MY_PRIVATE_KEY);
// Operator signs because it funds the initial balance

// ── Counterfactual addressing ─────────────────────────────────────────────────
// For an ECDSA account created with setECDSAKeyWithAlias, the Hedera account ID
// can be derived from the public key BEFORE the account is created on-chain.
// shard=0, realm=0 → standard Testnet/MainNet values.
const recipientAccountId = recipientAccountPublicKey.toAccountId(0, 0);
// This gives us the account ID to use in later transactions within the same batch,
// even though the account does not exist yet at batch construction time.

// ── Inner Tx 2: Update token name (requires admin key) ───────────────────────
const txTokenUpdate = await new TokenUpdateTransaction()
  .setTokenId(tokenId)
  .setTokenName("Your New Token Name")
  .batchify(client, batchPublicKey);
const signedTxTokenUpdate = await txTokenUpdate.sign(MY_PRIVATE_KEY);
// MY_PRIVATE_KEY is the admin key set at token creation

// ── Inner Tx 3: Token airdrop (HIP-904) ──────────────────────────────────────
// TokenAirdropTransaction works even if the recipient has NOT yet associated
// with the token. Use this instead of TransferTransaction for recipient-friendly drops.
const txTokenAirdrop = await new TokenAirdropTransaction()
  .addTokenTransfer(tokenId, MY_ACCOUNT_ID, -1000)       // debit treasury
  .addTokenTransfer(tokenId, recipientAccountId, 1000)   // credit recipient
  .batchify(client, batchPublicKey);
const signedTxTokenAirdrop = await txTokenAirdrop.sign(MY_PRIVATE_KEY);
// Sender (treasury) must sign

// ── Inner Tx 4: Burn tokens (requires supply key) ────────────────────────────
const txBurnToken = await new TokenBurnTransaction()
  .setTokenId(tokenId)
  .setAmount(1000)           // reduces total supply on-chain
  .batchify(client, batchPublicKey);
const signedTxBurnToken = await txBurnToken.sign(MY_PRIVATE_KEY);
// MY_PRIVATE_KEY is the supply key set at token creation

// ── Assemble and execute the batch ───────────────────────────────────────────
const batchTx = await new BatchTransaction()
  .addInnerTransaction(signedTxCreateAccount)
  .addInnerTransaction(signedTxTokenUpdate)
  .addInnerTransaction(signedTxTokenAirdrop)
  .addInnerTransaction(signedTxBurnToken)
  .freezeWith(client)
  .sign(batchKey);           // batch key signs the OUTER BatchTransaction

const txResponse = await batchTx.execute(client);
const receipt    = await txResponse.getReceipt(client);
const batchStatus = receipt.status;
const txId        = txResponse.transactionId.toString();

// ── HashScan URL (different format for batches) ───────────────────────────────
// Standard tx URL: /transaction/0.0.X@seconds.nanos
// Batch tx URL:    /transactionsById/0.0.X-seconds-nanos  ← hyphens, not @/.
const [entityId, timestamp] = txId.split('@');
const [seconds, nanos]      = timestamp.split('.');
const formattedTxId         = `${entityId}-${seconds}-${nanos}`;

const innerTxIds = batchTx.innerTransactionIds; // array of inner transaction IDs

console.log("Batch status          :", batchStatus.toString());
console.log("Transaction ID        :", txId);
console.log("Hashscan URL          :", `https://hashscan.io/testnet/transactionsById/${formattedTxId}`);
console.log("Inner transaction IDs :", innerTxIds.map(id => id.toString()));
```

---

## Pattern Reference

### `batchify()` vs Regular Transaction

| | Regular Transaction | Batchified Transaction |
|--|--------------------|-----------------------|
| Execution | Independent, immediate | Deferred — inside `BatchTransaction` |
| Atomicity | None — other txs are unaffected on failure | All-or-nothing — any failure rolls back all |
| Signing | Signers sign normally | Same signers required + batch key on outer tx |
| Receipt | Per-transaction | Per-batch (outer) + inner IDs accessible |

### TokenAirdropTransaction vs TransferTransaction (for tokens)

| | `TransferTransaction` + `addTokenTransfer` | `TokenAirdropTransaction` + `addTokenTransfer` |
|--|-------------------------------------------|------------------------------------------------|
| Recipient pre-requirement | Must have run `TokenAssociateTransaction` | None — association handled automatically |
| Cost | Standard transfer fee | Airdrop fee (slightly higher) |
| HIP | Standard | HIP-904 |
| Use case | Internal transfers between known accounts | Public token distributions, onboarding new users |

### Counterfactual Account ID Derivation

```javascript
// For ECDSA accounts with EVM alias, the account ID can be derived before creation:
const accountId = ecdsaPublicKey.toAccountId(0, 0);  // shard=0, realm=0

// This allows batching an account creation with subsequent operations
// (token airdrop, contract call) that reference the not-yet-created account.
```

This is only valid for accounts created with `setECDSAKeyWithAlias`. The derived `accountId` matches the EVM alias approach (keccak256 of the public key).

### HashScan URL Formats

| Transaction type | URL path | ID format |
|-----------------|----------|-----------|
| Standard | `/testnet/transaction/{txId}` | `0.0.XXXXX@seconds.nanos` |
| Batch | `/testnet/transactionsById/{txId}` | `0.0.XXXXX-seconds-nanos` (hyphens) |

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/hedera-network]] | HTS and HCS service architecture; JS SDK patterns |
| [[concepts/token-standards-erc20-erc721]] | ERC-20 interface matches HTS fungible token behaviour; HTS SDK layer |
| [[examples/hedera-account-creation-js]] | Account creation pattern reused inside the batch |
| [[examples/hedera-local-ledger-js]] | Earlier JS example: HBAR transfers and the `freezeWith + sign` pattern |
