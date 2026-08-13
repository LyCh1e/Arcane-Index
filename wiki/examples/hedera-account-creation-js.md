---
type: example
title: "Hedera Account Creation — JavaScript (ECDSA Key + EVM Alias + Mirror Node Query)"
domain: blockchain
tags: [hedera, javascript, account-creation, ECDSA, ED25519, EVM-alias, mirror-node, testnet, hiero-sdk]
created: 2026-08-13
updated: 2026-08-13
status: established
related:
  - "[[concepts/hedera-network]]"
  - "[[examples/hedera-local-ledger-js]]"
  - "[[concepts/crypto-wallets]]"
---

# Hedera Account Creation — JavaScript

Creates a new Hedera account from scratch: generates an ECDSA key pair, submits an `AccountCreateTransaction`, retrieves the native account ID from the receipt, then queries the Mirror Node REST API to confirm the on-chain EVM address.

---

## Full Annotated Code

```javascript
const {
  AccountId,
  PrivateKey,
  Client,
  AccountCreateTransaction,
  Hbar,
} = require("@hiero-ledger/sdk"); // v2.85.0

async function main() {
  let client;
  try {
    // ── 1. Load operator credentials from environment ──────────────────────
    // Operator = fee payer; all tx fees debited from this account.
    // NOTE: operator uses ED25519 (common for Hedera-native accounts);
    //       the new account will use ECDSA (required for EVM alias / MetaMask).
    const MY_ACCOUNT_ID  = AccountId.fromString(process.env.HEDERA_ACCOUNT_ID);
    const MY_PRIVATE_KEY = PrivateKey.fromStringED25519(process.env.HEDERA_PRIVATE_KEY);

    // ── 2. Build client and set operator ──────────────────────────────────
    client = Client.forTestnet();
    client.setOperator(MY_ACCOUNT_ID, MY_PRIVATE_KEY);
    // setOperator: operator auto-signs every tx on .execute() and pays fees.
    // No .sign(operatorKey) call needed for the operator's own transactions.

    // ── 3. Generate ECDSA key pair for the new account ────────────────────
    const accountPrivateKey = PrivateKey.generateECDSA();
    const accountPublicKey  = accountPrivateKey.publicKey;

    // ── 4. Build and execute AccountCreateTransaction ─────────────────────
    const txCreateAccount = new AccountCreateTransaction()
      // HIP-1313: high-volume entity creation (batch optimisation) — optional
      // .setHighVolume(true)
      // .setMaxTransactionFee(new Hbar(5))

      // setECDSAKeyWithAlias: derives EVM address from keccak256(publicKey)[12:]
      // → account gets BOTH a native 0.0.XXXXX ID AND an EVM 0x... alias.
      // ✅ Recommended — fully EVM compatible (MetaMask, Ethers.js, Hardhat).
      // ⚠  EVM compatibility breaks if the ECDSA key is later rotated.
      .setECDSAKeyWithAlias(accountPublicKey)

      // Alternative (not recommended for EVM use):
      // .setKeyWithoutAlias(accountPublicKey)
      // → EVM address derived from account ID, NOT the public key.
      //   NOT fully EVM compatible.

      .setInitialBalance(new Hbar(10)); // fund from operator account

    const txCreateAccountResponse = await txCreateAccount.execute(client);

    // ── 5. Parse receipt ───────────────────────────────────────────────────
    const receiptCreateAccountTx = await txCreateAccountResponse.getReceipt(client);
    const statusCreateAccountTx  = receiptCreateAccountTx.status;
    const accountId              = receiptCreateAccountTx.accountId;
    // Transaction ID format: 0.0.OPERATOR_ID@unix_seconds.nanoseconds
    const txIdAccountCreated     = txCreateAccountResponse.transactionId.toString();

    // ── 6. Query Mirror Node for EVM address ──────────────────────────────
    // Consensus nodes finalise immediately (~3–7 s), but Mirror Nodes
    // propagate asynchronously. Wait before querying to avoid a 404.
    await new Promise((resolve) => setTimeout(resolve, 5000)); // 5-second grace period

    let accountEvmAddress;
    const mirrorResponse = await fetch(
      `https://testnet.mirrornode.hedera.com/api/v1/accounts/${accountId.toString()}`
    );
    if (mirrorResponse.ok) {
      const mirrorData  = await mirrorResponse.json();
      accountEvmAddress = mirrorData.evm_address; // "0x..." hex string
    }

    // ── 7. Log results ─────────────────────────────────────────────────────
    console.log("--------- Create Account ---------");
    console.log("Receipt status :", statusCreateAccountTx.toString());
    console.log("Transaction ID :", txIdAccountCreated);
    console.log("Hashscan URL   :", `https://hashscan.io/testnet/transaction/${txIdAccountCreated}`);
    console.log("Account ID     :", accountId.toString());
    console.log("EVM Address    :", accountEvmAddress);
    console.log("Private key    :", `0x${accountPrivateKey.toStringRaw()}`);
    console.log("Public key     :", `0x${accountPublicKey.toStringRaw()}`);

  } catch (error) {
    console.error(error);
  } finally {
    if (client) client.close(); // always release the gRPC connection
  }
}

