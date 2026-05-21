---
type: concept
title: "Network Layer Protocols (OSPF, BGP, ICMP, ARP)"
domain: computer-networks
complexity: high
status: established
created: 2026-05-22
updated: 2026-05-22
address: c-000036
tags: [ospf, bgp, icmp, arp, routing-protocols, control-plane, igp, egp, INF1006]
---

# Network Layer Protocols (OSPF, BGP, ICMP, ARP)

The network layer has two planes: the **data plane** (forwarding — moving packets) and the **control plane** (routing — computing paths). This page covers the main control-plane protocols: OSPF (interior routing), BGP (inter-domain routing), ICMP (error reporting), and ARP (address resolution).

---

## Routing Protocol Taxonomy

```
Routing Protocols
├── IGP — Interior Gateway Protocol (within one Autonomous System)
│   ├── Distance Vector → RIP
│   └── Link State    → OSPF
└── EGP — Exterior Gateway Protocol (between Autonomous Systems)
    └── Path Vector   → BGP
```

- An **Autonomous System (AS)** is a network or group of networks under a single administrative authority (e.g., an ISP or a company).
- Different ASes may run different IGPs; all ASes must run the same EGP (BGP).

---

## OSPF — Open Shortest Path First

OSPF is a **link-state** IGP. Every router builds a complete map of the network topology, then runs Dijkstra's algorithm independently to compute shortest paths.

### Three Phases of OSPF Operation

| Phase | Description |
|---|---|
| **1. Neighbour Discovery** | Routers send Hello messages on each interface; adjacent routers become neighbours |
| **2. Topology Exchange** | Each router floods **Link State Advertisements (LSAs)** describing its directly connected links and their costs; all routers build an identical **Link State Database (LSDB)** |
| **3. Route Calculation** | Each router runs **Dijkstra's algorithm** on its LSDB to compute the shortest path tree from itself to all other routers |

### LSA Freshness Rules

When a router receives an LSA, it determines whether it is newer by checking (in order):

1. **Sequence number** — higher = more recent → accept.
2. **Age field** — if age difference > MaxAgeDiff (15 minutes) → accept the newer LSA.
3. **Checksum** — different checksums indicate different content.

### LSA Lifecycle

- LSAs are **refreshed every 30 minutes** (periodic refresh).
- The age field is incremented as an LSA propagates and is stored.
- LSAs reaching **MaxAge (1 hour)** are purged from the LSDB.
- Routers perform periodic **database description exchanges** to synchronise LSDBs.

> **Connection to existing wiki:** OSPF uses Dijkstra's shortest-path algorithm — the same algorithm covered in [[concepts/graph-algorithms]] for weighted directed graphs.

---

## BGP — Border Gateway Protocol

BGP is the **path-vector** EGP used to exchange routing information between Autonomous Systems on the Internet.

- Each routing table entry contains: destination network, next-hop router, and the **AS path** (list of ASes to reach the destination).
- Routers advertise reachability to their neighbours; each receiving router applies **policy filters** before accepting and re-advertising routes.
- BGP enables network administrators to enforce routing policies (e.g., traffic engineering, commercial agreements).

**Example BGP routing table:**

| Network | Next Router | AS Path |
|---|---|---|
| N01 | R01 | AS14, AS23, AS67 |
| N02 | R05 | AS22, AS67, AS05, AS89 |
| N03 | R06 | AS67, AS89, AS09, AS34 |

---

## ICMP — Internet Control Message Protocol

ICMP provides **error reporting and diagnostic** functions for IP. Despite travelling inside IP packets, it is considered part of the network layer.

### ICMP Message Format

```
+--------+--------+----------------+
|  Type  |  Code  |    Checksum    |
+--------+--------+----------------+
|           Rest of header         |
+----------------------------------+
|             Data                 |
+----------------------------------+
```

### Key ICMP Messages

| Message | Type | Code | Use |
|---|---|---|---|
| Echo Request (ping) | 8 | 0 | Query: is host reachable? |
| Echo Reply | 0 | 0 | Response to ping |
| Time Exceeded | 11 | 0 | TTL expired in transit (used by traceroute) |
| Destination Unreachable | 3 | various | Packet could not be delivered |
| Fragmentation Needed | 3 | 4 | Packet too large and DF bit set |

### Traceroute

Traceroute sends a sequence of ICMP Echo Requests with TTL = 1, 2, 3, … . Each router that decrements TTL to zero sends back an ICMP **Time Exceeded** message, revealing its identity and round-trip time. When the destination is reached, it sends an Echo Reply. This maps the full path and measures per-hop latency.

---

## ARP — Address Resolution Protocol

ARP bridges the gap between Layer 3 (IP addresses) and Layer 2 (MAC addresses). Before a host can send an IP packet over Ethernet, it must know the destination's MAC address.

### ARP Request (Broadcast)

- The source host broadcasts an ARP request on the local LAN: **"Who has IP address X? Tell MAC address Y."**
- Destination MAC in the Ethernet frame: `FF:FF:FF:FF:FF:FF` (broadcast).
- The ARP request contains: sender's MAC, sender's IP, target IP, target MAC = `00:00:00:00:00:00`.

### ARP Reply (Unicast)

- The host with the matching IP address sends an **ARP reply** directly (unicast) back to the requester.
- The reply contains the target's MAC address.

### ARP Table (Cache)

- ARP results are stored in the **ARP table** (ARP cache) to avoid repeated broadcasts.
- Entries typically expire after ≈ 20 minutes.

### ARP in Routing

When a host sends a packet to a destination on a **different subnet**, the ARP request targets the **default gateway's** IP address (not the final destination), because the gateway is the next hop on the local LAN.

---

## Key Connections

- [[concepts/tcp-ip-network-model]] — These protocols operate at Layer 3 (control plane)
- [[concepts/ip-addressing]] — Routing tables contain IP prefixes; ARP resolves IPs to MACs; ICMP is encapsulated in IP
- [[concepts/data-link-layer-ethernet]] — ARP resolves the MAC address needed to build the Ethernet frame; Ethernet broadcasts carry ARP requests
- [[concepts/graph-algorithms]] — OSPF's route calculation phase applies Dijkstra's shortest-path algorithm on the LSDB
- [[concepts/transport-layer-tcp-udp]] — TCP/UDP segments travel inside IP packets; ICMP errors reference the IP header of the offending packet
