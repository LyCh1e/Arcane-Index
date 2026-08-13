---
type: example
title: "Hedera Lecture 4 — Voting Contract (Poll V1 and V2)"
domain: blockchain
tags: [solidity, smart-contracts, voting, access-control, enum, mapping, struct, hedera, course-example]
created: 2026-08-13
updated: 2026-08-13
status: established
related:
  - "[[concepts/solidity-fundamentals]]"
  - "[[concepts/solidity-advanced-patterns]]"
  - "[[concepts/hedera-network]]"
  - "[[sources/hedera-lecture-4-hapi-tokens]]"
---

# Hedera Lecture 4 — Voting Contract (Poll V1 and V2)

A worked example from the Hedera Developer Course (Hendrik Ebbers, OpenElements / Swirlds Labs). The contract is built iteratively in two versions — V1 demonstrates the core data model and algorithm; V2 adds authorisation to make the poll production-worthy.

---

## Poll V1 — Basic Voting

### Design

| Component | Implementation |
|-----------|---------------|
| Proposal data | `struct Proposal { bytes32 name; uint count; }` |
| All proposals | `Proposal[] public proposals` — publicly readable array |
| Setup | Constructor takes `bytes32[]` of proposal names; iterates to populate the array |
| Vote | `vote(uint proposal)` — increments `proposals[proposal].count` |
| Result | `winner()` — iterates to find the proposal with the highest count |

`bytes32` is used for proposal names because it is cheaper than `string` for short fixed-size labels (no dynamic memory allocation).

### Full Contract

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.7.0 <0.9.0;

contract Poll {

    // ── Data model ────────────────────────────────────────────────────────────
    struct Proposal {
        bytes32 name;   // short label — cheaper than string for fixed-size data
        uint count;     // accumulated vote count
    }

    Proposal[] public proposals;   // publicly readable; index = proposal ID

    // ── Constructor ───────────────────────────────────────────────────────────
    constructor(bytes32[] memory proposalNames) {
        for (uint i = 0; i < proposalNames.length; i++) {
            Proposal memory proposal = Proposal({
                name: proposalNames[i],
                count: 0
            });
            proposals.push(proposal);
        }
    }

    // ── Vote ──────────────────────────────────────────────────────────────────
    function vote(uint proposal) public {
        proposals[proposal].count++;
    }

    // ── Read result ───────────────────────────────────────────────────────────
    function winner() public view returns (bytes32 result) {
        result = "";
        uint maxCount = 0;
        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].count > maxCount) {
                maxCount = proposals[i].count;
                result = proposals[i].name;
            }
        }
    }
}
```

### Problems with V1

| Problem | Impact |
|---------|--------|
| Anyone can vote any number of times | Results are meaningless — no Sybil resistance |
| No access control whatsoever | No admin; cannot restrict who votes |
| Anyone can vote on behalf of any address | No identity binding |

V2 addresses all three.

---

## Poll V2 — Access-Controlled Voting

### Design Additions

| Addition | Implementation | Purpose |
|----------|---------------|---------|
| Admin | `address public admin = msg.sender` (in constructor) | Single trusted party who authorises voters |
| Voter state | `enum VoterState { NotAuthorized, Authorized, Voted }` | Three-state finite state machine per voter |
| Voter tracking | `mapping(address => VoterState) public voters` | On-chain registry of all voter states |
| Vote guard | `require(voters[msg.sender] == Authorized, ...)` then set to `Voted` | One vote per address; requires pre-authorisation |
| Authorise function | `authorize(address voter)` — admin only, `NotAuthorized` only | Admin can approve eligible voters |

### Full Contract

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.7.0 <0.9.0;

contract Poll {

    // ── Access control ────────────────────────────────────────────────────────
    address public admin;

    enum VoterState { NotAuthorized, Authorized, Voted }
    mapping(address => VoterState) public voters;

    // ── Data model ────────────────────────────────────────────────────────────
    struct Proposal {
        bytes32 name;
        uint count;
    }

    Proposal[] public proposals;

    // ── Constructor ───────────────────────────────────────────────────────────
    constructor(bytes32[] memory proposalNames) {
        admin = msg.sender;   // deployer becomes admin

        for (uint i = 0; i < proposalNames.length; i++) {
            proposals.push(Proposal({
                name: proposalNames[i],
                count: 0
            }));
        }
    }

    // ── Authorise a voter (admin only) ────────────────────────────────────────
    function authorize(address voter) public {
        require(
            msg.sender == admin,
            "Only admin can authorize"
        );
        require(
            voters[voter] == VoterState.NotAuthorized,
            "Already authorized or already voted"
        );

        voters[voter] = VoterState.Authorized;
    }

    // ── Vote (authorized, not yet voted) ──────────────────────────────────────
    function vote(uint proposal) public {
        require(
            voters[msg.sender] == VoterState.Authorized,
            "Not authorized to vote"
        );

        voters[msg.sender] = VoterState.Voted;    // ✅ Effect before interaction
        proposals[proposal].count++;
    }

    // ── Read result ───────────────────────────────────────────────────────────
    function winner() public view returns (bytes32 result) {
        result = "";
        uint maxCount = 0;
        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].count > maxCount) {
                maxCount = proposals[i].count;
                result = proposals[i].name;
            }
        }
    }
}
```

