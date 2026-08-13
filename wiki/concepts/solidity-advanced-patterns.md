---
type: concept
title: "Solidity Advanced Patterns"
domain: blockchain
complexity: high
tags: [solidity, smart-contracts, delegatecall, inheritance, libraries, using-for, imports, patterns, code-organisation, proxy]
created: 2026-08-12
updated: 2026-08-12
status: established
related:
  - "[[concepts/solidity-fundamentals]]"
  - "[[concepts/solidity-security]]"
  - "[[concepts/ethereum-evm]]"
  - "[[sources/solidity-advanced-patterns-sources]]"
---

# Solidity Advanced Patterns

Code organisation, reuse, and inter-contract communication. These patterns are fundamental to building maintainable, modular smart contract systems and underpin nearly every production-grade Solidity codebase.

See [[concepts/solidity-fundamentals]] for the core language reference. See [[concepts/solidity-security]] for security implications of each pattern.

---

## 1. Calling Other Contracts

The recommended way to invoke another deployed contract is via a **typed reference** — the compiler checks the function signature at compile time, giving early error detection and no runtime ABI ambiguity.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract Callee {
    uint256 public x;
    uint256 public value;

    function setX(uint256 _x) public returns (uint256) {
        x = _x;
        return x;
    }

    function setXandSendEther(uint256 _x)
        public payable returns (uint256, uint256)
    {
        x = _x;
        value = msg.value;
        return (x, value);
    }
}

contract Caller {
    // ✅ Method 1 — pass contract type as parameter (preferred)
    function setX(Callee _callee, uint256 _x) public {
        uint256 x = _callee.setX(_x);
    }

    // ✅ Method 2 — cast an address to the contract type at call site
    function setXFromAddress(address _addr, uint256 _x) public {
        Callee callee = Callee(_addr);
        callee.setX(_x);
    }

    // ✅ Method 3 — forward Ether with {value: ...}; callee must be payable
    function setXandSendEther(Callee _callee, uint256 _x) public payable {
        (uint256 x, uint256 val) =
            _callee.setXandSendEther{value: msg.value}(_x);
    }
}
```

**When to use the low-level `.call`:** Only when the target's ABI is unknown at compile time (e.g., generic proxy forwarders, factory patterns). Always follow Checks-Effects-Interactions and verify the `bool success` return value. See [[concepts/solidity-security]] §1 for the reentrancy risk.

---

## 2. `delegatecall`

`delegatecall` is a low-level opcode that runs the **target contract's code** in the **caller's storage context**. This is how Solidity's `library` mechanism works internally, and it is the foundation of every upgradeable proxy pattern.

### Comparison: `call` vs `delegatecall`

| Property | Regular `.call` | `.delegatecall` |
|----------|----------------|-----------------|
| Code executed | Target's | Target's |
| Storage modified | **Target's** | **Caller's** |
| `msg.sender` in target | Caller contract address | Caller contract address |
| `msg.value` in target | Provided value | **Caller's original value** |

### Critical Constraint: Storage Layout Must Match

The target contract accesses the caller's storage by **slot index**, not by variable name. If the two contracts declare state variables in a different order, the target's code will corrupt the wrong storage slots.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

// ── Deploy B first ──────────────────────────────────────────────────────────
contract B {
    // Storage layout MUST match A exactly (same slot order)
    uint256 public num;      // slot 0
    address public sender;   // slot 1
    uint256 public value;    // slot 2

    function setVars(uint256 _num) public payable {
        num    = _num;
        sender = msg.sender;
        value  = msg.value;
    }
}

// ── Contract A delegates to B ────────────────────────────────────────────────
contract A {
    uint256 public num;      // slot 0
    address public sender;   // slot 1
    uint256 public value;    // slot 2

    event DelegateResponse(bool success, bytes data);
    event CallResponse(bool success, bytes data);

    // delegatecall: A's storage is written; B's storage is untouched
    function setVarsDelegateCall(address _contract, uint256 _num)
        public payable
    {
        (bool success, bytes memory data) = _contract.delegatecall(
            abi.encodeWithSignature("setVars(uint256)", _num)
        );
        emit DelegateResponse(success, data);
    }

    // regular call: B's storage is written; A's storage is untouched
    function setVarsCall(address _contract, uint256 _num) public payable {
        (bool success, bytes memory data) = _contract.call{value: msg.value}(
            abi.encodeWithSignature("setVars(uint256)", _num)
        );
        emit CallResponse(success, data);
    }
}
```

### Use Cases

| Use case | How `delegatecall` helps |
|----------|------------------------|
| **Upgradeable proxy** | Proxy stores state (slot layout); implementation holds logic. Upgrading = swapping the implementation address. |
| **Solidity libraries** | Public/external library functions are called via DELEGATECALL automatically. |
| **Diamond pattern (EIP-2535)** | Multiple implementation ("facet") contracts share a single storage layout via `delegatecall`. |

