---
type: lab
status: established
title: "INF2005 Lab Wk 1 — Cryptography (Ciphers, Cryptanalysis & RSA Team Challenge)"
course: INF2005
tags: [lab, inf2005, cryptography, caesar, vigenere, rail-fence, columnar-transposition, frequency-analysis, blowfish, rsa, diffie-hellman, base64, morse, xor, ctf]
created: 2026-09-03
updated: 2026-09-03
address: c-000125
---

# INF2005 Lab Wk 1 — Cryptography

Practical lab for **INF2005 Cyber Security Fundamentals** (AY26). Ten guided exercises across
symmetric / asymmetric / classical crypto, seven cryptanalysis challenges, and a team RSA-cracking
challenge (`netforce.enc`).

Parent concepts: [[classical-ciphers-and-cryptanalysis]] · [[public-key-cryptography-and-key-exchange]]

Source files: `Cryptography Lab Wk 1 AY26.pdf`, `Cryptography Lab team challenge with hints.pdf`,
`public_key.pem`, `GHMS1.uyu`, `netforce.zip`.

---

## Part A — Exercises

| # | Site / tool | Point of the exercise | Key result |
|---|---|---|---|
| 1 | encode-decode.com/encryption-functions | Symmetric encrypt/decrypt | Receiver recovers plaintext with the **same algorithm + key + IV/mode**; only the key is secret (Kerckhoffs). |
| 2 | kerryveenstra cryptosystem | Symmetric key | One key both directions; wrong key ⇒ noise; secret must be pre-shared. |
| 3 | devglan RSA | Asymmetric key pair | **Cannot** use one key both ways. public→encrypt/priv→decrypt = confidentiality; priv→encrypt/pub→decrypt = authentication. |
| 4 | encode-decode.com/blowfish | Symmetric block cipher | See decryption below. |
| 5 | kerryveenstra cryptosystem | Asymmetric for authentication | Decrypting with a sender's public key proves **origin + integrity** (not secrecy). Authentication ≠ confidentiality. |
| 6 | dcode.fr Diffie–Hellman | The shared weakness | Both schemes' weakness = **key distribution**. DH derives a shared secret over a public channel. |
| 7 | cryptii Caesar | Shift arithmetic | Shift is **mod 26**: `±26 ≡ 0`, `27 ≡ 1`. Only 26 distinct keys. |
| 8 | Vigenère table | Polyalphabetic decrypt | `KS ME HZ BBL KS ME MPOG AJ XSE JCSFLZSY` → **`TO BE OR NOT TO BE THAT IS THE QUESTION`** |
| 9 | (manual) | Diffie–Hellman by hand | **Shared key = 9** |
| 10 | cryptii / boxentriq rail fence | Transposition | Key = rail count; `r=1` or `r ≥ len` ⇒ no change; frequencies unchanged. |

### Q4 — Blowfish decryption

Ciphertext (Base64), key `SIT-UOG`:
```
X9NZsUj2CY3XkuJQyqfQYDErvHfLN2I+QNt5qZyab2a2++eH5+wMkAzEjiwY4RKdusMbWAKRYGN+Qv8wLm4t+9EFCYR8dZjpdDSUeUTJZmY=
```
→ **`Blowfish is a symmetric-key block cipher, designed in 1993 by Bruce Schneier`**

Mode = **Blowfish-CBC**, key = 7 ASCII bytes `SIT-UOG` (zero-padded to 8), IV = all zeros, PKCS padding.
```bash
echo '<base64>' | base64 -d | \
openssl enc -d -bf-cbc -provider legacy -provider default \
  -K 5349542d554f4700 -iv 0000000000000000
```

### Q9 — Diffie–Hellman (`p=11, G=2, a=9, b=4`)
```
A = 2^9 mod 11 = 6
B = 2^4 mod 11 = 5
s = B^a mod p = 5^9 mod 11 = 9   (check: A^b = 6^4 mod 11 = 9)
```

---

## Part B — Cryptanalysis Challenges

| # | Ciphertext / scheme | Method | Plaintext |
|---|---|---|---|
| 11 | `UGRhIGx3b29za256…Wxwaw==` | Base64 (`==` hint) → Caesar +4 | `The password for the challenge page is: crypto` |
| 12 | `PRRO IEACLCHSEO` (key `KEY`↔`YEK`) | Columnar transposition, read order Y-E-K | `CIPHERS ARE COOL` |
| 13 | `- .... . / .--. .- ...` … | Morse | `THE PASSWORD FOR THIS LEVEL IS WELL DONE` |
| 14 | two 152-bit binary strings | XOR → hex → ASCII | `the password is bin` |
| 15 | decimal runs, `909`-delimited | ASCII-decimal codes | `The password is …convert` (`Thepas`+`sword`+`isde…`+`onvert`) |
| 16 | `8i4 q5tt/>/>1se g1s …` | ASCII −1 on the whole string, then de-leet (`7=t 4=a 3=e 1=i 0=o`) — every odd cipher symbol is `leetchar + 1` | `the password for the challenge site is: elite` |
| 17 | long monoalphabetic block | Frequency analysis (anchor `GFS`=ONE, `OIS`=THE, `MFU`=AND) | a full paragraph *describing frequency analysis itself* |

