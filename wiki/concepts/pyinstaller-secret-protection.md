---
type: concept
status: established
created: 2026-07-26
name: pyinstaller-secret-protection
description: How to keep .env/API-key data out of a PyInstaller build in plaintext, and the hard limit on how far that protection can actually go.
metadata:
  type: concept
  domain: python-gui
  complexity: medium
---

# Protecting Secrets in a PyInstaller Build

## The problem

`--add-data ".env;."` on a PyInstaller build copies the file byte-for-byte
into the bundle. It is **not encrypted** — a onefile exe just self-extracts
to a temp dir at runtime, and tools like `pyinstxtractor` pull the original
`.env` back out unmodified. Bundling secrets this way is equivalent to
shipping a plaintext `secrets.txt` next to the exe.

## The hard limit — read this before implementing anything

If the running app needs the secret at runtime, the code that decrypts it —
and the key it uses — **must ship inside the same binary**. Any protection
applied at build time (encryption, PyArmor obfuscation) only raises the
effort required to extract the secret via reverse engineering; it does not
make extraction impossible. Treat all of the following as "stops casual
inspection," not "stops a motivated attacker."

**The actual fix**, when the secret is a live, blast-radius-bearing
credential (a shared API key, a DB connection string): don't ship it in the
client at all. Put a thin backend/proxy between the desktop app and the
external service; the desktop app authenticates to *your* backend, and the
backend — not the user's machine — holds the real key. No amount of
client-side obfuscation substitutes for this when the credential is one you
can't afford to leak.

Everything below is the appropriate stopgap when full backend-proxying
isn't in scope yet, or when the goal is genuinely just "stop a curious user
from grepping the exe," not "prevent extraction by a determined attacker."

## Layer 1 — encrypt the data file (Fernet)

Encrypt `.env` at build time with `cryptography.Fernet`, bundle the
ciphertext instead of the plaintext, decrypt to memory at process startup
(never write the plaintext back to disk).

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
token = Fernet(key).encrypt(env_path.read_bytes())
enc_path.write_bytes(token)
```

At runtime, decrypt and populate `os.environ` directly rather than using
`python-dotenv` (which expects a file on disk):

```python
data = Fernet(key).decrypt(enc_path.read_bytes())
for line in data.decode().splitlines():
    k, v = line.split("=", 1)
    os.environ.setdefault(k.strip(), v.strip())
```

This alone doesn't help much — the key has to live somewhere in the
bundled code as a literal, which is exactly as greppable as the original
`.env` was.

## Layer 2 — obfuscate just the key, not the whole app

PyArmor obfuscates Python bytecode so a decompiler can't trivially read a
module's source. Pair it with Layer 1 by isolating the Fernet key in its
own tiny module and obfuscating *only that module*:

```
_secrets_key.py     # generated at build time: FERNET_KEY = b"..."
_secrets_loader.py   # imports _secrets_key, decrypts .env.enc → os.environ
```

```bash
pyarmor gen -O build_obf src/_secrets_key.py
```

**Why scope it to one file instead of the whole codebase**: obfuscating
everything is the instinctive move, but it actively fights PyInstaller.
PyInstaller's static analysis walks plain-text `import` statements across
the whole source tree to decide what to bundle; once a module is
obfuscated bytecode, PyInstaller can no longer see *its* imports, so every
transitive dependency reachable only from inside obfuscated code has to be
declared by hand via `--hidden-import`. Scoping obfuscation to a single
leaf module (the key) keeps that manual-declaration surface to exactly one
item: the PyArmor runtime package itself.

### The PyInstaller + PyArmor integration gotcha

`pyarmor gen` emits a runtime support package alongside the obfuscated
module (e.g. `pyarmor_runtime_000000/`, containing a compiled `.pyd`/`.so`).
The obfuscated module imports it internally, but — per the point above —
PyInstaller can't see that import. Two flags are required or the frozen
exe fails at runtime with `ModuleNotFoundError`:

```bash
pyinstaller --paths build_obf \
    --hidden-import pyarmor_runtime_000000 \
    --add-data "build_obf/pyarmor_runtime_000000;pyarmor_runtime_000000" \
    ...
```

- `--paths build_obf` puts the obfuscated `_secrets_key.py` ahead of the
  plaintext source copy on PyInstaller's analysis search path, so the
  *obfuscated* version gets bundled, not the readable original.
- `--hidden-import` + `--add-data` manually pull in the runtime package
  PyInstaller's analysis is blind to.

## Layer 3 — clean up build artifacts

The plaintext key module, the encrypted `.env.enc`, and the PyArmor output
directory are all build-time-only. Delete them (in a `finally`/cleanup
step so a failed build doesn't leave them behind) once the exe is built —
none of them belong in version control or on disk after packaging.

## What this stack does and doesn't buy you

| Threat | Covered? |
|---|---|
| Someone opens the exe in a text editor / archive tool and reads `.env` | Yes |
| Someone runs `pyinstxtractor` and reads the extracted files without further effort | Yes |
| A dedicated reverse engineer with a decompiler and time | No — raises effort, doesn't stop it |
| The credential itself being usable by every install of the app | No — this is a distribution-architecture problem, not a build-obfuscation one |

## See also

[[examples/learnix-encrypted-env-build]] — concrete implementation (single
PowerShell build script, Learnix / SE-24). [[resources/pyarmor]] — tool
notes, license tiers, version-specific CLI invocation.
