---
type: concept
title: "Solidity Fundamentals"
domain: blockchain
complexity: high
tags: [solidity, smart-contracts, EVM, Ethereum, pragma, contract, functions, mappings, events, modifiers, types, deployment, compilation, solc]
created: 2026-08-12
updated: 2026-08-12
status: established
related:
  - "[[concepts/ethereum-evm]]"
  - "[[concepts/blockchain-technology]]"
  - "[[concepts/hedera-network]]"
---

# Solidity Fundamentals

Solidity is the primary high-level language for writing smart contracts that run on the Ethereum Virtual Machine (EVM). It is statically typed, object-oriented, and Turing complete — compiled to EVM bytecode, which executes deterministically on every full node in the network.

---

## Language Overview

| Property | Detail |
|----------|--------|
| Paradigm | Statically typed, object-oriented, contract-oriented |
| Influenced by | JavaScript, C++, Python |
| Execution target | EVM bytecode |
| Official docs | https://docs.soliditylang.org |
| Compiler | `solc` (Solidity compiler) |
| File extension | `.sol` |
| Versioning | Semantic versioning; `pragma` controls which compiler version is used |

---

## Version Pragma

Every Solidity file must declare which compiler version(s) it is compatible with:

```solidity
pragma solidity ^0.8.20;    // compatible with 0.8.20 and later patch versions
pragma solidity >= 0.7.0;   // compatible with any version >= 0.7.0
```

The pragma prevents compilation with an incompatible compiler — important because Solidity's semantics change across major versions (e.g. integer overflow behaviour changed in 0.8.0).

---

## Contract Structure

A **contract** is the fundamental unit of Solidity — analogous to a class in object-oriented languages:

```solidity
pragma solidity ^0.8.20;

contract MyContract {
    // state variables — persistent on-chain storage
    // events          — EVM log entries
    // constructor     — runs once on deployment
    // functions       — callable methods
    // modifiers       — reusable precondition blocks
}
```

---

## Hello World

```solidity
pragma solidity ^0.8.20;

contract HelloWorld {
    string public greet = "Hello World!";
}
```

The `public` keyword auto-generates a getter function — any external caller can read `greet` without writing explicit getter code.

---

## Full Reference Contract — Coin

This contract from the Hedera Developer Course Lecture 3 demonstrates all core constructs in one example:

```solidity
pragma solidity >= 0.7.0;

contract Coin {
    address public minter;                          // state variable
    mapping (address => uint) public balances;      // state variable — mapping

    event Sent(address from, address to, uint amount);  // event declaration

    constructor() {                                 // constructor
        minter = msg.sender;                        // deployer becomes minter
    }

    function mint(address receiver, uint amount) public {
        require(msg.sender == minter);              // access control
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        require(amount <= balances[msg.sender]);    // precondition
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);    // emit event
    }
}
```

---

## State Variables

State variables are stored **permanently on-chain** in the contract's storage trie:

```solidity
address public minter;                         // address type, publicly readable
mapping (address => uint) public balances;     // hash map: address → unsigned int
uint private count;                            // private — not auto-exposed
bool public isActive = true;                   // initialised with a value
```

- All state variables persist across function calls — they are the contract's memory
- Reading state is free (local call); writing state costs gas (`SSTORE` OpCode)
- The `public` modifier auto-generates a getter function at the same name

---

## Constructor

```solidity
constructor() {
    owner = msg.sender;   // msg.sender = address of the account that deployed the contract
}
```

- Runs **exactly once**, at deployment
- Not callable again after deployment
- Sets up the initial state — ownership, configuration, and so on
- If omitted, a default empty constructor is implicitly provided
- Think of the contract instance as a **singleton**: one per deployment, initialised once

---

## Functions

```solidity
contract MyContract {
    // Syntax: function name(params) visibility [modifiers] [returns (type)] { body }

    function hello() public { }                           // no params, no return
    function hello(int amount) public { }                 // one param
    function calculate(int a, int b) public { }           // multiple params
    function getCount() public returns (int) { }          // return value
    function isActive() public returns (bool) { }         // bool return
}
```

### Visibility

