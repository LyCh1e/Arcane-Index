---
name: github-actions-version-deprecations
description: GitHub Actions — Node 20 deprecation, floating vs pinned action tags, CodeQL v3→v4 migration, and linter double-substitution trap
metadata:
  type: feedback
---

# GitHub Actions: Action Version Deprecations

## The Problem

GitHub Actions runners deprecated Node 20 in September 2025. Actions whose internal runtime still bundles Node 20 trigger a warning:

> Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: `actions/checkout@v4.2.2`, `actions/setup-node@v4`, `actions/upload-artifact@v4`.

The warning is informational (GitHub forces Node 24 anyway), but it's noise that obscures real errors.

## Root Cause: Floating Major Tags Cache Stale SHAs

When you write `actions/checkout@v4`, GitHub resolves it to a specific commit SHA at first run and may cache that resolution. If that SHA was published before the Node 24 update, the action still internally uses Node 20.

**Fix:** Pin to a specific minor/patch version that bundles the Node 24 runtime:

| Action | Old (Node 20) | New (Node 24) |
|--------|--------------|--------------|
| `actions/checkout` | `@v4.2.2` | `@v4.3.0` |
| `actions/setup-node` | `@v4` (floating) | `@v4` (floating also works; or pin to `@v4.4.0+`) |
| `actions/upload-artifact` | `@v4` (floating) | `@v4.6.2` |
| `actions/setup-python` | `@v5.3.0` | `@v5.6.0` |
| `github/codeql-action/*` | `@v3` | `@v4` (also deprecated Dec 2026) |

## CodeQL v3 → v4

`github/codeql-action` v3 is deprecated in December 2026. Bump all three steps:

```yaml
# Old
uses: github/codeql-action/init@v3
uses: github/codeql-action/analyze@v3
uses: github/codeql-action/upload-sarif@v3

# New
uses: github/codeql-action/init@v4
uses: github/codeql-action/analyze@v4
uses: github/codeql-action/upload-sarif@v4
```

## Linter Double-Substitution Trap

When doing a global find-and-replace of `@v4` with `@v4.3.0`, a second pass that replaces `@v4` again will match the `v4` inside `@v4.3.0`, producing `@v4.3.0.3.0` — a version that does not exist.

**How to apply:** Always run `replace_all` on the full pinned string (e.g. `@v4.2.2`), not just the major tag `@v4`. If two replacement passes are needed, check the file between passes.

## CodeQL Job Requirements

To restore CodeQL to a workflow after removal:

```yaml
codeql-analysis:
  runs-on: ubuntu-latest
  permissions:
    security-events: write   # required — to upload results
    actions: read            # required — to access workflow metadata
    contents: read           # required — for checkout

  strategy:
    fail-fast: false
    matrix:
      language: ['javascript']   # or 'python', 'java', etc.

  steps:
    - uses: actions/checkout@v4.3.0
    - uses: github/codeql-action/init@v4
      with:
        languages: ${{ matrix.language }}
    - uses: github/codeql-action/analyze@v4
      with:
        category: "/language:${{ matrix.language }}"
```

> **GHAS caveat:** Code Scanning (including CodeQL results and SARIF uploads) requires GitHub Advanced Security — available on public repos or private repos under a GitHub Team/Enterprise plan. Personal private repos will receive a 403 on `upload-sarif`. Workaround: upload as an artifact instead (`actions/upload-artifact`). See [[examples/ict2216-lab8-static-code-analysis]].

## Permissions Block Gotcha

Any explicit `permissions:` block on a job drops all unspecified permissions to `none`. A job with only `security-events: write` will have `contents: none`, causing `actions/checkout` to fail with `fatal: repository not found`. Always pair security permissions with `contents: read`.

```yaml
permissions:
  security-events: write
  contents: read      # ← easy to forget
```
