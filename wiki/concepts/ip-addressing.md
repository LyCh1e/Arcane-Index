---
type: concept
title: "IP Addressing (IPv4 & IPv6)"
domain: computer-networks
complexity: high
status: established
created: 2026-05-22
updated: 2026-05-22
address: c-000035
tags: [ipv4, ipv6, subnetting, cidr, vlsm, fragmentation, routing, INF1006]
---

# IP Addressing (IPv4 & IPv6)

The network layer (Layer 3) identifies hosts using IP addresses and routes packets from source to destination. IPv4 has a 32-bit address space; IPv6 expands this to 128 bits. CIDR and subnetting allow flexible allocation; VLSM conserves addresses further.

---

## IPv4 Header

The IPv4 header is **20 bytes** by default (minimum). Key fields:

| Field | Size | Description |
|---|---|---|
| **Version** | 4 bits | `0100` = IPv4 |
| **HLEN** | 4 bits | Header length in 4-byte words (default 5 × 4 = 20 bytes) |
| **Service** | 1 byte | Differentiated Services (DSCP) + ECN |
| **Total Length** | 2 bytes | Total IP datagram size including header |
| **Identification** | 2 bytes | Unique ID grouping fragments of the same original packet |
| **Flags (DF, MF)** | 3 bits | Don't Fragment; More Fragments |
| **Fragment Offset** | 13 bits | Starting position of fragment in multiples of 8 bytes |
| **TTL** | 1 byte | Decremented by 1 at each router; packet discarded at TTL = 0 |
| **Protocol** | 1 byte | Layer 4 protocol: `0x01` ICMP, `0x06` TCP, `0x11` UDP |
| **Header Checksum** | 2 bytes | Error detection over the header |
| **Source IP** | 4 bytes | Sender's IP address |
| **Destination IP** | 4 bytes | Receiver's IP address |

---

## IPv4 Address Format

- **32 bits**, written in **dotted-decimal notation** (e.g., `192.168.1.1`).
- Divided into a **Network ID** and a **Host ID**.

### Classful Addressing (Legacy)

| Class | Leading Bits | Network Bits | Host Bits | Range |
|---|---|---|---|---|
| A | 0 | 8 | 24 | 0.0.0.0 – 127.255.255.255 |
| B | 10 | 16 | 16 | 128.0.0.0 – 191.255.255.255 |
| C | 110 | 24 | 8 | 192.0.0.0 – 223.255.255.255 |
| D | 1110 | Multicast | — | 224.0.0.0 – 239.255.255.255 |
| E | 1111 | Reserved | — | 240.0.0.0 – 255.255.255.255 |

### Special Addresses

| Address | Purpose |
|---|---|
| Host ID all zeros | Network address (identifies the subnet) |
| Host ID all ones | Directed broadcast address |
| `127.0.0.0/8` | Loopback (commonly `127.0.0.1`) |
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | Private (RFC 1918) — not routable on public Internet |

---

## CIDR — Classless Inter-Domain Routing

Replaces classful addressing. Uses **prefix notation**: `192.168.1.0/24`.

- The prefix length (e.g., `/24`) specifies how many leading bits belong to the network ID.
- Allows flexible block sizes; eliminates the rigid class boundaries.

---

## Subnetting

**Subnetting** divides the host portion of an address block into a **subnet ID** and a **host ID**, allowing a single organisation to segment its address space into multiple smaller networks.

> **Subnet mask = network prefix length + bits allocated to the subnet ID**

Example: A /16 block with 5 bits allocated as subnet ID → subnet mask = /21.

### Per-Subnet Rules

- **First address** in each subnet = network address (not assignable).
- **Last address** in each subnet = broadcast address (not assignable).
- Usable hosts = 2^(host bits) − 2.

### Host Count Quick Reference

| Subnet Mask | Host Bits | Usable Hosts |
|---|---|---|
| /24 | 8 | 254 |
| /25 | 7 | 126 |
| /26 | 6 | 62 |
| /27 | 5 | 30 |
| /28 | 4 | 14 |
| /29 | 3 | 6 |
| /30 | 2 | 2 |

### VLSM — Variable Length Subnet Mask

**VLSM** allows each subnet within a block to have a different prefix length, sized to match actual host requirements. This conserves addresses by avoiding over-allocation.

---

## Routing and Forwarding

Each router maintains a **routing table** with entries:

| Field | Description |
|---|---|
| Network Destination | Destination prefix (e.g., `192.168.2.0/24`) |
| Subnet Mask | Network mask |
| Next Hop / Exit Interface | Where to forward matching packets |

### Longest Prefix Match

When multiple routing table entries match a destination, the router selects the entry with the **longest (most specific) prefix**. If no specific route matches, the **default route** (`0.0.0.0/0`) is used.

---

## IPv4 Fragmentation and Reassembly

When an IP datagram is larger than the link's **MTU**, a router **fragments** it. The destination host **reassembles** fragments using three header fields:

| Field | Description |
|---|---|
| **Identification** | All fragments of the same datagram share the same ID |
| **DF (Don't Fragment)** | If set to 1 and packet > MTU, router discards the packet and sends an ICMP error |
| **MF (More Fragments)** | Set to 1 for all fragments except the last |
| **Fragment Offset** | Starting byte position ÷ 8 (all non-final fragments must be multiples of 8 bytes) |

> If any fragment is lost or corrupted, the entire original datagram is discarded by the destination host.

---

## IPv6

### Why IPv6?

- IPv4 provides ≈ 4.3 billion addresses (32 bits); address exhaustion is a reality.
- IPv6 uses **128-bit addresses** → 3.4 × 10³⁸ unique addresses.
- Simplified, fixed-length 40-byte header (vs. variable IPv4 header).

### IPv6 Address Format

- **128 bits** written as **8 groups of 16-bit hexadecimal**, separated by colons.
- Example: `2001:0DB8:AC10:FE01:0000:0000:0000:0000`

**Abbreviation rules:**
1. Leading zeros within each group may be omitted.
2. One contiguous run of all-zero groups may be replaced with `::` (used **at most once**).

```
2001:0DB8:0000:0100:0000:0000:0000:0030
→ 2001:DB8:0:100::30
```

---

## IPv4 → IPv6 Migration

| Technique | Description |
|---|---|
| **Dual Stack** | Devices run both IPv4 and IPv6 simultaneously |
| **Tunnelling (6to4)** | IPv6 packets encapsulated inside IPv4 packets to cross IPv4 infrastructure (RFC 2473) |
| **Tunnelling (4in6)** | IPv4 packets encapsulated inside IPv6 packets |
| **Translation (NAT64)** | Network-layer translation between IPv4 and IPv6 |

---

## Key Connections

- [[concepts/tcp-ip-network-model]] — IP operates at Layer 3; IP addresses identify hosts in the network layer
- [[concepts/network-layer-protocols]] — OSPF, BGP populate routing tables; ARP resolves IP → MAC; ICMP reports IP errors
- [[concepts/data-link-layer-ethernet]] — Ethernet frames carry IP packets; MTU of 1500 bytes drives fragmentation
- [[concepts/transport-layer-tcp-udp]] — Port numbers + IP address = socket; TCP/UDP run on top of IP
- [[concepts/application-layer-dhcp-dns]] — DHCP dynamically assigns IP addresses; DNS resolves names to IP addresses
