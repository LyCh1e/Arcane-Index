---
type: concept
title: "Crypto Wallets"
domain: blockchain
complexity: medium
tags: [crypto, wallets, private-key, public-key, hot-wallet, cold-wallet, hardware-wallet, HashPack, Ledger, mnemonic, BIP-39, HBAR, bitcoin]
created: 2026-08-12
updated: 2026-08-12
status: established
related:
  - "[[concepts/bitcoin-history]]"
  - "[[concepts/hedera-network]]"
  - "[[concepts/blockchain-technology]]"
  - "[[concepts/cryptographic-hash-functions]]"
---

# Crypto Wallets

A **crypto wallet** is a tool that stores and manages the cryptographic keys needed to access and transact with blockchain-based assets. The name is somewhat misleading: a wallet does not store cryptocurrency in the way a physical wallet holds cash. It stores **private keys** — the mathematical credentials that prove ownership of funds recorded on a blockchain.

---

## The Central Analogy

The most important mental model for wallets, as framed in the Hedera Developer Course Lecture 1:

| Key | Equivalent | Critical difference |
|-----|-----------|---------------------|
| **Public key** | Bank account number | Share it freely — others need it to send you funds |
| **Private key** | Online banking password | Never share — but unlike a password, **there is no recovery**. Loss = permanent loss of funds. |

The absence of a recovery mechanism is the defining characteristic of self-custodied cryptocurrency. There is no bank employee, no reset link, and no legal recourse if a private key is lost.

---

## Hot vs Cold

The primary security classification is based on internet connectivity:

| Category | Definition | Security | Convenience |
|----------|-----------|----------|-------------|
| **Hot wallet** | Connected to the internet during use | Lower — exposed to online attacks (phishing, malware, exchange hacks) | High — immediate access for trading and spending |
| **Cold wallet** | Never connected to the internet | Higher — private key cannot be extracted remotely | Lower — requires physical interaction for each transaction |

Neither type is universally better. The choice depends on use case: hot wallets for active trading and small amounts; cold wallets for long-term storage of significant holdings.

---

## Wallet Types

### Hardware Wallet (Cold)

A physical electronic device that generates and stores private keys internally. The key **never leaves the device** — transactions are signed on-chip and only the signed transaction (not the key) is transmitted to the network.

**Example: Ledger**
- Supports 1,000+ cryptocurrencies including BTC, ETH, and HBAR
- Recovery mechanism: a **24-word mnemonic phrase** (BIP-39 standard)
- The mnemonic is the only backup — must be written on paper and stored offline
- Loss of both the device and the mnemonic = permanent loss of funds

### Paper Wallet (Cold)

A document (physical or PDF) containing a printed private key and its corresponding public key, typically encoded as QR codes. The ultimate form of cold storage — no electronic device required.

Trade-offs:
- Secure from online attacks
- Extremely fragile: fire, water, or physical loss destroys access permanently
- Inconvenient for regular use; typically used as one-time vault storage
- Cannot be partially spent without importing the key into a hot wallet, at which point cold security is lost

### Desktop Wallet (Hot)

Software installed on a personal computer. Security depends on the host machine — malware, keyloggers, and physical access to the machine are threat vectors.

### Mobile Wallet (Hot)

Smartphone application. Convenient for everyday spending; exposed to phone theft, SIM-swapping, and malicious apps.

**Example: HashPack (HBAR)**
- Leading HBAR wallet for the Hedera ecosystem
- Available as Chrome extension and mobile app
- Supports Hedera **Mainnet and Testnet**
- Hedera Testnet accounts receive daily free HBAR from a faucet

### Web Wallet (Hot)

Browser-based; the private key may be managed by a third-party server (custodial) or by the browser itself (non-custodial). The most convenient and highest-risk category.

**Example: Coinbase Wallet**
- Mobile app and Chrome extension
- **Non-custodial** — Coinbase does not hold keys; the user is solely responsible
- Supports BTC, ETH, and ERC-20 tokens
- Note: distinct from a Coinbase exchange account (custodial — Coinbase holds the keys)

