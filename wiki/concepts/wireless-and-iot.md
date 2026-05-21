---
type: concept
title: "Wireless Networking & IoT"
domain: computer-networks
complexity: medium
status: established
created: 2026-05-22
updated: 2026-05-22
address: c-000038
tags: [wifi, csma-ca, 802.11, lpwan, iot, mqtt, nb-iot, lorawan, wireless, INF1006]
---

# Wireless Networking & IoT

Wireless networking replaces physical cables with radio communication. Wi-Fi (IEEE 802.11) dominates the WLAN space; LPWAN technologies serve low-power, long-range IoT deployments. MQTT provides a lightweight messaging protocol binding IoT devices together.

---

## Wi-Fi Architecture

### Infrastructure Mode

The standard deployment model for enterprise and home Wi-Fi:
- The network consists of **stations** (client devices) and one or more **Access Points (APs)**.
- All station-to-station communication passes **through the AP** — the AP acts as a Layer 2 bridge and Layer 3 router gateway.
- APs connect to the wired backbone (typically via Ethernet).

---

## CSMA/CA — Why Not CSMA/CD?

Wired Ethernet uses CSMA/CD (Collision Detection). Wireless LANs use **CSMA/CA (Collision Avoidance)** instead, for two reasons:

1. **Half-duplex nature:** A wireless node cannot simultaneously transmit and listen for collisions — its own signal drowns out any incoming signal.
2. **Hidden terminal problem:** Node A and Node C may be in range of AP (Node B) but not in range of each other. A cannot detect that C is transmitting and vice versa.

### CSMA/CA Operation

| Step | Action |
|---|---|
| **Carrier Sense** | Listen before transmitting — wait if medium is busy |
| **Random Backoff** | Wait a random time (contention window) before transmitting to reduce simultaneous attempts |
| **Transmission** | Send the frame |
| **Explicit ACK** | Receiver sends an ACK for every successfully received frame (unlike wired Ethernet which only uses ACKs at L4) |

### RTS/CTS (Optional)

To address the hidden terminal problem, a sender may first send a **Request-to-Send (RTS)** frame; the AP responds with **Clear-to-Send (CTS)**, which silences all other stations in the BSS for the duration of the transmission.

---

## IEEE 802.11 Wi-Fi Standards

| Standard | Common Name | Frequency | Max Speed | Technology |
|---|---|---|---|---|
| 802.11 (original) | — | 2.4 GHz | 1–2 Mbps | FHSS or DSSS |
| 802.11b | Wi-Fi 1 | 2.4 GHz | 11 Mbps | DSSS only |
| 802.11a | Wi-Fi 2 | 5 GHz | 54 Mbps | OFDM |
| 802.11g | Wi-Fi 3 | 2.4 GHz | 54 Mbps | OFDM |
| 802.11n | Wi-Fi 4 | 2.4 / 5 GHz | 600 Mbps | MIMO |
| 802.11ac | Wi-Fi 5 | 5 GHz | Multi-Gbps | MU-MIMO |
| 802.11ah | Wi-Fi HaLow | 900 MHz | ~150 Mbps | IoT-focused, long range |

---

## LPWAN — Low Power Wide Area Network

LPWANs are designed specifically for IoT applications that require:
- **Long range** (kilometres, not metres)
- **Low power** consumption (battery life of years)
- **Low data rate** (sensors sending small payloads infrequently)

### LPWAN Technology Comparison

| Technology | Range | Data Rate | Power | Spectrum | Standard Body |
|---|---|---|---|---|---|
| **NB-IoT** | ~15 km | ~250 kbps | Low | Licensed (LTE band, 200 kHz) | 3GPP |
| **LTE-M** | ~11 km | ~1 Mbps | Low–Medium | Licensed (LTE band) | 3GPP |
| **LoRaWAN** | ~15 km | ~50 kbps | Very Low | Unlicensed (Sub-GHz) | LoRa Alliance |
| **Wi-Fi HaLow** | ~1 km | ~150 Mbps | Low | Unlicensed (900 MHz) | IEEE |

### NB-IoT

- Developed by 3GPP; uses a **200 kHz** narrow-band slice of the LTE spectrum.
- Targets: indoor coverage, low cost, dense deployments, long battery life.
- Cannot support voice or high-mobility scenarios.

### LTE-M

- Also 3GPP; supports **higher data rates, mobility, and voice** compared to NB-IoT.
- More bandwidth and cost than NB-IoT; cannot operate in the LTE guard band.

### LoRaWAN

- Uses **LoRa** radio modulation (Long Range); the LoRaWAN protocol layer sits above it.
- Target use cases: smart agriculture, environmental monitoring, asset tracking.
- Very low power — end devices can run for years on a battery.

### Wi-Fi HaLow (802.11ah)

- Sub-GHz operation gives better range and wall penetration than standard Wi-Fi.
- Target use cases: smart home, industrial IoT, smart cities, surveillance.

---

## MQTT — Message Queuing Telemetry Transport

MQTT is the dominant IoT messaging protocol.

| Property | Detail |
|---|---|
| Architecture | **Publish–Subscribe** via a central **broker** |
| Transport | **TCP** (default); MQTT-SN variant uses UDP for constrained networks |
| Port | **1883** (plain), **8883** (TLS/SSL) |
| Design goals | Lightweight, low bandwidth, reliable over unreliable networks |

### Publish–Subscribe Model

- **Publishers** send messages to named **topics** on the broker (e.g., `sensors/temperature/room1`).
- **Subscribers** register interest in topics; the broker delivers matching messages.
- Publishers and subscribers are **decoupled** — they do not need to be online simultaneously.

### QoS Levels

| Level | Guarantee | Mechanism |
|---|---|---|
| **QoS 0** | At most once | Fire and forget — no acknowledgement |
| **QoS 1** | At least once | Receiver ACKs; sender retransmits until ACK received (may duplicate) |
| **QoS 2** | Exactly once | Four-step handshake ensures no duplicates |

---

## IoT Protocol Ecosystem

| Layer | Protocols |
|---|---|
| **Network** | Wi-Fi, Bluetooth, 4G/5G, ZigBee, NB-IoT, LoRaWAN, Wi-Fi HaLow |
| **Application/Data** | MQTT, CoAP, AMQP |

---

## Key Connections

- [[concepts/tcp-ip-network-model]] — Wi-Fi implements Layers 1 and 2; MQTT runs at the application layer (Layer 5)
- [[concepts/data-link-layer-ethernet]] — CSMA/CA (wireless) parallels CSMA/CD (wired); both are MAC sublayer protocols
- [[concepts/transport-layer-tcp-udp]] — MQTT uses TCP for reliable delivery; MQTT-SN uses UDP for constrained environments
- [[concepts/application-layer-dhcp-dns]] — IoT devices also use DHCP to obtain IP addresses on joining a network
