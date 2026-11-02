# INF 2005 - Cyber Security Fundamentals
**Dr Aris Cahyadi Risdianto**

## Network Security: Introduction to Network Defense

---

## Recap: Network Security: Attack and Exploits

Slide keywords: zombie, Spoofing, ARP, Concept

### How does the ARP work?

ARP = Address Resolution Protocol (animated explainer graphic).

---

## Network Defense-in-Depth

### Network Defense-in-depth

Diagram layers (outer to inner), with example controls:

- **Policies, procedures and awareness** – Passwords, policies and data classification
- **Physical** – Locks, fences and security guards
- **Perimeter** – Firewall, VPN and packet filters
- **Internal network** – Firewall, intrusion detection and encryption
- **Host** – Platform OS, patches and malware protection
- **App** – SSO, authentication and authorization
- **Data** – Database, content and message security

Source: https://www.wallarm.com/what/defense-in-depth-concept

- **Defense in depth** – defences are layered, the main objective is to delay the attack's progress rather than to stop it at the onset.
- **First level** – control access to and from unauthorized networks and will allow or block traffic based on security rules.
- **Second level** – systems detect (and protect) against malicious network activity and are typically signature-based.
- **Third level** – VPN provides encryption over a public IP network.

### Network-based Attacks (Recap)

Attacks shown: Denial of Service (DoS) Attack, Distributed Denial of Service (DDoS) Attack, Man-in-the-Middle (MitM) Attack, Packet Sniffing, Port Scanning, ARP Spoofing.

Source: https://www.educba.com/types-of-attack/

- **DoS** and **DDoS** exploit **open services** for TCP and UDP port numbers
- **MitM** exploits **unsecured physical ports** in the network devices
- **Packet sniffing** exploits **unencrypted packets** that contain credentials
- **Port scanning** exploits **unfiltered service** for TCP and UDP port numbers
- **ARP spoofing** exploits **unsecured physical ports** connected to attackers

### Network Defense-in-depth (attacks mapped to layers)

Attack-to-layer annotations on the diagram:

- DoS/DDoS, Sniffing, Scanning – Internal network
- DoS/DDoS – Perimeter
- Man-in-the-middle, Spoofing – Physical
- Spoofing – App
- Sniffing – Data

Source: https://www.wallarm.com/what/defense-in-depth-concept

- Defense against **DoS/DDoS** by filtering/limiting access to **TCP/UDP ports**
- Defense against **MitM** by securing **access to the devices' physical ports**
- Defense against **Sniffing** by encrypting **packets (data)**
- Defense against **Scanning** by filtering/limiting access to **TCP/UDP ports**
- Defense against **Spoofing** by securing **access to the physical ports** and applying **authentication/authorization/authorization (AAA) configuration**

---

## Network Defense: Firewall

### Firewalls

- Can be implemented as a hardware or software appliance
- Monitors and filters network traffic – DMZ, zone segregation
- Combination of security mechanisms (e.g., packet filters, proxies)
- Can support Virtual Private Networks

Left diagram (DMZ architecture): ISP → Boundary Router / Packet Filter → External DMZ Network (Main Firewall, External Web Server) → Internal DMZ Network (Internal Firewall, Internal Email Server) → Interior Protected Network.

Right diagram (**Zero Trust Model**): firewalls segment Partners and VPN Users, Internet, Extranet ("DMZ"), Exchange/Active Directory/Others, Sales and Marketing, Wireless Devices (BYOD), Development/R&D, Operations and Support.

### What Attacks does a Firewall Mitigate?

- **Port scanning** will have limited results, as it can lock down access to ports
- Could use it to stop **war driving**, requests allowed only from specific IP addresses
- Limited help with **DoS/DDoS** – stops a lot of requests from unwanted sources, <u>BUT</u> cannot protect against complex DDoS, e.g., Reflection DDoS
- Cannot protect against bypass attacks – e.g., dial-up server behind firewall

