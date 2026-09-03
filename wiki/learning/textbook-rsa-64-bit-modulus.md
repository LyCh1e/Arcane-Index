---
type: learning
status: resolved
title: "Textbook RSA with a 64-bit modulus is broken in milliseconds"
updated: 2026-09-03
tags: [learning, cryptography, rsa, factorisation, ctf, inf2005]
---

# Textbook RSA with a 64-bit modulus is broken in milliseconds

## Context
INF2005 Cyber Security Fundamentals — Week 1 crypto lab team challenge. Given only
`public_key.pem` and a file `netforce.enc` "encrypted with a public key", recover the plaintext
(a hidden note in `GHMS1.uyu` reveals it is raw RSA applied to 64-bit blocks).

## What happened
`openssl rsa -text -pubin -noout < public_key.pem` showed:
```
Modulus  n = 16513720463601767803   (only 64 bits)
Exponent e = 65537
```
RSA's entire security is the difficulty of factoring `n`. At 64 bits that is not difficult:
```
n    = 3917781347 × 4215069449          (p × q — instant on WolframAlpha / sympy.factorint / yafu)
φ(n) = (p−1)(q−1) = 16513720455468917008
d    = pow(e, -1, φ(n)) = 9440767265896423601   ← the private key, reconstructed from public data
```
Then `m = c^d mod n` per 8-byte block recovered the plaintext (an ASCII Base64 stream that
decoded to an MP3).

## Lesson
- **RSA key size is not a tuning knob — it is the security parameter.** Anything below ~2048 bits
  (ideally 3072) is decorative. 512-bit RSA was factored in 1999; 768-bit in 2009; 829-bit in 2020.
- If you can factor `n`, you get `d` for free — the public key *is* the private key at small sizes.
- **"Textbook" RSA** (bare `m^e mod n`, no OAEP) is additionally broken even at large sizes:
  deterministic, malleable, vulnerable to small-`m`, common-modulus, and Håstad broadcast attacks.
  Real systems use RSA-OAEP for encryption, RSA-PSS for signatures, and only to wrap a symmetric key.
- Recognising the attack: a *short* modulus in `openssl rsa -text` output is the whole tell.

## Related
- [[concepts/public-key-cryptography-and-key-exchange]]
- [[examples/inf2005-lab-wk1-cryptography]]
