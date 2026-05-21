# INF1006 Computer Networks Notes
### Singapore Institute of Technology | 2024-2025 Trimester 3

---

# TABLE OF CONTENTS

1. [Lecture 0: Course Briefing](#lecture-0-course-briefing)
2. [Lecture 1: Introduction to Computer Networks and the Internet](#lecture-1-introduction-to-computer-networks-and-the-internet)
3. [Lecture 2: LAN and Data Link Layer](#lecture-2-lan-and-data-link-layer)
4. [Lecture 3: Switches and Ethernet](#lecture-3-switches-and-ethernet)
5. [Lecture 4: IPv4 Addressing](#lecture-4-ipv4-addressing)
6. [Lecture 5: IPv4 Continued & IPv6](#lecture-5-ipv4-continued--ipv6)
7. [Lecture 6: Control Plane Protocols and ARP](#lecture-6-control-plane-protocols-and-arp)
8. [Lecture 8: Transport Layer Part 1](#lecture-8-transport-layer-part-1)
9. [Lecture 9: Transport Layer Part 2](#lecture-9-transport-layer-part-2)
10. [Lecture 10: Wireless Networking](#lecture-10-wireless-networking)
11. [Lecture 11: LPWAN, IoT, and MQTT](#lecture-11-lpwan-iot-and-mqtt)
12. [Lecture 12: Application Layer – DHCP and DNS](#lecture-12-application-layer--dhcp-and-dns)
13. [Tutorial 1: Data Link Layer / MAC Sublayer – Ethernet LAN](#tutorial-1-data-link-layer--mac-sublayer--ethernet-lan)
14. [Tutorial 2: Spanning Tree Protocol and Internet Protocol](#tutorial-2-spanning-tree-protocol-and-internet-protocol)
15. [Tutorial 3: Network Layer – Control Plane Protocols & ARP](#tutorial-3-network-layer--control-plane-protocols--arp)
16. [Tutorial 4: Transport Layer 1](#tutorial-4-transport-layer-1)
17. [Tutorial 5: Transport Layer 2](#tutorial-5-transport-layer-2)

---

# LECTURE 0: COURSE BRIEFING

## Computer Networks: Evolution

Today almost 50 years later, computer networks have evolved to become the indispensable Internet which supports so many new services and applications that have changed our life.

The Internet supports services and applications running over computer networks/Internet, including:
- Metaverse
- IoT (Internet of Things)
- And many more

## Conclusion

INF1006 will be focusing on the essential standard communication protocols of the TCP/IP architecture, which taken together is commonly called the **TCP/IP protocol stack**.

---

# LECTURE 1: INTRODUCTION TO COMPUTER NETWORKS AND THE INTERNET

## In This Lecture You Will Learn…

- Internet is basically a network of interconnection of computer networks, or packet-switching networks.
- Internet is implemented using the TCP/IP 5-layer network architecture model.
- Protocol is needed at each layer, which defines the rules (format and order of messages) for communications.
- The collection of protocols from the various layers together form a **protocol stack**.

## Network Infrastructure

Despite offering similar services, **data link layer** is different for different computer networks which can be broadly classified as **Local Area Network (LAN)** or **Wide Area Network (WAN)**.

### Local Area Network (LAN)
- Covers a small area like a room or a building.
- Typically consist of broadcast link with many nodes sharing the same transmission medium.
- The two most prominent LAN technologies in use today are **Ethernet** (wired LAN) and **WLAN** (wireless LAN).

### Wide Area Network (WAN)
- Covers a large geographical area.
- Typically consist of nodes interconnected by point-to-point links.
- Each point-to-point link is a direct link.

## What is Internet?

So after seeing different types of networks, what is Internet?
- Basically an **interconnection of computer networks**, or packet-switching networks, or simply a **network of networks**.
- **Network core:** ISPs consisting of mesh of routers (packet-switches) and links.
- **Network edge:** access networks, e.g. mobile, home and enterprise networks connected to the first router in the Internet.

## TCP/IP Network Model

TCP/IP (Transmission Control Protocol/Internet Protocol) was originally standardized as a **4-layer architecture** in RFC1122 but has become a **5-layer architecture** implemented by the Internet.

OSI (Open System Interconnect) 7-layer architecture was designed by ISO (International Standard Organization) to be the Internet standard but has lost out to TCP/IP and may now be considered as historic.

Today, TCP/IP network model is the **de-facto standard** implemented by Internet although there exists another well-known OSI model which may be considered as historic now.

## TCP/IP Network Model – Layer Services

Specifically, the services provided by each layer of the **5-layer TCP/IP network model** are logically divided as follows:

| Layer | Communication Type | Role |
|---|---|---|
| **Application layer** | Application-to-Application | Concern with application requirement |
| **Transport layer** | Process-to-Process | Supports end to end connection establishment of data segments and delivery with error control |
| **Network layer** | Host-to-Host | Responsible for packet delivery from end to end |
| **Data link layer** | Node-to-Node | The role is to deliver packets from hop to hop |
| **Physical layer** | Node-to-Node (physical) | Actual transmissions between node-to-node. Anything that carries 1's and 0's between two nodes |

Since there are many processes in a host, many hosts on the network, and many nodes on a link, we need **addresses** at different layers to identify them:
- **Port numbers** – To identify a specific **process** running in a host computer
- **IP addresses** – To identify a specific **host** on the network
- **Link addresses** – To identify a specific **node** on the network

## OSI 7-Layer Model (for reference)

| Layer | Name | Examples |
|---|---|---|
| 7 | Application (End User Layer) | HTTP, FTP, SSH, DNS |
| 6 | Presentation (Syntax Layer) | MPEG, JPEG |
| 5 | Session (Synch and send to port) | APIs |
| 4 | Transport | TCP, UDP |
| 3 | Network | IP, ICMP, IPSec |
| 2 | Data Link | Ethernet, Switch, Bridge |
| 1 | Physical | Coax, twisted pair, fiber, wireless |

## TCP/IP Encapsulation Terminology

In practice, you may hear the following terms being used equivalently:
- **segment** = layer 4 PDU
- **packet** = layer 3 PDU
- **frame** = layer 2 PDU

PDU (Protocol Data Unit) is a generic term used by OSI model.

## Packet Switched Network

In practice, packet-switched network **divides** data into **smaller packets** before sending due to limit of data that can be carried by data link layer (called **MTU** - maximum transfer unit).

Note that since there is **no reservation of communication path**, different packets may take different path depending on the load of packet switches.

As a result, packets may arrive **out of sequence, or in error, or lost**! Hence, datagram network is said to provide **unreliable service** with **'best-effort' delivery**.

---

# LECTURE 2: LAN AND DATA LINK LAYER

## In This Lecture You Will Learn…

- Data link layer deals with node-to-node or hop-to-hop delivery of data.
- Traditionally, data link layer for LAN required a **MAC sublayer** to coordinate sharing of transmission medium.
- Specifically, we will look at the Ethernet LAN adopting **CSMA/CD** for MAC that has won the LAN 'war' and is now the only wired LAN implemented in practice.
- Services provided by data link layer: **Framing**, **Flow and error control** and **Addressing**.
- Modern Ethernet is mainly implemented using a **switch**, hence called switched LAN.
- Main functions of a switch: **Address self-learning** and **Frame forwarding**.

## MAC Sublayer for Wired LAN

As a result, the data link layer of LAN has an additional service to coordinate sharing of transmission medium which is achieved by the **MAC sublayer**.

Today, there are different LAN technologies standardized by IEEE for the MAC sublayer, but Ethernet which is implementing CSMA/CD has won the LAN 'war' and has become the standard for wired LAN.

The main function of the **Logical Link Control (LLC) layer** is to act as an interface between the lower MAC sublayer and the network layer within during the data transfer.

MAC Protocols:
- **Ethernet MAC** (IEEE 802.3 CSMA/CD)
- **Token ring MAC** (IEEE 802.5)
- **WiFi MAC** (IEEE 802.11 CSMA/CA)

## MAC for Ethernet

- Traditionally, nodes in a wired LAN were using the **same transmission medium** for communicating with each other.
- So, for Medium Access Control (MAC) in the traditional LAN, **CSMA/CD** (Carrier Sensing Multiple Access with Collision Detection), specifically **1-persistent CSMA/CD with Binary Exponential Backoff (BEB)** was implemented to avoid collisions.
- Note that MAC for wireless LAN is slightly different and will be covered in the later part of the course.

## 1-Persistent CSMA/CD with BEB

**What is the condition to detect a collision?**
- To be able to confirm a collision is due to its own transmission, a node must be still transmitting.
- As a result, there is a requirement for **minimum frame length** in CSMA/CD.
- Ethernet has the requirement for the frame length to be **minimum 64 bytes**.

**Key condition:**
> t_frame ≥ 2 × t_prop

This ensures the transmitting node is still sending when the collision signal propagates back to it.

## Binary Exponential Backoff (BEB)

After a collision:
- After the k-th collision, each station randomly picks an integer R in the range [0, 2^k − 1]
- Station waits R × t_prop time before retransmitting
- After 10 collisions, the range is frozen at [0, 1023]
- After 16 collisions, a failure is reported

## Addressing: MAC Address

The need for Ethernet or MAC address in the Ethernet frame is to identify individual node since Ethernet is designed for shared medium with many nodes.

Ethernet address is standardized to be **48-bit** consisting of 2 fields:
- First **24-bits OUI** is assigned by IEEE, and
- Remaining **24-bits** is assigned by the manufacturer

Ethernet address is also known as **physical address** because it is 'burnt' into the NIC (Network Interface Card) by the manufacturer.

Written as: `00:60:2F:3A:07:BC` or `00-60-2F-3A-07-BC`

## CSMA/CD for Switches?

With wide availability of inexpensive switches, it's becoming a standard to use a switch to directly connect hosts together, forming a LAN called **switched LAN**.

Is CSMA/CD with BEB required to be implemented for switched LAN?
- **No.** Because each host has a dedicated link to the switch, there is no shared medium. Therefore, there are no collisions and CSMA/CD is not required in a switched LAN.

## In Summary

- **How was traditional LAN implemented?** Bus, Ring and Star Topology.
- **Collisions and MAC sublayer:** Collisions occur because of shared transmission medium. Traditional LAN uses MAC sublayer. Example is CSMA/CD.
- **Ethernet Frame structure and Addressing mechanism**
- **What is the advantage of using switches?** No Collisions as dedicated links between switch and the nodes exist.
- **What are the functions of a switch?** Address self-learning and frame forwarding.

---

# LECTURE 3: SWITCHES AND ETHERNET

## In The Last Lecture…

- Traditional Ethernet topology that used bus, ring or star topology and deployed hubs and repeaters had many issues which were tackled using different protocols and algorithms.
- Specifically, we saw how CSMA/CD can be used to avoid collisions.
- We also saw why a minimum frame length is required in such case.
- However, by deploying **switches**, the above problems become obsolete.
- We saw the different operations of a switch. Specifically, we saw how the switch stores the MAC address of the devices connected to it and the ports they are connected to.
- We also saw how the **Ethernet frame** is designed to enable successful communication between two devices.

## Ethernet Frame Structure

An Ethernet frame consists of the following fields:
- **Preamble** (7 bytes): Pattern of alternating 1s and 0s used for synchronization
- **SFD – Start Frame Delimiter** (1 byte): Signals start of frame
- **Destination Address** (6 bytes): MAC address of destination
- **Source Address** (6 bytes): MAC address of source
- **Type/Length** (2 bytes): Indicates higher layer protocol (e.g., 0x0800 = IPv4)
- **Data** (46–1500 bytes): Payload data
- **FCS – Frame Check Sequence** (4 bytes): CRC error detection

Minimum frame size: **64 bytes** (required for CSMA/CD collision detection)
Maximum frame size: **1518 bytes**

## Switch Operations

### Address Self-Learning
- When a frame arrives, the switch records the **source MAC address** and the **port** it arrived on in the MAC address table (also called forwarding table or CAM table).
- Entries expire after a timeout if not refreshed.

### Frame Forwarding
A switch decides what to do with an incoming frame based on the destination MAC address:
1. **Known destination:** Forward the frame only to the port where the destination MAC address was learned.
2. **Unknown destination:** **Flood** the frame out all ports except the incoming port.
3. **Broadcast (FF:FF:FF:FF:FF:FF):** Flood to all ports except incoming port.

### Spanning Tree Protocol (STP)
- To avoid loops in a network with redundant switch paths, STP is used.
- STP selects a **Root Bridge** (switch with lowest Bridge ID/priority).
- Non-root switches select a **Root Port** (port with lowest cost path to root).
- For each network segment, a **Designated Port** is selected.
- All other ports are placed in **blocking state** to prevent loops.

---

# LECTURE 4: IPv4 ADDRESSING

## Network Layer

Theoretically, network layer may be implemented using circuit-switched or packet-switched which can be further subdivided into datagram or virtual-circuit networks.

Examples:
- **Circuit-Switched Networks:** Telephone Network
- **Datagram Networks:** IP Networks/Internet
- **Virtual-Circuit Networks:** Async. Transfer Mode (ATM) and frame relay

```
Switched Networks
├── Circuit-Switched
└── Packet Switched
    ├── Datagram Networks
    └── Virtual-circuit Networks
```

## IPv4 – Header

To support the required services, the IP header, specifically IPv4 (version 4) is designed as follows:

| Field | Length | Description |
|---|---|---|
| **Version** | 4 bits | IPv4 = 0100 |
| **HLEN (Header Length)** | 4 bits | Header length in multiples of 4 bytes; default is 0101 = 5 × 4 = 20 bytes |
| **Service** | 1 byte | Redefined for Differentiated Service (RFC2474) and Explicit Congestion Notification (ECN) (RFC3168) |
| **Total Length** | 2 bytes | Total length of IP datagram including header |
| **Identification** | 2 bytes | Unique ID for fragmentation |
| **Flags (DF, MF)** | 3 bits | Don't Fragment and More Fragments flags |
| **Fragment Offset** | 13 bits | Starting position of fragment in multiples of 8 |
| **Time to Live (TTL)** | 1 byte | Acts as a counter, decremented by one each time processed by a router; ensures datagram does not circulate the Internet forever |
| **Protocol** | 1 byte | Type of protocol the datagram is carrying. Example: 0x01 for ICMP, 0x06 for TCP, 0x11 for UDP |
| **Header Checksum** | 2 bytes | Error detection for header |
| **Source IP Address** | 4 bytes | Sender's IP address |
| **Destination IP Address** | 4 bytes | Receiver's IP address |
| **Option** | Varies | Rarely used; Many options have been deprecated (RFC6814) |

## IPv4 Address Format

- IPv4 address is **32 bits** (4 bytes)
- Written in dotted-decimal notation, e.g. `192.168.1.1`
- Divided into **Network ID** and **Host ID**

### Classful Addressing (Legacy)

| Class | First Bits | Network Bits | Host Bits | Range |
|---|---|---|---|---|
| A | 0 | 8 | 24 | 0.0.0.0 – 127.255.255.255 |
| B | 10 | 16 | 16 | 128.0.0.0 – 191.255.255.255 |
| C | 110 | 24 | 8 | 192.0.0.0 – 223.255.255.255 |
| D | 1110 | Multicast | — | 224.0.0.0 – 239.255.255.255 |
| E | 1111 | Reserved | — | 240.0.0.0 – 255.255.255.255 |

### Special IPv4 Addresses

- **Network Address:** Host ID all zeros (e.g., 192.168.1.0) – identifies the network itself
- **Broadcast Address:** Host ID all ones (e.g., 192.168.1.255) – sent to all hosts on network
- **Loopback:** 127.0.0.0/8 (commonly 127.0.0.1)
- **Private Addresses:** 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16

### CIDR (Classless Inter-Domain Routing)

- Replaces classful addressing
- Uses **prefix notation**: IP address / prefix length (e.g., `192.168.1.0/24`)
- Network mask indicates which bits belong to the network ID
- Allows more flexible allocation of address blocks

## IPv4 – Subnetting

Technically, subnetting is done by dividing the **host number or ID** (which the company has control) into **subnet number** and **host number**.

Extending the idea of network mask, **subnet mask** is introduced to indicate the length of network ID + subnet number.

> **Subnet mask = (Network mask + bits allocated to the Subnet ID)**

Therefore, for an example where 5 bits are allocated from the host ID as subnet ID, if the network mask is /16, the subnet mask is /21.

In each subnet:
- The **first** host ID cannot be used (network address)
- The **last** host ID cannot be used (broadcast address)
- The rest can be assigned to any host in the subnet

### VLSM (Variable Length Subnet Mask)

To further conserve IPv4 addresses, **VLSM** is introduced which allows subnet ID to be of **variable length** depending on needs.

### Number of Hosts per Subnet

| Subnet Mask | Hosts per Subnet |
|---|---|
| /24 | 254 |
| /25 | 126 |
| /26 | 62 |
| /27 | 30 |
| /28 | 14 |
| /29 | 6 |
| /30 | 2 |

Formula: **Number of hosts = 2^(host bits) – 2**

## Routing and Forwarding

### Routing Table
- Each router maintains a routing table with entries:
  - **Network Destination**
  - **Subnet Mask (Netmask)**
  - **Next Hop / Exit Interface**

### Longest Prefix Match
- When multiple routing table entries match a destination IP address, the router selects the entry with the **longest (most specific) prefix**.
- If no specific route matches, the **default route (0.0.0.0/0)** is used.

---

# LECTURE 5: IPv4 CONTINUED & IPv6

## IPv4 – Fragmentation and Reassembly

To support fragmentation and reassembly service, IP header is designed with **Identification**, **Flag** and **Fragmentation offset** fields.

| Field | Field Length | Description |
|---|---|---|
| **Identification** | 16 bits | Unique number to identify related fragments of an IP packet so that destination host can reassemble them together |
| **DF** | 1 bit | Don't Fragment flag. If set ('1') and packet > MTU, router will not fragment but discard the packet |
| **MF** | 1 bit | More Fragment flag. Last fragment is set to '0' and others are set to '1' |
| **Fragmentation offset** | 13 bits | Indicate the starting position of the fragment w.r.t. the original IP packet in multiples of 8 |

Due to the design of fragmentation offset field, **all fragments except the last must be a multiple of 8 bytes**.

Each fragmented datagram can be further fragmented into multiple fragments. If a fragment happens to traverse through another link with even smaller MTU, then it can be further fragmented.

Finally, the **destination host** will reassemble the fragments based on identification and offset field to recover the original IP datagram.

> **Note:** If any fragment is lost or corrupted, the whole packet will be discarded by destination host.

## Introduction to IPv6

### Why IPv6?
- IPv4 uses 32-bit addresses → approximately 4.3 billion addresses
- IPv6 uses **128-bit addresses** → vastly larger address space
- IPv6 was designed to solve IPv4 address exhaustion and other limitations

### IPv6 Packet Header
- The size of IPv4 header is **20 Bytes** whereas the size of the header of IPv6 is **40 Bytes**.
- IPv6 has a simplified, fixed-length header compared to IPv4.

## IPv6 Address Format

- IPv6 address is **128 bits** written as **8 groups of 16-bit hexadecimal** numbers separated by colons.
- Example: `2001:0DB8:AC10:FE01:0000:0000:0000:0000`

**Abbreviation rules:**
- Contiguous "0"s between ":" can be omitted **ONCE** using `::`
- Leading "0" within the groups can also be omitted.

Example:
```
2001:0DB8:0000:0100:0000:0000:0000:0030
→ 2001:DB8:0:100::30
```
But NOT `2001:DB8::100::30` (only "::" once, else no way of knowing how many "0"s in between!)

## Communication: IPv4 and IPv6

- Since IPv4 is still widely used, we need technologies to transform between IPv4 and IPv6. Also, there is no specific date to move to IPv6.
- Both IPv4 and IPv6 will **coexist** for now as the transition will take several years.
- The IETF has created various protocols and tools to help network administrators migrate their networks to IPv6.

### Migration Techniques

1. **Dual Stack** – Devices run both IPv4 and IPv6 simultaneously
2. **Tunnelling** – IPv6 packets are encapsulated within IPv4 packets (or vice versa) to travel across the other type of network
3. **Translation (NAT64)** – Network Address Translation between IPv4 and IPv6

### Tunnelling: IPv6 over IPv4 Tunnel (6to4)

6to4 tunnels (also called "manually configured tunnels") are the simplest way to tunnel IPv6 packets over IPv4. This transition mechanism is specified in **RFC 2473**, "Generic Packet Tunneling in IPv6 Specification".

**Packet structure through tunnel:**
```
[IPv4 Header | IPv6 Header | IPv6 Data]
```

### Tunnelling: IPv4 over IPv6 Tunnels (4in6)

The underlying transport is IPv6, not IPv4, and the tunneled packets are IPv4, not IPv6. 4in6 tunnels are specified in the same RFC as 6to4 tunnels (RFC 2437).

### Translation using NAT64

Network Address Translation 64 (NAT64) allows IPv6-enabled devices to communicate with IPv4-enabled devices using a translation technique similar to NAT for IPv4.
- An IPv6 packet is translated to an IPv4 packet and an IPv4 packet is translated to an IPv6 packet.

---

# LECTURE 6: CONTROL PLANE PROTOCOLS AND ARP

## What We Will Learn Today

- Categories of routing protocols:
  - Interior Gateway Protocol (IGP)
  - Exterior Gateway Protocol (EGP)
- Link state routing – Open Shortest Path First (OSPF)
- OSPF operation
- Internet Control Message Protocol (ICMP)
- Address Resolution Protocol (ARP)

## Routing Protocols Classification

```
Routing Protocols
├── IGP (Intradomain)
│   ├── Distance Vector → RIP
│   └── Link State → OSPF
└── EGP (Interdomain)
    └── Path Vector → BGP
```

- **IGP (Interior Gateway Protocol)** is designed to run inside a single autonomous system (AS). Different AS may run different IGP; e.g. RIP or OSPF. Another IGP is the proprietary EIGRP by Cisco.
- **EGP (Exterior Gateway Protocol)** is designed for use between different AS. To communicate, all AS must run the same EGP. The current standard is **BGP**.

## OSPF: Basic Concepts

- Uses **link state routing** approach to capture routes of entire network.
- Routers periodically test the quality of links directly connected and broadcast information to others using **flooding** approach.
- Quality of links may be broadcasted on:
  - Periodical timing
  - If changes occur that are significant
- Each router takes a snapshot of map of network, with costs of links.
- Each router uses **Dijkstra algorithm** to compute the shortest paths from its node to all other nodes.

### OSPF Three Phases
1. **Neighbor Discovery** – Routers discover neighbors using Hello messages
2. **Topology Exchange** – Routers flood Link State Advertisements (LSAs) to share topology info
3. **Route Calculation** – Each router runs Dijkstra's algorithm on its complete Link State Database (LSDB)

### LSA Processing
A router determines whether an LSA is newer by checking (in order):
1. **Sequence Number** – Higher sequence number = more recent → Accept
2. **Age** – Lower age = more recent; if age difference > MaxAgeDiff (15 minutes) → Accept newer
3. **Checksum** – Different checksums indicate different content

### Ensuring Topology Accuracy
1. **Periodic Refresh:** LSAs refreshed every 30 minutes
2. **Age Field:** Incremented during propagation and storage
3. **MaxAge Processing:** LSAs reaching MaxAge (1 hour) are purged
4. **Database Synchronization:** Periodic database description exchange

## Path Vector Routing (BGP)

- Each entry in routing table contains destination network, next router and the **path** to reach destination.
- Autonomous boundary routers are required to advertise its path routing vector to indicate the reachability of their networks.
- Each vector path received by the neighboring router is verified against its policies (can be set by administrator).
- If OK, it updates its table and forwards the path vector to the next router.

Example BGP routing table:

| Network | Next Router | Path |
|---|---|---|
| N01 | R01 | AS14, AS23, AS67 |
| N02 | R05 | AS22, AS67, AS05, AS89 |
| N03 | R06 | AS67, AS89, AS09, AS34 |
| N04 | R12 | AS62, AS02, AS09 |

## ICMP (Internet Control Message Protocol)

- ICMP messages are sent **over IP packets** which in turn are sent over data link layer such as Ethernet.
- Nevertheless, it is an integral part of IP and considered to be at the **network layer**.

### ICMP Message Format

```
+--------+--------+----------------+
|  Type  |  Code  |    Checksum    |
+--------+--------+----------------+
|           Rest of the header     |
+----------------------------------+
|             Data section         |
+----------------------------------+
```

### ICMP Request and Reply (Ping)

An example of ICMP query message is the **echo request** message (Type=0x08, Code=0x00) sent by a source host to query a router or destination host, which will respond with an **echo reply** message (Type=0x00, Code=0x00).

Fields include:
- Identifier (for matching reply)
- Sequence number (for matching reply)
- Data (optional)

### ICMP Traceroute

Traceroute works by sending a sequence of ICMP echo request messages with TTL set to 1, 2, … until the destination is reached. As each router decrements TTL to zero, it sends an ICMP **Time Exceeded** message back to the source, allowing traceroute to map the path.

## ARP (Address Resolution Protocol)

### Introduction to ARP

- **Address Resolution Protocol (ARP):** Connects logical names (IP addresses) to physical locations (MAC addresses) on a network.
- Analogy: Like a phonebook for network devices, finding physical addresses from names.
- Crucial for routing data packets to their correct destinations.

Before sending IP over Ethernet, ARP is developed for source host or routers to resolve target IP address to target MAC address.

### ARP Request
- ARP consists of an **ARP request** for a MAC address corresponding to a requested target IP address.
- **ARP request is broadcast** (sent to all nodes on the LAN: FF:FF:FF:FF:FF:FF).
- The request contains the sender's MAC and IP address, and the target IP address (target MAC = 00:00:00:00:00:00).

### ARP Reply
- The host or routers with the **matching** target IP address will then respond with an **ARP reply** with the corresponding MAC address.
- **ARP reply is unicast** (sent directly back to the requester).

### ARP Table (Cache)
- ARP results are cached in an **ARP table** to avoid repeated ARP requests.
- Entries expire after a timeout (typically 20 minutes).

## Summary: Control Plane Protocols and ARP

- Different categories of routing protocols
- **OSPF** interior gateway protocol – Link state routing protocol with three phases
- **BGP** exterior gateway protocol – Path Vector
- **ICMP** and its applications – error feedback at network layer
- **ARP** and its operations – translating IP addresses to MAC addresses

---

# LECTURE 8: TRANSPORT LAYER PART 1

## Agenda

1. The transport layer services
2. Socket Programming
3. UDP
4. TCP
   - Connection Management
   - Flow Control
   - Reliable Data Transfer
   - Congestion Control

## Internet Transport Layer Protocols

| Feature | TCP | UDP |
|---|---|---|
| Reliability | Reliable, in-order delivery | Unreliable data transfer |
| Flow Control | Yes | No |
| Congestion Control | Yes | No |
| Connection Setup | Connection-oriented (setup required) | Connectionless |
| Timing guarantee | No | No |
| Throughput guarantee | No | No |
| Security | No (by default) | No (by default) |

### TCP Properties:
1. Reliable transport between sending and receiving process
2. Flow control: sender won't overwhelm receiver
3. Congestion control: throttle sender when network overloaded
4. Does not provide: timing, minimum throughput guarantee, security
5. Connection-oriented: setup required between client and server processes

### UDP Properties:
1. Unreliable data transfer between sending and receiving process
2. Does not provide: reliability, flow control, congestion control, timing, throughput guarantee, security, or connection setup

> DNS is an example of an application-layer protocol that typically uses UDP.

## TCP – Further Reading

First and foremost, TCP provides **reliable data transfer**:
- Using flow control, sequence numbers, acknowledgments, and timers, TCP ensures that data is delivered from sending process to receiving process, correctly and in order. TCP thus converts IP's unreliable service between end systems into a reliable data transport service between processes.

TCP also provides **congestion control**:
- Congestion control is not so much a service provided to the invoking application as it is a service for the Internet as a whole. Loosely speaking, TCP congestion control prevents any one TCP connection from swamping the links and routers between communicating hosts with an excessive amount of traffic.
- TCP strives to give each connection traversing a congested link an **equal share of the link bandwidth**. This is done by regulating the rate at which the sending sides of TCP connections can send traffic into the network. UDP traffic, on the other hand, is unregulated.

## TCP Segment Structure

TCP segment consists of:
- **Source Port** and **Destination Port** (16 bits each)
- **Sequence Number** (32 bits)
- **Acknowledgment Number** (32 bits)
- **Header Length (HLEN)** – Length of header in words (i.e., 4 bytes each)
- **Control Flags:** R, S, F (Connection establishment commands); ACK, RST, SYN, FIN, URG, PSH
- **Window Size** (16 bits)
- **Internet Checksum** (as in UDP)
- **Urgent Pointer** (16 bits)
- **Options** (variable)
- **Data**

## TCP 3-Way Handshake

The idea: Both sender and receiver uses **"hesitate" attitude** during connection establishment to assure that both RFCs are acknowledged before declaring a connection as "open".

```
Client                          Server
LISTEN                          LISTEN
  |                               |
  |--- SYNbit=1, Seq=x ---------->| (choose init seq num, x; send TCP SYN msg)
SYNSENT                       SYN RCVD
  |                               |
  |<-- SYNbit=1, Seq=y ---------- | (choose init seq num, y; send TCP SYNACK)
  |    ACKbit=1; ACKnum=x+1       |
ESTAB                             |
  |                               |
  |--- ACKbit=1, ACKnum=y+1 ----->| (received SYNACK; send ACK; may contain data)
  |                           ESTAB
```

- **Step 1:** Client sends SYN (SYNbit=1, Seq=x)
- **Step 2:** Server responds with SYNACK (SYNbit=1, Seq=y, ACKbit=1, ACKnum=x+1)
- **Step 3:** Client sends ACK (ACKbit=1, ACKnum=y+1)

## TCP Flow Control

- Receiver controls sender so sender won't overflow receiver's buffer by transmitting too much, too fast.
- Receiver advertises **rwnd** (receiver window) in the TCP header.
- Sender limits amount of unacknowledged data to rwnd value.
- The receive window field in TCP header indicates the number of bytes the receiver is willing to accept.

## TCP Reliable Data Transfer

TCP creates reliable data transfer service on top of IP's unreliable service using:
- **Sequence numbers** – Number bytes in data stream
- **Acknowledgment numbers** – Cumulative ACK; ACK number = next expected byte
- **Timers** – Retransmit segment on timeout
- **Retransmission** – Retransmit lost or corrupted segments

### RTT Estimation and Timeout

**Exponentially Weighted Moving Average (EWMA):**
```
EstimatedRTT = α × EstimatedRTT + (1-α) × SampleRTT
```
TCP typically uses α = 0.875.

**Timeout Interval:**
```
TimeoutInterval = EstimatedRTT + 4 × DevRTT
```
where DevRTT tracks RTT deviation.

### Fast Retransmit

If sender receives **3 duplicate ACKs** for same data, it assumes segment is lost and retransmits immediately without waiting for timeout.

## TCP Congestion Control – Three Phases

**Slow Start Phase:**
- Starts with cwnd = 1 MSS
- Increment is **exponential** (doubles each RTT) until reaching ssthresh (slow start threshold)

**Congestion Avoidance Phase:**
- After reaching ssthresh, increment is **by 1 MSS per RTT** (linear growth)

**Congestion Detection Phase:**
- Sender goes back to Slow Start phase or Congestion Avoidance phase depending on type of loss:
  - **Timeout:** cwnd reset to 1 MSS; ssthresh = cwnd/2; return to Slow Start
  - **Triple duplicate ACK (Fast Retransmit):** ssthresh = cwnd/2; cwnd = ssthresh + 3 MSS; enter Congestion Avoidance

---

# LECTURE 9: TRANSPORT LAYER PART 2

## We Will Be Looking At

1. TCP connection management
2. TCP reliable data transfer
3. Flow Control
4. Congestion Control

## Go-Back-N vs Selective Repeat

### Stop-and-Wait
- Sender sends one packet, then waits for acknowledgment before sending the next.
- **Efficiency** = t_packet / (t_packet + 2 × t_prop) = 1 / (1 + 2a)
  where a = t_prop / t_packet

### Go-Back-N (GBN)
- Sender can have up to N unacknowledged packets in pipeline (window size = N)
- Receiver only accepts packets **in order**; discards out-of-order packets
- On error: retransmit ALL packets from the lost packet onward
- **Efficiency** = N × t_packet / (t_packet + 2 × t_prop) = N / (1 + 2a)

### Selective Repeat (SR)
- Sender can have up to N unacknowledged packets in pipeline
- Receiver **buffers** out-of-order packets
- On error: retransmit **only** the lost/corrupted packet
- **Efficiency** = N / (1 + 2a)

## TCP Congestion Control

**Question:** Look at the picture. Try to explain how TCP congestion control works.

### TCP Congestion Control Phases Summary

| Event | ssthresh | cwnd | State |
|---|---|---|---|
| Initialization | Set high | 1 MSS | Slow Start |
| Each ACK (Slow Start) | — | Double (×2 per RTT) | Slow Start |
| cwnd ≥ ssthresh | — | Linear (+1 per RTT) | Congestion Avoidance |
| Timeout | cwnd/2 | 1 MSS | Slow Start |
| 3 dup ACKs | cwnd/2 | ssthresh + 3 | Congestion Avoidance |

### Retransmission Timer

- The **Retransmission Timer** determines the maximum time to wait for an ACK before considering a packet lost.
- If the timer is set too short: unnecessary retransmissions, wasting bandwidth.
- If the timer is set too long: slow recovery from packet loss.

---

# LECTURE 10: WIRELESS NETWORKING

## Introduction to Wireless Networking

- A wireless network is a computer network that uses **wireless data connections** between network nodes.
- Wireless networking is a method by which homes, telecommunications networks and business installations avoid the costly process of introducing cables into a building, or as a connection between various equipment locations.
- Admin telecommunications networks are generally implemented and administered using **radio communication**. This implementation takes place at the **PHY layer** of the OSI model network structure.

## Open Systems Interconnection (OSI) – Recap

| Layer | Role | Examples |
|---|---|---|
| Application | End User Layer | HTTP, FTP, SSH, DNS |
| Presentation | Syntax Layer | MPEG, JPEG |
| Session | Synch and send to port | APIs |
| Transport | Segment | TCP, UDP |
| Network | Packet | IP, ICMP, IPSec |
| Data Link | Frames | Ethernet, Switch, Bridge |
| Physical | Physical medium | Coax, twisted pair, fiber, wireless |

## Wi-Fi Architecture

### WLAN Infrastructure Mode

- In infrastructure mode, WLAN network is composed of **stations** as well as one or more **access points (APs)**.
- The device Access Point is like base station used in cellular system. All the communications between stations will go through AP.
- Access point is like a router.
- Wi-Fi technology uses a multiple access technique called **Carrier-sense multiple access/collision avoidance (CSMA/CA)**.

## Wi-Fi Standards

### Wi-Fi 1 – 802.11b
- 802.11 — applies to wireless LANs and provides 1 or 2 Mbps transmission in the **2.4 GHz** band using either frequency hopping spread spectrum (FHSS) or direct sequence spread spectrum (DSSS).
- 802.11b (also referred to as 802.11 High Rate or Wi-Fi) — an extension to 802.11 that applies to wireless LANS and provides **11 Mbps** transmission (with a fallback to 5.5, 2 and 1-Mbps) in the 2.4 GHz band.
- 802.11b uses only DSSS. 802.11b was a 1999 ratification to the original 802.11 standard, allowing wireless functionality comparable to Ethernet.

### Wi-Fi 2 – 802.11a
- 802.11a — an extension to 802.11 that applies to wireless LANs and provides up to **54 Mbps** in the **5GHz** band.
- 802.11a uses an **orthogonal frequency division multiplexing (OFDM)** encoding scheme rather than FHSS or DSSS.

### Summary of IEEE 802.11 Standards

| Standard | Frequency | Max Speed | Notes |
|---|---|---|---|
| 802.11 (original) | 2.4 GHz | 1-2 Mbps | FHSS or DSSS |
| 802.11b | 2.4 GHz | 11 Mbps | DSSS only |
| 802.11a | 5 GHz | 54 Mbps | OFDM |
| 802.11g | 2.4 GHz | 54 Mbps | OFDM |
| 802.11n (Wi-Fi 4) | 2.4/5 GHz | 600 Mbps | MIMO |
| 802.11ac (Wi-Fi 5) | 5 GHz | Multi-Gbps | MU-MIMO |

## MAC for Wireless LAN (CSMA/CA)

Unlike wired Ethernet using CSMA/CD, wireless LAN uses **CSMA/CA (Collision Avoidance)** because:
- Wireless nodes cannot detect collisions while transmitting (half-duplex nature)
- Hidden terminal problem: node A and node C may not hear each other but both communicate with node B

CSMA/CA uses:
- **Carrier Sense:** Listen before transmitting
- **Random Backoff:** Wait random time if medium is busy
- **ACKs:** Receiver sends explicit ACK for each received frame
- **RTS/CTS (optional):** Request-to-Send / Clear-to-Send handshake to reserve medium

---

# LECTURE 11: LPWAN, IoT, AND MQTT

## Table of Contents

- Internet of Things (IoT)
- MQTT: An IoT Communications Protocol
- Low Power Wide Area Network (LPWAN)
- Technology Example: Wi-SUN
- Technology Example: Wi-Fi HaLow (802.11ah)
- Technology Example: NB-IoT
- Technology Example: LoRaWAN

## Objective

At the end of this lecture, students are expected to understand:
- The basic idea of IoT and related applications
- MQTT: a protocol enabling IoT communications
- The relationship between IoT and LPWAN
- Examples of wireless technologies applied to enable IoT applications

## Introduction to IoT Protocols

### Network Protocols
Provide methods of connecting IoT edge devices with other edge devices or the Internet:
- Wi-Fi
- Bluetooth
- 4G / 5G
- ZigBee
- …

### Data Protocols
Focus on information exchange:
- Constrained Application Protocol (CoAP)
- Advanced Message Queuing Protocol (AMQP)
- Message Queuing Telemetry Transport (MQTT)
- …

## Introduction to MQTT

- A lightweight messaging protocol designed for efficient and reliable communication between devices or applications in IoT and other resource-constrained environments.
- **Publish-Subscribe** model for bi-directional machine-to-machine communication.
- **Broker (Server)-based** architecture.
- Relies on **TCP** for data transmission (Variants can use UDP, e.g., MQTT-SN).
- TCP ports **8883** and **1883** are registered for MQTT TLS and non-TLS communication respectively.
- Three levels of **Quality of Service (QoS)**, i.e., QoS 0, 1, and 2.

## LPWAN (Low Power Wide Area Network)

LPWAN is a category of wireless communication technologies designed for:
- **Long range** communication
- **Low power** consumption
- **Low data rate** applications
- Specifically designed for IoT applications

## What is NB-IoT

- NB-IoT is an LPWAN radio technology standard developed by **3GPP** to enable a wide range of cellular devices and services.
- NB-IoT focuses on **indoor coverage**, **low cost**, **long battery life**, and **high connection density**.
- NB-IoT uses a subset of the LTE standard, but limits the bandwidth to a single **narrow-band of 200kHz**.

## 3GPP LPWAN Standards

- **LTE-M (Machine):** Another standard developed to address LPWAN radio technology to enable a wide range of cellular devices and services specifically for M2M and IoT applications.
- **NB-IoT:** Yet another developed LPWAN standard to further pronounce its usage models in indoor coverage, low cost, long battery life, and high connection density. NB-IoT uses a subset of the LTE standard, but limits the bandwidth to a single narrow-band of 200kHz.
- The advantage of LTE-M over NB-IoT is its comparatively **higher data rate, mobility, and voice** over the network, but it requires more bandwidth, is more costly, and cannot be put into guard band frequency band.

## What is 802.11ah (Wi-Fi HaLow)

- IEEE 802.11ah, a.k.a **Wi-Fi HaLow**, is a wireless networking protocol published in 2017.
- Targeted use cases: general IoT applications such as smart homes, surveillance systems, access control, industrial process control, logistics and asset management, smart cities, agriculture and environmental sensors.
- Operates in **900MHz** band (sub-GHz), providing longer range and better wall penetration than standard Wi-Fi.

## What is LoRa and LoRaWAN

- **Long Range (LoRa)** is a radio modulation technology for wireless LAN networks in the category of LPWA network technologies.
- **Long Range Wide Area Network (LoRaWAN)** is a network (protocol) using LoRa.
- Supports very **low power consumption** and **long-range** applications.
- Targeted use cases: smart agriculture, smart environmental monitoring.

### Comparison of LPWAN Technologies

| Technology | Range | Data Rate | Power | Frequency |
|---|---|---|---|---|
| NB-IoT | ~15 km | ~250 kbps | Low | Licensed (LTE band) |
| LTE-M | ~11 km | ~1 Mbps | Low-Medium | Licensed (LTE band) |
| LoRaWAN | ~15 km | ~50 kbps | Very Low | Unlicensed (Sub-GHz) |
| Wi-Fi HaLow | ~1 km | ~150 Mbps | Low | Unlicensed (900 MHz) |

---

# LECTURE 12: APPLICATION LAYER – DHCP AND DNS

## What We Will Learn Today

- Introduction to application layer protocols
- Two important application layer protocols:
  - **Dynamic Host Configuration Protocol (DHCP)**
  - **Domain Name System (DNS)**

## Introduction to Application Layer

- There are many network applications and application layer protocols in use today. The common ones are **HTTP** for WWW, **SMTP** for email, etc.
- With the benefits of layering, network applications only need to be concerned with application details and can simply call **socket APIs** to send/receive messages over the Internet.

## DHCP (Dynamic Host Configuration Protocol)

DHCP is used to automatically assign IP configuration parameters to hosts:
- IP address
- Subnet mask
- Default gateway
- DNS server address

### DHCP Message Format

DHCP message contains:
- **Operation Code** – Request or Reply
- **Hardware Type** – Type of hardware (e.g., Ethernet)
- **Hardware Address Length** – Length of MAC address
- **Hops** – Used by relay agents
- **Transaction Identifier** – Matches requests with replies
- **Seconds** – Time elapsed since client began process
- **Flags** – Includes **Broadcast Flag** (used to indicate whether DHCP client is able to receive unicast or broadcast DHCP Offer message)
- **Client IP Address (CIAddr)** – Client's current IP (if any)
- **"Your" IP Address (YIAddr)** – IP address offered by server
- **Server IP Address (SIAddr)** – DHCP server IP
- **Gateway IP Address (GIAddr)** – Relay agent IP
- **Client Hardware Address (CHAddr)** – Client's MAC address (16 bytes)
- **Server Name (SName)** – 64 bytes
- **Boot Filename** – 128 bytes
- **Options** – Variable size

The **broadcast flag** is used to indicate whether DHCP client is able to receive unicast or broadcast DHCP Offer message.

### DHCP Operation (DORA Process)

1. **DHCP Discover** – Client broadcasts to find DHCP server
2. **DHCP Offer** – Server responds with offered IP configuration
3. **DHCP Request** – Client requests the offered IP
4. **DHCP ACK** – Server confirms the assignment

## DNS (Domain Name System)

DNS is a distributed hierarchical naming system that translates human-readable domain names to IP addresses.

DNS is an example of an application-layer protocol that typically uses **UDP** (port 53).

### DNS Hierarchical Design

```
Root (.)
├── .com
│   ├── google.com
│   └── amazon.com
├── .edu
│   └── mit.edu
└── .sg
    └── singaporetech.edu.sg
```

### DNS Resolution Process

1. User types domain name in browser (e.g., www.example.com)
2. **Local DNS resolver** checks its cache first
3. If not cached, queries **Root DNS server** → returns address of TLD server
4. Queries **TLD DNS server** (e.g., .com) → returns address of authoritative server
5. Queries **Authoritative DNS server** → returns IP address
6. Local resolver returns IP to client and caches the result

### Types of DNS Records

| Record Type | Purpose |
|---|---|
| **A** | Maps hostname to IPv4 address |
| **AAAA** | Maps hostname to IPv6 address |
| **CNAME** | Canonical name (alias) |
| **MX** | Mail exchange server |
| **NS** | Name server for domain |
| **PTR** | Reverse DNS (IP to hostname) |

## Summary

- Introduction to the application layer
- How DHCP works
- DNS and its hierarchical design
- Resolve a domain name

---

# TUTORIAL 1: DATA LINK LAYER / MAC SUBLAYER – ETHERNET LAN

## Question 1: CSMA/CD Minimum Frame Size Analysis

**Given:**
- Bus network with stations A and B
- t_frame = 40 μs
- t_prop = 25 μs (propagation time between A and B)
- Station A starts sending at t = 0.0 μs

### Part (a): Can station B start transmitting at t = 23.0 μs?

**Answer:** No, the protocol does not allow station B to start transmitting at t = 23.0 μs.

**Explanation:**
- At t = 23.0 μs, station A's signal has not yet reached station B (since t_prop = 25 μs)
- Station B will sense the medium as idle and may attempt to transmit
- However, this violates the CSMA (Carrier Sense Multiple Access) principle
- **What will happen:** A collision will occur when A's signal reaches B at t = 25.0 μs, while B is already transmitting

### Part (b): Can stations A and B detect the collision?

**Answer:** No, neither station A nor station B will be able to detect the collision.

**Explanation:**
- For collision detection to work in CSMA/CD, the minimum frame transmission time must satisfy: **t_frame ≥ 2 × t_prop**
- In this scenario: t_frame = 40 μs, but 2 × t_prop = 2 × 25 = 50 μs
- Since 40 μs < 50 μs, the condition is not met
- Station A will finish transmitting at t = 40 μs, before the collision signal can propagate back to A (which would take 50 μs total)
- This is why Ethernet has a minimum frame size requirement to ensure collision detection works properly

---

## Question 2: Binary Exponential Backoff in CSMA/CD

**Given:**
- 1-persistent CSMA/CD
- t_prop = 12.5 μs
- t_frame = 120 μs
- Stations A and B start simultaneously, causing collision
- After collision: Station A generates R = 0, Station B generates R = 1

### Part (a): Do frames collide again during first retransmission?

**Answer:** No, the frames will not collide during the first retransmission.

**Explanation:**
- After collision detection, both stations enter backoff
- Station A chooses R = 0: waits for 0 × t_prop = 0 μs before retransmitting
- Station B chooses R = 1: waits for 1 × t_prop = 12.5 μs before retransmitting
- Station A starts retransmitting immediately after the backoff period
- Station B will sense A's transmission during its carrier sensing and will not transmit
- Therefore, no collision occurs

### Part (b): Can station B retransmit at time-slot R = 1?

**Answer:** No, station B cannot retransmit at time-slot R = 1.

**Explanation:**
- When station B's backoff timer expires (after 12.5 μs), it will perform carrier sensing
- At this point, station A is already transmitting (started at R = 0)
- Since the protocol is 1-persistent CSMA, station B will sense the busy medium
- Station B will wait until the medium becomes idle before attempting transmission
- Station B will successfully transmit after station A completes its frame transmission

---

## Question 3: Ethernet Switch Learning and Forwarding

**Scenario:** PC-A sends a frame to PC-B through switches S1 and S2 (initially empty MAC tables)

### Address Learning and Frame Forwarding Process:

**Step 1: PC-A sends frame to PC-B**
- Frame: Source MAC = PC-A, Destination MAC = PC-B

**Step 2: Frame arrives at Switch S1**
- S1 learns PC-A's MAC address on the incoming interface
- S1 doesn't know PC-B's location, so it floods the frame to all other interfaces

**Step 3: Frame arrives at Switch S2**
- S2 learns PC-A's MAC address from the incoming interface (connected to S1)
- S2 doesn't know PC-B's location, so it floods the frame to all other interfaces
- PC-B receives the frame

**Step 4: PC-B sends reply frame to PC-A**
- Frame: Source MAC = PC-B, Destination MAC = PC-A

**Step 5: Reply frame arrives at Switch S2**
- S2 learns PC-B's MAC address on the incoming interface
- S2 knows PC-A's location (learned in Step 3), so it forwards directly to S1

**Step 6: Reply frame arrives at Switch S1**
- S1 learns PC-B's MAC address from the incoming interface (connected to S2)
- S1 knows PC-A's location, so it forwards directly to PC-A

### Updated MAC Address Tables:

**S1:**
| Address | Interface |
|---|---|
| PC-A | Interface to PC-A |
| PC-B | Interface to S2 |

**S2:**
| Address | Interface |
|---|---|
| PC-A | Interface to S1 |
| PC-B | Interface to PC-B |

**Note:** The exact interface names would depend on the specific network diagram, but the principle shows how switches learn MAC addresses dynamically and build their forwarding tables through the learning process.

---

# TUTORIAL 2: SPANNING TREE PROTOCOL AND INTERNET PROTOCOL

## Question 1: Spanning Tree Protocol (STP) Analysis

**Given:** 5 switches with priorities indicated by SW followed by 4-bit numbers

### STP Algorithm Steps:

**Step 1: Root Bridge Election**
- The switch with the lowest priority becomes the root bridge
- Assuming the 4-bit numbers represent priorities, the switch with the smallest number becomes root
- **Root Bridge:** The switch with the lowest priority value

**Step 2: Root Port Selection**
- Each non-root switch selects one port as its root port
- Root port is the port with the lowest cost path to the root bridge
- In case of tie, use lowest port ID

**Step 3: Designated Port Selection**
- For each LAN segment, one port becomes the designated port
- Designated port is the port on the segment that has the lowest cost to root bridge
- All ports on the root bridge are designated ports

**Step 4: Blocking Ports**
- All remaining ports are placed in blocking state to prevent loops

**Note:** Without the specific network diagram showing switch connections and priorities, I cannot provide the exact port assignments. The general process would follow the above steps based on the actual topology and priority values.

---

## Question 2: VLSM (Variable Length Subnet Masking)

**Given:**
- Network block: 214.97.254.0/23
- Subnet requirements:
  - Subnet A: 250 hosts
  - Subnet B: 120 hosts
  - Subnet C: 50 hosts
  - Subnets D, E, F: Router interfaces (2 hosts each)

### Part (a): VLSM Subnet Allocation

**Available Address Space:**
- 214.97.254.0/23 provides 512 total addresses (2^9)
- Usable range: 214.97.254.0 to 214.97.255.255

**Subnet Calculations:**

**Subnet A (250 hosts):**
- Requires 256 addresses (2^8)
- Subnet mask: /24
- **Subnet A: 214.97.254.0/24**
- Range: 214.97.254.0 – 214.97.254.255

**Subnet B (120 hosts):**
- Requires 128 addresses (2^7)
- Subnet mask: /25
- **Subnet B: 214.97.255.0/25**
- Range: 214.97.255.0 – 214.97.255.127

**Subnet C (50 hosts):**
- Requires 64 addresses (2^6)
- Subnet mask: /26
- **Subnet C: 214.97.255.128/26**
- Range: 214.97.255.128 – 214.97.255.191

**Subnet D (Router interfaces):**
- Requires 4 addresses (2^2)
- Subnet mask: /30
- **Subnet D: 214.97.255.192/30**
- Range: 214.97.255.192 – 214.97.255.195

**Subnet E (Router interfaces):**
- Requires 4 addresses (2^2)
- Subnet mask: /30
- **Subnet E: 214.97.255.196/30**
- Range: 214.97.255.196 – 214.97.255.199

**Subnet F (Router interfaces):**
- Requires 4 addresses (2^2)
- Subnet mask: /30
- **Subnet F: 214.97.255.200/30**
- Range: 214.97.255.200 – 214.97.255.203

### Part (b): Router Interface IP Assignment

**Router R1:**
- Interface to Subnet A: 214.97.254.1/24
- Interface to Subnet D: 214.97.255.193/30
- Interface to Subnet E: 214.97.255.197/30

**Router R2:**
- Interface to Subnet B: 214.97.255.1/25
- Interface to Subnet D: 214.97.255.194/30
- Interface to Subnet F: 214.97.255.201/30

**Router R3:**
- Interface to Subnet C: 214.97.255.129/26
- Interface to Subnet E: 214.97.255.198/30
- Interface to Subnet F: 214.97.255.202/30

---

## Question 3: Routing Table Analysis

**Given Routing Table for R1:**

| Network Destination | Netmask | Exit Interface/Next-hop |
|---|---|---|
| 140.24.7.192 | 255.255.255.192 | G0/1 |
| 140.24.7.0 | 255.255.255.0 | G0/0 |
| 0.0.0.0 | 0.0.0.0 | G0/2 |

### Part (a): Destination 140.24.7.200

**Analysis:**
- Check against 140.24.7.192/26 (255.255.255.192):
  - 140.24.7.200 & 255.255.255.192 = 140.24.7.192 ✓ (Match)
- Check against 140.24.7.0/24 (255.255.255.0):
  - 140.24.7.200 & 255.255.255.0 = 140.24.7.0 ✓ (Match)

**Result:** Multiple matches found. Router uses **longest prefix match**.
- /26 is more specific than /24
- **Packet forwarded via G0/1**

### Part (b): Destination 140.24.8.200

**Analysis:**
- Check against 140.24.7.192/26: 140.24.8.200 & 255.255.255.192 = 140.24.8.192 ✗ (No match)
- Check against 140.24.7.0/24: 140.24.8.200 & 255.255.255.0 = 140.24.8.0 ✗ (No match)
- Check against 0.0.0.0/0 (default route): Always matches ✓

**Result:** No specific route matches.
- **Packet forwarded via G0/2 (default route)**

### Summary:
- **140.24.7.200** → Forwarded via **G0/1** (longest prefix match)
- **140.24.8.200** → Forwarded via **G0/2** (default route)

---

# TUTORIAL 3: NETWORK LAYER – CONTROL PLANE PROTOCOLS & ARP

## Question 1: Dijkstra's Algorithm Implementation

**Given Network Links and Costs:**
- R1 to R2: cost 5
- R1 to R3: cost 10
- R2 to R3: cost 2
- R2 to R4: cost 6
- R3 to R4: cost 4

### Network Diagram:
```
    R1
   /  \
  5    10
 /      \
R2------R3
|    2   |
6        4
|        |
   R4----
```

### Dijkstra's Algorithm from R1:

**Initialization:**
- Distance[R1] = 0 (source)
- Distance[R2] = ∞
- Distance[R3] = ∞
- Distance[R4] = ∞
- Unvisited = {R1, R2, R3, R4}

**Step 1:** Select R1 (distance = 0)
- Update neighbors:
  - Distance[R2] = min(∞, 0 + 5) = 5
  - Distance[R3] = min(∞, 0 + 10) = 10
- Visited = {R1}

**Step 2:** Select R2 (distance = 5)
- Update neighbors:
  - Distance[R3] = min(10, 5 + 2) = 7
  - Distance[R4] = min(∞, 5 + 6) = 11
- Visited = {R1, R2}

**Step 3:** Select R3 (distance = 7)
- Update neighbors:
  - Distance[R4] = min(11, 7 + 4) = 11 (no change)
- Visited = {R1, R2, R3}

**Step 4:** Select R4 (distance = 11)
- No unvisited neighbors
- Visited = {R1, R2, R3, R4}

### Final Shortest Paths from R1:
- **R1 to R2:** Distance = 5, Path = R1 → R2
- **R1 to R3:** Distance = 7, Path = R1 → R2 → R3
- **R1 to R4:** Distance = 11, Path = R1 → R2 → R4 (or R1 → R2 → R3 → R4)

---

## Question 2: ICMP Troubleshooting with Ping and Traceroute

### Step 1: Use Ping to Test Basic Connectivity
```bash
ping external-server.com
```

**Possible Ping Results and Interpretations:**

**Scenario A: Intermittent Packet Loss**
```
64 bytes from server: icmp_seq=1 time=45ms
Request timeout for icmp_seq=2
64 bytes from server: icmp_seq=3 time=47ms
Request timeout for icmp_seq=4
```
**Interpretation:** Network congestion or unstable link

**Scenario B: High Latency**
```
64 bytes from server: icmp_seq=1 time=250ms
64 bytes from server: icmp_seq=2 time=280ms
```
**Interpretation:** Network congestion or suboptimal routing

**Scenario C: Complete Failure**
```
Request timeout for icmp_seq=1
Request timeout for icmp_seq=2
```
**Interpretation:** Complete connectivity loss or firewall blocking

### Step 2: Use Traceroute to Identify Problem Location
```bash
traceroute external-server.com
```

**Scenario A: Timeout at Specific Hop**
```
1  gateway (192.168.1.1)  1.234 ms
2  isp-router (10.0.0.1)  15.234 ms
3  * * *
4  * * *
```
**Interpretation:** Problem at hop 3 (router failure or blocking)

**Scenario B: High Latency at Specific Hop**
```
1  gateway (192.168.1.1)  1.234 ms
2  isp-router (10.0.0.1)  15.234 ms
3  backbone-router (203.0.113.1)  250.234 ms
4  destination (198.51.100.1)  255.234 ms
```
**Interpretation:** Congestion or issues starting at hop 3

---

## Question 3: OSPF LSA Processing

### LSA (Link State Advertisement) Acceptance Process:

**Step 1: LSA Validation** – Verify LSA checksum, check LSA type and format, validate originating router ID

**Step 2: Database Lookup** – Search Link State Database (LSDB) for existing LSA from same originator

**Step 3: Freshness Determination** – Router uses the following criteria (in order):
- **A. Sequence Number Comparison:** Higher sequence number = more recent → If new LSA has higher sequence number → Accept
- **B. Age Comparison (if sequence numbers equal):** Lower age = more recent; if age difference > MaxAgeDiff (15 minutes) → Accept newer
- **C. Checksum Comparison (if sequence and age similar):** Different checksums indicate different content → Accept the LSA

**Step 4: Installation Decision**
- **Accept and Install:** If new LSA is more recent
- **Reject:** If existing LSA is more recent
- **Send Update:** If router has more recent version than received

**Step 5: Flooding Control** – Accepted LSAs are flooded to neighbors (except originating interface); Acknowledgment sent back to sender

---

## Question 4: OSPF vs BGP Comparison

| Criteria | OSPF (Open Shortest Path First) | BGP (Border Gateway Protocol) |
|---|---|---|
| **Type of protocol** | Interior Gateway Protocol (IGP) / Link State | Exterior Gateway Protocol (EGP) / Path Vector |
| **Routing Domain** | Within single Autonomous System (AS) | Between Autonomous Systems (Inter-AS) |
| **Scalability** | Limited to AS size (~100-200 routers optimal) | Highly scalable (handles entire Internet) |
| **Routing Metric** | Cost (bandwidth-based, configurable) | AS Path length, policies, attributes |
| **Algorithm** | Dijkstra's Shortest Path First (SPF) | Best Path Selection with policy rules |
| **Convergence Time** | Fast (seconds to minutes) | Slow (minutes to hours) |
| **Policy Support** | Limited (mainly through area design) | Extensive (route filtering, preference, manipulation) |
| **Use Cases** | Enterprise networks, ISP internal routing | Internet backbone, ISP peering, multi-homing |

### Key Similarities:
- Both are standardized protocols (OSPF: RFC 2328, BGP: RFC 4271)
- Both maintain routing tables and make forwarding decisions
- Both support authentication mechanisms
- Both use TCP for reliable message transport (BGP directly, OSPF for some functions)

### Key Differences:
- **Scope:** OSPF for internal AS routing, BGP for inter-AS routing
- **Objectives:** OSPF optimizes for shortest path, BGP optimizes for policy compliance
- **State Information:** OSPF maintains complete topology, BGP maintains only best paths
- **Update Triggers:** OSPF floods all changes, BGP sends incremental updates

---

## Question 5: OSPF Simulator Analysis

**Note:** This question requires using the OSPF simulator from the LMS. The following provides the theoretical framework for analysis:

### Part (a): LSDB Convergence
1. Each node generates LSAs for its directly connected links
2. LSAs are flooded throughout the network
3. Each node builds identical LSDB containing all network links
4. LSDB convergence achieved when all nodes have same link state information

### Part (b): Dijkstra's Algorithm from Node A and D
- **From Node A:** Node A calculates shortest paths to all other nodes; builds shortest path tree with A as root
- **From Node D:** Node D calculates shortest paths from its perspective; may result in different next-hop choices for same destinations
- **Expected Differences:** Different next-hop interfaces due to different source perspectives

### Part (c): Link Failure (c-d link disabled)
- LSAs generated to reflect link failure
- Network topology updated in all LSDBs
- Shortest path calculations recomputed
- Alternative paths through remaining links established
- **Observation:** Routing paths will change to avoid failed link

### Part (d): Node Failure (Node C disabled)
- All links connected to Node C become unavailable
- More significant topology change than single link failure
- Nodes A and D recalculate paths avoiding Node C entirely
- **Observation:** May result in longer paths or network partitioning if C was critical for connectivity

---

# TUTORIAL 4: TRANSPORT LAYER 1

## Question 1: TCP Three-Way Handshake Calculation

**Given Scenario:**
- Host A: Initial sequence number = 150, sends SYN
- Host B: Initial sequence number = 500, sends SYN-ACK with ACK = 151

### Part (a): Host A's Final ACK Packet

**Answer:**
- **Sequence Number:** 151
- **Acknowledgment Number:** 501

**Explanation:**
- **Sequence Number = 151:** This is Host A's next sequence number after sending the initial SYN (150 + 1)
- **Acknowledgment Number = 501:** This acknowledges Host B's SYN by setting ACK to B's initial sequence number + 1 (500 + 1)

**Complete Three-Way Handshake:**
1. **A → B:** SYN, Seq=150
2. **B → A:** SYN-ACK, Seq=500, ACK=151
3. **A → B:** ACK, Seq=151, ACK=501

### Part (b): How Three-Way Handshake Ensures Connection Agreement

**1. Sequence Number Synchronization:**
- Both hosts exchange their initial sequence numbers
- Each host acknowledges the other's initial sequence number
- This establishes the starting point for data transmission

**2. Bidirectional Communication Verification:**
- Host A proves it can send to Host B (Step 1)
- Host B proves it can receive from A and send back to A (Step 2)
- Host A proves it can receive from B (Step 3)
- This confirms the communication path works in both directions

**3. Connection State Agreement:**
- After successful handshake, both hosts transition to ESTABLISHED state
- Both sides agree on connection parameters (sequence numbers, window sizes)
- Both parties confirm readiness to exchange data

**4. Duplicate Connection Prevention:**
- Sequence numbers help identify and reject old duplicate connection requests
- Each new connection uses different initial sequence numbers

---

## Question 2: TCP Cumulative Acknowledgment and Lost Segment

**Given Scenario:**
- Segment 1: 200 bytes, sequence 100-299 (LOST)
- Segment 2: 200 bytes, sequence 300-499 (RECEIVED)

### Part (a): Acknowledgment Number from Host B

**Answer:** Host B should send ACK = 100

**Explanation:**
- TCP uses cumulative acknowledgment
- ACK number indicates the next expected sequence number
- Since Segment 1 (bytes 100-299) was lost, Host B cannot acknowledge beyond byte 99
- Even though Segment 2 was received, Host B cannot acknowledge it due to the gap
- **ACK = 100** means "I expect the next byte starting from sequence 100"

### Part (b): How Cumulative Acknowledgment Helps Detect Loss

**1. Gap Detection:**
- When Host A receives ACK = 100 repeatedly, it indicates bytes 100-299 are missing

**2. Duplicate ACK Generation:**
- Host B will continue sending ACK = 100 for any subsequent segments received

**3. Fast Retransmit Trigger:**
- After receiving 3 duplicate ACKs (total of 4 ACKs with same number), Host A triggers fast retransmit
- This allows quick recovery without waiting for timeout

**4. Retransmission Process:**
- Host A retransmits Segment 1 (bytes 100-299)
- Once Host B receives Segment 1, it can acknowledge all received data

---

## Question 3: TCP Flow Control Problem

**Given Scenario:**
- Receiver's advertised window size = 500 bytes
- Host A needs to send 800 bytes

### Part (a): TCP Flow Control Handling

**Flow Control Mechanism:**

**1. Initial Window Check:**
- Host A checks receiver's advertised window (500 bytes)
- Since 800 bytes > 500 bytes, Host A cannot send all data at once

**2. Data Segmentation:**
- Host A will send maximum of 500 bytes initially
- Remaining 300 bytes must wait for window space

**3. Transmission Process:**
```
Step 1: A sends 500 bytes (fills receiver's window)
Step 2: B processes some data, advertises new window size
Step 3: A sends remaining data based on available window space
```

**Example Sequence:**
1. **A → B:** 500 bytes (Seq=1000-1499)
2. **B → A:** ACK=1500, Window=200 (processed 300 bytes)
3. **A → B:** 200 bytes (Seq=1500-1699)
4. **B → A:** ACK=1700, Window=400 (processed more data)
5. **A → B:** 100 bytes (Seq=1700-1799, remaining data)

### Part (b): Issues if Sender Ignores Advertised Window

**1. Buffer Overflow:** Receiver's buffer becomes full → Data loss and segment drops

**2. Performance Degradation:** Dropped segments trigger retransmissions → Reduced effective throughput

**3. Receiver Overload:** Receiver cannot process data fast enough → System instability

**4. Congestion Creation:** Excessive data in network queues → Network-wide performance issues

**5. Connection Instability:** Frequent retransmissions due to drops → Unreliable data transfer

**6. Unfair Resource Usage:** Other connections suffer from reduced bandwidth

---

## Question 4: Designing Reliability over UDP

### Part (a): Simple Reliability Protocol Design

**Protocol Components:**

**1. Packet Loss Detection:**
- Sequence Numbers: Add unique sequence number to each packet
- Acknowledgments: Receiver sends ACK for each received packet
- Timeouts: Sender starts timer for each sent packet
- If ACK not received within timeout → packet assumed lost

**2. Packet Ordering:**
- Sequence Numbers: Use incremental sequence numbers
- Receiver Buffer: Maintain buffer to store out-of-order packets
- In-Order Delivery: Deliver packets to application in sequence order

**3. Retransmission Mechanism:**
- Sender maintains list of unacknowledged packets
- Timeout Event: Retransmit unacknowledged packets

**Protocol Header Format:**
```
+--+--+--+--+--+--+--+--+
|  Seq Number (32 bits)   |
+--+--+--+--+--+--+--+--+
|Type|       Checksum     |
+--+--+--+--+--+--+--+--+
|        Data...          |
```

### Part (b): Comparison with TCP

| Aspect | Custom UDP Protocol | TCP |
|---|---|---|
| **Connection Setup** | Connectionless (no handshake) | Connection-oriented (3-way handshake) |
| **Overhead** | Lower (minimal headers) | Higher (larger headers, connection state) |
| **Latency** | Lower (no connection setup) | Higher (connection establishment delay) |
| **Flow Control** | None (unless added) | Built-in window-based flow control |
| **Congestion Control** | None (unless added) | Built-in AIMD-based |

---

# TUTORIAL 5: TRANSPORT LAYER 2

## Question 1: Efficiency Calculation for Go-Back-N Scenario

**Given Parameters:**
- Distance: 3000 km = 3 × 10⁶ m
- Propagation speed: 2.5 × 10⁸ m/sec
- Window size: 20 packets
- Packet size: 1000 bytes
- Bandwidth: 100 Mbps = 100 × 10⁶ bps

### Preliminary Calculations:

**Propagation Delay (t_prop):**
```
t_prop = Distance / Propagation Speed
t_prop = (3 × 10⁶ m) / (2.5 × 10⁸ m/sec)
t_prop = 0.012 seconds = 12 ms
```

**Transmission Time per Packet (t_trans):**
```
t_trans = Packet Size / Bandwidth
t_trans = (1000 bytes × 8 bits/byte) / (100 × 10⁶ bps)
t_trans = 8000 / (100 × 10⁶) = 0.00008 seconds = 0.08 ms
```

**Round Trip Time (RTT):**
```
RTT = 2 × t_prop = 2 × 12 ms = 24 ms
```

### Part (a): Compute the Efficiency

**Go-Back-N Efficiency Formula:**
```
Efficiency = min(1, N × t_trans / RTT)
where N = window size
```

**Calculation:**
```
Efficiency = min(1, 20 × 0.08 ms / 24 ms)
Efficiency = min(1, 1.6 / 24)
Efficiency = min(1, 0.0667)
Efficiency = 0.0667 = 6.67%
```

**Answer:** The efficiency of the Go-Back-N protocol is **6.67%**

### Part (b): Minimum Window Size for Maximum Efficiency

**For maximum efficiency (100%), we need:**
```
N × t_trans ≥ RTT
N ≥ RTT / t_trans
N ≥ 24 ms / 0.08 ms
N ≥ 300 packets
```

**Answer:** The minimum window size needed to achieve maximum efficiency is **300 packets**

**Explanation:** With a window size of 300 packets, the sender can continuously transmit without waiting for acknowledgments, fully utilizing the available bandwidth.

---

## Question 2: Handling Packet Loss in Go-Back-N

**Scenario:** Sender transmits packets 1-10, packet 4 is lost, packets 5-10 received but discarded

### Step-by-Step Process:

**Step 1: Initial Transmission**
- Sender transmits packets 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
- Network: Packet 4 is lost during transmission
- Receiver receives packets 1, 2, 3, [4 missing], 5, 6, 7, 8, 9, 10

**Step 2: Receiver Processing**
- Packet 1: Received in order → Send ACK 1, deliver to application
- Packet 2: Received in order → Send ACK 2, deliver to application
- Packet 3: Received in order → Send ACK 3, deliver to application
- Packet 5: Out of order (expecting 4) → Discard, Send ACK 3 (duplicate)
- Packet 6: Out of order → Discard, Send ACK 3 (duplicate)
- Packets 7-10: Out of order → Discard, Send ACK 3 (duplicate)

**Step 3: Sender ACK Processing**
- Sender receives: ACK 1, ACK 2, ACK 3, ACK 3, ACK 3, ACK 3, ACK 3, ACK 3, ACK 3
- Multiple ACK 3: Indicates packet 4 was lost

**Step 4: Timeout and Retransmission**
- Sender's timer for packet 4 expires
- Sender retransmits ALL unacknowledged packets: 4, 5, 6, 7, 8, 9, 10
- This is the "Go-Back-N" behavior – go back to packet 4 and retransmit all subsequent packets

**Step 5: Successful Retransmission**
- Packet 4: Now received in order → Send ACK 4, deliver to application
- Packets 5-10: Now in order → Delivered sequentially

### Key Go-Back-N Characteristics:

**1. Cumulative Acknowledgment:** ACK n means "all packets up to n received correctly"

**2. Receiver Simplicity:** Only accepts packets in order; Discards out-of-order packets

**3. Sender Complexity:** Maintains window of unacknowledged packets; Retransmits from first unacknowledged packet

**4. Inefficiency:** Correctly received packets (5-10) are retransmitted unnecessarily; Bandwidth waste, especially with large windows

---

## Question 3: RTT Estimation and Retransmission Timer

**Given:**
- Previous RTT estimate: 100 ms
- New RTT measurement: 120 ms
- Smoothing factor (α): 0.8

### RTT Estimation Calculation:

**TCP RTT Estimation Formula:**
```
EstimatedRTT = α × EstimatedRTT + (1-α) × SampleRTT
```

**Calculation:**
```
New EstimatedRTT = 0.8 × 100 ms + (1-0.8) × 120 ms
New EstimatedRTT = 0.8 × 100 + 0.2 × 120
New EstimatedRTT = 80 + 24 = 104 ms
```

**Answer:** The new RTT estimate is **104 ms**

### Importance of Smoothing Factor:

**1. Noise Reduction:** Smoothing averages out temporary fluctuations in measurements

**2. Stability:** Prevents retransmission timer from changing too rapidly; Avoids premature timeouts

**3. Adaptation Balance:**
- High α (closer to 1): More weight to historical data, slower adaptation
- Low α (closer to 0): More weight to recent measurements, faster adaptation
- TCP typically uses α = 0.875 for good balance

**4. Performance Impact:**
- **Too responsive (low α):** Timer fluctuates wildly, unnecessary retransmissions
- **Too conservative (high α):** Slow adaptation to changing network conditions

**Additional RTT Components:**
```
TimeoutInterval = EstimatedRTT + 4 × DevRTT
```
where DevRTT tracks RTT deviation for better timeout estimation.

---

## Question 4: TCP Congestion Control – Slow Start and Loss Reaction

**Given:**
- Initial cwnd: 1 MSS
- Slow start phase: cwnd doubles each RTT
- After 4 RTTs: packet loss detected via three duplicate ACKs

### Part (a): Congestion Window after 4 RTTs

**Slow Start Growth:**
- RTT 0: cwnd = 1 MSS (initial)
- RTT 1: cwnd = 2 MSS (1 × 2)
- RTT 2: cwnd = 4 MSS (2 × 2)
- RTT 3: cwnd = 8 MSS (4 × 2)
- RTT 4: cwnd = 16 MSS (8 × 2)

**Answer:** After 4 RTTs, cwnd = **16 MSS**

### Part (b): TCP Response to Three Duplicate ACKs

**Fast Recovery Algorithm Response:**

**1. Set ssthresh (Slow Start Threshold):**
```
ssthresh = max(cwnd/2, 2 MSS)
ssthresh = max(16/2, 2) = max(8, 2) = 8 MSS
```

**2. Set cwnd for Fast Recovery:**
```
cwnd = ssthresh + 3 MSS (for the 3 duplicate ACKs)
cwnd = 8 + 3 = 11 MSS
```

**3. Retransmit Lost Packet:**
- Immediately retransmit the packet indicated by duplicate ACKs
- Don't wait for timeout (this is "fast retransmit")

### Part (c): Phase After Loss Recovery

**Connection enters Fast Recovery Phase:**
- For each additional duplicate ACK: cwnd += 1 MSS
- When new ACK arrives: cwnd = ssthresh = 8 MSS → Enter Congestion Avoidance phase

**Subsequent Phase: Congestion Avoidance**
- cwnd increases linearly: cwnd += MSS²/cwnd per ACK
- Approximately 1 MSS increase per RTT

**State Transition Summary:**
1. Slow Start (cwnd: 1→16 MSS)
2. Packet Loss Detection (3 duplicate ACKs)
3. Fast Recovery (cwnd: 11 MSS, retransmit lost packet)
4. Congestion Avoidance (cwnd: 8 MSS, linear growth)

**Key Differences from Timeout:**
- **Timeout Loss:** cwnd reset to 1 MSS, return to slow start
- **Duplicate ACK Loss:** cwnd reduced by half, enter congestion avoidance
- Fast recovery maintains higher throughput than timeout recovery

---

## Question 5: TCP Congestion Control Simulator

**Simulation Parameters:**
- Negotiated Maximum Window Size: 64 segments
- Number of Cycles (RTTs): 50
- Events:
  - Cycle 20: Duplicate ACK event
  - Cycle 30: Timeout event

### Expected Simulation Behavior:

**Phase 1: Cycles 1-20 (Before Duplicate ACK)**
- Slow Start Phase: cwnd grows exponentially: 1, 2, 4, 8, 16, 32, 64
- May hit maximum window size limit
- If ssthresh reached, switches to congestion avoidance

**Phase 2: Cycle 20 (Duplicate ACK Event)**
- Fast Recovery Response: ssthresh = cwnd/2
- cwnd reduced but not to 1 (maintains some throughput)
- Enter congestion avoidance phase

**Phase 3: Cycles 21-30 (Recovery Period)**
- Congestion Avoidance: Linear growth: cwnd increases by ~1 MSS per RTT

**Phase 4: Cycle 30 (Timeout Event)**
- Timeout Response (more severe): cwnd reset to 1 MSS
- ssthresh = previous cwnd/2; Return to slow start phase

**Phase 5: Cycles 31-50 (Final Recovery)**
- Slow Start Resume: Exponential growth from cwnd = 1
- Growth until reaching ssthresh, then linear growth

### Impact Analysis:

**Impact of Duplicate ACK:**
- Moderate window reduction (fast recovery)
- Maintains network utilization better than timeout
- Indicates partial network congestion

**Impact of Timeout:**
- Severe window reduction (back to 1 MSS)
- Complete restart of congestion control
- Indicates serious network congestion or loss

**Overall Pattern:**
- Demonstrates TCP's adaptive nature
- Shows different responses to different loss indicators
- Illustrates trade-off between throughput and network stability

**Expected Graph Characteristics:**
- Exponential curves during slow start phases
- Sharp drops at congestion events
- Linear recovery slopes during congestion avoidance
- Timeout causing more dramatic impact than duplicate ACKs

---

*End of INF1006 Computer Networks Notes*
*Singapore Institute of Technology | 2024-2025 Trimester 3*