### State Machine Diagram

```
                       authorize(voter)
NotAuthorized ──────────────────────────► Authorized
                    (admin only)               │
                                               │ vote(proposal)
                                               ▼
                                            Voted
```

Each voter's `VoterState` only ever moves forward — there is no path back to `NotAuthorized` or `Authorized` once `Voted`.

---

## Patterns Demonstrated

| Pattern | Where | Notes |
|---------|-------|-------|
| `struct` with array | `Proposal[]` | Canonical struct-in-array pattern; index used as ID |
| Enum as voter FSM | `VoterState` | Three-state machine; default value is `NotAuthorized` (0) — the mapping zero-value |
| `mapping` for state | `mapping(address => VoterState)` | O(1) lookup per voter; default `VoterState.NotAuthorized` for unseen addresses |
| Admin pattern | `admin = msg.sender` in constructor | Single-owner access control; no modifier here, but could use `onlyAdmin` modifier |
| `require` for access control | In `authorize` and `vote` | Two guards: caller identity + state check |
| Checks-Effects-Interactions | In `vote` | State updated (`VoterState.Voted`) **before** any external interaction |
| `bytes32` for short strings | `Proposal.name` | More gas-efficient than `string` for fixed-size labels; convert with `abi.encodePacked("Label")` off-chain |

---

## Known Limitations and Possible Improvements

| Limitation | Improvement |
|------------|------------|
| `winner()` loops over all proposals — O(n) gas | Track `winnerIndex` in storage, update on each vote (O(1) query) |
| Admin cannot be changed | Add `transferAdmin(address newAdmin)` with two-step ownership transfer |
| No delegation (proxy voting) | Add a `delegate(address to)` function that transfers voting rights |
| Admin can vote too | Separate admin role from voter eligibility; optionally restrict admin from voting |
| `bytes32` names awkward to pass | Use `string[]` names with `keccak256` comparison in `winner()` |
| No event emission | Emit `VoteCast(address voter, uint proposal)` and `VoterAuthorized(address voter)` for off-chain indexing |

---

## Deploying on Hedera (HAPI Java SDK)

```java
// 1. Compile Poll.sol → bytecodeHex (via solc or web3j)
ContractCreateFlow flow = new ContractCreateFlow()
    .setBytecode(bytecodeHex)
    .setGas(1_000_000);

ContractId pollId = flow.execute(client)
                        .getReceipt(client)
                        .contractId;

// 2. Call authorize (admin account as operator)
new ContractExecuteTransaction()
    .setContractId(pollId)
    .setGas(100_000)
    .setFunction("authorize",
        new ContractFunctionParameters().addAddress(voterAddress))
    .execute(client);

// 3. Call vote (voter account as operator)
new ContractExecuteTransaction()
    .setContractId(pollId)
    .setGas(100_000)
    .setFunction("vote",
        new ContractFunctionParameters().addUint256(proposalIndex))
    .execute(client);

// 4. Query winner
ContractFunctionResult result = new ContractCallQuery()
    .setContractId(pollId)
    .setGas(50_000)
    .setFunction("winner")
    .execute(client);
String winnerName = result.getString(0);
```
