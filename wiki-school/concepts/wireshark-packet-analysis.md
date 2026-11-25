---
type: concept
title: Wireshark Packet Analysis — Reading Captures
domain: cyber-security
status: established
created: 2026-11-22
updated: 2026-11-22
address: c-000144
sources:
  - inf2005-week10-tutorial-scanning-packet-analysis
tags:
  - wireshark
  - packet-analysis
  - pcap
  - follow-tcp-stream
  - display-filter
  - telnet
  - ftp
  - brute-force
  - sip
  - rtp
  - cleartext-credentials
  - inf2005
related:
  - "[[digital-forensics]]"
  - "[[network-security-attacks]]"
  - "[[network-security-defence]]"
  - "[[tcp-ip-network-model]]"
  - "[[inf2005-week10-tutorial-worked-answers]]"
  - "[[inf2005-week10-tutorial-scanning-packet-analysis]]"
---

# Wireshark Packet Analysis — Reading Captures

**Wireshark** is a graphical packet analyser that reads live captures or saved files (`.pcap`, `.dmp`). The forensics lecture ([[digital-forensics]]) lists packet analysis as parsing fields, filtering and pattern matching; this page turns that into a working routine, practised in [[inf2005-week10-tutorial-worked-answers]].

## A routine for an unknown capture

1. **Statistics → Conversations / Protocol Hierarchy**: who talks to whom, on which ports, and which protocols dominate.
2. **Identify the protocol from the port**, then confirm in the payload (a port is only a hint).
3. **Right-click → Follow → TCP Stream** (or UDP stream) to read a whole session as text.
4. **Apply a display filter** to isolate the evidence.
5. For media, use **Telephony → VoIP Calls** and play the stream.

## Useful display filters

| Goal | Filter |
|------|--------|
| One host | `ip.addr == 192.168.0.1` |
| Telnet | `telnet` or `tcp.port == 23` |
| FTP logins | `ftp.request.command == "USER" \|\| ftp.request.command == "PASS"` |
| FTP failures | `ftp.response.code == 530` |
| Plain-text web logins | `http.request.method == "POST"` |
| SYN-only packets (scan signature) | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| SIP signalling | `sip` |
| RTP media | `rtp` |

## Cleartext protocols that expose secrets

| Protocol | Port | What the sniffer sees | Encrypted replacement |
|----------|------|-----------------------|-----------------------|
| **Telnet** | TCP 23 | Every keystroke, including login and password | SSH (22) |
| **FTP** | TCP 21 | `USER` and `PASS` commands and file data | SFTP or FTPS |
| **HTTP** | TCP 80 | Pages, cookies and form posts | HTTPS |
| **MSN Messenger** (legacy) | TCP 1863 | Account names and message text | modern encrypted messengers |
| **SIP + RTP** | UDP 5060 / dynamic | Call set-up, and the audio itself unless SRTP is used | SIPS and SRTP |

Credentials in these protocols are readable by anyone on the path: the sniffer-placement options (hub, SPAN port, tap) are in [[digital-forensics]], and the active and passive sniffing attacks are in [[network-security-attacks]] §5.

## Attack signatures seen in a trace

- **Port scan**: bulk SYN-only packets; vertical (many ports, one host) or horizontal (one port, many hosts).
- **Online password guessing**: many short, *completed* TCP connections to one login service, each ending in a failure reply (FTP `530`), with a different password every time and a small set of usernames.
- **Cleartext credential exposure**: a login exchange readable in a followed stream.

The difference between the first two is the handshake: a half-open scan never completes it, whereas a guessing attack does, because it must reach the login prompt.

## Reading VoIP

**SIP** sets up the call (INVITE, then `100 Trying`, `180 Ringing`, `200 OK`, ACK, and BYE to end). Its **SDP** body lists offered codecs and the RTP port. **RTP** carries the audio in separate UDP streams, one per direction; the codec (for example G.711 PCMA or PCMU) decides whether Wireshark can play it back.

## Measuring a web page load (Task 9, expected pattern)

A capture of one page load normally begins with **DNS** (resolve the name), then the **TCP three-way handshake**, then a **TLS handshake** for HTTPS, then the **HTTP** request and response; some sites use **QUIC over UDP** instead of TCP and TLS. This is the expected order, not a measured result: the packet count depends on your own capture.
