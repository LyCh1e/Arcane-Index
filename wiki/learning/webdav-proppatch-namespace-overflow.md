# mod_dav_fs PROPPATCH namespace-overflow: wrong payload shape → no crash

**Context:** ACW3 lab, CVE-2026-93546 (Apache 2.4.68 `mod_dav_fs`, CWE-190
integer overflow, CVSS 8.8). A teammate reported "the website doesn't crash"
following the exploit guide. Verified against the local `vulnerable-env` lab on
2026-10-29.

## Root cause of the "no crash"

The trigger is **a large *number* of distinct XML namespace *declarations*** in
the PROPPATCH body (`<p xmlns="u0"/><p xmlns="u1"/>…` ×tens of thousands) — the
per-request namespace *count* overflows. It is **not** one namespace with a giant
URI string, which is what the old guide used. A giant single token just:
- returns `207` if it parses, or
- hits Apache's default `LimitXMLRequestBody` (**1 MB**) → `413`.

Either way the server never crashes. The official CVE text said it plainly:
"…via PROPPATCH requests declaring **many XML namespaces**." Read the CVE record
verbatim before writing the payload.

## Second trap: worker crash ≠ container/site down

Apache = parent + pool of worker children. The exploit kills **one worker**; the
parent respawns it in ~1 s. So `docker ps` stays **Up**, `RestartCount` stays
**0**, and the site answers again immediately. Evidence lives at the *worker*
level: connection reset on the malicious request, memory spike in `docker stats`,
`AH00052 … exit signal Segmentation fault (11)` in the error log, and a parallel
flood making the service briefly unreachable. Don't expect a whole-site outage.

## Third trap: uncapped memory is dangerous on a laptop

The blow-up is O(n²) in memory. A single ~1 MB request (≈52k namespaces, under
the default limit) drove the worker to **>5 GB**; a 70k–200k sweep hit **>10.8 GB**
and nearly OOM'd the host. Fix for a safe, fast, repeatable demo: cap the
container (`mem_limit: 512m` + `memswap_limit: 512m`). Then ~45k namespaces kills
the worker in ~5 s via OOM, the host stays safe, and the service auto-recovers.
The authentic **SIGSEGV** (the CWE-190 corruption) only appears with lots of free
RAM — reproduce it only on a disposable VM.

## Also learned
- `curl --digest` with a large body returns a confusing final `401` because the
  auth retry doesn't cleanly re-send the big body. Use `python3 requests`
  (`HTTPDigestAuth`) to send the body in one authenticated request.
- `python -I` ignores user site-packages, so `requests` isn't importable under it.
- Namespaces get persisted into the resource's `.DAV` propdb → it bloats on disk
  (~4.2 MB for one file), matching the "persistently corrupt the property
  database" clause.

See working PoC + rewritten guide:
`INF2005-ACW3/vulnerable-env/guides/poc_dav_overflow.py` and
`.../guides/CVE-2026-93546-mod_dav_fs.md`.