### Q11
```
base64 -d  →  "Pda lwoosknz bkn pda ydwhhajca lwca eo: ynulpk"
Caesar +4  →  "The password for the challenge page is: crypto"
```

### Q12 — grid rebuild
Column lengths (14 letters / 3 cols): Y=4, E=5, K=5. Ciphertext slices `PRRO | IEACL | CHSEO` placed back in key order K,E,Y:
```
K E Y
C I P
H E R
S A R
E C O
O L
```
Read across → `CIPHERSARECOOL`.

### Q14
```python
x = int(A, 2) ^ int(B, 2)          # A, B = the two 152-bit strings
x.to_bytes(19, "big")              # b'the password is bin'
```

### Q17 — recovered substitution (cipher → plain)
```
A→B B→K C→F D→L E→M F→N G→O H→P I→H J→Q K→R L→S M→A
N→C O→T P→I Q→U R→G S→E U→D V→V W→W X→X Y→Y
```
Plaintext (abridged): *"ONE WAY TO SOLVE AN ENCRYPTED MESSAGE, IF WE KNOW ITS LANGUAGE, IS TO FIND A DIFFERENT PLAINTEXT OF THE SAME LANGUAGE LONG ENOUGH TO FILL ONE SHEET OR SO, AND THEN WE COUNT THE OCCURRENCES OF EACH LETTER… WE CALL THE MOST FREQUENTLY OCCURRING LETTER THE 'FIRST'…"* — the message is a description of the method used to break it.

---

## Part C — Team Challenge: crack `netforce.enc`

**Given:** `netforce.enc` (in `netforce.zip`), `public_key.pem`, `GHMS1.uyu`. Decrypt using only the public key.

1. **`GHMS1.uyu` (211 B, unknown type).** Hex-editor view is mostly printable → substitution cipher. Adding 1 to every byte (Caesar +1 on bytes) yields the note: *"The file 'netforce.enc' can be decrypted with a private key. Every 64-bit chunk was encrypted at a time using the raw algorithm… by Rivest, Shamir, & Adleman."* ⇒ **textbook RSA, 64-bit blocks.**

2. **Inspect the public key.**
   ```
   openssl rsa -inform PEM -text -pubin -noout < public_key.pem
   #   Modulus  n = 16513720463601767803   (64-bit!)
   #   Exponent e = 65537
   ```

3. **Factor `n` (trivial at 64 bits — WolframAlpha / sympy / yafu).**
   ```
   n     = 3917781347 × 4215069449
   φ(n)  = (p−1)(q−1) = 16513720455468917008
   d     = 65537⁻¹ mod φ(n) = 9440767265896423601
   ```

4. **Decrypt each 8-byte block `m = c^d mod n`; the bytes are ASCII of a Base64 stream.**
   ```python
   import zipfile, base64
   data = zipfile.ZipFile("netforce.zip").read("netforce.enc")
   n, d = 16513720463601767803, 9440767265896423601
   b64 = bytearray()
   for i in range(len(data)//8):
       c = int.from_bytes(data[i*8:i*8+8], "big")
       b64 += pow(c, d, n).to_bytes(8, "big")
   s = bytes(b64).rstrip(b"\x00")
   open("netforce.mp3", "wb").write(base64.b64decode(s + b"=" * (-len(s) % 4)))
   ```

5. **Result:** `netforce.mp3` — a 935 KB MPEG-1 Layer III audio file (256 kbps, 48 kHz stereo), generated by the *TextAloud* TTS tool (ID3 tag: voice "Sam", `www.NextUp.com`). *"You know you got it if you can hear."* Play it for the spoken flag.

This is the classic **NetForce "Private Parts"** CTF challenge (infosecinstitute writeup).

---

## Notes / lessons

- **Encodings are not encryption.** Base64 / Morse / hex / ASCII-decimal / binary give zero confidentiality — always peel them off first. `==` vs `=` tells you the final-group byte count.
- **Transposition preserves letter frequencies**; substitution changes letter identities. That single observation routes you to the right attack.
- **RSA security = the cost of factoring `n`.** A 64-bit modulus falls in milliseconds → the private key drops out via `d = e⁻¹ mod φ(n)`. Use ≥ 2048-bit keys and OAEP/PSS padding. See [[learning/textbook-rsa-64-bit-modulus]].
- **Blowfish on OpenSSL 3.x** needs `-provider legacy` (it was moved out of the default provider).
- No prompt-injection or hidden text was found in either lab PDF this time (cf. [[learning/prompt-injection-in-lab-handout-pdf]] for the ICT3112 case).
