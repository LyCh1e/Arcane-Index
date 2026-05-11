---
type: learning
title: "Docker on Windows: CRLF Line Endings Break Linux Container Scripts"
domain: devops
tags: [docker, windows, crlf, line-endings, git-bash, powershell, linux]
created: 2026-05-11
---

# Docker on Windows: CRLF Line Endings Break Linux Container Scripts

## The Bug

Running a shell script inside a Docker Linux container fails with "file not found" or "no such file or directory" — even though the file clearly exists in the container. The error refers to the interpreter path (e.g., `/bin/sh`), not the script itself.

**Example:**
```sh
docker exec securityrat-mariadb sh -c './var/dumpRequirements.sh'
# Error: ./var/dumpRequirements.sh: not found
```

## Root Cause

Windows uses `\r\n` (CRLF) as its line ending. Linux uses `\n` (LF) only.

Git on Windows checks out text files with CRLF by default (controlled by `core.autocrlf`). When Docker copies such a file into a Linux container, the CRLF endings are preserved. The shebang line becomes:

```
#!/bin/sh\r
```

Linux reads the `\r` as part of the interpreter path. It then tries to execute `/bin/sh\r`, which does not exist — hence "file not found." The file itself exists; the *interpreter* named in the shebang does not.

This also affects every other line in the script. A command like:

```sh
mysql ... < /var/requirements.sql\r
```

tries to read `/var/requirements.sql\r`, which also does not exist.

## Fix — Strip CRLF Inside the Container

```powershell
# IMPORTANT: use PowerShell, not Git Bash (see Gotcha #2 below)
docker exec securityrat-mariadb sed -i 's/\r$//' /var/dumpRequirements.sh
```

`sed -i 's/\r$//'` replaces every `\r` at the end of a line with nothing, converting CRLF → LF in-place.

## Fix — Bypass the Script Entirely

If `sed` is unavailable, run the underlying command directly:

```powershell
docker exec securityrat-mariadb sh -c 'mysql -u root -p"$MYSQL_ROOT_PASSWORD" securityrat < /var/requirements.sql'
```

## Fix — Prevent at Source (Best Long-Term)

Convert the file before building the image:

```powershell
# In PowerShell — convert to LF before docker-compose up --build
(Get-Content "mariadb\dumpRequirements.sh" -Raw) -replace "`r`n", "`n" | Set-Content "mariadb\dumpRequirements.sh" -NoNewline
```

Or add a `.gitattributes` file to the repo:
```
*.sh text eol=lf
```

## Gotcha #2 — Git Bash Translates Linux Paths

When using Git Bash on Windows, absolute Linux paths like `/var/` are silently translated to Windows paths (e.g., `C:/Git/var/`). Running:

```bash
# In Git Bash — WRONG
docker exec securityrat-mariadb sed -i 's/\r$//' /var/dumpRequirements.sh
# Error: sed: can't read C:/Git/var/dumpRequirements.sh: No such file or directory
```

**Solution:** Use PowerShell (not Git Bash) for any `docker exec` command that passes Linux absolute paths as arguments.

## Diagnostic Checklist

| Symptom | Likely Cause |
|---------|--------------|
| Script "not found" but `docker exec ls /var/` shows it | CRLF shebang |
| `sed` fails with `C:/Git/...` path | Running in Git Bash instead of PowerShell |
| Script runs but inner commands fail | CRLF on non-shebang lines |

## Related

- [[securityrat]] — the specific case where this was encountered