main();
```

---

## Key Patterns and Concepts

### ED25519 vs ECDSA Key Types

| | ED25519 | ECDSA |
|--|---------|-------|
| Used for | Hedera-native accounts (faster, smaller signatures) | EVM-compatible accounts (MetaMask, Ethers.js) |
| `fromString` helper | `PrivateKey.fromStringED25519(str)` | `PrivateKey.fromStringECDSA(str)` |
| `generate` | `PrivateKey.generateED25519()` | `PrivateKey.generateECDSA()` |
| EVM alias support | No | Yes — `setECDSAKeyWithAlias` |

**Rule:** Use ECDSA for any account that will interact with EVM smart contracts or be imported into MetaMask. Use ED25519 for pure Hedera-native operations where EVM interop is not needed.

### `setECDSAKeyWithAlias` vs `setKeyWithoutAlias`

| Method | EVM Address derived from | EVM Compatibility | Notes |
|--------|------------------------|------------------|-------|
| `setECDSAKeyWithAlias(pub)` | `keccak256(pub)[12:]` — the public key | ✅ Full | Standard Ethereum key derivation. Breaks if key is later rotated. |
| `setKeyWithoutAlias(pub)` | Account ID (`0.0.XXXXX` → EVM mapping) | ⚠️ Partial | Not compatible with Ethereum tooling that derives address from key. |

**Recommended:** Always use `setECDSAKeyWithAlias` unless you have a specific reason not to require EVM compatibility.

### Mirror Node REST API

The Mirror Node provides a read-only REST API over historical transaction and account data. The consensus nodes handle the live ledger; Mirror Nodes index it for querying.

```
Base URL (Testnet): https://testnet.mirrornode.hedera.com/api/v1/
Base URL (MainNet): https://mainnet.mirrornode.hedera.com/api/v1/
```

**Key endpoints:**

| Endpoint | Returns |
|----------|---------|
| `GET /accounts/{idOrAddress}` | Full account info including `evm_address`, `balance`, `key` |
| `GET /transactions/{transactionId}` | Full transaction record |
| `GET /contracts/{idOrAddress}` | Contract info and bytecode |
| `GET /tokens/{tokenId}` | Token metadata |

**Propagation delay:** There is a gap between Hedera consensus finalisation (~3–7 s) and Mirror Node propagation. Always wait before querying — a 5-second `setTimeout` is a common heuristic for development. Production code should poll with retries and exponential backoff.

```javascript
// Production-grade Mirror Node poll with retry
async function fetchWithRetry(url, retries = 5, delayMs = 2000) {
  for (let i = 0; i < retries; i++) {
    const res = await fetch(url);
    if (res.ok) return res.json();
    await new Promise(r => setTimeout(r, delayMs * (i + 1)));
  }
  throw new Error(`Mirror Node fetch failed after ${retries} attempts: ${url}`);
}
```

### Transaction ID Format

```
0.0.4567788@1752930600.123456789
│           │          │
│           │          └─ nanoseconds within the second
│           └──────────── Unix seconds (UTC)
└──────────────────────── Payer account ID (the operator)
```

HashScan URL: `https://hashscan.io/testnet/transaction/${txId}`

### HIP-1313 — High-Volume Entity Creation (commented out)

HIP-1313 is a Hedera Improvement Proposal for batch account creation optimisations. The `setHighVolume(true)` flag reduces the per-account cost for bulk creation (e.g., onboarding thousands of users). Not needed for single-account creation in development.

---

## Output Example

```
--------- Create Account ---------
Receipt status : SUCCESS
Transaction ID : 0.0.4567788@1752930600.123456789
Hashscan URL   : https://hashscan.io/testnet/transaction/0.0.4567788@1752930600.123456789
Account ID     : 0.0.5123456
EVM Address    : 0xa1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0
Private key    : 0xdeadbeef...
Public key     : 0x04abcdef...
```

---

## Security Notes

- **Never log private keys in production.** The `console.log` of `accountPrivateKey.toStringRaw()` is for development and educational use only.
- Always load credentials from environment variables (`.env` via `dotenv`), never hardcode them.
- Store the private key immediately after generating — it is not persisted anywhere by the SDK.
- The `evm_address` returned by the Mirror Node matches `keccak256(publicKey)[12:]` when `setECDSAKeyWithAlias` is used. You can verify this derivation off-chain.

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/hedera-network]] | Mirror Node architecture, network environments, JS SDK patterns |
| [[examples/hedera-local-ledger-js]] | More complex JS example: account creation + HBAR transfers + local hash chain |
| [[concepts/crypto-wallets]] | ECDSA key derivation mirrors Ethereum wallet key derivation (same curve: secp256k1) |
