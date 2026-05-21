---
type: concept
title: "TCP/IP Network Model"
domain: computer-networks
complexity: medium
status: established
created: 2026-05-22
updated: 2026-05-22
address: c-000033
tags: [tcp-ip, osi-model, network-layers, pdu, packet-switching, encapsulation, INF1006]
---

# TCP/IP Network Model

The TCP/IP model is the de-facto architectural standard for the Internet. It defines a layered communication framework in which each layer provides specific services and uses the services of the layer below it.

---

## The 5-Layer TCP/IP Architecture

Originally standardised as a 4-layer model in RFC 1122, the Internet implementation uses a **5-layer architecture**.

| Layer | Communication Scope | Role |
|-------|---------------------|------|
| **5 — Application** | Application-to-Application | Concerned with application requirements (HTTP, DNS, SMTP) |
| **4 — Transport** | Process-to-Process | End-to-end connection establishment, error control, delivery of segments |
| **3 — Network** | Host-to-Host | Packet delivery from source host to destination host |
| **2 — Data Link** | Node-to-Node | Hop-to-hop delivery of frames across a single link |
| **1 — Physical** | Node-to-Node (physical) | Actual transmission of bits between adjacent nodes |

> **Mnemonic:** "All Tired Network Dogs Pant" (Application → Transport → Network → Data Link → Physical).

---

## Addresses at Each Layer

Because a host runs many processes, is one of many hosts on a network, and sits on one of many nodes on a link, different address types exist at different layers:

| Address Type | Scope | Identifies |
|---|---|---|
| **Port numbers** | Transport | A specific process running on a host |
| **IP addresses** | Network | A specific host on the network |
| **MAC / Link addresses** | Data Link | A specific node on the local link |

---

## PDU Terminology

| Term | Layer | Meaning |
|---|---|---|
| **Segment** | Transport (L4) | TCP/UDP protocol data unit |
| **Packet** | Network (L3) | IP protocol data unit |
| **Frame** | Data Link (L2) | Link-layer protocol data unit |

PDU (Protocol Data Unit) is the generic OSI term. Each layer adds its own header (and sometimes trailer) when encapsulating the payload from the layer above — this is called **encapsulation**.

---

## The OSI 7-Layer Model (Reference Only)

The OSI model was designed by ISO as the intended Internet standard but lost to TCP/IP. It serves as a conceptual reference and terminology source.

| Layer | Name | Examples |
|---|---|---|
| 7 | Application | HTTP, FTP, SSH, DNS |
| 6 | Presentation | MPEG, JPEG |
| 5 | Session | APIs, RPC |
| 4 | Transport | TCP, UDP |
| 3 | Network | IP, ICMP, IPSec |
| 2 | Data Link | Ethernet, Switch |
| 1 | Physical | Coax, fibre, wireless |

TCP/IP layers 5, 4, 3, 2, 1 map roughly to OSI layers 7+6+5, 4, 3, 2, 1 respectively.

---

## Packet-Switched Networking

The Internet is a **packet-switched datagram network**:

- Data is divided into smaller **packets** before transmission because each link has a maximum transfer unit (**MTU**).
- There is **no reservation of a communication path** — different packets may take different routes through the network.
- Packets may arrive **out of order**, be **corrupted**, or be **lost** entirely.
- The network layer therefore provides **unreliable, best-effort delivery**; reliability is the responsibility of the transport layer (TCP).

### Network Types

| Type | Example | Path behaviour |
|---|---|---|
| Circuit-switched | Telephone network | Dedicated path reserved for duration |
| Datagram (packet-switched) | IP / Internet | No reservation; each packet routed independently |
| Virtual-circuit | ATM, Frame Relay | Logical path established before data transfer |

---

## LAN vs WAN

| Feature | LAN | WAN |
|---|---|---|
| Coverage | Room or building | Large geographical area |
| Links | Shared broadcast medium or switched | Point-to-point links |
| Examples | Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11) | Leased lines, ISP backbone |

---

## Key Connections

- [[concepts/data-link-layer-ethernet]] — Layer 2 detail: CSMA/CD, MAC addresses, Ethernet frames, switches
- [[concepts/ip-addressing]] — Layer 3 detail: IPv4/IPv6 addressing, subnetting, CIDR
- [[concepts/network-layer-protocols]] — Layer 3 control plane: OSPF, BGP, ICMP, ARP
- [[concepts/transport-layer-tcp-udp]] — Layer 4 detail: TCP 3-way handshake, flow/congestion control, UDP
- [[concepts/application-layer-dhcp-dns]] — Layer 5 detail: DHCP, DNS
- [[concepts/web-fundamentals]] — HTTP at the application layer; browser-to-server communication
- [[concepts/os-processes-and-threads]] — Sockets as the OS abstraction that connects processes to transport layer ports
