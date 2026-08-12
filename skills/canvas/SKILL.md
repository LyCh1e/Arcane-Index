---
name: canvas
description: "Visual layer of the wiki. Add images, text cards, PDFs, and wiki pages to Obsidian canvas files with auto-positioning inside zones. All canvas files are stored in canvases/ at the vault root. Integrates with /banana for image capture. Triggers on: /canvas, canvas new, canvas add image, canvas add text, canvas add pdf, canvas add note, canvas zone, canvas list, canvas from banana, add to canvas, put this on the canvas, open canvas, create canvas."
allowed-tools: Read Write Edit Glob Grep Bash
---

# canvas: Visual Reference Layer

The three knowledge capture layers:
- `/save` → text synthesis (wiki/questions/, wiki/concepts/)
- `/autoresearch` → structured knowledge (wiki/sources/, wiki/concepts/)
- `/canvas` → visual references (**canvases/** at the vault root)

**Storage rule: every canvas file is created in `canvases/` at the vault root — never in `wiki/`, the vault root itself, or any other location.** If `canvases/` does not exist, create it before writing the canvas file.

A canvas is a JSON file Obsidian renders as an infinite visual board. This skill reads and writes canvas JSON directly. Read `references/canvas-spec.md` for the full format reference before making any edits. This spec aligns with the [JSON Canvas open standard](https://jsoncanvas.org/). If the kepano/obsidian-skills plugin is installed, its json-canvas skill is the authoritative canvas spec reference. Otherwise, use the guidance below.

---

## Default Canvas

`canvases/main.canvas`

If it does not exist, create it:

```json
{
  "nodes": [
    {
      "id": "title",
      "type": "text",
      "text": "# Visual Reference\n\nDrop images, PDFs, and notes here.",
      "x": -400, "y": -300, "width": 400, "height": 120, "color": "6"
    },
    {
      "id": "zone-default",
      "type": "group",
      "label": "General",
      "x": -400, "y": -140, "width": 800, "height": 400, "color": "4"
    }
  ],
  "edges": []
}
```

---

## Operations

### open / status (`/canvas` with no args)

1. Check if `canvases/main.canvas` exists.
2. If yes: read it, count nodes by type, list all group node labels (zone names).
   Report: "Canvas has N nodes: X images, Y text cards, Z wiki pages. Zones: [list]"
3. If no: create it with the starter structure above.
   Report: "Created canvases/main.canvas with a General zone."
4. Tell user: "Open `canvases/main.canvas` in Obsidian to view."

---

### new (`/canvas new [name]`)

1. Slugify the name: lowercase, spaces → hyphens, strip special chars.
2. Create `canvases/[slug].canvas` with the starter structure, title updated to `# [Name]`.
   - Create `canvases/` directory first if it does not exist.
3. Add entry to `wiki/overview.md` under a "## Canvases" subsection (append after the Current State section). Do not modify `wiki/index.md`. It uses a fixed section schema (Domains, Entities, Concepts, Sources, Questions, Comparisons).
4. Report: "Created canvases/[slug].canvas"

---

### add image (`/canvas add image [path or url]`)

**Resolve the image:**
- If URL (starts with `http`): download with `curl -sL [url] -o _attachments/images/canvas/[filename]`
  Derive filename from URL path, or use `img-[timestamp].jpg` if unclear.
- If local path outside vault: `cp [path] _attachments/images/canvas/`
- If already vault-relative: use as-is.

Create `_attachments/images/canvas/` if it doesn't exist.

**Detect aspect ratio:**
Use `python3 -c "from PIL import Image; img=Image.open('[path]'); print(img.width, img.height)"` or `identify -format '%w %h' [path]`.
See `references/canvas-spec.md` for the full aspect ratio → canvas size table (7 ratios including 4:3, 3:4, ultra-wide). Do not use an inline table here. The spec is the single source of truth for sizing.

**Position using auto-layout** (see Auto-Positioning section below).

**Append node to canvas JSON and write.**

Report: "Added [filename] to [zone] zone at position ([x], [y])."

---

### add text (`/canvas add text [content]`)

Create a text node:
```json
{
  "id": "text-[timestamp]",
  "type": "text",
  "text": "[content]",
  "x": [auto], "y": [auto],
  "width": 300, "height": [calculated],
  "color": "4"
}
```

**Height calculation — measure every element; never guess:**

```
CHARS_PER_LINE = floor(width / 8)   # ~8 px per character at Obsidian's default font
LINE_HEIGHT    = 28                 # px per rendered line
PADDING        = 80                 # top + bottom chrome + breathing room
MIN_HEIGHT     = 100
```

Walk every line of the markdown string and accumulate `total_lines`:

| Element | Rule |
|---------|------|
| Empty line (`""` after split) | `+0.5` |
| `# ` H1 | `+2.2` |
| `## ` H2 | `+1.8` |
| `### ` H3 | `+1.4` |
| `#### ` H4+ | `+1.2` |
| `` ``` `` fence open/close | `+0.8` each |
| Code line inside fence | `+1.0` (no wrapping — monospace) |
| Table separator row (`\|---`) | `+0.4` |
| Table data row (`\|`) | `+1.1` |
| Blockquote line (`> `) | `+1.2 × ceil(line_len / CHARS_PER_LINE)` |
| Bullet / numbered list item | `+1.0 × ceil(item_text_len / (CHARS_PER_LINE - 3))` |
| Horizontal rule (`---`, `***`) | `+0.5` |
| Regular paragraph line | `+max(1, ceil(line_len / CHARS_PER_LINE))` |

Then:

```
raw_height = ceil(total_lines × LINE_HEIGHT) + PADDING
height     = max(MIN_HEIGHT, ceil(raw_height / 10) × 10 + 20)
```

The final `+ 20` is a mandatory breathing margin — never omit it. A node whose text is clipped is a broken node.

**Worked examples at width 300 (≈ 37 chars/line):**

| Content | total_lines | height |
|---------|-------------|--------|
| `### Heading` + blank + 2-sentence body (60 chars, wraps × 1) | `1.4 + 0.5 + 3 = 4.9` | `ceil(4.9×28)+80 = 217 → 230` |
| `## H2` + blank + 5-row table | `1.8 + 0.5 + 0.4 + 5×1.1 = 8.2` | `ceil(8.2×28)+80 = 310 → 320` |
| 10-line code block (``` + 10 lines + ```) | `0.8+10+0.8 = 11.6` | `ceil(11.6×28)+80 = 405 → 420` |

Position using the anti-overlap algorithm. Write and report.

---

### add pdf (`/canvas add pdf [path]`)

Same as add image. Obsidian renders PDFs natively as file nodes.
- Copy to `_attachments/pdfs/canvas/` if outside vault.
- Fixed size: width=400, height=520.
- Report page count if you can determine it.

---

### add note (`/canvas add note [wiki-page]`)

1. Search `wiki/` for a file matching the page name (case-insensitive, partial match ok).
2. Use the vault-relative path as the `file` field.
   - Use `"type": "file"` (not `"type": "link"`): `.md` files use file nodes, not link nodes.
   - `"type": "link"` takes a `url: "https://..."`: it is for web URLs only.
3. Create a file node: width=300, height=100.
4. Position using auto-layout.

```json
{
  "id": "note-[timestamp]",
  "type": "file",
  "file": "wiki/concepts/LLM Wiki Pattern.md",
  "x": [auto], "y": [auto],
  "width": 300, "height": 100
}
```

---

### zone (`/canvas zone [name] [color]`)

1. Read canvas JSON.
2. Find max_y: `max(node.y + node.height for all nodes) + 60`. Use 280 if no nodes (leaves room above the starter title node).
3. Create a group node:

```json
{
  "id": "zone-[slug]",
  "type": "group",
  "label": "[name]",
  "x": -400,
  "y": [max_y],
  "width": 1000,
  "height": 400,
  "color": "[color or '3']"
}
```

Valid colors: `"1"`=red `"2"`=orange `"3"`=yellow `"4"`=green `"5"`=cyan `"6"`=purple

Write and report.

---

### list (`/canvas list`)

1. `glob canvases/*.canvas`
2. For each canvas: read JSON, count nodes by type.
3. Report:

```
canvases/main.canvas                 14 nodes (8 images, 3 text, 2 file, 1 group)
canvases/blockchain-hash-chain.canvas  28 nodes (0 images, 26 text, 2 file, 0 groups)
```

---

### from banana (`/canvas from banana`) (if the banana-claude plugin is installed)

1. Check `canvases/.recent-images.txt` first (session log of newly written images).
2. If not found or empty: use `find` with correct precedence (parentheses required. Without them `-newer` only binds to the last `-name` clause):
   ```bash
   python3 -c "import time,os; open('/tmp/ten-min-ago','w').close(); os.utime('/tmp/ten-min-ago',(time.time()-600,time.time()-600))"
   find _attachments/images -newer /tmp/ten-min-ago \( -name "*.png" -o -name "*.jpg" \)
   ```
   Note: `/banana` is an optional external skill not shipped in this plugin. If the user has it installed, the `.recent-images.txt` log will be populated. If not, the `find` command above is the fallback.
3. If still none: show the 5 most recently modified images.
4. Present list: "Found N recent images: [list]. Add to canvas? Which zone? (zone name / 'new [name]' / 'skip')"
5. On confirmation: add each using the add image logic.

---

## Layout Rules

### Rule 1 — Content wrapping

Every text node must be tall enough to display its full content without clipping.
Apply the height formula from the `add text` section to **every** text node created or edited — including title cards, group banner nodes, and inline annotations. Never copy a height from a previous node without recalculating.

### Rule 2 — No overlapping nodes

**No two nodes may overlap, and no node may be positioned closer than `GAP = 40 px` to any other node (in any direction).**

This applies globally — across zones, between sections, and between newly added nodes and all pre-existing nodes. Groups (type `"group"`) are excluded from overlap checking; they are visual guides, not physical objects.

### Anti-Overlap Placement Algorithm

```python
GAP = 40   # minimum clear space between any two node bounding boxes

def boxes(nodes):
    """Bounding box (x1,y1,x2,y2) for every non-group node."""
    return [
        (n['x'], n['y'],
         n['x'] + n.get('width', 200),
         n['y'] + n.get('height', 100))
        for n in nodes if n.get('type') != 'group'
    ]

def clear(x, y, w, h, existing_boxes):
    """True if (x,y,w,h) does not overlap any box in existing_boxes."""
    for bx1, by1, bx2, by2 in existing_boxes:
        if not (x + w + GAP <= bx1 or bx2 + GAP <= x or
                y + h + GAP <= by1 or by2 + GAP <= y):
            return False
    return True

def place(nodes, anchor_x, anchor_y, new_w, new_h, row_limit=2400):
    """
    Find the first free position starting at (anchor_x, anchor_y).

    Strategy:
      1. Try the anchor position.
      2. If blocked, slide RIGHT past the conflicting node.
      3. If x + new_w exceeds row_limit, start a NEW ROW:
         y = bottom of the deepest existing node + GAP, x = anchor_x.
      4. Repeat until a clear spot is found.
    """
    existing = boxes(nodes)
    x, y = anchor_x, anchor_y

    for _ in range(200):   # safety cap
        if clear(x, y, new_w, new_h, existing):
            return x, y

        # Find the rightmost edge of any node blocking this row
        blocker_right = x
        for bx1, by1, bx2, by2 in existing:
            if not (x + new_w + GAP <= bx1 or bx2 + GAP <= x or
                    y + new_h + GAP <= by1 or by2 + GAP <= y):
                blocker_right = max(blocker_right, bx2)

        x = blocker_right + GAP

        if x + new_w > row_limit:
            # Wrap to a new row
            max_bottom = max((by2 for _, _, _, by2 in existing), default=anchor_y)
            y = max_bottom + GAP
            x = anchor_x

    # Fallback: stack directly below everything
    max_bottom = max((by2 for _, _, _, by2 in existing), default=anchor_y)
    return anchor_x, max_bottom + GAP
```

**How to use it in practice:**

1. After computing the node's width and height, choose an `anchor_x` / `anchor_y`:
   - Inside a zone: `anchor_x = zone.x + 20`, `anchor_y = zone.y + 40` (below the label)
   - No zone: `anchor_x = 0`, `anchor_y = max_bottom_of_all_nodes + GAP`
2. Call `place(all_nodes, anchor_x, anchor_y, new_w, new_h)` → `(x, y)`
3. Write the node at `(x, y)`.
4. Add its bounding box to the working set before placing the next node in the same batch.

Read `references/canvas-spec.md` for the coordinate system (y increases downward; node x/y is the top-left corner).

---

## ID Generation

Read the canvas file from `canvases/`, collect all existing IDs. Never reuse one.

Safe ID pattern: `[type]-[content-slug]-[full-unix-timestamp]`

Use the full Unix timestamp (10 digits) to avoid collisions in batch operations.

Examples: `img-cover-1744032823`, `text-note-1744032845`, `zone-branding-1744032901`

If a collision is detected (ID already exists in the canvas), append `-2`, `-3`, etc.

---

## Session Log (optional hook)

If `canvases/.recent-images.txt` exists, append any new image path written to `_attachments/images/` during this session (one path per line, keep last 20).

`/canvas from banana` reads this file first, making it instant without filesystem search.

---

## Banana Integration (if the banana-claude plugin is installed)

After any `/banana` run in the same session, if the user says "add to canvas" or "put on canvas", treat it as `/canvas from banana`.

When `/banana` finishes generating images, suggest:
> "Add generated images to canvas? Run `/canvas from banana`"

---

## Summary

1. **Storage** — All canvas files live in `canvases/` at the vault root. Never write a canvas anywhere else. Create `canvases/` if it does not exist.
2. **Read first** — Always read the canvas JSON before writing. Parse existing nodes to collect IDs and bounding boxes before placing anything.
3. **No clipping** — Every text node must be tall enough for its full content. Use the element-by-element height formula in `add text` for every text node — including titles, banners, and annotation cards. A node whose text is clipped is a broken node.
4. **No overlapping** — No two nodes may overlap or sit closer than 40 px to each other. Use the `place()` anti-overlap algorithm for every node position, sliding right then wrapping to a new row. When placing multiple nodes in one operation, update the working bounding-box set after each placement before computing the next.
5. **Spec first** — Read `references/canvas-spec.md` before editing canvas JSON (coordinate system, node types, edge format, color codes).
6. **Images** — Create `_attachments/images/canvas/` for downloaded or copied images.
7. **Index** — Update `wiki/index.md` when creating new canvases.
8. **Report** — After every operation, report: file path, node count, position `(x, y)`, and zone (if applicable).

## See Also

For standalone visual production (12 templates, 6 layout algorithms, AI generation,
presentations), see [claude-canvas](https://github.com/AgriciDaniel/claude-canvas).
This skill handles wiki-scoped visual boards. claude-canvas handles full-featured
canvas orchestration for any project.