**Security warning:** Passing a user-controlled address to `delegatecall` gives that address full write access to your storage. Never `delegatecall` to an untrusted or arbitrary address. See [[concepts/solidity-security]] §9.

---

## 3. Inheritance

Solidity supports multiple inheritance with polymorphism. When a contract inherits from others, **only one contract is deployed** — the compiler merges all base contract code. All internal calls between base and derived contracts use `JUMP`, not message calls.

### `virtual` and `override`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.23;

contract Base {
    // virtual: permits derived contracts to override this function
    function greet() public virtual returns (string memory) {
        return "Hello from Base";
    }
}

contract Middle is Base {
    // override: replaces Base.greet; virtual: allows further overrides
    function greet() public virtual override returns (string memory) {
        return "Hello from Middle";
    }
}

contract Leaf is Middle {
    function greet() public override returns (string memory) {
        // super traverses the full C3 chain: Leaf → Middle → Base
        return string.concat(super.greet(), " and Leaf");
    }
}
```

### Visibility and Mutability Rules

| Change | Permitted? | Reason |
|--------|-----------|--------|
| `external` → `public` | ✅ | Widens access |
| `public` → `external` | ❌ | Narrows access |
| `nonpayable` → `view` | ✅ | Stricter (view ⊂ nonpayable) |
| `nonpayable` → `pure` | ✅ | Stricter |
| `payable` → anything | ❌ | Cannot remove Ether acceptance |
| Different return type | ❌ | ABI incompatibility |

### Multiple Inheritance and C3 Linearisation

List bases **most base-like first, most derived last** in the `is` clause:

```solidity
contract A {
    function f() public virtual returns (string memory) { return "A"; }
}
contract B is A {
    function f() public virtual override returns (string memory) { return "B"; }
}

// Correct: A is more base-like, B is more derived
contract C is A, B {
    // Must name all contracts that define f() after `override`
    function f() public override(A, B) returns (string memory) {
        return super.f();   // calls B.f() first, then A.f() per C3 chain
    }
}
```

**State variable shadowing** (declaring a variable with the same name as a visible base variable) is a **compiler error** in Solidity. Unlike functions, variables cannot be overridden.

### Constructor Inheritance

Provide base constructor arguments in one of two places — not both:

```solidity
contract Owned {
    address public owner;
    constructor(address _owner) { owner = _owner; }
}

// Option A: in the inheritance list — use for constant arguments
contract ContractA is Owned(0xABCD...) {}

// Option B: in the derived constructor — use when the argument is dynamic
contract ContractB is Owned {
    constructor(address _owner) Owned(_owner) {}
}
```

### Abstract Contracts and Interfaces

```solidity
// Abstract: has at least one function without an implementation
abstract contract Shape {
    function area() public virtual returns (uint256);  // no body
    function perimeter() public virtual returns (uint256);
}