| Modifier | Callable from |
|----------|---------------|
| `public` | Anyone — external callers, other contracts, within the contract |
| `private` | Only within this contract |
| `internal` | Within this contract and derived contracts (inheritance) |
| `external` | Only from outside the contract (more gas-efficient than `public` for large arguments) |

### `msg` Global

| Property | Type | Description |
|----------|------|-------------|
| `msg.sender` | `address` | Address of the account that called this function |
| `msg.value` | `uint` | Amount of ETH (in wei) sent with the call |
| `msg.data` | `bytes` | Full calldata |

---

## Events

Events are logged to the EVM's **transaction receipt** — they are cheap to write, cannot be read by contracts on-chain, but are accessible to off-chain consumers (dApps, indexers):

```solidity
// Declare
event Sent(address from, address to, uint amount);

// Emit (inside a function)
emit Sent(msg.sender, receiver, amount);
```

Use cases: notification to a front-end (via `eth_getLogs`), indexing by The Graph, audit trails.

---

## Types

### Value Types

| Type | Description | Notes |
|------|-------------|-------|
| `bool` | Boolean | `true` / `false` |
| `int` | Signed integer | Default = `int256`; variants: `int8`, `int16`, … `int256` (8-bit steps) |
| `uint` | Unsigned integer | Default = `uint256`; variants: `uint8`, `uint16`, … `uint256` |
| Fixed-point | `fixed` / `ufixed` | Partially supported; avoid in production |
| `address` | 20-byte Ethereum address | Supports `.transfer(amount)`, `.call{value:}("")` |
| `bytes1`…`bytes32` | Fixed-size byte arrays | Packed storage |
| `bytes` | Dynamic byte array | Cheaper than `string` for non-text data |
| `string` | Dynamic UTF-8 string | More expensive than `bytes` |
| `enum` | Named constants | Internally stored as `uint8` |

**Integer arithmetic note:** In Solidity ≥ 0.8.0, arithmetic overflows and underflows revert by default. In earlier versions they wrap silently — a common source of security vulnerabilities.

### Reference Types

| Type | Syntax | Description |
|------|--------|-------------|
| `array` | `uint[]` (dynamic) / `uint[5]` (fixed) | Ordered list; dynamic arrays support `.push()`, `.pop()` |
| `mapping` | `mapping(KeyType => ValueType)` | Hash map; keys are not stored; lookups are O(1); no iteration |
| `struct` | `struct Name { fields; }` | Custom composite type; can group related data |

```solidity
// Array
uint[] public scores;
scores.push(95);

// Mapping
mapping(address => uint) public balances;
balances[msg.sender] = 100;

// Struct
struct Person {
    string name;
    uint age;
}
Person public owner = Person("Alice", 30);
```

---

## Control Structures

```solidity
// Conditional
if (balance > 0) {
    // ...
} else {
    // ...
}

// Loops
while (i < 10) { i++; }
do { i++; } while (i < 10);
for (uint i = 0; i < arr.length; i++) { /* ... */ }

// Loop control
break;      // exit loop
continue;   // skip to next iteration

// Return
return value;
```

**Gas caution:** Loops over unbounded arrays or mappings can exhaust the gas limit, causing the transaction to revert. Always bound loop iterations or use off-chain enumeration.

---

## Error Handling

| Mechanism | Behaviour | Typical use |
|-----------|-----------|-------------|
| `require(cond, "msg")` | Reverts if `cond` is `false`; returns unused gas; emits revert reason | Input validation, access control |
| `revert("msg")` | Unconditional revert with a message | Complex conditional error paths |
| `assert(cond)` | Reverts and **consumes all remaining gas** if `cond` is `false` | Internal invariants that should never fail |
| `try / catch` | Catches errors from external calls and contract creation | Interacting with external contracts safely |

**All state changes within a failed (reverted) transaction are rolled back atomically.** The ledger behaves as if the transaction never happened, except that gas consumed up to the point of revert is not returned.

```solidity
function withdraw(uint amount) public {
    require(amount <= balances[msg.sender], "Insufficient balance");
    balances[msg.sender] -= amount;
    payable(msg.sender).transfer(amount);
}
```

---

## Modifiers

Modifiers are reusable precondition blocks that wrap function bodies:

