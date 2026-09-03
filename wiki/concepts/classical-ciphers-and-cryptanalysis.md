---
type: concept
title: "Classical Ciphers and Cryptanalysis"
aliases: ["Caesar cipher", "Vigenere cipher", "rail fence cipher", "columnar transposition", "monoalphabetic substitution", "frequency analysis", "substitution cipher", "transposition cipher"]
tags: [cryptography, classical-ciphers, substitution, transposition, cryptanalysis, frequency-analysis, encoding, base64, morse, xor, inf2005]
created: 2026-09-03
updated: 2026-09-03
status: established
domain: cryptography
address: c-000123
---

# Classical Ciphers and Cryptanalysis

## 1. Overview

**Classical ciphers** are pre-computer, hand-workable encryption schemes. They fall into two families:

| Family | Mechanism | What it changes | What it preserves |
|---|---|---|---|
| **Substitution** | Replace each symbol with another | Letter *identities* | Letter *positions* and frequency profile (monoalphabetic) |
| **Transposition** | Rearrange the existing symbols | Letter *positions* | The exact multiset of letters (frequencies identical to plaintext) |

Every classical cipher is broken today, but they remain the standard teaching vehicle for the core ideas of cryptography: keyspace size, Kerckhoffs's principle (security must rest on the key, not the secrecy of the algorithm), diffusion, and the statistical structure that cryptanalysis exploits.

A related skill is recognising **encodings** (Base64, Morse, ASCII-decimal, hex) — these provide *no* confidentiality but are constantly layered on top of ciphers in CTF-style challenges.

> **One-line definition:** A classical cipher hides a message by systematically substituting or permuting its letters under a small key; classical cryptanalysis recovers the message by exploiting the language statistics the cipher fails to destroy.

---

## 2. Substitution Ciphers

### 2.1 Caesar (shift) cipher

Each letter is shifted `k` places along the alphabet: `C = (P + k) mod 26`, `P = (C − k) mod 26`.

* **Key:** a single number `k`.
* **Keyspace:** only 25 useful keys → brute force is instant.
* **Shift beyond ±26:** arithmetic is mod 26, so `k = 27 ≡ 1`, `k = 30 ≡ 4`, `k = ±26 ≡ 0` (ciphertext = plaintext). There are only 26 distinct shifts no matter what number you type.
* **ROT13** is Caesar with `k = 13` (self-inverse).

### 2.2 Monoalphabetic substitution (general)

Each plaintext letter maps to a fixed but arbitrary ciphertext letter (a permutation of the alphabet), often generated from a keyword.

* **Keyspace:** 26! ≈ 4 × 10²⁶ — brute force is infeasible.
* **Fatal weakness:** the mapping is *fixed*, so the ciphertext's letter-frequency profile is just the plaintext's profile with relabelled bars. Broken by **frequency analysis** (§4).

### 2.3 Vigenère cipher (polyalphabetic)

A repeating keyword selects a different Caesar shift for each position:
`Cᵢ = (Pᵢ + Kᵢ) mod 26`, `Pᵢ = (Cᵢ − Kᵢ) mod 26`, where `K` is the keyword repeated to the length of the message.

* Flattens single-letter frequencies (the same plaintext letter enciphers differently at different positions), which defeated naive frequency analysis for ~300 years ("le chiffre indéchiffrable").
* **Broken by** Kasiski examination / index of coincidence: find the key length `L` (repeated ciphertext substrings tend to be `L` apart), then split the ciphertext into `L` columns and solve each as an independent Caesar cipher.
* Worked example (keyword `RELATIONS`): `KS ME HZ BBL KS ME MPOG AJ XSE JCSFLZSY` → `TO BE OR NOT TO BE THAT IS THE QUESTION`.

---

## 3. Transposition Ciphers

### 3.1 Rail fence

Write the plaintext in a zig-zag over `r` rails (top→bottom→top…), then read off **row by row**.

* **Key:** the rail count `r`.
* `r = 1` → no change. `r ≥ message length` → no change (the zig-zag never turns).
* Larger `r` separates originally-adjacent letters further.
* Broken by trying all `r` (small keyspace) — frequencies are untouched.

### 3.2 Columnar transposition

Write the plaintext in rows under a keyword; number the columns by the alphabetical order of the keyword's letters; read the ciphertext **column by column** in that numeric order.

* **Key:** the keyword (defines column count and read order). Decryption reverses the column order (the "`KEY` ↔ `YEK`" hint in the INF2005 lab).
* To decrypt: compute column lengths (`len mod ncols` columns are one longer), slice the ciphertext into columns, place them back in keyword order, read across rows.
* Worked example: `PRRO IEACLCHSEO`, key `KEY` (read order Y,E,K) → `CIPHERS ARE COOL`.
* Stronger than rail fence; **double** columnar transposition was a serious field cipher into the 20th century.

---

## 4. Frequency Analysis (breaking monoalphabetic substitution)

The method (which the INF2005 Q17 ciphertext literally describes in its own plaintext):

1. Take a large plaintext sample **in the target language** and rank its letters by frequency (English: **E T A O I N S H R D L …**; `E` ≈ 12.7 %, `T` ≈ 9.1 %).
2. Count symbol frequencies in the ciphertext and rank them.
3. Map the most common ciphertext symbol → `E`, next → `T`, and so on as a first guess.
4. Refine using **structure**: one-letter words (`A`, `I`); common bigrams (`TH`, `HE`, `IN`, `ER`); trigrams (`THE`, `AND`); doubled letters (`LL`, `SS`, `EE`, `OO`); word patterns and apostrophes.
5. Iterate until the plaintext reads.