Reflection occurs when an attacker forges the source address of request packets, pretending to be the victim. Servers are unable to distinguish legitimate from spoofed requests when UDP is used – **WHY?**

**The attack caused exploited Memcached servers to send huge amounts of traffic to the victim.**

Example Nmap output shown on the slide (target www.nus.edu.sg, port 11211):

```
nmap -p 11211 -v ...
Starting Nmap 7.70 ( https://nmap.org ) at 2020-02-13 14:06 Malay Pen
Initiating Ping Scan at 14:06
Scanning www.nus.edu.sg (45.60.35.225) [4 ports]
Completed Ping Scan at 14:06, 1.25s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:06
Completed Parallel DNS resolution of 1 host. at 14:06, 0.01s elapsed
Initiating SYN Stealth Scan at 14:06
Scanning www.nus.edu.sg (45.60.35.225) [1 port]
Completed SYN Stealth Scan at 14:06, 0.21s elapsed (1 total ports)
Nmap scan report for www.nus.edu.sg (45.60.35.225)
Host is up (0.011s latency).

PORT        STATE     SERVICE
11211/tcp   filtered  memcache

Read data files from: C:\Program Files (x86)\Nmap
Nmap done: 1 IP address (1 host up) scanned in 7.51 seconds
           Raw packets sent: 6 (240B) | Rcvd: 1 (44B)
```

### Firewall Policies and Rule Sets

Flow: "it should do X" (e.g., deny all incoming TCP traffic) → **firewall policies** → **firewall rule set**

Outbound Firewall Rules table (drag and drop rows to change rule order):

| Rule | Protocol | Source IP / Port | Destination IP / Port | Policy |
|---|---|---|---|---|
| Bad Rule ✗ | TCP | Any / 80 | 24.180.49.139 / 80 | Deny |
| Good Rule ✓ | TCP | Any / Any | 24.180.49.139 / 80 | Deny |
| Default | Any | Any | Any | Allow |

The **bad one** only looks for requests from port 80 to port 80, but we could have **HTTP requests** from any port between 1024-65535 so traffic could still be let through.

### Packet Filtering

- A **packet filtering firewall** tests each packet that crosses the firewall according to a set of user-defined rules.
- Most common type of firewall
- Security rules pass/block/filter traffic based on eg. port, IP address and IP protocol
- Hardware and software packet filtering
- In addition, compare **Stateless vs Stateful**

Examples shown: **Windows Application Firewall** (Windows Defender Firewall inbound rules, e.g., Apache HTTP Server rules with Public/Private/Domain profiles set to Block or Allow) and **Intel 82599 NIC Packet Filter** (hardware).

### Stateless vs Stateful Firewall

- **Stateless packet filter** - Does not look at the state of connections but just at the packets themselves (packet by packet, using ACL rules). An example is the Extended Access Control Lists on Cisco IOS Routers.
- **Stateful packet filter** - aware of the connections that pass through it. It adds and maintains information about a user's connections in a state table. It then uses this table to implement the security policies for user connections. Examples: PIX, ASA, Checkpoint.

---

## Network Defense: IDS and IPS

### Intrusion Detection Systems (IDS)

Diagram: Attacker → Internet → Router → Firewall, with NIDS sensors on Subnet 1 and Subnet 2 (via switches), HIDS on hosts and on the Server.

- **Network Intrusion Detection System (NIDS)** detects attacks without needing traffic flow over it.
- NIDS can be connected to a Hub network in *promiscuous* mode or to a Switch network via *port mirroring (span port)* to monitor multiple/different sub-networks.
- NIDS can be extended via **Host IDS (HIDS)** or **agents** for a larger attack detection scope
- Support **deep packet inspection (DPI)** – examines the packet's header and data, to get more detailed than packet filtering
- Use **signature-based** or **statistical anomaly-based** detection techniques with higher accuracy

