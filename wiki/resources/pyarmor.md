---
type: resource
status: established
created: 2026-07-26
name: pyarmor
description: Python bytecode obfuscator used to hide a decrypt key/module from reverse engineering in PyInstaller builds.
metadata:
  type: resource
  restype: tool
---

# PyArmor

Bytecode obfuscator for Python. Used to make a specific module's source
harder to recover via decompilation — not a general-purpose encryption
tool, and not a substitute for keeping real secrets server-side. See
[[concepts/pyinstaller-secret-protection]] for the pattern this supports
and its actual limits.

## Install & invoke (v9.2.6, installed 2026-07-26)

```bash
pip install pyarmor
```

The `pyarmor` console script may land in a user-scripts directory that
isn't on `PATH` (observed: `%APPDATA%\Python\Python3XX\Scripts` on
Windows, via `pip install --user`-style resolution even without `--user`
passed explicitly). The reliable invocation that doesn't depend on `PATH`:

```bash
python -m pyarmor.cli <command>
```

`python -m pyarmor` (no `.cli`) fails on 9.x with `No module named
pyarmor.__main__; 'pyarmor' is a package and cannot be directly executed`.

## Core command used

```bash
python -m pyarmor.cli gen -O <output_dir> <script_or_package>
```

Produces the obfuscated module plus a `pyarmor_runtime_XXXXXX/` support
package (contains a compiled `.pyd`/`.so`) in `<output_dir>`. Both must
ship together — see [[concepts/pyinstaller-secret-protection]] for the
PyInstaller flags required to bundle the runtime package correctly.

## License tiers

`pyarmor --version` prints the active license. Default `pip install` gives
a **trial** license (confirmed working, sufficient for the pattern in
[[examples/learnix-encrypted-env-build]]). Paid tiers unlock BCC mode,
RFT (restrict runtime) mode, and CI/CD mode — none of which the basic
key-obfuscation pattern needs. Check PyArmor's own licensing terms before
relying on it in anything shipped commercially, not just academic/
non-profit use.

## See also

[[concepts/pyinstaller-secret-protection]], [[examples/learnix-encrypted-env-build]]
