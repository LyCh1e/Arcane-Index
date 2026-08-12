---
type: concept
title: "Solidity Fundamentals"
domain: blockchain
complexity: high
tags: [solidity, smart-contracts, EVM, Ethereum, pragma, contract, functions, mappings, events, modifiers, types, deployment, compilation, solc, security, patterns]
created: 2026-08-12
updated: 2026-08-12
status: established
related:
  - "[[concepts/ethereum-evm]]"
  - "[[concepts/blockchain-technology]]"
  - "[[concepts/hedera-network]]"
  - "[[concepts/solidity-security]]"
  - "[[sources/solidity-docs-0.8.36]]"
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

---

## Data Locations

Reference types (`array`, `struct`, `bytes`, `string`, `mapping`) require an explicit **data location** annotation. The location controls both gas cost and copy-vs-reference semantics.

| Location | Lifetime | Mutability | Gas cost |
|----------|----------|------------|----------|
| `storage` | Permanent (on-chain) | Read/write | Expensive (`SSTORE`) |
| `memory` | Single function call | Read/write | Cheap |
| `calldata` | Single external call | Read-only | Cheapest (no copy) |

### Assignment Rules

| From → To | Behaviour |
|-----------|-----------|
| `storage` ↔ `memory` or `calldata` | Always creates an independent copy |
| `memory` → `memory` | Creates a **reference** (changes are shared) |
| `storage` → local `storage` variable | Creates a **reference** (writes modify state) |

```solidity
function example(uint[] calldata data) external {
    uint[] memory copy = data;       // copy from calldata to memory
    uint[] storage ref = myArray;    // reference — writes go on-chain
}
```

**Prefer `calldata` over `memory` for read-only external function parameters** — it avoids copying the data into memory and saves gas.

---

## Full Type Reference

### Value Types (copied on assignment)

| Type | Description | Key rules |
|------|-------------|-----------|
| `bool` | `true` / `false` | `&&` and `\|\|` short-circuit |
| `int8`…`int256` | Signed integers (8-bit steps) | Default alias: `int` = `int256` |
| `uint8`…`uint256` | Unsigned integers (8-bit steps) | Default alias: `uint` = `uint256`; checked arithmetic ≥ 0.8 |
| `fixed` / `ufixed` | Fixed-point decimal | **Not fully supported** — avoid in production |
| `address` | 20-byte address | Comparisons; `.balance`, `.code`, `.codehash`, `.call()`, `.delegatecall()`, `.staticcall()` |
| `address payable` | Like `address` but can receive Ether | Adds `.transfer(amount)` and `.send(amount)` |
| `bytes1`…`bytes32` | Fixed-size byte arrays | Index access `x[k]`; `.length` read-only |
| `enum` | Named constants | Stored as `uint8`; max 256 members; `type(E).min/max` |
| User-defined value type | `type C is V` | Zero-cost abstraction; `C.wrap()` / `C.unwrap()` |
| Function type | `function (T) visibility [mutability] returns (R)` | Internal (jump) or external (address + selector) |

**Integer bounds:** `type(uint256).max = 2**256 - 1`; `type(int256).min = -2**255`.

**Arithmetic notes (≥ 0.8.0):**
- `+`, `-`, `*`, `**`, `++`, `--` revert on overflow/underflow by default.
- Use `unchecked { ... }` to restore wrapping behaviour (gas saving for known-safe maths).
- Division always rounds toward zero. Division by zero always reverts (cannot be disabled).
- `0**0` is defined as `1` by the EVM.

**`address` vs `address payable`:**
- `address payable → address`: implicit.
- `address → address payable`: explicit via `payable(addr)`.
- `tx.origin` and `msg.sender` are `address` (not payable) since v0.8.0.

### Reference Types

```solidity
// Dynamic array
uint[] public scores;
scores.push(95);
scores.pop();
uint len = scores.length;

// Fixed array — size is part of the type
uint[5] public fixedScores;

// Bytes / string
bytes public data;     // dynamic byte array (efficient, tightly packed)
string public name;    // dynamic UTF-8 string (no length/index access)

// Struct
struct Funder { address addr; uint amount; }
Funder memory f = Funder(msg.sender, msg.value);

// Mapping (storage only — no iteration, no length)
mapping(address => uint) public balances;
```

**Array members:**
- `.length` — element count (read-only in memory).
- `.push()` — appends zero-element and returns a reference (dynamic storage / bytes only).
- `.push(x)` — appends `x`.
- `.pop()` — removes and implicitly deletes last element.

**String comparison** — no native operator; use `keccak256(abi.encodePacked(a)) == keccak256(abi.encodePacked(b))`.  
**String concatenation** — `string.concat(a, b)` (≥ 0.8.12) or `bytes.concat(...)`.

**Mappings** — `mapping(KeyType => ValueType)`. Keys may be any value type or `string`/`bytes`. Values can be any type including other mappings. Only in `storage`. No enumeration — use a companion array to track keys if iteration is needed.

**Array slices** — `x[start:end]` on `calldata` arrays only. Returns a view; elements from `x[start]` to `x[end-1]`.

