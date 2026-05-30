---
name: git-amend-remove-sensitive-push
description: Remove sensitive info (IP, username, key filename) from the latest pushed commit using git commit --amend + git push --force
metadata:
  type: feedback
---

# Git: Remove Sensitive Info from a Pushed Commit

**Rule:** If sensitive info (server IP, SSH username, key filename) is in the latest pushed commit, amend it and force-push immediately. This replaces the bad commit on GitHub — the old hash becomes unreachable.

**Why:** GitHub keeps old commits accessible by hash for a period — but force-pushing the branch tip means the bad commit is no longer reachable via the branch. For truly sensitive secrets (passwords, private keys), also rotate the credential itself.

## When This Applies
- Username, server IP, SSH key filename in README/docs
- **Not** for: actual private key content, passwords, API keys — rotate those immediately regardless

## The Fix (latest commit only)

```bash
# 1. Edit the file to remove/redact the sensitive content
#    (use placeholders like <user>@<ec2-ip>, <path/to/key.pem>)

# 2. Stage the cleaned file
git add README.md tasks.md

# 3. Amend the commit — rewrites the HEAD commit with the fix included
git commit --amend --no-edit

# 4. Force-push to replace the old commit on the remote
git push --force origin main
```

The old commit hash is now orphaned — GitHub will GC it eventually.

## If the Sensitive Commit Is Not the Latest
Use interactive rebase to edit the specific commit:
```bash
git rebase -i <hash-before-bad-commit>
# Mark the bad commit as 'edit'
# Make changes, git add, git commit --amend
# git rebase --continue
# git push --force origin main
```

## Harder Alternative: `git filter-repo`
For sensitive data deep in history (e.g. a committed `.env` file), use `git-filter-repo` to scrub it from every commit. Requires all collaborators to re-clone.

## Context
Applied during ICT2216 TrialGuard deployment (2026-05-30). A README commit included the EC2 IP, SSH username, and key filename. Commit was the HEAD of main on GitHub. Amended and force-pushed; old hash `9403ecd` replaced by `12233b2`. See [[examples/ict2216-project-deployment-phases-9-12]].

**How to apply:** Use whenever sensitive server details end up in a docs commit. Always redact to placeholders (`<user>@<ec2-ip>`) rather than just deleting the section, so the workflow instructions remain useful.
