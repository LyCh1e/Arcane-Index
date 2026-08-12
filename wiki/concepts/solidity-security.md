---
type: concept
title: "Solidity Security"
domain: blockchain
complexity: high
tags: [solidity, smart-contracts, security, reentrancy, access-control, overflow, gas, patterns, audit]
created: 2026-08-12
updated: 2026-08-12
status: established
related:
  - "[[concepts/solidity-fundamentals]]"
  - "[[concepts/ethereum-evm]]"
  - "[[sources/solidity-docs-0.8.36]]"
---

# Solidity Security

Smart contract security is qualitatively different from conventional software security: **bugs are permanent and funds are real**. Once deployed, contract code cannot be patched; any exploitable vulnerability may drain the contract before a fix can be deployed. This page catalogs the principal attack vectors and defences from the official Solidity documentation.

---

## 1. Reentrancy

**The canonical smart contract vulnerability.** When contract A calls contract B (or transfers Ether to it), B's code runs before A's state updates complete. B can re-enter A's function in a still-vulnerable state.

### Vulnerable Pattern

```solidity
mapping(address => uint) public shares;

function withdraw() public {
    // ❌ State updated AFTER interaction
    (bool success,) = msg.sender.call{value: shares[msg.sender]}("");
    if (success) shares[msg.sender] = 0;   // too late — attacker already looped
}
```

**Attack:** Attacker's contract implements a `receive()` function that calls `withdraw()` again before `shares[msg.sender] = 0` executes. Each recursive call passes the check because the balance has not yet been zeroed.

### Safe Pattern: Checks-Effects-Interactions (CEI)

```solidity
function withdraw() public {
    uint share = shares[msg.sender];
    shares[msg.sender] = 0;               // ✅ Effect first
    payable(msg.sender).transfer(share);   // ✅ Interaction last
}
```

**Rule:** Always follow this sequence within every function:
1. **Checks** — validate parameters and state (`require`, `if revert`)
2. **Effects** — update contract state
3. **Interactions** — call external contracts, transfer Ether

**Additional defence:** Reentrancy guard (mutex):

```solidity
bool private locked;

modifier nonReentrant() {
    require(!locked, "Reentrant call");
    locked = true;
    _;
    locked = false;
}
```

---

## 2. `tx.origin` Authentication — Never Use It

`tx.origin` is the original EOA that initiated the entire call chain. `msg.sender` is the immediate caller.

### Phishing Attack Via `tx.origin`

```solidity
// ❌ Vulnerable
contract Wallet {
    address owner;
    function transfer(address payable dest, uint amount) public {
        require(tx.origin == owner, "Not owner");   // checks original initiator
        dest.transfer(amount);
    }
}

// Attacker's contract — owner is tricked into calling this:
contract Attack {
    Wallet wallet;
    address payable attacker;
    receive() external payable {
        wallet.transfer(attacker, address(wallet).balance);
        // tx.origin is still the owner — the require passes!
    }
}
```

### Fix

```solidity
// ✅ Correct
require(msg.sender == owner, "Not owner");
```

**Rule:** Never use `tx.origin` for authorisation. Use `msg.sender`.

---

## 3. Integer Overflow and Underflow

Pre-0.8.0 Solidity silently wrapped on overflow. A counter at `uint8` max (255) incremented by 1 became 0 — used to bypass balance checks.

### ≥ 0.8.0 Default Behaviour

Arithmetic reverts on overflow/underflow. This is safe by default.

### `unchecked` — Use With Care

```solidity
// Gas-saving for known-safe loops (index cannot overflow)
for (uint256 i = 0; i < length;) {
    // ... process array[i] ...
    unchecked { ++i; }   // safe because i < length < 2**256
}
```

**Never use `unchecked` on user-controlled values without bounds validation.**

### Input Validation

```solidity
function deposit(uint256 amount) external {
    require(amount > 0 && amount <= MAX_DEPOSIT, "Invalid amount");
    balances[msg.sender] += amount;
}
```

---

## 4. Gas Limit and Loops

**Unbounded loops can permanently brick a contract function.**

```solidity
// ❌ Danger — loop over user-controlled storage array
function payAll() public {
    for (uint i = 0; i < recipients.length; i++) {
        payable(recipients[i]).transfer(shares[recipients[i]]);
    }
}
```

If `recipients` grows large enough, this function will exceed the block gas limit and always revert — **permanently locking funds**.

### Fixes

1. **Withdrawal pattern** — let each recipient pull their own funds (O(1) per user).
2. **Paginated processing** — pass `start` and `end` indices; process in batches.
3. **Off-chain computation** — compute the recipient list off-chain; pass it as calldata.

```solidity
// ✅ Withdrawal pattern (O(1) per call)
function withdraw() external {
    uint amount = shares[msg.sender];
    shares[msg.sender] = 0;
    payable(msg.sender).transfer(amount);
}
```

---

## 5. Sending and Receiving Ether — Pitfalls