---

## Panic Codes (≥ 0.8.0)

When `assert` or a runtime condition fails, Solidity throws `Panic(uint256)` with a code:

| Code | Cause |
|------|-------|
| `0x01` | `assert(false)` |
| `0x11` | Arithmetic overflow/underflow outside `unchecked` |
| `0x12` | Division or modulo by zero |
| `0x21` | Converting invalid value to `enum` |
| `0x22` | Accessing incorrectly-encoded storage byte array |
| `0x31` | `.pop()` on empty array |
| `0x32` | Array/`bytesN` index out of bounds or negative |
| `0x41` | Allocating too much memory |
| `0x51` | Calling zero-initialised internal function variable |

---

## try / catch — Full Reference

`try` works only with external function calls or `new` contract creation:

```solidity
interface DataFeed { function getData(address token) external returns (uint); }

contract Consumer {
    DataFeed feed;

    function rate(address token) public returns (uint value, bool success) {
        try feed.getData(token) returns (uint v) {
            // success path — v is the return value
            return (v, true);
        } catch Error(string memory reason) {
            // caught revert("reason") or require(false, "reason")
            return (0, false);
        } catch Panic(uint errorCode) {
            // caught assert failure, overflow, etc. — errorCode is the Panic code
            return (0, false);
        } catch (bytes memory lowLevelData) {
            // caught revert() with no data, or unknown error encoding
            return (0, false);
        }
    }
}
```

**Important caveats:**
- State changes from a failed external call are reverted, but state changes in *the calling contract* before the `try` are not.
- Errors inside the `try` expression itself (before the external call executes) are not caught.
- Decoding errors in the return data cause an exception in the calling contract (not caught by `try/catch`).
- A bare `catch { }` clause catches everything without inspecting the data.

---

## Function Calls — Internal vs External

```solidity
// Internal call — compiles to a jump; shares memory
uint result = computeInternal(x);

// External call — creates a message call; allocates new memory
uint result2 = this.computePublic(x);          // via this
uint result3 = otherContract.someFunction(x);  // via contract instance

// With value and gas options
otherContract.someFunction{value: 1 ether, gas: 50000}(x);
```

**Named call arguments (any order):**
```solidity
set({value: 2, key: 3});
```

**Destructuring return values:**
```solidity
(uint a, , uint c) = multiReturn();   // skip middle value
(a, c) = (c, a);                      // swap
```

---

## CREATE2 — Deterministic Addresses

```solidity
// Predict address before deployment
address predicted = address(uint160(uint(keccak256(abi.encodePacked(
    bytes1(0xff),
    address(this),
    salt,            // bytes32
    keccak256(abi.encodePacked(type(D).creationCode, abi.encode(constructorArg)))
)))));

D d = new D{salt: salt}(constructorArg);
require(address(d) == predicted);
```

Useful for counterfactual deployments — contracts that are instantiated only on dispute.

---

## Common Patterns

### Withdrawal Pattern (safe fund dispersal)

```solidity
contract WithdrawalContract {
    address public richest;
    uint public mostSent;
    mapping(address => uint) pendingWithdrawals;

    function becomeRichest() public payable {
        require(msg.value > mostSent, "Not rich enough");
        pendingWithdrawals[richest] += mostSent;
        richest = msg.sender;
        mostSent = msg.value;
    }

    function withdraw() public {
        uint amount = pendingWithdrawals[msg.sender];
        pendingWithdrawals[msg.sender] = 0;   // zero BEFORE transfer (CEI pattern)
        payable(msg.sender).transfer(amount);
    }
}
```

Never push funds to recipients — let them pull. This isolates failure: if one recipient's receive function reverts, other withdrawals still succeed.

### Access Restriction with Modifiers

```solidity
error Unauthorized();
error TooEarly(uint time);

modifier onlyBy(address account) {
    if (msg.sender != account) revert Unauthorized();
    _;
}

modifier onlyAfter(uint time) {
    if (block.timestamp <= time) revert TooEarly(time);
    _;
}

modifier costs(uint amount) {
    require(msg.value >= amount, "Insufficient payment");
    _;
    if (msg.value > amount)
        payable(msg.sender).transfer(msg.value - amount);  // refund excess
}
```

### State Machine Pattern

```solidity
enum Stage { AcceptingBids, RevealBids, Finished }
Stage public stage = Stage.AcceptingBids;
uint public creationTime = block.timestamp;

modifier atStage(Stage s) {
    require(stage == s, "Wrong stage");
    _;
}

modifier timedTransitions() {
    if (stage == Stage.AcceptingBids && block.timestamp >= creationTime + 10 days)
        stage = Stage.RevealBids;
    if (stage == Stage.RevealBids && block.timestamp >= creationTime + 12 days)
        stage = Stage.Finished;
    _;   // timedTransitions must come BEFORE atStage in modifier list
}

function bid() public timedTransitions atStage(Stage.AcceptingBids) { /* ... */ }
function reveal() public timedTransitions atStage(Stage.RevealBids)  { /* ... */ }
```

