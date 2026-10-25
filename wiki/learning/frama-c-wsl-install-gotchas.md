---
type: learning
title: "Frama-C 33 on WSL Ubuntu — opam install gotchas"
domain: tooling
status: resolved
created: 2026-10-20
tags: [frama-c, opam, wsl, windows, installation]
---

# Frama-C 33 on WSL Ubuntu: opam install gotchas

Context: ICT3112 Lab 0. See [[resources/frama-c]] and [[examples/ict3112-frama-c-labs-0-2]].

| Symptom | Cause | Fix |
|---|---|---|
| `eval $(opam env)` run through `wsl -- bash -lc` gives `syntax error near ;;` | WSL inherits the Windows `PATH`, which contains `Program Files (x86)` | Use `opam exec --switch=frama -- cmd`, or put commands in a `.sh` file and run `wsl -- bash file.sh` |
| `opam install depext ...` fails with "unmet availability conditions" | depext is obsolete on opam 2.1+ | Skip it; opam handles system packages itself |
| Install stops at "install graphviz? [Y/n] n" in a non-interactive run | The prompt was auto-answered no | `apt-get install graphviz` as root, then `opam install --assume-depexts` |
| opam suddenly asks to upgrade the root layout 2.1 → 2.6 | `apt` upgraded opam while installing packages | Answer `y` (fresh root, safe), then rerun |
| `frama-c` not found though install finished | Binaries are in `~/.opam/<switch>/bin` | Add to `PATH` in the script |
| Git Bash turns `wsl -- bash /mnt/c/...` into `C:/Git/mnt/c/...` | MSYS path conversion | Run the `wsl` command from PowerShell, or set `MSYS_NO_PATHCONV=1` |
| `apt` has `z3`, `cvc5`, `why3` but no `frama-c` or `alt-ergo` | Not packaged on Ubuntu 24.04 | Install those two with opam; `apt install z3 cvc5`; then `why3 config detect` |
| `frama-c-gui`: "requires node version 24 or later" | No Node/yarn in WSL | Install nvm, `nvm install 24`, `npm install -g yarn` (Lab 0 section 2.2.3) |
| `frama-c-gui`: `libnspr4.so: cannot open shared object file` | Electron (Ivette) system libs missing from Ubuntu | `apt install libnspr4 libnss3 libgbm1 libasound2t64 libgtk-3-0t64 libxss1 libxtst6 libxkbcommon0 libdrm2 libatk-bridge2.0-0t64 libcups2t64` |
| `frama-c` not found in a fresh terminal | opam switch not on PATH | Append `eval "$(opam env --switch=frama --set-switch)"` to `~/.bashrc` |
| `frama-c` warns `-wp-no-simpl is a deprecated alias for -wp-no-subst` | Lab text uses an old option name | Use `-wp-no-subst` (or `-wp-no-qed`) |
| `-rte` shows 4 `rte_pointer_alignment` timeouts on array code | `ligned` unsupported in WP 33.0 | Use `-wp-rte` (skips those guards) or run without `-rte` |
| `frama-c-gui` window opens then vanishes (started with `wsl -- bash -lc "... &"`) | WSL kills background children when the launching shell exits | Run the GUI as the foreground command of a long-lived task (e.g. Claude Code `run_in_background`), not backgrounded inside a short `wsl` call |
| Annotated file proves 92/94 with the default prover; the two failures are `assert non_increasing(...)` after a shifting loop | Alt-Ergo alone times out on the nested `\forall` in the predicate | `-wp-prover alt-ergo,z3,cvc5 -wp-timeout 30` closes them (94/94, Assignment 1) |
| Read tool says the assignment PDF is "password-protected" | False positive, same as [[learning/ict3112-lab3-tooling-gotchas]] | `python -c "import pypdf; ..."` extracts the text; `is_encrypted` is False |

Build takes ~30–40 minutes (OCaml compiler plus Frama-C from source). The GUI (`frama-c-gui`, Ivette) builds itself on first start (a few minutes) and opens through WSLg. The CLI `frama-c -wp -rte` is enough for all lab proofs.
