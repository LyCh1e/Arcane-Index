---
type: concept
title: "Network Security — Defence"
domain: cyber-security
status: established
created: 2026-11-02
updated: 2026-11-02
sources: [inf2005-csf-network-security-defence]
tags: [network-security, defence-in-depth, firewall, stateful-firewall, ids, ips, nids, hids, proxy, vpn, ipsec, openvpn, port-security, mac-flooding, aaa, radius, tacacs, inf2005]
related:
  - "[[concepts/network-security-attacks]]"
  - "[[concepts/access-control]]"
  - "[[concepts/digital-forensics]]"
  - "[[sources/inf2005-csf-network-security-defence]]"
---

# Network Security — Defence

Defence in depth layers several controls so that the failure of one does not expose the whole network. The aim is to **delay** an attack's progress rather than stop it at the outset. This page is the defensive counterpart to [[concepts/network-security-attacks]].

## 1. Defence in depth

Layers, outer to inner, with example controls:

| Layer | Example controls |
|-------|------------------|
| Policies, procedures and awareness | Passwords, policies, data classification |
| Physical | Locks, fences, guards |
| Perimeter | Firewall, VPN, packet filters |
| Internal network | Firewall, intrusion detection, encryption |
| Host | OS platform, patches, malware protection |
| Application | Single sign-on, authentication, authorisation |
| Data | Database, content and message security |

Three network-level tiers: the **first** controls access to and from untrusted networks (firewall); the **second** detects and protects against malicious activity, typically signature-based (IDS/IPS); the **third** is the VPN, which encrypts traffic over a public IP network.

### Attack, weakness, layer and defence

| Attack | Exploits | Layer | Defence |
|--------|----------|-------|---------|
| DoS / DDoS | Open TCP/UDP services | Perimeter, internal | Filter or limit access to ports |
| Man-in-the-middle | Unsecured physical ports | Physical | Secure access to device ports |
| Packet sniffing | Unencrypted packets with credentials | Internal, data | Encrypt packets and data |
| Port scanning | Unfiltered services | Internal | Filter or limit access to ports |
| ARP spoofing | Unsecured physical ports | Physical, application | Secure ports and apply AAA |

## 2. Firewalls

A firewall is a hardware or software appliance that monitors and filters traffic using a combination of mechanisms (packet filters, proxies). It supports zone segregation and DMZs, and can support VPNs.

- **DMZ architecture:** ISP → boundary router (packet filter) → external DMZ (main firewall, external web server) → internal DMZ (internal firewall, internal mail server) → interior protected network.
- **Zero-trust model:** firewalls segment partners and VPN users, the extranet, directory services, sales, BYOD wireless, R&D and operations from each other, so trust is never assumed from location alone.

### What a firewall mitigates