// Interface: all functions are implicit external; no state variables,
// no constructors, no non-abstract functions
interface IERC20 {
    event Transfer(address indexed from, address indexed to, uint256 value);
    function totalSupply() external view returns (uint256);
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

**Additional rules:**
- Private functions cannot be `virtual`.
- Modifiers can be `virtual` and `override` using the same rules as functions.
- A derived contract that does not implement all abstract functions must itself be marked `abstract`.

---

## 4. Libraries

A library is a stateless, deployable code module. Its functions execute in the **calling contract's context** (via DELEGATECALL), but the library has no context of its own.

### Restrictions

| What a library cannot do | Why |
|--------------------------|-----|
| Hold state variables | Libraries have no persistent storage of their own |
| Inherit or be inherited | No inheritance hierarchy |
| Receive Ether | No fallback or receive function |
| Call `selfdestruct` | Would destroy the shared deployment |

### Internal vs External Functions

| Function visibility | Calling convention | Deployment required? |
|--------------------|-------------------|---------------------|
| `internal` / `private` | `JUMP` (inlined into caller at compile time) | No |
| `public` / `external` | `DELEGATECALL` (at runtime) | Yes — address must be linked |

Use `internal` functions for pure computation and small utilities (free at deployment). Use `public`/`external` when the library is large and many contracts share it.

### Set Library — Storage Pointer Pattern

The first parameter may be a `storage` pointer, giving the library direct write access to the caller's state:

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

struct Data {
    mapping(uint => bool) flags;
}

library Set {
    // `self` is a storage pointer — operates directly on the caller's storage
    function insert(Data storage self, uint value) public returns (bool) {
        if (self.flags[value]) return false;
        self.flags[value] = true;
        return true;
    }

    function remove(Data storage self, uint value) public returns (bool) {
        if (!self.flags[value]) return false;
        self.flags[value] = false;
        return true;
    }

    function contains(Data storage self, uint value) public view returns (bool) {
        return self.flags[value];
    }
}

contract C {
    Data knownValues;

    function register(uint value) public {
        require(Set.insert(knownValues, value));   // explicit library call syntax
    }
}
```

### BigInt Library — Internal Functions, Memory Types

Internal library functions are inlined — no DELEGATECALL overhead, no separate deployment:

```solidity
pragma solidity ^0.8.0;

struct bigint { uint[] limbs; }

library BigInt {
    function fromUint(uint x) internal pure returns (bigint memory r) {
        r.limbs = new uint[](1);
        r.limbs[0] = x;
    }

    function add(bigint memory a, bigint memory b)
        internal pure returns (bigint memory r)
    {
        r.limbs = new uint[](max(a.limbs.length, b.limbs.length));
        uint carry = 0;
        for (uint i = 0; i < r.limbs.length; ++i) {
            uint la = limb(a, i);
            uint lb = limb(b, i);
            unchecked {
                r.limbs[i] = la + lb + carry;
                carry = (la + lb < la ||
                    (la + lb == type(uint).max && carry > 0)) ? 1 : 0;
            }
        }
    }

    function limb(bigint memory a, uint i) internal pure returns (uint) {
        return i < a.limbs.length ? a.limbs[i] : 0;
    }

    function max(uint a, uint b) private pure returns (uint) {
        return a > b ? a : b;
    }
}

contract C {
    using BigInt for bigint;   // enables member-function syntax

    function f() public pure {
        bigint memory x = BigInt.fromUint(7);
        bigint memory y = BigInt.fromUint(type(uint).max);
        bigint memory z = x.add(y);   // using-for syntax
        assert(z.limb(1) > 0);
    }
}
```

**Call protection:** The compiler embeds an `ADDRESS` opcode check in every non-view/non-pure library function. If the function is called via a regular `CALL` (rather than `DELEGATECALL`), it reverts. This prevents misuse of libraries as ordinary contracts.

---

## 5. `using for` Directive

Attaches functions as **member methods** to a type, enabling object-like call syntax (`value.method()`). Works with library names or explicit lists of free functions.

### Syntax Reference

```solidity
// Inside a contract
using LibraryName for TypeName;   // all non-private library functions
using LibraryName for *;          // attach to all types in this contract

// At file level (explicit function list)
using {insert, remove, contains} for Data;

// At file level, global (propagates to all importing files)
using {add as +, div as /} for UFixed16x2 global;
```

### Struct + Free Functions Pattern

The first parameter of each function is treated as `self` and must be implicitly convertible to the target type:

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.23;

struct Data {
    mapping(uint => bool) flags;
}

using {insert, contains} for Data;

function insert(Data storage self, uint value) returns (bool) {
    if (self.flags[value]) return false;
    self.flags[value] = true;
    return true;
}

function contains(Data storage self, uint value) view returns (bool) {
    return self.flags[value];
}

contract C {
    Data knownValues;

    function register(uint value) public {
        require(knownValues.insert(value));   // member-style call
    }
}
```

### Custom Operators for User-Defined Value Types

Operator-defining functions must be `pure` free functions and declared `global`:

```solidity
type UFixed16x2 is uint16;
using {add as +, div as /} for UFixed16x2 global;

uint32 constant SCALE = 100;

function add(UFixed16x2 a, UFixed16x2 b) pure returns (UFixed16x2) {
    return UFixed16x2.wrap(UFixed16x2.unwrap(a) + UFixed16x2.unwrap(b));
}

function div(UFixed16x2 a, UFixed16x2 b) pure returns (UFixed16x2) {
    uint32 result = uint32(UFixed16x2.unwrap(a)) * SCALE
                  / uint32(UFixed16x2.unwrap(b));
    require(result <= type(uint16).max, "Divide overflow");
    return UFixed16x2.wrap(uint16(result));
}

contract Math {
    function avg(UFixed16x2 a, UFixed16x2 b) public pure returns (UFixed16x2) {
        return (a + b) / UFixed16x2.wrap(200);   // uses the defined operators
    }
}
```

**Supported operator categories:** bitwise (`&`, `|`, `^`, `~`), arithmetic (`+`, `-`, `*`, `/`, `%`), comparison (`==`, `!=`, `<`, `<=`, `>`, `>=`). Unary and binary `-` require separate definitions.

---

## 6. Imports and Source Organisation

### Import Syntax

| Form | Syntax | Use |
|------|--------|-----|
| Simple (avoid) | `import "filename";` | All globals — risks namespace pollution |
| Namespace | `import * as Name from "filename";` | Access via `Name.Symbol` |
| Alias | `import "filename" as Name;` | Equivalent to namespace form |
| Selective | `import {Foo, Bar as Baz} from "filename";` | Only named symbols; rename with `as` |

### Path Types

| Path | Example | Resolution |
|------|---------|-----------|
| Relative | `"./Token.sol"` | From the current file's directory |
| Parent | `"../interfaces/IERC20.sol"` | One directory up |
| Package | `"@openzeppelin/contracts/token/ERC20/ERC20.sol"` | Via remapping or npm |
| HTTP/IPFS | `"https://github.com/..."` | Remix IDE only |

Solidity resolves imports against an internal virtual filesystem (VFS) — it does not directly access the host filesystem. The compiler or IDE provides a callback to populate the VFS from the actual source files.

### Importing from GitHub in Remix

Always specify a **release tag** — importing from a branch (e.g., `main`) means the dependency can change silently between sessions:

```solidity
// ✅ Pinned to a release — deterministic and auditable
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.0.2/contracts/token/ERC20/ERC20.sol";

// ❌ Avoid — pulls main branch; may change without warning
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";
```

Files imported via URL are placed in the `.deps` folder in Remix's File Explorer. Relative imports from `.deps` files work without traversal back to `github/`.

### Selective Import Example

```solidity
// Import only what you need; rename to avoid collisions
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {Ownable as OwnableBase} from "@openzeppelin/contracts/access/Ownable.sol";

contract MyToken is ERC20, OwnableBase {
    constructor() ERC20("MyToken", "MTK") OwnableBase(msg.sender) {}
}
```

---

## 7. Modular Contracts Pattern

Separate business-logic invariants into a library; use `using for` to give the contract shell clean call syntax. Auditors only need to verify the library — every call path shares one implementation.

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.5.0 <0.9.0;

// ── Module: transfer invariant ────────────────────────────────────────────────
library Balances {
    function move(
        mapping(address => uint256) storage balances,
        address from,
        address to,
        uint amount
    ) internal {
        require(balances[from] >= amount, "Insufficient balance");
        require(balances[to] + amount >= balances[to], "Receiver overflow");
        balances[from] -= amount;
        balances[to]   += amount;
    }
}

// ── Contract: thin shell, delegates logic to library ─────────────────────────
contract Token {
    mapping(address => uint256) balances;
    using Balances for *;   // attaches `move` to the mapping type

    mapping(address => mapping(address => uint256)) allowed;

    event Transfer(address from, address to, uint amount);
    event Approval(address owner, address spender, uint amount);

    function transfer(address to, uint amount) external returns (bool) {
        balances.move(msg.sender, to, amount);   // library call via using-for
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    function transferFrom(address from, address to, uint amount)
        external returns (bool)
    {
        require(allowed[from][msg.sender] >= amount);
        allowed[from][msg.sender] -= amount;
        balances.move(from, to, amount);         // same invariant — no duplication
        emit Transfer(from, to, amount);
        return true;
    }

    function approve(address spender, uint tokens) external returns (bool) {
        require(allowed[msg.sender][spender] == 0, "Reset allowance to 0 first");
        allowed[msg.sender][spender] = tokens;
        emit Approval(msg.sender, spender, tokens);
        return true;
    }

    function balanceOf(address owner) external view returns (uint) {
        return balances[owner];
    }
}
```

**Why this matters:**
- `Balances.move` is the single source of truth for the transfer invariant. A security audit reviews one function, not N call paths.
- Adding `transferFrom`, `transferBatch`, or any future transfer path cannot introduce a divergent invariant — they all delegate to the same library.
- This is structurally identical to how OpenZeppelin's ERC-20 and ERC-721 implementations are organised.

---

## Summary: Pattern Selection Guide

| Goal | Pattern |
|------|---------|
| Call a contract whose ABI is known | Typed reference: `Callee(addr).method(args)` |
| Run code in your own storage | `delegatecall` (ensure layout matches!) |
| Share pure computation across contracts | Library with `internal` functions |
| Share stateful logic, one deployment | Library with `public` functions + DELEGATECALL |
| Attach library/free functions as methods | `using for` directive |
| Reuse a base implementation | Inheritance + `virtual`/`override` |
| Separate logic from state (upgradeable) | Proxy pattern via `delegatecall` |
| Separate invariants from call paths | Modular: library + `using for` |

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/solidity-fundamentals]] | Core language reference: types, error handling, modifiers, common patterns |
| [[concepts/solidity-security]] | Security implications: `delegatecall` proxy risk (§9), reentrancy in library calls (§1) |
| [[concepts/ethereum-evm]] | EVM execution model: DELEGATECALL opcode, JUMP, storage slot layout |
| [[sources/solidity-advanced-patterns-sources]] | Primary sources for this page (8 URLs) |
