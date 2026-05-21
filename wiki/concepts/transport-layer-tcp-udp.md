---
type: concept
title: "Transport Layer — TCP & UDP"
domain: computer-networks
complexity: high
status: established
created: 2026-05-22
updated: 2026-05-22
address: c-000037
tags: [tcp, udp, transport-layer, congestion-control, flow-control, reliable-transfer, handshake, go-back-n, selective-repeat, INF1006]
---

# Transport Layer — TCP & UDP

The transport layer (Layer 4) provides **process-to-process communication** between applications running on different hosts. TCP offers reliable, ordered delivery with flow and congestion control. UDP offers lightweight, connectionless, best-effort delivery.

---

## TCP vs UDP — Comparison

| Feature | TCP | UDP |
|---|---|---|
| Reliability | Reliable, in-order delivery | Unreliable (best-effort) |
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Flow Control | Yes (receiver window `rwnd`) | No |
| Congestion Control | Yes (`cwnd`-based) | No |
| Overhead | Higher (20-byte header) | Lower (8-byte header) |
| Timing guarantee | No | No |
| Throughput guarantee | No | No |
| Typical use | HTTP, HTTPS, SMTP, FTP, SSH | DNS, DHCP, VoIP, video streaming, gaming |

---

## TCP Segment Structure

| Field | Size | Description |
|---|---|---|
| **Source Port** | 16 bits | Sending process |
| **Destination Port** | 16 bits | Receiving process |
| **Sequence Number** | 32 bits | Byte offset of first byte in this segment |
| **Acknowledgement Number** | 32 bits | Next byte the receiver expects (cumulative ACK) |
| **Header Length (HLEN)** | 4 bits | Header size in 4-byte words |
| **Control Flags** | 6 bits | URG, ACK, PSH, RST, **SYN**, **FIN** |
| **Window Size** | 16 bits | Receiver buffer space available (`rwnd`) |
| **Checksum** | 16 bits | Error detection over header + data |
| **Urgent Pointer** | 16 bits | Offset to urgent data (if URG set) |
| **Options** | Variable | e.g., MSS negotiation, timestamps |

---

## TCP 3-Way Handshake

Both endpoints exchange sequence numbers and confirm readiness before data transfer begins.

```
Client                           Server
  |                                |
  |--- SYN (Seq=x) -------------->|   Step 1: Client initiates
  |                                |
  |<-- SYNACK (Seq=y, ACK=x+1) ---|   Step 2: Server acknowledges + picks its own seq
  |                                |
  |--- ACK (ACK=y+1) ------------>|   Step 3: Client acknowledges
  |                            ESTABLISHED
```

- **SYN** — Synchronise sequence numbers.
- **SYNACK** — Server acknowledges client's SYN and sends its own SYN.
- **ACK** — Client acknowledges server's SYN. Connection is now open.

---

## TCP Reliable Data Transfer

TCP converts IP's unreliable service into reliable delivery using:

| Mechanism | How It Works |
|---|---|
| **Sequence numbers** | Each byte in the stream is numbered; segments carry the seq number of the first byte |
| **Cumulative ACKs** | ACK number = next byte the receiver expects; acknowledges all bytes up to that point |
| **Retransmission timer** | If no ACK received before timer expires, the unacknowledged segment is retransmitted |
| **Fast Retransmit** | If the sender receives **3 duplicate ACKs** for the same data, it retransmits immediately without waiting for timeout |

### RTT Estimation

TCP estimates round-trip time using an **Exponentially Weighted Moving Average (EWMA)**:

```
EstimatedRTT = α × EstimatedRTT + (1 − α) × SampleRTT
```
TCP uses α = **0.875** (smoothing factor giving more weight to history than to the new sample).

**Timeout Interval:**
```
TimeoutInterval = EstimatedRTT + 4 × DevRTT
```
where `DevRTT` tracks RTT variation (safety margin).

---

## TCP Flow Control

- The **receiver** advertises its available buffer space in the **window size (rwnd)** field of every ACK.
- The **sender** limits the total amount of unacknowledged data in flight to ≤ `rwnd`.
- This prevents the sender from overwhelming a slow receiver's buffer.

---

## TCP Congestion Control

Congestion control prevents any single TCP connection from flooding the network. The sender maintains a **congestion window (cwnd)**.

Effective send rate ≈ min(cwnd, rwnd) / RTT.

### Three Phases

| Phase | Trigger | `cwnd` Behaviour | `ssthresh` change |
|---|---|---|---|
| **Slow Start** | Start / after timeout | Doubles each RTT (exponential growth) | — |
| **Congestion Avoidance** | `cwnd ≥ ssthresh` | Increases by 1 MSS per RTT (linear) | — |
| **Congestion Detection (timeout)** | Packet loss via timeout | Reset to 1 MSS | Set to `cwnd / 2` |
| **Congestion Detection (3 dup ACKs)** | Fast Retransmit | Set to `ssthresh + 3` | Set to `cwnd / 2` |

> **Timeout** indicates severe congestion → return to Slow Start.
> **3 duplicate ACKs** indicates moderate loss (some packets still arriving) → stay in Congestion Avoidance (TCP Reno behaviour).

---

## Sliding Window Protocols

Before examining TCP in isolation, these three protocols explain the general principle of pipelined reliable transfer:

### Stop-and-Wait

- Send one packet; wait for ACK before sending the next.
- Efficiency = 1 / (1 + 2a), where a = t_prop / t_packet.
- Very inefficient on high-bandwidth, high-latency links.

### Go-Back-N (GBN)

- Sender may have up to **N** unacknowledged packets in the pipeline (window size = N).
- Receiver accepts only **in-order** packets; discards out-of-order packets.
- On loss: retransmits **all** packets from the lost one onward.
- Efficiency = N / (1 + 2a).

### Selective Repeat (SR)

- Same window size N as GBN.
- Receiver **buffers** out-of-order packets.
- On loss: retransmits **only** the lost packet.
- Efficiency = N / (1 + 2a) — same formula as GBN but achieved with fewer retransmissions.

TCP uses a hybrid approach closer to Selective Repeat (cumulative ACKs + fast retransmit + selective ACKs via SACK option).

---

## Key Connections

- [[concepts/tcp-ip-network-model]] — Transport layer sits above the network layer; port numbers + IP address form a socket
- [[concepts/ip-addressing]] — TCP segments travel inside IP packets; the IP header carries source/destination addresses
- [[concepts/network-layer-protocols]] — IP's unreliable datagram service is what TCP compensates for with sequence numbers and ACKs
- [[concepts/application-layer-dhcp-dns]] — DNS uses UDP (low overhead, short messages); DHCP uses UDP (broadcast before IP is configured)
- [[concepts/os-processes-and-threads]] — Sockets are the OS interface connecting application processes to transport-layer endpoints
