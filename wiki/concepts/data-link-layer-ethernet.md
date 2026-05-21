---
type: concept
title: "Data Link Layer & Ethernet"
domain: computer-networks
complexity: high
status: established
created: 2026-05-22
updated: 2026-05-22
address: c-000034
tags: [data-link-layer, ethernet, csma-cd, mac-address, switching, stp, frames, INF1006]
---

# Data Link Layer & Ethernet

The data link layer (Layer 2) is responsible for **node-to-node (hop-to-hop) delivery** of data across a single link. In a LAN, it includes a MAC sublayer to coordinate shared medium access. Ethernet — using CSMA/CD — won the LAN standards war and is now the universal wired LAN technology.

---

## Data Link Layer Services

| Service | Description |
|---|---|
| **Framing** | Encapsulates network-layer packets into frames with header and trailer |
| **Addressing** | Uses MAC addresses to identify source and destination nodes |
| **Error control** | Detects (and sometimes corrects) transmission errors |
| **Flow control** | Prevents a fast sender from overwhelming a slow receiver (within a link) |
| **Medium Access Control** | Coordinates access to shared transmission medium (MAC sublayer) |

---

## MAC Sublayer

Traditional LANs share a single transmission medium among many nodes. The **MAC (Medium Access Control) sublayer** arbitrates access to prevent collisions.

| IEEE Standard | Technology | MAC Protocol |
|---|---|---|
| 802.3 | Ethernet | CSMA/CD |
| 802.5 | Token Ring | Token passing |
| 802.11 | Wi-Fi | CSMA/CA |

---

## CSMA/CD — Carrier Sense Multiple Access with Collision Detection

Ethernet's MAC protocol. Full name: **1-persistent CSMA/CD with Binary Exponential Backoff (BEB)**.

### How It Works

1. **Carrier Sense (CS):** Before transmitting, a station listens to the medium. If busy, it waits until idle (1-persistent: retries immediately once idle).
2. **Multiple Access (MA):** All stations share the same medium.
3. **Collision Detection (CD):** While transmitting, a station monitors the medium. If it detects a collision (signal distortion), it stops and sends a jam signal.
4. **Backoff (BEB):** After a collision, the station waits a random backoff period before retrying.

### Minimum Frame Length Requirement

A collision can only be detected by the transmitting station if it is **still transmitting** when the collision signal propagates back to it.

> **Condition:** t_frame ≥ 2 × t_prop

This is why Ethernet mandates a **minimum frame length of 64 bytes**.

### Binary Exponential Backoff (BEB)

After the k-th collision:
- Each station randomly picks R in the range [0, 2^k − 1].
- The station waits R × t_prop before retransmitting.
- After 10 collisions, the range is frozen at [0, 1023].
- After 16 collisions, the transmission is aborted and an error is reported.

### Switched LAN — No CSMA/CD Needed

Modern Ethernet uses **switches**: each host has a dedicated full-duplex link to the switch. There is no shared medium, no collisions, and therefore no need for CSMA/CD.

---

## MAC Addresses

| Property | Detail |
|---|---|
| Length | **48 bits** (6 bytes) |
| Format | `00:60:2F:3A:07:BC` or `00-60-2F-3A-07-BC` |
| OUI (first 24 bits) | Assigned by IEEE; identifies the manufacturer |
| NIC-specific (last 24 bits) | Assigned by the manufacturer |
| Also called | Physical address, hardware address — "burnt" into the NIC |

**Special address:** `FF:FF:FF:FF:FF:FF` = Ethernet broadcast (sent to all nodes on the LAN).

---

## Ethernet Frame Structure

| Field | Size | Description |
|---|---|---|
| **Preamble** | 7 bytes | Alternating 1s and 0s — synchronises receiver clock |
| **SFD (Start Frame Delimiter)** | 1 byte | Marks the end of preamble and start of frame |
| **Destination Address (DA)** | 6 bytes | Recipient MAC address |
| **Source Address (SA)** | 6 bytes | Sender MAC address |
| **Type / Length** | 2 bytes | Higher-layer protocol (e.g., `0x0800` = IPv4, `0x0806` = ARP) |
| **Data (Payload)** | 46–1500 bytes | Network-layer packet |
| **FCS (Frame Check Sequence)** | 4 bytes | CRC error detection over DA+SA+Type+Data |

- **Minimum frame size:** 64 bytes (required for CSMA/CD collision detection)
- **Maximum frame size:** 1518 bytes (defines the Ethernet MTU of 1500 bytes payload)

---

## Switch Operation

### Address Self-Learning

When a frame arrives at a switch port:
1. The switch records the **source MAC address** and the **incoming port** in its MAC address table (also called the forwarding table or CAM table).
2. Entries expire after a timeout if not refreshed.

The switch builds its table organically — no configuration is required.

### Frame Forwarding

| Scenario | Action |
|---|---|
| **Known unicast destination** | Forward only to the port where that MAC was learnt |
| **Unknown destination** | **Flood** out all ports except the incoming port |
| **Broadcast (FF:FF:FF:FF:FF:FF)** | Flood out all ports except the incoming port |

### Spanning Tree Protocol (STP)

Redundant switch paths prevent single points of failure but create **loops**, which cause broadcast storms. STP prevents loops by placing redundant ports into a **blocking state**.

**STP Port Roles:**

| Role | Description |
|---|---|
| **Root Bridge** | Switch with the lowest Bridge ID (priority + MAC). One per network. |
| **Root Port** | Each non-root switch's port with the lowest-cost path to the root bridge |
| **Designated Port** | For each network segment, the port with the lowest cost to the root |
| **Blocked Port** | All other ports — receive BPDUs but do not forward frames |

STP ensures there is exactly one active forwarding path between any two switches, eliminating loops whilst preserving redundancy.

---

## Key Connections

- [[concepts/tcp-ip-network-model]] — Layer 2 sits between the physical layer and the network layer; frames carry IP packets
- [[concepts/ip-addressing]] — IP packets are encapsulated in Ethernet frames; ARP resolves IP → MAC
- [[concepts/network-layer-protocols]] — ARP operates at the boundary of Layer 2 and Layer 3
- [[concepts/wireless-and-iot]] — Wi-Fi uses CSMA/CA instead of CSMA/CD; shares the MAC sublayer concept
