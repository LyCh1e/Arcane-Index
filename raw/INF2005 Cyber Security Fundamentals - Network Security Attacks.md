# Network Security: Vulnerabilities and Exploits

*INF2005 Cyber Security Fundamentals, Week 9 — Dr Aris Cahyadi Risdianto*

## 1. Network Basics

### What is a Network?
- A **computer network** is a collection of **autonomous computers interconnected by a single technology**. Two computers are interconnected if they can **exchange information**.
- The medium can be copper wire, fibre optics, microwaves, infrared or satellites.
- Networks are usually joined into larger networks. The **Internet** is the best-known **network of networks** (Tanenbaum & Wetherall).

### Network Architectures
| | Client-Server | Peer-to-Peer (P2P) |
|---|---|---|
| Approach | **Centralized** | **Decentralized** |
| Strengths | More **scalable** for large networks such as the Internet | More **fault-tolerant** against single points of failure; more **cost-effective** for smaller networks (for example Blockchain) |
| Weaknesses | Can suffer **bottlenecks** and high costs | |

### Network Protocols and Layers
- Packets are crafted and processed according to the **network layer hierarchy** (TCP/IP vs OSI models).
- Application data gets **specific headers added at each layer** before being sent from source to destination.

---

## 2. Vulnerabilities, Threats and Risk

```
Vulnerabilities + Threats = Risks
```

- A vulnerability will **never cause any risk or loss without an attack or exploit** launched by an attacker.
- Risk or loss can be measured by the **severity of the vulnerability** and the **likelihood of an attack exploiting it**. The **CVSS** calculator is a standard scoring tool.

### Common Network Vulnerabilities
- **Unsecured SSID** (fake AP)
- **Unfiltered service ports**
- **Unsecured physical ports**
- **Malicious users**
- **Unencrypted packets**

### Network-based Attacks and What They Exploit
| Attack | Exploits |
|---|---|
| **DoS / DDoS** | Open services on TCP and UDP port numbers |
| **Man-in-the-Middle (MitM)** | Unsecured physical ports on network devices |
| **Packet sniffing** | Unencrypted packets containing credentials |
| **Port scanning** | Unfiltered services on TCP and UDP port numbers |
| **ARP spoofing** | Unsecured physical ports connected to attackers |

---

## 3. (Distributed) Denial of Service

A **DoS** attack disrupts the **availability** of a target.

### Two Basic Forms
- **Bandwidth flood** — overwhelms the target's bandwidth. If the target can only service 100 MB of requests, sending 150 MB at once overloads it.
- **Service request flood** — disrupts the service with anomalous **HTTP requests, DNS queries or TCP connection requests**. The requests don't need to succeed, they only need to **use up resources**. Example: the **SYN flood**.

### Distributed Reflective DoS (DRDoS)
- Takes down availability through an **overwhelming volume of responses**.
- The attacker sends requests **without establishing connection state**.
- **Bots (reflectors)** send traffic with a **modified (spoofed) source address**, so the **replies go to the victim**. The bots are controlled by a **command and control (C&C)** server.

### Bots, Zombies and Botnets
| Term | Meaning |
|---|---|
| **Bot** | Malware that gives the attacker **complete control** of a computer |
| **Zombie** | An Internet-connected computer **infected with a bot** |
| **Botnet** | A **collection of zombies** used together, for example for DDoS |
| **IoT botnet** | IoT devices used as zombies. Their OS is usually a **stripped-down Linux**, so malware is easily compiled for the target architecture |

---

## 4. Man-in-the-Middle: Access Point Attacks

- **Anyone close to your router can get on** (WiFi hotspots, and your neighbours).
- **Wardriving** — mapping WiFi access points, to locate and potentially exploit them.
- **Evil Twin** — a **fake WiFi access point** that looks legitimate but is set up to **eavesdrop on wireless communications**.
- **SSID** = Service Set Identifier, the network name that can be imitated.
- **Access point hijacking** — victims connect to the attacker's AP, which sits in the path of their traffic.

---

## 5. Network Sniffing

### Packet Sniffing Overview
- Works differently on **hubs** and **switched networks**:
  - **Hubs:** nodes can be put into **promiscuous mode**, since input is broadcast to everyone.
  - **Switches:** need **ARP poisoning**, since the switch forwards by MAC address.
- If traffic is **unencrypted**, privacy is lost: credit card info, authentication details, confidential messages and so on.

