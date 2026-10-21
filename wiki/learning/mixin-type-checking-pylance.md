---
type: learning
status: resolved
created: 2026-10-21
updated: 2026-10-21
name: mixin-type-checking-pylance
description: Lesson — Pylance reports "Cannot access attribute X for class Mixin" for members that live on sibling mixins or the window class; fix with value-less annotations, TYPE_CHECKING method stubs and a type-only base class, with no runtime change.
metadata:
  type: feedback
---

# Type-checking mixin classes (Pylance / pyright)

**Project context**: Learnix `LearnixApp(ctk.CTk, TopbarPanel, SidebarPanel, ChatPanel, ...)` — each panel is a mixin that uses members created by its siblings or by `ctk.CTk`.

## Symptoms

`Cannot access attribute "_sidebar" for class "TopbarPanel*"`, then the same for `_main`, `_faq_view`, `_admin_view`, `winfo_width`, `bind`, `after_cancel`, `tk`. A checker only sees one class at a time, so anything defined elsewhere looks missing. The warnings were pre-existing and harmless at runtime.

## Fixes (none change runtime behaviour)

1. **Value-less class annotations** for attributes created elsewhere. A bare `_sidebar: ctk.CTkFrame` creates no class attribute (checked: `hasattr` is `False`):

```python
class TopbarPanel(_Base):
    _sidebar:  ctk.CTkFrame            # SidebarPanel
    _user:     dict                    # LearnixApp
    _trace_log: Any
```

2. **`if TYPE_CHECKING:` method stubs** for methods defined on siblings:

```python
    if TYPE_CHECKING:
        def _trace(self, event: str, *, session_id: str | None = None, **detail) -> None: ...
        def _populate_admin(self) -> None: ...
```

3. **A type-only base class** so Tk methods resolve, while the runtime base stays `object`:

```python
_Base = ctk.CTk if TYPE_CHECKING else object
class TopbarPanel(_Base): ...
```

Confirmed: `TopbarPanel.__mro__ == (TopbarPanel, object)` and `LearnixApp`'s MRO is unchanged.

4. **Dynamically created module constants** (`globals().update(palette)` in `theme.py`) show as `"BLUE" is unknown import symbol` everywhere. Bare annotations were **not enough** for Pylance; real assignments were (`BLUE: str = _DARK["BLUE"]` for every key, before the dynamic update).

## Smaller ones in the same pass

- `width=inner_w` (a float) → `round(inner_w)` for a parameter typed `int`.
- A function parameter typed `dict` that is compared with `None` → `dict | None`.

## Checking without installing pyright

Ask the editor: the VS Code `getDiagnostics` tool returns the Problems-panel list for a file, so the fix can be verified directly. Hints like "is not accessed" remain and are not errors.

**See also**: [[concepts/customtkinter-window-lifecycle]], [[concepts/customtkinter-widget-scaling]].