Standard English letter-frequency histogram is the reference chart (the lab's "H1"). Frequency analysis fails on: polyalphabetic ciphers, very short texts, and texts with abnormal statistics (e.g. lipograms).

---

## 5. Encodings (not encryption)

These transform representation only — anyone can reverse them with no key. Recognise and peel them off first.

| Encoding | Tell-tale signs | Notes |
|---|---|---|
| **Base64** | `A–Z a–z 0–9 + /`, length multiple of 4, `=`/`==` padding | `==` ⇒ 1 byte in final group, `=` ⇒ 2 bytes. Decodes 4 chars → 3 bytes. |
| **Hex** | only `0–9 a–f`, even length | 2 chars → 1 byte |
| **Morse** | dots/dashes with `/` or spaces | letter gap vs word gap; "military use" hint |
| **ASCII-decimal** | runs of numbers, values ~32–126 (or 65–122) | needs a delimiter convention; look for a repeated separator token |
| **Binary** | only `0`/`1` | group into 8 → bytes → ASCII |
| **Leetspeak** | digits/symbols inside words: `8=B/t`, `4=A/e`, `5=S/a`, `1=l/o`, `0=o`, `3=e`, `2=i` | ad-hoc; anchor on a known word like "the" |

**XOR** sits on the border: `A ⊕ B = password` is a one-time-pad-style combine. XOR is its own inverse (`X ⊕ K ⊕ K = X`). Convert the result to hex then ASCII. XOR with a repeating key is broken like Vigenère.

---

## 6. Worked Recognition Workflow (CTF / cryptanalysis challenges)

You never *know* the cipher up front — you **diagnose it from the shape of the data**, then try the
cheapest matching attack. Read structure, not content.

### 6.1 Identify the layer

1. **Look at the character set.** Only `0/1` → binary. Only hex digits → hex. `A–Za–z0–9+/` with `=` padding → Base64. Dots/dashes → Morse. Digit runs in the 30–126 band → ASCII-decimal.
2. **Peel encodings** until you have "real" text or bytes. (The INF2005 Q11 hint *"there is a reason for the `==`"* is telling you Base64 is the outer layer.)

### 6.2 Classify what's underneath — a decision table

Given decoded text like `Pda lwoosknz bkn pda ydwhhajca lwca eo: ynulpk`:

| Observation | Rules in / out |
|---|---|
| Letters + spaces + punctuation, **not** high-entropy bytes | a *classical letter cipher*, not another encoding, not a modern block cipher |
| **Spaces and punctuation preserved** | the cipher only touches letters → **substitution**, not transposition, not a reblocking scheme |
| **Word lengths preserved** | letter-for-letter substitution; positions not scrambled |
| **Repeats align with English** (a repeated short word, `xx:` looking like `is:`, doubled letters) | consistent with **monoalphabetic** substitution (one fixed cipher→plain map) |
| Frequencies match English but reading order is scrambled; word lengths destroyed | **transposition** (rail fence, columnar) — letter multiset is unchanged |
| Frequencies *too flat* for the text length; no single map works | **polyalphabetic** (Vigenère / repeating-key XOR) |

### 6.3 Caesar vs general substitution — the constant-offset test

Once you believe it's monoalphabetic, test for the *special case* (a shift) with **one crib**:

* Guess the most common short word: a repeated 3-letter word is almost always `the`.
* Compute the offset per letter (A=0…Z=25). For `Pda → the`: P(15)→t(19) = +4, d(3)→h(7) = +4, a(0)→e(4) = +4.
* **All offsets equal ⇒ it's a shift cipher (Caesar)**, and you've just found the key.
* **Offsets differ ⇒ general substitution** — fall back to full frequency analysis (§4).

### 6.4 Cheapest-attack-first ordering (letter text)

1. ROT13 (1 try)
2. **All 25 Caesar shifts** — brute-forceable in a second; print them and eyeball for English
3. Frequency analysis for a general monoalphabetic map
4. Vigenère (Kasiski / index of coincidence → per-column Caesar)
5. …

Caesar sits near the top because ruling it out costs nothing. One shift producing clean English on
*every* word retroactively confirms the diagnosis; if none of the 25 do, escalate to step 3.

### 6.5 Practicalities

* **Anchor on cribs:** short words, doubled letters, `password` / `flag` / `the`, known file headers (`RIFF`, `PK`, `%PDF`, `ID3`).
* Automate with a few lines of Python or an online tool (cryptii, dcode.fr, CyberChef, boxentriq).

---

## 7. Connections

- [[concepts/public-key-cryptography-and-key-exchange]] — the modern successor: symmetric vs asymmetric, RSA, Diffie–Hellman, and why key size matters
- [[concepts/cryptographic-hash-functions]] — one-way functions; digit-sum as the toy analogue of a toy cipher
- [[examples/inf2005-lab-wk1-cryptography]] — full worked lab exercising every cipher and encoding on this page
- [[concepts/propositional-logic]] / [[concepts/combinatorics]] — modular arithmetic and keyspace counting
- [[concepts/security-terminology]] — Kerckhoffs's principle, confidentiality vs authentication
