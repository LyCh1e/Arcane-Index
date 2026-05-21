---
type: area
title: "Computer Networks"
domain: computer-networks
status: established
created: 2026-05-22
updated: 2026-05-22
address: c-000040
tags: [area, computer-networks, networking, tcp-ip, INF1006]
---

# Computer Networks

The study of how data travels across interconnected systems — from the physical transmission of bits to the application-level protocols that power the modern Internet. This domain covers the TCP/IP stack from the ground up.

---

## Core Concepts

| Page | Topics | Lectures |
|---|---|---|
| [[concepts/tcp-ip-network-model\|TCP/IP Network Model]] | 5-layer model, OSI 7-layer reference, PDUs, packet switching, LAN vs WAN | L1 |
| [[concepts/data-link-layer-ethernet\|Data Link Layer & Ethernet]] | CSMA/CD, BEB, MAC addresses, Ethernet frame structure, switch self-learning, STP | L2, L3 |
| [[concepts/ip-addressing\|IP Addressing (IPv4 & IPv6)]] | IPv4 header, classful/CIDR, subnetting, VLSM, fragmentation, IPv6, migration | L4, L5 |
| [[concepts/network-layer-protocols\|Network Layer Protocols]] | OSPF (link-state, 3 phases, Dijkstra), BGP (path-vector), ICMP, ARP | L6 |
| [[concepts/transport-layer-tcp-udp\|Transport Layer — TCP & UDP]] | TCP vs UDP, 3-way handshake, flow/congestion control, GBN/SR, RTT estimation | L8, L9 |
| [[concepts/wireless-and-iot\|Wireless Networking & IoT]] | CSMA/CA, 802.11 standards, LPWAN (NB-IoT, LTE-M, LoRaWAN, Wi-Fi HaLow), MQTT | L10, L11 |
| [[concepts/application-layer-dhcp-dns\|Application Layer — DHCP & DNS]] | DHCP DORA, DNS hierarchy, recursive resolution, record types | L12 |

---

## Source

| Source | Type | Date |
|---|---|---|
| [[sources/INF1006-computer-networks\|INF1006 Computer Networks]] | Course (SIT) | 2026-05-22 |

---

## Cross-Domain Connections

- **Operating Systems** — Sockets connect application processes to transport layer ports; see [[concepts/os-processes-and-threads]]
- **Web Development** — HTTP, DNS, and TCP underpin every browser request; see [[concepts/web-fundamentals]]
- **Algorithms** — OSPF uses Dijkstra's shortest-path algorithm on the link-state database; see [[concepts/graph-algorithms]]
- **Security** — Network protocols are attack surfaces: ARP spoofing, DNS poisoning, TCP session hijacking; see [[concepts/owasp-top-10]] and [[concepts/threat-modeling]]
- **IoT / Mobile** — MQTT over TCP; DHCP address assignment for constrained devices; see [[concepts/wireless-and-iot]] and [[concepts/android-architecture]]