---

## Custodial vs Non-Custodial

| Model | Who holds the key? | Risk |
|-------|-------------------|------|
| **Custodial** | Third party (exchange, bank) | Counterparty risk — if the exchange fails (cf. Mt. Gox 2014, FTX 2022), funds may be lost |
| **Non-custodial** | The user | Self-custody risk — loss of the key has no recourse |

The Bitcoin principle is **self-custody**: removing trust in third parties by taking personal responsibility for key management. In practice, most retail users hold funds on custodial exchanges for convenience.

---

## Mnemonic Phrases (Seed Phrases)

Modern wallets use a **mnemonic phrase** (also called a seed phrase or recovery phrase) as the human-readable representation of the wallet's master private key:

| Property | Detail |
|----------|--------|
| Standard | BIP-39 (Bitcoin Improvement Proposal 39) |
| Length | 12 or 24 words |
| Word list | 2,048 words (English standard; other languages available) |
| Derivation | The mnemonic is a deterministic encoding of 128–256 bits of entropy |
| Recovery | The entire wallet — all accounts, all keys — can be restored from the mnemonic alone |

**Security rule:** The mnemonic must be stored **offline, on paper**, in a secure physical location. Photographing it, emailing it, or storing it in a cloud service defeats its purpose. Anyone with the mnemonic has full access to all funds.

---

## Security Features

When evaluating any wallet, look for:

| Feature | Purpose |
|---------|---------|
| **Encryption** | Private key stored encrypted on the device; requires a PIN or password to decrypt |
| **2FA (Two-Factor Authentication)** | Additional verification layer for web/mobile wallets |
| **Backup and recovery** | Mnemonic phrase or encrypted keystore file for device loss |
| **Multi-signature (multi-sig)** | Requires *m* of *n* keys to authorise a transaction; eliminates single points of failure; common in corporate treasury management |

---

## Wallet Selection by Use Case

| Use case | Recommended type | Example |
|----------|-----------------|---------|
| Long-term BTC/ETH storage | Hardware (cold) | Ledger |
| Active HBAR development / Testnet | Web extension (hot) | HashPack |
| Daily crypto spending | Mobile (hot) | Coinbase Wallet |
| Corporate treasury / high-value multi-party | Multi-sig hardware | Ledger + multi-sig policy |
| Offline archival vault | Paper | Self-generated paper wallet |

---

## The Hedera Ecosystem Wallet — HashPack

HashPack is the primary wallet for interacting with the Hedera network:

- Native support for HBAR and Hedera Token Service (HTS) tokens
- **Testnet mode** — creates a free testnet account (funded daily via faucet); essential for development exercises
- **EVM alias support** — HashPack accounts can expose a `0x`-style EVM address for MetaMask compatibility
- Integration with HashScan (the Hedera block explorer) for transaction visibility
- Used in Hedera Developer Course hands-on exercises: create Testnet account, send HBAR, explore HashScan

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/bitcoin-history]] | Bitcoin's design is built around self-custody; Mt. Gox 2014 and FTX 2022 are custodial failure case studies |
| [[concepts/hedera-network]] | HashPack is the standard Hedera development wallet; Hedera accounts have both a native ID (`0.0.XXXXX`) and an EVM alias |
| [[concepts/cryptographic-hash-functions]] | Public/private key pairs are derived using ECDSA over elliptic curves; private keys are 256-bit integers; public keys are derived, not stored separately on most wallets |
| [[concepts/blockchain-technology]] | Wallets interact with the UTXO model (Bitcoin) or account model (Hedera, Ethereum); keys sign transactions broadcast to the network |
| [[examples/hedera-local-ledger-js]] | `PrivateKey.generateECDSA()` and `setECDSAKeyWithAlias(publicKey)` demonstrate programmatic account creation equivalent to a wallet generating a new account |
