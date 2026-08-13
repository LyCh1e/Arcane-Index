---
type: source
title: "Hedera Developer Course — Lecture 4: HAPI, Smart Contract Deployment & Tokens"
source: raw/Blockchain_Lecture4.md
fetched: 2026-08-13
domain: blockchain
tags: [hedera, HAPI, java-sdk, smart-contracts, deployment, ERC-20, ERC-721, tokens, stablecoins, voting-contract]
quality: primary — official Hedera developer course by Hendrik Ebbers (OpenElements / Swirlds Labs)
related:
  - "[[concepts/hedera-network]]"
  - "[[concepts/token-standards-erc20-erc721]]"
  - "[[concepts/solidity-fundamentals]]"
  - "[[examples/hedera-lecture4-voting-contract]]"
---

# Source: Hedera Developer Course — Lecture 4

**File:** `raw/Blockchain_Lecture4.md`  
**Speaker:** Hendrik Ebbers (@HendrikEbbers) — OpenElements / Swirlds Labs  
**Part:** 3 of 3 in the Hedera Developer Course (Java + Solidity)  
**Slides:** 66 slides across four major sections

---

## What This Lecture Covers

| Section | Slides | Topic |
|---------|--------|-------|
| Hedera Network Overview | 1–17 | Architecture, sustainability facts, network environments, Testnet access |
| Development Workflow — HAPI | 18–35 | Java SDK, smart contract deployment pipeline, web3j, Solidity on Hedera |
| Voting Contract Sample | 36–48 | Full worked Solidity example, V1 (basic) → V2 (access-controlled) |
| Coins & Tokens | 50–66 | Fungible (ERC-20) vs non-fungible (ERC-721), stablecoins, USDC on Hedera |

---

## Key Concepts Extracted

### Hedera Network — Facts and Environments

**Network facts (current production data):**

| Metric | Hedera | Ethereum (comparison) |
|--------|--------|----------------------|
| Transactions/day | >40,000,000 | ~1,000,000 |
| Cost per transaction | $0.001 | ~$1.72 |
| Energy per transaction | 0.000003 kWh | 0.006 kWh (2,000× more) |
| TPS (MainNet) | >1,000 | ~15–30 |
| Total production transactions | >35,000,000,000 | — |

**Network environments:**

| Environment | Purpose |
|-------------|---------|
| **MainNet** | Live production network |
| **TestNet** | Free development/testing — 10,000 HBAR/day via faucet |
| **PreviewNet** | Preview upcoming protocol changes before TestNet |
| **LocalNode** | Local Docker-based network (`bit.ly/3JqeMvz`) — fully isolated |

**Sustainability:** Hedera is committed to carbon-negative operations via quarterly carbon offset purchases.

---

### HAPI — Hedera API

HAPI is Hedera's native API, accessible via SDKs for multiple languages. The Java SDK is:

```xml
<dependency>
    <groupId>com.hedera.hashgraph</groupId>
    <artifactId>sdk</artifactId>
    <version>2.17.0</version>
</dependency>
```

(GitHub: `hashgraph/hedera-sdk-java`)

**Smart contract deployment — four steps:**

1. Connect to the ledger
2. Upload compiled bytecode (creates a `FileId`)
3. Create the contract from the file (creates a `ContractId`)
4. Call contract functions via query

**Step 1 — Connect:**
```java
final Client client = Client.forNetwork(
    Collections.singletonMap(consensusNodeAddress, consensusNodeId))
    .setMirrorNetwork(List.of(mirrorNodeAddress));
client.setOperator(AccountId.fromString(operatorId), PrivateKey.fromString(operatorKey));
```

Simplified for Testnet:
```java
Client client = Client.forTestnet();
client.setOperator(myAccountId, myPrivateKey);
client.setDefaultMaxTransactionFee(new Hbar(100));
client.setMaxQueryPayment(new Hbar(50));
```

**Step 2 — Upload bytecode:**
```java
byte[] bytecode = readCompiledContract();
FileCreateTransaction fileCreateTx = new FileCreateTransaction();
fileCreateTx.setContents(bytecode);
TransactionResponse response = fileCreateTx.execute(client);
FileId fileId = response.getReceipt(client).fileId;
```

**Step 3 — Create contract:**
```java
ContractCreateTransaction contractTx = new ContractCreateTransaction()
    .setBytecodeFileId(fileId)
    .setGas(100_000);   // set max gas cost
TransactionResponse contractResponse = contractTx.execute(client);
ContractId contractId = contractResponse.getReceipt(client).contractId;
```

