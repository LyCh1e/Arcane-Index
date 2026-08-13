---
type: concept
title: "Token Standards — ERC-20 and ERC-721"
domain: blockchain
complexity: medium
tags: [tokens, ERC-20, ERC-721, fungible, NFT, stablecoins, Ethereum, Hedera, HTS, smart-contracts]
created: 2026-08-13
updated: 2026-08-13
status: established
related:
  - "[[concepts/hedera-network]]"
  - "[[concepts/solidity-fundamentals]]"
  - "[[concepts/ethereum-evm]]"
  - "[[sources/hedera-lecture-4-hapi-tokens]]"
---

# Token Standards — ERC-20 and ERC-721

Tokens are digital assets issued on an existing blockchain. Unlike **coins** (native assets of their own chain), tokens are implemented as smart contracts that conform to a standard interface — ensuring wallets, exchanges, and DeFi protocols can interact with any compliant token without custom integration.

---

## 1. Coin vs Token

| Property | Coin | Token |
|----------|------|-------|
| Examples | BTC, ETH, HBAR | USDT, USDC, any ERC-20/ERC-721 |
| Lives on | Its own dedicated blockchain | An existing chain (Ethereum, Hedera, etc.) |
| Created by | Protocol (mining, staking, genesis) | Deploying a smart contract |
| Needs its own chain | Yes | No — piggybacks on the host chain's security |

**Key insight:** A token creator does not need to build consensus, validators, or a p2p network. They deploy a contract, and the host chain handles all of that. This dramatically lowers the barrier to issuance — but also means token security inherits the host chain's security plus any bugs in the contract.

---

## 2. Fungible vs Non-Fungible

| Property | Fungible | Non-Fungible |
|----------|----------|-------------|
| Definition | Every unit is identical and interchangeable | Each unit is unique and distinguishable |
| Divisible | Yes — fractions make sense (0.5 USDC) | No — integer token IDs only |
| Uniform | Yes — 1 USDC on Binance = 1 USDC on Coinbase | No — token #42 of a collection ≠ token #43 |
| Standard | ERC-20 | ERC-721 |
| Use cases | Currency, governance, staking, stablecoins | Art, collectibles, identity, real-world asset tokenisation |

---

## 3. ERC-20 — Fungible Token Standard

ERC-20 defines a minimal interface every fungible token must implement. Any contract exposing these functions and events is compatible with wallets, DEXes, and DeFi protocols without further integration work.

### Interface

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    // ── Events ────────────────────────────────────────────────────────────────
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // ── State queries ─────────────────────────────────────────────────────────
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);

    // ── Transfers ─────────────────────────────────────────────────────────────
    function transfer(address to, uint256 amount) external returns (bool);

    // ── Allowance (delegated spending) ────────────────────────────────────────
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
}
```

### Key Mechanisms

**Direct transfer:** The token holder calls `transfer(to, amount)` — tokens move from `msg.sender` to `to`.

**Delegated transfer (allowance model):**
1. Token holder calls `approve(spender, amount)` — grants `spender` the right to move up to `amount` tokens.
2. `spender` (e.g., a DEX smart contract) calls `transferFrom(holder, dest, amount)`.

This two-step pattern enables DeFi composability: you approve a DEX router once, then it can execute swaps on your behalf without holding your tokens.

**Minimal implementation example:**

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply);
    }
}
```

---

## 4. ERC-721 — Non-Fungible Token Standard

ERC-721 assigns a unique `tokenId` (uint256) to each token. Ownership is tracked per `tokenId`, not per address balance.

### Interface

```solidity
interface IERC721 {
    // ── Events ────────────────────────────────────────────────────────────────
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);
    event Approval(address indexed owner, address indexed approved, uint256 indexed tokenId);
    event ApprovalForAll(address indexed owner, address indexed operator, bool approved);

    // ── Ownership ─────────────────────────────────────────────────────────────
    function balanceOf(address owner) external view returns (uint256);
    function ownerOf(uint256 tokenId) external view returns (address);

    // ── Transfers ─────────────────────────────────────────────────────────────
    function safeTransferFrom(address from, address to, uint256 tokenId, bytes calldata data) external;
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function transferFrom(address from, address to, uint256 tokenId) external;

    // ── Approvals ─────────────────────────────────────────────────────────────
    function approve(address to, uint256 tokenId) external;
    function getApproved(uint256 tokenId) external view returns (address);

    // ── Operator approvals (approve all tokens) ───────────────────────────────
    function setApprovalForAll(address operator, bool approved) external;
    function isApprovedForAll(address owner, address operator) external view returns (bool);
}
```