### Intrusion Protection Systems (IPS)

Diagram comparison: **Intrusion Detection System (IDS)** vs **Intrusion Prevention System (IPS)**.
- IDS: Internet → Firewall → Switch → Corporate Network (Web Server, E-mail Server); IDS and Management System attached to the switch.
- IPS: Internet → Firewall → IPS (inline) → Switch → Corporate Network (Web Server, E-mail Server); Management System attached.

- A Network Intrusion Prevention System (NIPS) does what a NIDS does, plus **automated responses to block** the intrusions, protect against system hijacking and data theft (including changing firewall settings).
- NIPS is usually located inline between the **firewall and the protected network** and thus requires greater logging capacity and ability to respond in real-time.

---

## Network Defense: Proxies

### Network Proxy

Diagram: devices → Proxy → Firewall → Internet.

- A proxy firewall, or application gateway, protects network resources by redirecting web requests at the application layer (no direct connections with external servers).
- Scans incoming traffic for layer 7 protocols like FTP or HTTP, and also offers deep packet inspection of the incoming data packets for possible maliciousness.
- Functioning at a high level in the OSI stack enables them to detect and address spoofing and other sophisticated attacks;
- Examines the data for content that is not allowed; can limit applications supported by network.
- Provides private or anonymous Internet access (hides IP address).

### Application Proxy

Diagram: within a firewall, separate proxy servers (Web Proxy Server for HTTP, FTP Proxy Server for FTP, Mail Proxy Server for SMTP) operate at the Application Layer (DPI), above TCP (Transport Layer) and IP (Network Layer), between the Outside Network and the Internal Network.

**Examples:** Symantec Advanced Security and Gateway ProxySG

- Have extensive logging capabilities due to the ability to examine the contents of the entire network packet rather than just addresses and ports.
- It can also cache frequently accessed web pages to reduce network traffic – improved network performance.
- May not be well-suited for real-time or high-bandwidth applications.

---

## Network Defense: Virtual Private Networks

### Virtual Private Networks (VPNs)

Extend corporate networks to remote offices, mobile users, telecommuters, and other extranet partners.

**HTTPS** only provides encryption between the website and your browser.

VPN allows you to extend a private network across a public one, such as the internet – the result the attacker cannot read your data (strong encryption)

### VPN Sub-Systems

Diagram: YOU → (VPN tunnel, "Secures your Data") → THE INTERNET, with Government, Hackers and Snoopers unable to read the traffic.

**Internet Protocol Security (IPSec) and Transport Layer Security (TLS)**

- **Authentication** – users must be authenticated before a secure tunnel is established.
- **Tunnelling** – encapsulate one type of protocol in the datagram of a different protocol and maintain by a tunnel management protocol to create, maintain, and terminate the tunnel.
- **Encryption** – to protect data traveling through tunnel.

### IPSec VPN vs TLS VPN (Security)

- Layer 2 Tunnelling Protocol (L2TP) is a tunnelling protocol implemented with IPsec for security
- OpenVPN is an open-source s/w implementing VPN techniques and uses Transport Layer Security (TLS) for key exchange

| | L2TP/IPsec | OpenVPN |
|---|---|---|
| Key size | 256-bit | 160-bit + 256-bit |
| Platforms | Windows, Mac OS X, Linux, iOS, Android | Windows, Mac OS X, iOS, Android |
| Compatibility | Compatible with most PC, Mobile and Tablet Operating Systems. | Compatible with most PC Operating Systems. |
| Security | Highest level of encryption. Verifies data integrity and encapsulates the information twice. (AES) | Encrypts data with digital certificate, highest level of security. (advanced AES) |
| Speed | Double encryption on all data, higher CPU usage. | Best overall performance, fast speeds even over high latency networks. |

---

## Network Defense: (Physical) Port Security

### Switch MAC address Learning (1/2)

