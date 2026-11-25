---
type: example
status: established
title: INF2005 Week 10 Tutorial — Worked Answers for the Packet Captures (Tasks 5–8)
course: INF2005
address: c-000142
tags:
  - inf2005
  - tutorial
  - wireshark
  - telnet
  - ftp
  - brute-force
  - msn-messenger
  - sip
  - rtp
  - pcap
  - cleartext-credentials
created: 2026-11-22
updated: 2026-11-22
related:
  - "[[inf2005-week10-tutorial-scanning-packet-analysis]]"
  - "[[wireshark-packet-analysis]]"
---

# INF2005 Week 10 Tutorial — Worked Answers (Tasks 5–8)

Answers were derived by decoding the packets directly (Python and Scapy), not by reading the Wireshark GUI, so check them against your own screen. Task 8's language question is **not** answered. Captures: `_attachments/pcaps/`. Method: [[wireshark-packet-analysis]].

## Task 5 — `telnet.pcap`: who is logged in to 192.168.0.1?

| Item | Finding |
|------|---------|
| Packets | 92; client `192.168.0.2:1550` to server `192.168.0.1:23` |
| Server | OpenBSD 2.6-beta host named `oof` (banner `OpenBSD/i386 (oof) (ttyp2)`) |
| **Username** | **`fake`** |
| **Password** | **`user`** |
| Session | `/sbin/ping www.yahoo.com` (6 replies, 0% loss), `ls`, `ls -a`, `exit` |

**Method:** Analyse → Follow → TCP Stream. After the Telnet option negotiation (bytes starting `0xFF`), the server prints `login:`, the client sends `fake`, the server prints `Password:` and the client sends `user`. Each keystroke line is plain ASCII, so anyone on the path can read it. **Lesson:** Telnet has no encryption; use SSH.

## Task 6 — `ftp.pcap`: suspicious activity

| Question | Finding |
|----------|---------|
| Usernames | **`admin`** and **`administrator`** |
| Passwords used | **1,406 `PASS` commands, 703 distinct words**: every word was tried against both usernames |
| Attack type | **Dictionary (brute-force) password guessing against the FTP login** |

Supporting evidence: 19,730 packets in about 45 seconds; 704 separate TCP connections from `10.121.70.151` to the FTP server `10.234.125.254:21`; the server answered `220` (ready) 1,404 times, `331` (password needed) 1,414 times and **`530` (login failed) 1,410 times**; **no `230` (login successful) appears**, so no guess succeeded in this capture. The words are in alphabetical order (merlin, mercury, mets, mgr, mickey, …), which is typical of a wordlist.

**Method:** filter `ftp.request.command == "USER" || ftp.request.command == "PASS"`; Statistics → Conversations shows hundreds of short TCP sessions to port 21. Contrast with port-scan detection in [[digital-forensics]]: a scan sends bare SYN packets, whereas here every connection completes the handshake and attempts a login, so it is a *credential* attack rather than a scan.

## Task 7 — `chat.dmp`: protocol and conversation

| Item | Finding |
|------|---------|
| Protocol | **MSN Messenger (MSNP)** over TCP **port 1863**, plaintext; server `207.46.26.167` |
| Email addresses | **`tesla_brian@hotmail.com`** (Brian, client `192.168.0.114`) and **`tesla_thomas@hotmail.com`** (Thomas) |
| Packets | 50 |

**The new IT guy:** Brian asks whether Thomas has heard about the new IT guy they hired. Thomas has heard he is a "real jerk", and Brian says he has heard the same. Thomas then suggests they try hacking into a server to mess with him, and Brian agrees. (The first line, which Brian sends, reads "Hey Brian", apparently a typo in the capture.)

**Method:** Follow TCP Stream, or filter `msnms`. Commands such as `USR`, `CAL`, `JOI` and `MSG` carry the account names and message bodies; the `text/x-msmsgscontrol` MSGs are typing notifications.

## Task 8 — `sip_chat.pcap`: protocol and language

| Item | Finding |
|------|---------|
| Protocol | **SIP** (signalling, UDP 5060) plus **RTP** (audio, UDP) |
| Parties | Jitsi client `10.0.20.14` (user `333603`) and an **Asterisk** PBX at `119.40.81.1` |
| Call | `INVITE sip:01730041455@119.40.81.1`; first answered by `407 Proxy Authentication Required` (MD5 digest), repeated with credentials, then `100 Trying`, `180 Ringing`, `183 Session Progress`, later `BYE` |
| Codec | The client offers G.722, Speex, PCMU, PCMA, iLBC and others; the PBX answers **PCMA (G.711 A-law)** and PCMU |
| Media | RTP between client port 5000 and PBX port 15414; about 5,000 packets over roughly 51 seconds |
| **Language** | **Not determined.** It can only be found by listening. |

**To answer it:** Telephony → VoIP Calls → select the call → **Play Streams**, or Telephony → RTP → RTP Streams → Analyse. Do not infer the language from the dialled number or addresses.

> [!note] Same capture, extra traffic
> About 9,586 packets in total; most are unrelated browsing, NetBIOS name queries (UDP 137) and SSDP (UDP 1900) on the same network segment, which is why the call has to be isolated by the VoIP Calls view.