### Unexpected Ether

Contracts cannot fully prevent receiving Ether:
- A miner can target any address as `block.coinbase`.
- `selfdestruct(target)` forces Ether into any address, bypassing `receive()` and `fallback()`.

**Do not write logic that depends on `address(this).balance` being exactly a specific value.**

### Gas Stipend Problem

`transfer()` and `send()` forward only **2300 gas** — not enough for storage writes in the recipient's `receive()`. Using `call{value:}("")` forwards all remaining gas and enables reentrancy if CEI is not followed.

| Method | Failure behaviour | Gas forwarded | Reentrancy risk |
|--------|-----------------|---------------|-----------------|
| `.transfer(x)` | Reverts | 2300 (fixed) | Very low |
| `.send(x)` | Returns `false` | 2300 (fixed) | Very low |
| `.call{value:x}("")` | Returns `(bool,bytes)` | All remaining | **High** — must use CEI |

**Best practice:** Use `.call` with CEI pattern; check the return value.

```solidity
(bool success,) = payable(recipient).call{value: amount}("");
require(success, "Transfer failed");
```

---

## 6. Mapping Deletion — Phantom Storage

Mappings have no key tracking — `delete myMapping` does nothing useful because the keys are not stored. Deleting an array of structs that contain mappings leaves the inner mapping data accessible.

```solidity
struct Record { mapping(uint => uint) data; }
Record[] public records;

// Adding then deleting a record does NOT clear the mapping
records.push();
records[0].data[1] = 42;
delete records[0];   // struct zeroed, but mapping data PERSISTS in storage
records.push();      // new record at index 0 can access the old mapping value
```

### Fix

Implement an **iterable mapping** that tracks keys explicitly:

```solidity
mapping(address => uint) public balances;
address[] public keys;

function set(address key, uint value) public {
    if (balances[key] == 0) keys.push(key);
    balances[key] = value;
}

function remove(address key) public {
    delete balances[key];
    // also remove from keys array
}
```

---

## 7. Private Data is Not Private

`private` prevents *other contracts* from calling the variable. It does **not** hide the value from external observers. All storage slots are readable via `eth_getStorageAt`.

```solidity
contract Lottery {
    bytes32 private winnerHash;   // ❌ Anyone can read this off-chain
}
```

**Do not store secrets in contract storage.** Use commit-reveal schemes:
1. Player submits `keccak256(secret, nonce)` (the commitment).
2. After a deadline, player reveals `secret` and `nonce`; contract verifies.

---

## 8. Dirty High-Order Bits (Low-Level calldata)

Types occupying fewer than 32 bytes may have non-zero high-order bits in raw `msg.data`. Two calls with different calldata can appear identical to the function but produce different `keccak256(msg.data)` hashes.

**Avoid hashing `msg.data` directly** as a replay-protection nonce.

---

## 9. Authorised Proxy Contracts

A proxy that calls arbitrary addresses with user-supplied data effectively lends its identity (and any stored Ether or permissions) to the caller. The proxy's permissions will be used in the sub-call.

### Safe Permissionless Proxy

```solidity
contract PermissionlessProxy {
    function callOther(address addr, bytes memory payload)
        public returns (bool, bytes memory)
    {
        return addr.call(payload);   // proxy itself has zero special permissions
    }
}
```

---

## 10. Call Stack Depth

EVM call stacks are limited to **1024 frames**. An attacker can pre-fill the stack with 1023 internal calls and then call the target — the next `.call()` or `.send()` in the target will silently fail (pre-Tangerine Whistle) or run out of gas (post-Tangerine Whistle: `63/64` gas forwarding rule).

**Always check the return value of `.send()` and `.call()`.**

---

## Summary: Security Checklist

| # | Rule |
|---|------|
| 1 | Follow **Checks-Effects-Interactions** in every function |
| 2 | Never use `tx.origin` for authentication |
| 3 | Never rely on `address(this).balance` being a specific value |
| 4 | Use `.call` with CEI; check `bool success`; avoid `.send()` and `.transfer()` in complex contracts |
| 5 | Bound all loops — prefer withdrawal pattern over push-to-all |
| 6 | Do not store secrets in contract storage |
| 7 | Never use `unchecked` on user-supplied values |
| 8 | Use iterable mapping helpers if you need to `delete` structs containing mappings |
| 9 | Add a reentrancy guard (`nonReentrant` modifier) as defence-in-depth |
| 10 | Seek peer review and a formal audit before mainnet deployment |
| 11 | Heed all compiler warnings; enable `pragma abicoder v2` |
| 12 | Cap stored Ether/token amounts; minimise blast radius of any bug |

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/solidity-fundamentals]] | Language reference: CEI syntax, error handling, modifiers |
| [[concepts/ethereum-evm]] | EVM execution model, gas mechanics, call stack depth |
| [[sources/solidity-docs-0.8.36]] | Primary source: official security-considerations section |
