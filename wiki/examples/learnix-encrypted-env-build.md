---
type: example
status: established
created: 2026-07-26
name: learnix-encrypted-env-build
description: Learnix (SE-24) — single PowerShell build script that encrypts .env, obfuscates the decrypt key with PyArmor, and packages a windowed PyInstaller exe, verified end-to-end.
metadata:
  type: example
---

# Learnix: Encrypted `.env` + PyArmor Build Pipeline

Original dev build command bundled `.env` in plaintext:

```
python -m PyInstaller --onefile --windowed -n Learnix --add-data ".env;." --collect-data customtkinter main.py
```

Replaced with a build pipeline applying
[[concepts/pyinstaller-secret-protection]]: encrypt `.env` → obfuscate the
decrypt key with PyArmor → PyInstaller. User explicitly wanted this
consolidated into **one PowerShell script**, not several Python tool files
— the only Python that's genuinely unavoidable is the runtime decrypt
module, since that has to execute *inside* the frozen app.

## Files

- **`build.ps1`** (repo root) — the entire build pipeline: encrypts, calls
  PyArmor, calls PyInstaller, cleans up. The encryption step is a Python
  script written to `$env:TEMP` via a PowerShell here-string and run with
  `python`, then deleted — keeps the crypto logic in Python (needs
  `cryptography`) without needing a separate committed `.py` tool file.
- **`src/_secrets_loader.py`** — the one piece of runtime code that can't
  be PowerShell. Decrypts `.env.enc` into `os.environ` when the app is
  frozen (`sys.frozen`).
- **`src/main.py`** — branches at the top: frozen → `_secrets_loader`,
  dev → the original `python-dotenv` `load_dotenv()` call, unchanged dev
  workflow.

```python
# src/main.py
if getattr(sys, "frozen", False):
    from _secrets_loader import load_encrypted_env
    load_encrypted_env()
else:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent / ".env")
```

```python
# src/_secrets_loader.py
def load_encrypted_env() -> None:
    from _secrets_key import FERNET_KEY  # obfuscated build artifact

    enc_path = _bundle_dir() / ".env.enc"
    data = Fernet(FERNET_KEY).decrypt(enc_path.read_bytes())
    for raw_line in data.decode("utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
```

## `build.ps1` — the three steps

```powershell
# 1. Encrypt .env -> .env.enc, write plaintext _secrets_key.py (temp python script, deleted after)
python $tmpPy   # generates Fernet key, encrypts, writes FERNET_KEY = ... to _secrets_key.py

# 2. Obfuscate just the key module
python -m pyarmor.cli gen -O $ObfDir $KeyFile

# 3. Build — --paths shadows the plaintext key module with the obfuscated one;
#    --hidden-import / --add-data pull in the PyArmor runtime PyInstaller can't see
python -m PyInstaller `
    --onefile --windowed -n Learnix `
    --paths $ObfDir `
    --add-data "$EncFile;." `
    --add-data "$($RuntimePkg.FullName);$($RuntimePkg.Name)" `
    --hidden-import $RuntimePkg.Name `
    --collect-data customtkinter `
    --noconfirm `
    main.py
```

Wrapped in `try { } finally { Remove-BuildSecrets }` so a failed build
never leaves `.env.enc`, `_secrets_key.py`, or `build_obf/` on disk —
`Remove-BuildSecrets` also runs unconditionally at script start in case a
previous run died partway through.

## Two gotchas hit while building this

**PowerShell here-string mangling over the tool-call transport.** The
first attempt embedded the Python encrypt script as a single-quoted
`@'...'@` here-string passed inline through a command-execution tool. The
closing `'@` got re-indented by the transport layer, silently breaking the
here-string parse — variables downstream (`$tmpPy`) ended up empty, and a
`Remove-Item -Path ""` degenerated into an attempt to remove `/`
(blocked as a protected path, which is what surfaced the bug). Fix:
double-quoted `@"..."@` here-string with PowerShell variable interpolation
(`r'$Src'` substituted directly into the embedded Python), written via a
real file-write tool instead of inline command text — here-strings are
fragile enough over any text-mangling transport that a real file write is
the safer construction path, not just a style preference.

**`python -m pyarmor` fails; `python -m pyarmor.cli` works.** PyArmor 9.x's
top-level package isn't directly executable
(`No module named pyarmor.__main__`). See [[resources/pyarmor]].

## Verification performed

Ran the actual `build.ps1` end-to-end (not just reviewed): confirmed
`.env.enc` / `_secrets_key.py` / `build_obf/` were all deleted after a
successful build, launched the resulting `dist/Learnix.exe`, confirmed no
`conhost`/`cmd` process appeared (windowed build genuinely has no console),
confirmed the process stayed responsive rather than crashing on a failed
decrypt, then killed it. This caught nothing wrong, but running the exe
was the only way to confirm the `--paths` shadowing actually picked the
obfuscated key module over the plaintext one at PyInstaller analysis time
— that step has no equivalent static check.

## Takeaways

- When PyInstaller + PyArmor are combined, scope obfuscation to the
  smallest module that holds the actual secret, not the whole app — see
  [[concepts/pyinstaller-secret-protection]] for why full-app obfuscation
  fights PyInstaller's static import analysis.
- A build script that shells out to `python -c`-equivalent temp scripts
  can consolidate "one language's worth of unavoidable logic" into an
  otherwise single-script pipeline in a different shell, without needing
  a separate committed tooling file — useful when the user's constraint is
  "minimize file count," not "minimize languages used."
- This is a stopgap, not a real fix, for the underlying issue that Learnix
  ships live Gemini/Mongo credentials to every install. Noted in
  [[concepts/pyinstaller-secret-protection]] as a distribution-architecture
  problem (needs a backend proxy) that no amount of client-side
  obfuscation solves.

**See also**: [[concepts/pyinstaller-secret-protection]], [[resources/pyarmor]]
