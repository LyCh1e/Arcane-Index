---
type: learning
status: established
created: 2026-05-31
updated: 2026-05-31
name: windows-openssl-strawberry-broken
description: Strawberry Perl's OpenSSL on Windows maps config to a non-existent Z: drive — generate TLS certs on Linux/EC2 instead
metadata:
  type: feedback
---

# Windows: Strawberry Perl's OpenSSL Has Broken Config

**Rule:** Do not use the system `openssl` on Windows if Strawberry Perl is installed — it maps its config to `Z:/extlib/.../ssl/openssl.cnf` which does not exist. Generate TLS certs on Linux or EC2 instead.

## Symptom
```
Can't open "Z:/extlib/_5040__/ssl/openssl.cnf" for reading, No such file or directory
error:10000080:BIO routines:BIO_new_file:no such file
```
The command appears to succeed (exit 0) but the `-subj` flag is silently ignored — the old cert is left in place or a broken cert is generated.

## Diagnosis
```powershell
(Get-Command openssl).Source
# C:\Strawberry\c\bin\openssl.exe  ← this is the broken one
```

## Fix: Generate Certs on EC2

SSH to the Linux server and generate there:
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /tmp/key.pem \
  -out /tmp/cert.pem \
  -subj "/CN=medi.trialguard.com/O=YourOrg/C=SG"

# Verify
openssl x509 -in /tmp/cert.pem -noout -subject -dates
```
Then SCP the files back to Windows:
```powershell
scp -i $PEM "${HOST}:/tmp/cert.pem" nginx\certs\cert.pem
scp -i $PEM "${HOST}:/tmp/key.pem"  nginx\certs\key.pem
```

## Alternative: Git Bash OpenSSL
Git for Windows ships its own OpenSSL that usually works:
```bash
# In Git Bash (not PowerShell)
/usr/bin/openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout nginx/certs/key.pem -out nginx/certs/cert.pem \
  -subj "/CN=medi.trialguard.com"
```

## Context
Encountered during ICT2216 TrialGuard deployment (2026-05-30) when regenerating the TLS cert with a new CN. Strawberry Perl was installed as a dependency of some other tool. Solution was to generate on EC2 and SCP back. See [[examples/ict2216-project-deployment-phases-9-12]].