Diagram: Host A sends a frame "A to B" into Port 1. MAC address table is incomplete (A → Port 1, C → Port 3). Host B is unknown so the switch will flood the frame; Host C sees traffic to Host B.

- Source MAC addresses are used to build the all-important MAC address table
- The switch built the MAC address table dynamically based on the request by the source
- If the destination MAC address of a frame is not found in the table, it will be flooded out to all ports except incoming port.

### Switch MAC address Learning (2/2)

Diagram: MAC address table now has A → Port 1, B → Port 2, C → Port 3 ("MAC address tables are limited in size"). The switch has learned that Host B is on Port 2; Host C does not see traffic to Host B anymore.

- After the source address is self-learning by the switch, a unicast frame will only be forwarded out to the intended port → switch is considered to be more 'secure' than a hub.
- Switch's MAC address table cannot be of infinite size.
- **What happens when a switch does not have sufficient memory to store more new MAC addresses?**

### Switch Port Security

Diagram (source: PIVIT): Port Fa0/1: Allow MAC of PC1; Port Fa0/2: Allow MAC of Admin PC; Port Fa0/3: Allow Max 1 MAC. SW1 and SW2 with PC1, PC2, PC3 and an Attacker; the attacker's MAC is blocked.

Source: https://info.pivitglobal.com/resources/port-security-layer-2-protection

- **MAC flooding attack:** Make the switch MAC address table full of fake source MAC addresses, so an authentic frame is not found, flooded, and received by attackers.
- **Port security** restricts input to a switch interface by identifying and limiting the MAC addresses of the hosts that are allowed to access the interface
- For port security violation with **shutdown mode**, the port will be moved to error disabled state if violation is detected

---

## Network Defense: Network AAA

### What is AAA?

Source: https://www.computernetworkingnotes.com/ccna-study-guide/aaa-in-computer-networking-explained.html

It is a three-layer security model:

- **Who are you? – Authentication** (User1 sends username/password; server replies Access Granted)
- **What can you do? – Authorization** (User1 opens File-A, File-A opened; tries to write in File-A, "You are not authorized to modify the file")
- **When do you do? – Accounting** (log: "User1 accessed File-A at 9:34 AM.")

### What is Network AAA?

**Remote Authentication Dial In User Service (RADIUS)** consist of **NAS** (connecting point between an individual and a network access server), **client/supplicant** (machine/person requesting network connectivity), and **RADIUS Server** (verification server to ensure the individual has the proper authorization levels to enter the network.

**Terminal Access Controller Access Control System (TACACS)** is protocol between authentication server to determine if users have the permission to access the network. It is different with RADIUS in data transmission, encryption mode, authentication and authorization, and event recording

RADIUS protocol architecture diagram: access clients connect through RADIUS clients / Network Access Servers (Network access server, VPN server, Wireless access point, 802.1x switch), which talk to the RADIUS server.
Source: https://www.wallarm.com/what/radius-remote-authentication-dial-in-user-service-protocol

TACACS message flow diagram (User, HWTACACS client, HWTACACS server):

1. User logs in.
2. Client sends an Authentication Start packet.
3. Server sends an Authentication Reply packet to request the user name.
4. Client requests the user name; user enters the user name.
5. Client sends an Authentication Continue packet containing the user name.
6. Server sends an Authentication Reply packet to request the password.
7. Client requests the user password; user enters the password.
8. Client sends an Authentication Continue packet containing the password.
9. Server sends an Authentication Reply packet, indicating successful authentication.
10. Client sends an Authorization Request packet.
11. Server sends an Authorization Response packet, indicating successful authorization.
12. User logs in successfully.
13. Client sends an Accounting-Request (Start) packet; server sends an Accounting-Response (Start) packet.
14. User logs out.
15. Client sends an Accounting-Request (Stop) packet; server sends an Accounting-Response (Stop) packet.

Source: https://info.support.huawei.com/info-finder/encyclopedia/en/TACACS.html

---

## Q&A
