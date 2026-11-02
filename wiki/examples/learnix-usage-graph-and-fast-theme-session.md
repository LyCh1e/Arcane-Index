---
type: example
status: established
created: 2026-11-03
name: learnix-usage-graph-and-fast-theme-session
description: Learnix (SE-24) — one UAT-driven session: an admin token usage graph drawn on a tk.Canvas, a theme switch cut from about 16.5s to 1.6s by rebuilding widgets inside the open window, and a clearer label for a destructive admin button.
metadata:
  type: example
---

# Learnix: Admin Usage Graph, Fast Theme Switch and a Clearer Delete Label

Three UAT-driven desktop changes on branch `QOL/theme-change-and-token-usage`, merged in PR #231. The full write-up, with every measurement, is in the project's `cy-documentation.md` (update log, 2026-11-03).

## 1. Admin token usage graph

**Request:** a usage graph with 1 week, 2 weeks and 1 month views on the admin Token Usage screen.

**What was built**
- `src/ui/usage_chart.py`: a `UsageChart` widget with one column per day, totalled across all users, with empty days filled with zero.
- A range button, a period summary line and a hover tooltip showing date, tokens and estimated cost.
- A "Show daily values" table, because the tooltip only works with a mouse. It uses one multi-line label per column, so 30 rows cost three widgets.

**Decisions**
- **No new query.** `all_usage_summary()` already returns each user's full `per_day` history, so switching range makes no database call.
- **Columns, not a line.** Each day is a separate count and many are zero, and a line would imply usage between them.
- **No chart library.** None is bundled, so it draws on a `tk.Canvas` hosted in a `CTkFrame` subclass to follow the font size setting.
- **Days stay UTC.** `_summarise` buckets by UTC day, so before 08:00 Singapore time today's usage appears under yesterday's date. The graph says so; a real fix would also change the student view.
- **1 Month means the last 30 days,** and the KPI tiles stay all-time.

**Lesson:** rendering caught a crash that unit tests and ruff missed. See [[learning/customtkinter-subclass-method-collision]].

## 2. Faster theme switching

**Finding:** UAT said changing theme took too long.

| Page open | Before | Learner | Admin |
|---|---|---|---|
| Settings (the normal path) | ~16.5s | 1.60s | 2.11s |
| Chat, empty | ~16.5s | 1.20s | 1.33s |
| Chat, 40 messages | ~16.5s | 2.26s | 2.46s |
| My Dashboard | ~16.5s | 2.47s | n/a |
| Token Usage | ~16.5s | 2.34s | 3.82s |
| Admin Dashboard | ~16.5s | n/a | 12.04s |

**Root cause:** building widgets took about 0.8s. The rest was the window being destroyed and startup repeating behind a 14s splash: FAISS index, database bootstrap and FAQ seeding.

**Fix:** rebuild every widget inside the open window, keeping the retriever, sessions and threads. Apply the theme first and save it in the background. See [[learning/customtkinter-fast-theme-rebuild]] for the pattern and its traps.

**Side benefits:** the user stays on the same page, the window keeps its size and position, and in-flight replies, drafts and attachments survive.

**Still open**
- The Admin Dashboard takes about 12s with the UI frozen. It only happens when the OS flips light/dark for a System-theme admin on that page, and the fix belongs in that page's 3,000-4,000 widgets.
- `wj-documentation.md` §6 still describes the old `request_theme_rebuild` behaviour. One app session now spans a theme change, which affects how session trace data reads.

## 3. Destructive button label

"Del All" in User Management deletes the account **and** the chat history. The first requested label, "Delete All Chat", read as if the account would survive, so it became **Del Account + Chat**, matching its neighbour "Del Account". The Actions column minimum rose from 240px to 305px in both the table and its separate header grid, so they stay aligned.

**Lesson:** when renaming a destructive action, check what the code really does before choosing the words.

## Process lessons

- **Measure before optimising.** The assumed cost (recolouring) was about 5% of the total.
- **Distrust a speed-up that looks too good.** The first top-down destroy was fast partly because it silently skipped cleanup. An error flood in the probe exposed it.
- **Label figures by what actually differed.** A "before tuning" column was corrected once it turned out only one change separated the two runs.
- **Render UI changes.** Screenshots and captured frames found the crash, and the piecemeal white repaint, that tests could not.

Related: [[concepts/customtkinter-widget-scaling]], [[examples/learnix-hci-caching-and-loading-session]], [[examples/learnix-fontsize-and-srl-pacing]].