Alternative one-step flow:
```java
final ContractCreateFlow flow = new ContractCreateFlow()
    .setBytecode(bytecodeInHex)
    .setGas(1_000_000);
final TransactionResponse transactionResponse = flow.execute(client);
final ContractId contractId = transactionResponse.getReceipt(client).contractId;
```

**Step 4 — Call a function:**
```java
final ContractCallQuery contractQuery = new ContractCallQuery()
    .setGas(100_000)
    .setContractId(contractId)
    .setFunction("greet");
ContractFunctionResult result = contractQuery.execute(client);
```

**Transaction fields (apply to any transaction):**
```java
Transaction transaction = new AccountCreateTransaction()
    .setKey(key)
    .setInitialBalance(Hbar.fromTinybars(1000))
    .setMaxTransactionFee(new Hbar(2))
    .setTransactionMemo("memo");
```

---

### web3j (Alternative Java Library)

`web3j` was created for Ethereum but works with Hedera via EVM compatibility:
- API for interacting with smart contracts
- Java wrapper generator for smart contracts
- Smart contract compilation wrapper
- Maven plugin

Useful when code must be portable between Ethereum and Hedera.

---

### Voting Contract (V1 and V2)

See [[examples/hedera-lecture4-voting-contract]] for the full annotated contracts.

**V1 — Basic Poll:** `struct Proposal { bytes32 name; uint count; }` array; constructor populates from `bytes32[]` parameter; `vote(uint)` increments counter; `winner()` iterates to find max.

**V2 — Access-Controlled Poll:** Adds `address public admin` (= `msg.sender` in constructor), `enum VoterState { NotAuthorized, Authorized, Voted }`, `mapping(address => VoterState)`. `vote()` requires `Authorized`; `authorize()` requires caller is admin and voter is `NotAuthorized`.

---

### Coins and Tokens

**Coin vs Token:**

| | Coin | Token |
|--|------|-------|
| Example | BTC, ETH, HBAR | USDT, USDC, any ERC-20/721 |
| Created by | Mining / protocol (native asset) | Smart contract on existing chain |
| Needs own chain | Yes | No |

**Fungible vs Non-Fungible:**

| Property | Fungible (ERC-20) | Non-Fungible (ERC-721) |
|----------|------------------|----------------------|
| Interchangeable | Yes — 1 USDC = 1 USDC | No — each token is unique |
| Divisible | Yes | No (integer token IDs) |
| Use case | Currency, governance, staking | Art, collectibles, identity |

**ERC-20 interface:**
```
totalSupply(): uint256
balanceOf(address): uint256
transfer(address, uint256): bool
allowance(address, address): uint256
approve(address, uint256): bool
transferFrom(address, address, uint256): bool
```

**ERC-721 interface:**
```
balanceOf(owner): balance
ownerOf(tokenId): owner
safeTransferFrom(from, to, tokenId, data)
transferFrom(from, to, tokenId)
approve(to, tokenId)
setApprovalForAll(operator, approved)
getApproved(tokenId): operator
isApprovedForAll(owner, operator): bool
```

**Stablecoins:**
- **Fiat-collateralised:** USDT (Tether), USDC (Circle), BUSD (Binance/Paxos)
- **Crypto-collateralised:** backed by other crypto assets with overcollateralisation
- **Algorithmic:** use protocol mechanics (e.g., seigniorage) to maintain the peg — highest risk (see Luna/Terra collapse)
- USDC is available on Hedera: `circle.com/en/usdc-multichain/hedera`
- USDC Ethereum contract: `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` (verifiable on Etherscan)

---

## Source Quality Assessment

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Authority | ★★★★★ | Official Hedera developer course — Hendrik Ebbers (OpenElements / Swirlds Labs) |
| Accuracy | ★★★★☆ | Production facts current to 2023; SDK versions may be superseded |
| Depth | ★★★★☆ | Code examples are slide-level — sufficient for patterns, not production-ready without expansion |
| Freshness | ★★★☆☆ | 2023 course material; HAPI / web3j sections are directionally correct but SDK versions evolve |
| Applicability | ★★★★★ | Directly relevant to Hedera HSCS and the Hedera Developer Course exercises |

---

## Wiki Pages Generated / Updated from This Source

- [[concepts/hedera-network]] — added: network environments table (MainNet/TestNet/PreviewNet/LocalNode), Java SDK smart contract deployment pipeline, web3j overview
- [[concepts/token-standards-erc20-erc721]] — new page: coin vs token, fungible vs non-fungible, ERC-20 and ERC-721 interfaces, stablecoin taxonomy
- [[examples/hedera-lecture4-voting-contract]] — new example page: Poll V1 and Poll V2 fully annotated contracts
