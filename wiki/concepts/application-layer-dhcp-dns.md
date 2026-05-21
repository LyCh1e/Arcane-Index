---
type: concept
title: "Application Layer — DHCP & DNS"
domain: computer-networks
complexity: medium
status: established
created: 2026-05-22
updated: 2026-05-22
address: c-000039
tags: [dhcp, dns, application-layer, dora, domain-names, name-resolution, INF1006]
---

# Application Layer — DHCP & DNS

The application layer (Layer 5 in TCP/IP) provides services directly to network applications. DHCP automates IP address assignment; DNS translates human-readable domain names into IP addresses. Both are foundational to how modern networks bootstrap and operate.

---

## DHCP — Dynamic Host Configuration Protocol

DHCP removes the need to manually configure IP addresses. A DHCP server automatically assigns:
- IP address
- Subnet mask
- Default gateway address
- DNS server address(es)

---

### DHCP DORA Process

The four-message exchange between a client and server:

```
Client                         Server
  |                               |
  |--- DISCOVER (broadcast) ----->|  "I need an IP address"
  |                               |
  |<-- OFFER (broadcast/unicast) -|  "Here is 192.168.1.50 for you"
  |                               |
  |--- REQUEST (broadcast) ------>|  "I accept 192.168.1.50"
  |                               |
  |<-- ACK (broadcast/unicast) ---|  "Confirmed. Use it for X seconds."
```

| Step | Message | Direction | Description |
|---|---|---|---|
| **D** | DHCP Discover | Client → broadcast | Client announces it needs configuration |
| **O** | DHCP Offer | Server → client | Server proposes an IP and configuration |
| **R** | DHCP Request | Client → broadcast | Client accepts the offer (broadcast so other servers know) |
| **A** | DHCP ACK | Server → client | Server confirms the lease |

### Key DHCP Message Fields

| Field | Description |
|---|---|
| **CIAddr** (Client IP Address) | Client's current IP address, if it has one |
| **YIAddr** ("Your" IP Address) | IP address the server is offering |
| **SIAddr** (Server IP Address) | IP address of the DHCP server |
| **GIAddr** (Gateway IP Address) | IP address of a DHCP relay agent (for cross-subnet DHCP) |
| **CHAddr** (Client Hardware Address) | Client's MAC address (16-byte field) |
| **Broadcast Flag** | Indicates whether the client can receive unicast DHCP replies before it has an IP address |
| **Transaction Identifier** | Random value used to match requests with replies |

---

## DNS — Domain Name System

DNS is the Internet's **distributed, hierarchical naming system**. It translates human-readable hostnames (e.g., `www.example.com`) into IP addresses. DNS uses **UDP on port 53** for most queries (small messages; low overhead).

> **Cross-reference:** DNS at the protocol level is covered here. For DNS as a web concept (how browsers use it), see [[concepts/web-fundamentals]].

---

### DNS Hierarchy

```
Root  (.)
├── .com
│   ├── google.com
│   └── amazon.com
├── .edu
│   └── mit.edu
└── .sg
    └── singaporetech.edu.sg
```

| Level | Name | Role |
|---|---|---|
| **Root** | 13 root server clusters (`a.root-servers.net` … `m.root-servers.net`) | Knows the addresses of all TLD name servers |
| **TLD (Top-Level Domain)** | `.com`, `.edu`, `.sg`, `.org` etc. | Knows the addresses of authoritative name servers for their domain |
| **Authoritative** | `ns1.example.com` | Holds the actual DNS records for the domain |
| **Local Resolver** | ISP or enterprise DNS cache | First stop for client queries; caches results |

---

### DNS Resolution Process (Recursive)

1. User types `www.example.com` in the browser.
2. The operating system checks its **local cache** (and `/etc/hosts` or equivalent). If found → done.
3. If not cached, the query goes to the **local DNS resolver** (provided by DHCP or configured manually).
4. Local resolver checks its own cache. If not cached:
5. Resolver queries a **Root DNS server** → returns the address of the `.com` TLD server.
6. Resolver queries the **.com TLD server** → returns the address of `example.com`'s authoritative server.
7. Resolver queries the **authoritative server** → returns the IP address (A record).
8. Local resolver caches the result (respecting the TTL) and returns the IP to the client.

---

### DNS Record Types

| Record | Purpose |
|---|---|
| **A** | Maps a hostname to an IPv4 address |
| **AAAA** | Maps a hostname to an IPv6 address |
| **CNAME** | Canonical name — alias pointing to another hostname |
| **MX** | Mail exchanger — specifies mail server for the domain |
| **NS** | Name server — delegates a zone to a specific name server |
| **PTR** | Pointer record — reverse DNS lookup (IP address → hostname) |

---

## Key Connections

- [[concepts/tcp-ip-network-model]] — DHCP and DNS operate at Layer 5 (application layer); both use UDP at Layer 4
- [[concepts/ip-addressing]] — DHCP assigns the IP address, subnet mask, and default gateway that IP addressing relies on
- [[concepts/transport-layer-tcp-udp]] — Both DHCP and DNS use UDP; DHCP because the client has no IP yet (must broadcast); DNS because queries are short and low latency is preferred
- [[concepts/web-fundamentals]] — HTTP requests begin with a DNS lookup; DNS is the first step in every browser navigation
- [[concepts/wireless-and-iot]] — MQTT IoT devices obtain their IP addresses via DHCP before connecting to the broker
