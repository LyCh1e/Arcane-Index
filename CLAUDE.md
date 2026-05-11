# claude-obsidian — Claude + Obsidian Wiki Vault

This folder is both a Claude Code plugin and an Obsidian vault.

**Plugin name:** `claude-obsidian`
**Skills:** `/wiki`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint`
**Vault path:** This directory (open in Obsidian directly)

## What This Vault Is For

This vault demonstrates the LLM Wiki pattern — a persistent, compounding knowledge base for Claude + Obsidian. Drop any source, ask any question, and the wiki grows richer with every session.

## Vault Structure

```
raw/                source documents — immutable, Claude reads but never modifies
wiki/               Claude-generated knowledge base
  concepts/         deep concept and theory pages
  sources/          source index pages (one per ingested file)
  examples/         real-world examples and ingested lab sessions
  learning/         study notes, flashcard-style summaries
  goals/            personal and academic targets
  areas/            topic domain overviews
  synthesis/        cross-concept synthesis pages
  gaps/             open questions and knowledge gaps
  resources/        external references
  entities/         people, organisations, tools
_templates/         Obsidian Templater templates
_attachments/       images and PDFs referenced by wiki pages
```

## How to Use

Drop a source file into `raw/`, then tell Claude: "ingest [filename]".

Ask any question. Claude reads the index first, then drills into relevant pages.

Run `/wiki` to scaffold a new vault or check setup status.

Run "lint the wiki" every 10-15 ingests to catch orphans and gaps.

## Cross-Project Access

There are three layers to connecting any VSCode/Claude Code project to this vault. Use whichever layers suit the project.

### Layer 1 — CLAUDE.md snippet (required, ~1 min setup)

Drop this block into any project's `CLAUDE.md`. It tells Claude where the vault lives, when to read it, and when to write back.

```markdown
## Wiki Knowledge Base

Vault: C:\Arcane-Index

### Reading from the wiki
When you need context not in this project:
1. Read `wiki/hot.md` first — recent context, ~500 words
2. If not enough, read `wiki/index.md` for the full catalogue
3. Drill into `wiki/concepts/<page>.md` for specifics
Do NOT read the wiki for general coding questions already answered here.

### Writing back to the wiki
At the end of any session where something genuinely new was learned or built, write it back:
- **New concept or pattern** → create or update `wiki/concepts/<topic>.md`
- **Real-world example or working code** → create `wiki/examples/<project>-<topic>.md`
- **Bug, mistake, or lesson learnt** → append to `wiki/learning/<topic>.md`
- **Useful library or tool discovered** → create or update `wiki/resources/<tool>.md`
- Always update `wiki/index.md` tables and append to `wiki/log.md`
- Update `wiki/hot.md` to reflect the session's main output (~300 words)

### What counts as "something new"
- A design pattern or architectural decision that took effort to reach
- A library, API, or tool not already in the wiki
- A bug whose root cause was non-obvious
- A working solution to a problem that is likely to recur
- A gap in your understanding that was resolved
```

### Layer 2 — Claude Code stop hook (automated, ~5 min setup)

This fires automatically at the end of every Claude Code session in the project, prompting Claude to write back anything worth keeping — without you having to remember to ask.

Add to the **project's** `.claude/settings.json` (create the file if it does not exist):

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Session ended. Review conversation for anything worth ingesting into C:\\Arcane-Index wiki.'"
          }
        ]
      }
    ]
  }
}
```

For a fully automated ingest, replace the `echo` with a call to Claude Code in non-interactive mode:

```json
"command": "claude --print \"Read C:\\Arcane-Index\\wiki\\hot.md then review this session and write any new concepts, examples, or lessons into the Arcane-Index wiki at C:\\Arcane-Index. Update wiki/index.md and wiki/log.md.\""
```

> **Note:** The automated hook runs Claude again as a sub-process. It costs tokens but requires no manual action.

### Layer 3 — VSCode task (on-demand, ~2 min setup)

Adds an "Ingest to Wiki" entry to VSCode's task runner (`Ctrl+Shift+P` → Run Task) for when you want to trigger ingestion manually mid-session.

Add to the project's `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Ingest to Wiki",
      "type": "shell",
      "command": "claude",
      "args": [
        "--print",
        "Read C:\\Arcane-Index\\wiki\\index.md, then look at the recent work in this project and write any new concepts, patterns, or examples into the Arcane-Index wiki. Update wiki/index.md, wiki/hot.md, and wiki/log.md."
      ],
      "problemMatcher": [],
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    }
  ]
}
```

### Recommended setup per project type

| Project type | Layers to use |
|---|---|
| Active coursework / studying | 1 + 3 (manual ingest after each lab) |
| Side project / personal build | 1 + 2 (auto-ingest at session end) |
| Work project (sensitive code) | 1 only (manual, selective — don't ingest proprietary logic) |
| Quick experiment / throwaway | None — not worth the overhead |

## Plugin Skills

| Skill | Trigger |
|-------|---------|
| `/wiki` | Setup, scaffold, route to sub-skills |
| `ingest [source]` | Single or batch source ingestion |
| `query: [question]` | Answer from wiki content |
| `lint the wiki` | Health check |
| `/save` | File the current conversation as a structured wiki note |
| `/autoresearch [topic]` | Autonomous research loop: search, fetch, synthesize, file |
| `/canvas` | Visual layer: add images, PDFs, notes to Obsidian canvas |

## Writing Style

All content written into this vault — wiki pages, concept notes, source summaries, examples, log entries, and any other prose — **must** follow these rules:

- **British English** spelling and grammar at all times (e.g. *colour*, *organise*, *analyse*, *behaviour*, *programme*, *licence* (noun), *practise* (verb), *centre*, *catalogue*).
- Grammatically correct sentences — no sentence fragments used as prose, no dangling modifiers, subject–verb agreement throughout.
- Formal but readable register: technical precision without unnecessary jargon.
- These rules apply to Claude-generated content only; raw source files in `raw/` are ingested verbatim and are exempt.

## MCP (Optional)

If you configured the MCP server, Claude can read and write vault notes directly.
See `skills/wiki/references/mcp-setup.md` for setup instructions.