**Modifier order matters:** `timedTransitions` must appear before `atStage` so the stage is updated before being checked.

---

## Global Variables & Cheatsheet

### Block Properties

| Variable | Type | Description |
|----------|------|-------------|
| `block.number` | `uint` | Current block number |
| `block.timestamp` | `uint` | Current block Unix timestamp (seconds) |
| `block.chainid` | `uint` | EIP-155 chain ID |
| `block.coinbase` | `address payable` | Current block miner |
| `block.gaslimit` | `uint` | Current block gas limit |
| `block.basefee` | `uint` | Current block base fee (EIP-1559) |
| `block.prevrandao` | `uint` | Randomness from beacon chain (replaces `block.difficulty` post-Merge) |
| `blockhash(n)` | `bytes32` | Hash of block `n` (only last 256 blocks) |
| `blobhash(i)` | `bytes32` | Versioned hash of the i-th blob (EIP-4844) |

### Transaction / Message Properties

| Variable | Type | Description |
|----------|------|-------------|
| `msg.sender` | `address` | Immediate caller |
| `msg.value` | `uint` | Wei sent with call |
| `msg.data` | `bytes calldata` | Complete calldata |
| `msg.sig` | `bytes4` | First 4 bytes of calldata (function selector) |
| `tx.origin` | `address` | Original external account (never use for auth) |
| `tx.gasprice` | `uint` | Gas price of the transaction |
| `gasleft()` | `uint` | Remaining gas |

### Cryptographic & Math Functions

| Function | Description |
|----------|-------------|
| `keccak256(bytes memory)` | Keccak-256 hash |
| `sha256(bytes memory)` | SHA-256 hash |
| `ripemd160(bytes memory)` | RIPEMD-160 hash |
| `ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s)` | Recover signer address from ECDSA signature |
| `addmod(x, y, k)` | `(x + y) % k` with arbitrary precision |
| `mulmod(x, y, k)` | `(x * y) % k` with arbitrary precision |

### Address Members

| Member | Description |
|--------|-------------|
| `.balance` | Wei balance |
| `.code` | `bytes memory` — EVM bytecode (may be empty) |
| `.codehash` | `bytes32` — keccak256 of code |
| `.call(bytes memory)` | Low-level CALL; returns `(bool, bytes memory)` |
| `.delegatecall(bytes memory)` | Low-level DELEGATECALL |
| `.staticcall(bytes memory)` | Low-level STATICCALL (read-only) |
| `.transfer(uint)` | `address payable` only; reverts on failure; 2300 gas stipend |
| `.send(uint)` | `address payable` only; returns `bool`; 2300 gas stipend |

### ABI Encoding

| Function | Description |
|----------|-------------|
| `abi.encode(...)` | ABI-encode arguments (padded) |
| `abi.encodePacked(...)` | Packed encoding — no padding; collision-prone for variable-length types |
| `abi.encodeWithSelector(sel, ...)` | Prepend 4-byte selector |
| `abi.encodeWithSignature("f(uint)", ...)` | Compute selector from string |
| `abi.encodeCall(fn, (...))` | Fully type-checked call encoding |
| `abi.decode(data, (T1, T2, ...))` | Decode ABI-encoded bytes |

### Type Information

```solidity
type(uint256).min    // 0
type(uint256).max    // 2**256 - 1
type(int256).min     // -2**255
type(MyContract).name          // contract name as string
type(MyContract).creationCode  // creation bytecode
type(MyContract).runtimeCode   // runtime bytecode
type(MyInterface).interfaceId  // EIP-165 interface ID (XOR of function selectors)
```

---

## 0.8.x Changes at a Glance

| Change | Impact |
|--------|--------|
| **Overflow/underflow reverts** | Safe by default; use `unchecked { }` for gas saving |
| **ABI coder v2 default** | Supports structs/nested arrays in external calls |
| **`byte` removed** | Use `bytes1` |
| **`assert` uses Panic** | Same gas refund as `require`; separate error code for tooling |
| **Address literals are `address`** | Use `payable(addr)` explicitly |
| **`tx.origin`/`msg.sender` are `address`** | Cast to `address payable` where needed |
| **Exponentiation right-associative** | `2**3**2 = 2**9 = 512` |

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/ethereum-evm]] | Architecture Solidity compiles to: EVM bytecode, OpCodes, gas, state machine |
| [[concepts/solidity-security]] | Dedicated security pitfalls page: reentrancy, CEI, tx.origin, mapping deletion |
| [[concepts/blockchain-technology]] | Smart contracts section (§7) gives the broader context |
| [[concepts/hedera-network]] | HSCS accepts Solidity contracts; HTS precompile at `0x167` allows native Hedera tokens to behave as ERC-20 from Solidity |
| [[concepts/crypto-wallets]] | Wallets interact with deployed contracts — MetaMask calls contract functions via `eth_sendTransaction` |
| [[sources/hedera-lecture-3-ethereum-solidity]] | Source lecture for initial concept page |
| [[sources/solidity-docs-0.8.36]] | Official Solidity docs — full type system, patterns, security |