```solidity
modifier onlyOwner() {
    require(msg.sender == owner, "Not the owner");
    _;   // _ is the placeholder — the decorated function's body runs here
}

modifier validAmount(uint amount) {
    require(amount > 0, "Amount must be positive");
    _;
}

function adminAction() public onlyOwner {
    // body executes only if onlyOwner passes
}

function deposit(uint amount) public validAmount(amount) {
    balances[msg.sender] += amount;
}
```

Multiple modifiers can be chained: `function f() public onlyOwner validAmount(x) { }`. They execute left to right.

---

## Compilation and Deployment Lifecycle

### 1. Write the Contract

```solidity
pragma solidity >= 0.7.0;
contract MyContract {
    address owner;
    constructor() { owner = msg.sender; }
    function sayHi() public pure returns (string memory) {
        return "Hi";
    }
}
```

### 2. Compile

```bash
# Local install
solc --bin -o build/contracts contracts/hello_world.sol

# Docker (no local install)
docker run -v $(pwd)/contracts:/contracts \
  ethereum/solc:stable \
  -o /contracts/output --bin
```

Output: a binary `.bin` file — EVM bytecode ready for deployment.

### 3. Deploy

```
Deploy contract → Ledger receives bytecode
                → Constructor executes (owner = msg.sender)
                → Unique contract address returned
```

| Property | Detail |
|----------|--------|
| Each deployment is independent | Deploying the same `.sol` file three times creates three separate contract instances at three different addresses |
| Contract address | Globally unique; derived from the deployer's address and their nonce |
| Immutability | Once deployed, the contract's code cannot be changed (unless it uses an upgradeable proxy pattern) |
| Lifecycle | One instance per deployment; that instance holds all state; no "class" on-chain — only instances |

---

## Advanced Patterns (Reference Links)

| Pattern | Description | Resource |
|---------|-------------|----------|
| `delegatecall` | Execute another contract's code in the calling contract's storage context | solidity-by-example.org/delegatecall |
| Calling contracts | Invoke functions on other deployed contracts by address | solidity-by-example.org/calling-contract |
| Inheritance | `contract B is A { }` — B inherits A's functions and state variables | Solidity docs — `contracts.html#inheritance` |
| `using for` | Attach library functions to types | Solidity docs — `contracts.html#using-for` |
| Libraries | Reusable code deployed once, shared by multiple contracts | Solidity docs — `contracts.html#libraries` |
| Import (local) | `import "./OtherContract.sol";` | Standard |
| Import (Remix / GitHub) | `import "https://github.com/OpenZeppelin/.../ERC20.sol";` | Remix IDE docs |

---

## Hedera and Solidity

The **Hedera Smart Contract Service (HSCS)** runs a Besu EVM instance — Solidity contracts compile and deploy identically on Hedera as on Ethereum mainnet. Key differences:

| Property | Ethereum | Hedera |
|----------|----------|--------|
| Gas price | Volatile (ETH market price) | Fixed USD-denominated ($0.05/contract call) |
| Finality | Probabilistic (6+ confirmations ≈ final) | Mathematical (ABFT, ~3–7 s) |
| TPS | ~15–30 base layer | 15M gas/second |
| Native tokens | ERC-20 / ERC-721 Solidity contracts | HTS precompile at `0x167` — native tokens usable from Solidity |

See [[concepts/hedera-network]] → Developer SDK section and [[concepts/ethereum-evm]] for full EVM architecture detail.

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/ethereum-evm]] | Architecture Solidity compiles to: EVM bytecode, OpCodes, gas, state machine |
| [[concepts/blockchain-technology]] | Smart contracts section (§7) gives the broader context; this page adds full Solidity syntax reference |
| [[concepts/hedera-network]] | HSCS accepts Solidity contracts; HTS precompile at `0x167` allows native Hedera tokens to behave as ERC-20 from Solidity |
| [[concepts/crypto-wallets]] | Wallets interact with deployed contracts — MetaMask calls contract functions via `eth_sendTransaction`; EVM contract addresses are 20-byte values derived the same way as wallet addresses |
| [[sources/hedera-lecture-3-ethereum-solidity]] | Source lecture for this concept page |