### Key Differences from ERC-20

| | ERC-20 | ERC-721 |
|--|--------|---------|
| `balanceOf` | Total tokens owned (integer amount) | Number of distinct NFTs owned |
| Identification | Amount only — all tokens are identical | By `tokenId` — each is unique |
| `ownerOf` | Not applicable | Returns the owner of a specific `tokenId` |
| Approval granularity | By amount | By `tokenId` (single) or by operator (all) |
| `safeTransferFrom` | Not required | Required — checks recipient can handle NFTs |

`safeTransferFrom` calls `onERC721Received` on the recipient if it is a contract — preventing NFTs from being permanently locked in contracts that cannot handle them.

### Minimal implementation example

```solidity
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract MyNFT is ERC721 {
    uint256 private _tokenIdCounter;

    constructor() ERC721("MyNFT", "MNFT") {}

    function safeMint(address to) public {
        _safeMint(to, _tokenIdCounter);
        _tokenIdCounter++;
    }
}
```

---

## 5. Stablecoins

A stablecoin is a token designed to maintain a stable value, typically pegged to a fiat currency. The peg mechanism determines the risk profile.

### Taxonomy

| Type | Mechanism | Examples | Risk |
|------|-----------|---------|------|
| **Fiat-collateralised** | Backed 1:1 by fiat held in reserve | USDT (Tether), USDC (Circle), BUSD (Binance/Paxos) | Counterparty risk — requires trusting the issuer |
| **Crypto-collateralised** | Backed by over-collateralised crypto assets | DAI (MakerDAO) | Smart contract risk; collateral volatility |
| **Algorithmic** | Protocol-controlled supply expansion/contraction | Terra UST (collapsed May 2022) | Structural fragility — death spiral risk |

### USDC — Case Study

USDC is the canonical regulated fiat-collateralised stablecoin:
- Issued by Circle, regulated by US financial institutions
- Each USDC is fully backed by 1 USD in reserve
- Available on multiple chains including **Ethereum, Hedera, Solana, Avalanche**
- On Hedera: `circle.com/en/usdc-multichain/hedera`
- On Ethereum, the ERC-20 contract is deployed at `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` (verifiable on Etherscan)
- Solidity source code: `github.com/circlefin/stablecoin-evm`

---

## 6. Tokens on Hedera — HTS vs ERC

Hedera offers two mechanisms for tokens:

| | **HTS (Hedera Token Service)** | **ERC-20/721 on HSCS** |
|--|-------------------------------|----------------------|
| How | Native protocol primitive — no Solidity required | Standard EVM smart contract via HSCS |
| Cost | $0.0001/transfer, 10,000 TPS | $0.05/contract call, 15M gas/s |
| Built-in features | KYC, freeze, pause, wipe, supply controls, royalties | Must implement in Solidity |
| Interoperability | `0x167` HTS precompile lets Solidity contracts use HTS tokens | Full ERC standard compatibility |
| Use case | Enterprise, regulated tokens, high-volume transfer | DeFi protocols, complex tokenomics |

**The HTS precompile at `0x167`** bridges both worlds: a Solidity contract can call native HTS operations (transfer, mint, burn) using the same EVM CALL that it would use to call any other contract. This means an ERC-20–compatible DEX can trade native HTS tokens without wrapping them.

---

## 7. Summary: Which Standard?

| Goal | Standard / Service |
|------|-------------------|
| Currency, governance token, staking | ERC-20 / HTS fungible token |
| Digital art, collectible, identity | ERC-721 / HTS NFT |
| Stable value pegged to USD | ERC-20 stablecoin (USDC, USDT) |
| High-volume transfer on Hedera | HTS (no Solidity needed) |
| DeFi composability on Hedera | ERC-20/721 on HSCS, using HTS precompile for native tokens |

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/hedera-network]] | HTS service details (TPS, cost, precompile at `0x167`), HSCS deployment |
| [[concepts/solidity-fundamentals]] | Solidity used to implement ERC-20/ERC-721 contracts |
| [[concepts/ethereum-evm]] | EVM executes token contract code; DELEGATECALL used by HTS precompile |
| [[concepts/solidity-security]] | Token contracts need CEI pattern, access control, reentrancy guards |
| [[sources/hedera-lecture-4-hapi-tokens]] | Primary source for this page |