### Passive vs. Active Sniffing
| | Passive sniffing | Active sniffing |
|---|---|---|
| Method | A sniffer (for example **Cain and Abel, Wireshark**) monitors packets | **Injects packets** to make traffic for other nodes flow to the attacker (for example **ArpSpoof**) |
| Depends on | **Promiscuous mode** of the NIC | Bypassing the **segmentation that switches provide** |
| Detection | **Difficult to detect** | More detectable |
| Works well on | Hubs; **does not work well on switched networks** | Switched networks |
| Wireless | | Active wireless sniffing sends **multiple network probes** to identify access points |

### Demo: Web Login Password Capture (Wireshark)
1. Start Wireshark, select all interfaces and start capturing.
2. In a browser, go to an **HTTP (not HTTPS)** login page and submit a test username and password. The login may fail, which doesn't matter.
3. Stop the capture.
4. Filter with `http.request.method == POST`.
5. Locate the HTTP packet and **Follow TCP stream**. The **password appears in clear text**.

> Lesson: credentials sent over unencrypted HTTP are trivially visible to a sniffer. Use **HTTPS/encryption**.

---

## 6. Network Spoofing and Poisoning

### Port Spoofing
- Security infrastructure decides what is legitimate traffic **by port number**.
- **SSH** normally uses port **22**, so security tools lock port 22 down. An attacker can disguise SSH sessions as **faux-HTTPS packets** on another port. These can carry malware or exfiltrate confidential data without alarming port-based tools.

### Defence: Deep Packet Inspection (DPI)
- **DPI** locates, identifies, classifies, reroutes or blocks packets with specific **data or code payloads**.
- Conventional packet filtering only examines **headers**, so it misses these.
- DPI (for example application filtering) identifies the spoofed traffic as SSH and forwards it to the appropriate security tools for analysis.

### Address Resolution Protocol (ARP)
- **Purpose:** translates **IP addresses to Ethernet MAC addresses**, linking the **32-bit IP address (internet layer)** to the **48-bit MAC address (link layer)**. RARP does the reverse.
- The **MAC address** is a physical machine address. The NIC driver needs it to transfer a packet.
- Each host keeps an **ARP cache**, a table of IP to MAC mappings.
  - Example: IP `192.168.174.100`, MAC `00:00:5e:00:53:af`
- **No verification in ARP:** it is a **stateless protocol**, so **requests and replies can be forged**.

#### How ARP Works
1. The source host **checks its ARP cache**. If the IP is not listed, it sends an **ARP request** ("Who has 129.119.103.2?").
2. The request is **broadcast** to MAC `FF:FF:FF:FF:FF:FF`. The switch forwards a broadcast to every other port.
3. The host that owns the IP sends an **ARP reply** with its MAC address.
4. The source **updates its ARP table** with the IP-to-MAC mapping.

#### ARP Spoofing (ARP Poisoning)
- A **forged ARP reply** is sent to the source, and it can be **unsolicited**.
- The victim's **ARP cache is updated with a forged entry**, so traffic meant for one host goes to the attacker (a man-in-the-middle position on a switched network).
- ARP cache entries are **not long-lived** because network adapters can be swapped, so the attacker keeps re-sending forged replies.

---

## 7. Port Scanning

- **Port scanning** checks a host's ports to see which are **open, closed or filtered**, and listens to data arriving at and leaving each port. Example ports: 21 (FTP), 25 (SMTP), 80 (HTTP).
- It exploits **unfiltered services** on TCP/UDP ports.

### Basic Nmap Scans
| Scan | Command | Notes |
|---|---|---|
| **TCP Connect scan** | `nmap -sT <ip address>` | Tries to connect to all ports; **a logging system will record the attempts** |
| **Focused port scan** | `nmap -p <port no> <ip address>` | Scans specific ports only |
| **Zenmap Quick Scan** | `-T4 -F` | `-T4` sets timing (0–5, higher is faster); `-F` is a fast scan of 100 ports |

- Findings can be cross-referenced with vulnerability databases: **cve.mitre.org** and **nvd.nist.gov**.

---

## Key Takeaways
- **Risk = vulnerability + threat.** A vulnerability alone causes no loss until someone exploits it.
- **DoS/DDoS** targets availability. Floods consume bandwidth or resources, and DRDoS uses spoofed source addresses so reflectors send replies to the victim. Botnets (including IoT botnets) supply the traffic.
- **Evil twins and wardriving** exploit open WiFi. **Packet sniffing** exploits unencrypted traffic, so use encryption such as HTTPS.
- **ARP has no authentication**, so forged replies can poison caches and redirect traffic on switched networks.
- **Port-based security can be fooled** by port spoofing. **Deep Packet Inspection** looks at payloads, not just headers.
- **Port scanning** (nmap) maps open services. It is a reconnaissance step that defenders can detect through logs.