- **Port scanning:** limited results, because ports are locked down (the slide's Nmap run shows Memcached port 11211 as `filtered`).
- **War driving:** requests can be limited to specific IP addresses.
- **DoS/DDoS:** limited help. It stops many unwanted sources but cannot stop complex attacks such as **reflection DDoS**.
- **Bypass attacks:** no protection against paths around it, such as a dial-up server behind the firewall.

### Reflection and UDP

A reflection attack forges the victim's source address in request packets. Servers cannot tell legitimate from spoofed requests over UDP because UDP is connectionless: there is no handshake that proves the sender owns the address, so the reply goes to the forged address. The slide's example is exploited Memcached servers sending huge volumes of traffic to the victim. (The explanation of *why* is an addition; the slide only poses the question.)

### Policies and rule sets

A policy ("deny all incoming TCP traffic") is translated into a **rule set**. Rules are evaluated in order, so ordering matters, and a default rule ends the list.

| Rule | Protocol | Source | Destination | Policy |
|------|----------|--------|-------------|--------|
| Bad | TCP | Any / **80** | 24.180.49.139 / 80 | Deny |
| Good | TCP | Any / **Any** | 24.180.49.139 / 80 | Deny |
| Default | Any | Any | Any | Allow |

The bad rule matches only requests *from* port 80, but HTTP clients use ephemeral source ports (1024–65535), so the traffic still gets through.

### Packet filtering: stateless against stateful

- **Stateless:** judges each packet alone against ACL rules, for example extended ACLs on Cisco IOS routers.
- **Stateful:** tracks connections in a **state table** and applies policy to the connection (examples: PIX, ASA, Check Point).

Examples on the slides: Windows Defender Firewall inbound rules (Public, Private, Domain profiles) and the Intel 82599 NIC hardware packet filter.

## 3. IDS and IPS

| | IDS | IPS |
|---|-----|-----|
| Placement | Out of band, fed by a mirror or sensor | Inline, between the firewall and the protected network |
| Action | Detects and alerts | Detects and **automatically blocks**, including changing firewall settings |
| Demand | Logging | Greater logging capacity and real-time response |

- **NIDS** can sit on a hub in *promiscuous* mode or on a switch **SPAN port** (port mirroring) to watch several subnets. **HIDS** or agents widen the scope to individual hosts.
- Both support **deep packet inspection** (header and data) and use **signature-based** or **statistical anomaly-based** detection.

## 4. Proxies

A proxy firewall (application gateway) redirects requests at the **application layer**, so internal hosts never connect directly to external servers.

- Scans layer 7 protocols (FTP, HTTP) with DPI, which lets it catch spoofing and other sophisticated attacks and block disallowed content.
- Hides internal IP addresses (private or anonymous access) and can restrict supported applications.
- Extensive logging, because it sees whole packets rather than only addresses and ports; can **cache** popular pages.
- Drawback: unsuited to real-time or high-bandwidth applications.
- Separate proxies per protocol: web (HTTP), FTP and mail (SMTP). Examples: Symantec ProxySG.

## 5. VPNs

A VPN extends a private network across a public one. **HTTPS only protects traffic between the site and the browser**; a VPN protects everything through the tunnel. Three sub-systems:

1. **Authentication** before the tunnel is established.
2. **Tunnelling:** encapsulate one protocol in another, with a management protocol to create, maintain and end the tunnel.
3. **Encryption** of data in the tunnel (IPsec or TLS).

| | L2TP/IPsec | OpenVPN |
|---|------------|---------|
| Key size (slide) | 256-bit | 160-bit + 256-bit |
| Security | Encapsulates twice; verifies integrity (AES) | Digital certificates; TLS key exchange (AES) |
| Speed | Double encryption, higher CPU use | Best overall; fast over high latency |
| Compatibility | Most PC, mobile and tablet OSs | Most PC OSs |

## 6. Physical port security

**Switch MAC learning:** the switch builds a MAC address table dynamically from *source* addresses. If the destination is unknown it **floods** the frame out of every port except the incoming one. Once learned, unicast frames go only to the intended port, which makes a switch more secure than a hub.

**MAC flooding:** the table has a finite size. An attacker fills it with fake source addresses; with no room for new entries the switch cannot find genuine destinations, so it floods frames and the attacker receives them. This answers the slide's question: the switch degrades to hub-like behaviour. (The answer is an addition.)

**Port security** limits which MAC addresses may use an interface (for example, allow a named PC's MAC or a maximum of one MAC). In **shutdown** violation mode the port moves to the *error-disabled* state.

## 7. Network AAA

| Question | Function | Example |
|----------|----------|---------|
| Who are you? | **Authentication** | Username and password accepted |
| What can you do? | **Authorisation** | May read File-A, may not write to it |
| What did you do? | **Accounting** | "User1 accessed File-A at 9:34 AM" |

- **RADIUS:** a network access server (NAS: VPN server, wireless AP or 802.1X switch) relays the supplicant's credentials to a RADIUS server that verifies authorisation.
- **TACACS (HWTACACS):** separates authentication, authorisation and accounting, which differs from RADIUS in transport, encryption, authorisation and event recording. Its flow is: authentication start, reply for username, continue, reply for password, continue, success; then an authorisation request and response; then accounting start and stop packets on login and logout.

See [[concepts/access-control]] for the identity, authentication and authorisation model that AAA servers implement.

> [!gap] The slides compare RADIUS and TACACS only in general terms. Specifics (UDP against TCP, which parts of the packet are encrypted) need a primary source.
