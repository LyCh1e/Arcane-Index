---
type: concept
title: "Software Configuration Management"
domain: software-engineering
complexity: medium
source: "[[sources/INF2001-intro-software-engineering]]"
address: c-000052
created: 2026-05-23
updated: 2026-05-23
tags: [concept, software-engineering, scm, version-control, ci-cd, git, INF2001]
---

# Software Configuration Management

Software Configuration Management (SCM) is the discipline of tracking and controlling changes to software artefacts throughout the SDLC. It ensures that the evolution of a software system is a managed, auditable process.

---

## Four Pillars of SCM

```
Change Control      Version Management      System Building      Release Management
     ↓                      ↓                       ↓                     ↓
Manage requests     Track multiple versions  Compile & link        Distribute approved
and approvals       prevent interference     into executable       versions to users
```

---

## 1. Change Control

Ensures system evolution is managed — priority is given to the most urgent and cost-effective changes.

### Activities

- Analyse the costs and benefits of proposed changes
- Approve worthwhile changes (via a Change Control Board, CCB)
- Track which components have been changed

### Change Request Process

```
Identify item for change
     ↓
Submit Change Request (CR)
     ↓
Technical & business evaluation + impact analysis
     ↓
CCB Decision (approve / reject)
     ↓ (if approved)
Engineering Change Order (ECO) generated
     ↓
Configuration item checked out from repository
     ↓
Changes made and reviewed
     ↓
Configuration item checked back in → BASELINE
```

### Factors in Change Analysis

| Factor | Description |
|---|---|
| Consequence of not making the change | Risk of leaving the defect or omission |
| Benefits of the change | Value delivered by implementing it |
| Number of users affected | Business impact of the change |
| Cost of making the change | Engineering effort + regression risk |
| Product release cycle | When the change can realistically ship |

---

## 2. Version Management

Tracks different **versions** of configuration items and prevents developer interference.

### Terminology

| Term | Definition |
|---|---|
| **Version** | A configuration item at one point in its development; differs from other instances of itself |
| **Revision** | A version linked to another via a *revision-of* relationship, ordered in time (1.2 → 1.3 → 1.4) |
| **Variant** | Functionally equivalent versions for different platforms/settings |
| **Repository** | Shared database of all versions and their metadata |
| **Workspace** | An isolated private environment where a developer works without affecting others |
| **Check-out** | Copy an item from the repository to the workspace |
| **Check-in** | Copy changes from the workspace back to the repository |
| **Branching** | Create a new workflow from an existing version; both lines develop independently |
| **Merging** | Combine simultaneous changes from different developers / branches |

### Branching and Merging Pattern

```
main:    V1.0 ──── V2.0 ──────────── V2.1 (merged hotfix) ──── V3.0
                     │
feature branch:      └─── f2.0 ──── f2.1
```

---

## 3. System Building

The process of creating a complete, executable system by **compiling and linking** all components, external libraries, and configuration files.

Build systems automate:
- Dependency resolution
- Compilation order
- Linking
- Packaging

Manual builds are error-prone; automated build tools (Make, Gradle, Maven, npm scripts) are standard practice.

---

## 4. Release Management

The formal distribution of an **approved version** to users outside the development team.

### Release Types

| Type | Purpose |
|---|---|
| **Major release** | Significant new functionality |
| **Minor release** | Bug fixes and small improvements |
| **Hotfix** | Critical patch branched from the current production release |

### Release Package Contents

- Executable code
- Configuration files (installation-specific settings)
- Data files (error messages, reference data)
- Installation programme
- Electronic and paper documentation
- Packaging and publicity materials

### Hotfix Pattern

```
production main:  V2.0 ──── V2.1 (hotfix merged) ──── V3.0
                    │
hotfix branch:     └─── fix bug ──── merge back to main
```

---

## Version Control Systems (VCS)

A VCS provides both version management and change management in a single tool. GitHub is the most widely used, combining Git hosting with issue tracking and project boards.

### Git Workflow

```
Workspace (local dir)  →  Index (staging area)  →  Local Repo  →  Remote Repo
       │                           │                     │               │
       │        git add            │     git commit      │   git push    │
       │ ◄──────────────────────── │ ◄─────────────────  │ ──────────►  │
       │        git diff           │     git log         │   git fetch   │
       │ ◄──────────────────────── │                     │ ◄──────────── │
       │        git restore        │                     │   git merge   │
       └──────────────────         └─────────────────    │ ◄──────────── │
                                                         │   git pull    │
                                                         │ ◄──────────── │
```

| Command | Effect |
|---|---|
| `git add <file>` | Stage changes in workspace to index |
| `git commit -m "msg"` | Record staged snapshot to local repo |
| `git push` | Upload local commits to remote repo |
| `git fetch` | Download remote changes without merging |
| `git merge` | Incorporate fetched changes into local branch |
| `git pull` | Fetch + merge in one step |
| `git clone` | Copy remote repo to local workspace |
| `git diff HEAD` | Compare workspace against latest commit |
| `git log` | Show commit history |

---

## Continuous Integration and Continuous Delivery (CI/CD)

### The Integration Hell Problem

Without discipline, separate developers' branches **diverge** over time. Re-integrating them takes longer than writing the feature in the first place ("integration hell", Fowler 2006).

### Continuous Integration (CI)

> "A software development practice where members of a team integrate their work frequently, usually each person integrates at least daily. Each integration is verified by an automated build (including tests) to detect integration errors as quickly as possible." — Grady Booch (1994), popularised by Martin Fowler

**Practices:**
- All developers commit to the main branch at least daily
- Every commit triggers an automated build + test suite
- If the build fails, fixing it is the team's top priority

### Continuous Delivery (CD)

Automates the release process so that software can be **reliably released at any time**:
- Infrastructure changes are scripted
- Deployment to staging is automated
- Manual approval step (if needed) is the only gate before production

### CI/CD Pipeline

```
Developer commits code
         ↓
CI server detects change → triggers build
         ↓
Compile → Unit tests → Integration tests
         ↓
Test results reported to developer
         ↓ (on success)
Artifacts deployed to staging
         ↓
Further automated/manual testing on staging
         ↓ (on approval)
CD system deploys to production
```

### CI vs CD Summary

| Aspect | CI | CD |
|---|---|---|
| Scope | Build, test, merge | Release, deploy |
| Frequency | Every commit | On approval / on schedule |
| Goal | Detect integration errors early | Enable reliable releases at any time |
| Key metric | Build success rate, test pass rate | Deployment frequency, lead time for changes |

---

## SDLC with CI/CD

CI/CD does not replace the SDLC; it **automates** the iterative execution of implementation and deployment phases:

```
Requirements → Design → Development ──► CI Pipeline ──► Staging ──► Production
                                    ←──── Bug report / feedback ──────────────
```

---

## Related Pages

- [[concepts/sdlc-models|SDLC Models]] — SCM practices apply across all SDLC models
- [[concepts/software-project-management|Software Project Management]] — planning and tracking feed into change control
- [[concepts/web-security-and-devops|Web Security and DevOps]] — CI/CD in the web development context
- [[sources/INF2001-intro-software-engineering|INF2001 Source Index]]
