---
type: learning
title: "Bugs and Lessons — Vite + React SPA Migration from UMD Prototype"
tags: [learning, vite, react, react-router, spa, bugs]
created: 2026-05-25
updated: 2026-05-25
---

# Bugs and Lessons — Vite + React SPA Migration from UMD Prototype

Lessons from migrating the TrialGuard prototype (UMD/CDN React) to a proper Vite + React 18 + React Router v6 SPA. See [[examples/ict2216-project-vite-refactor]] for the full worked example.

---

## Bug 1: `React.Fragment` with `key` requires named import

**Symptom:** JSX error — `React` is not defined when using `<React.Fragment key={n}>`.

**Root cause:** When you import `{ useState } from 'react'` you don't get the `React` namespace object, so `React.Fragment` is undefined.

**Fix:**
```jsx
// Wrong
import { useState } from 'react'
// ...
<React.Fragment key={n}>...</React.Fragment>

// Correct
import { useState, Fragment } from 'react'
// ...
<Fragment key={n}>...</Fragment>
```

**Rule:** Never use `React.Anything` unless you have `import React from 'react'`. Prefer named imports (`Fragment`, `memo`, `forwardRef`) which are always safe.

---

## Bug 2: `useState` used instead of `useEffect` for modal-open side effects

**Symptom:** Form fields didn't reset when a modal was opened; the reset callback accepted a deps array, which `useState` ignores (it only uses the initial-value argument once).

**Root cause:** A copy-paste error — the side-effect call signature looked like `useState(() => { ... }, [dep])` but the second argument is meaningless to `useState`.

**Fix:**
```jsx
// Wrong — useState ignores the second argument
useState(() => {
  if (open) { setForm({ name: '', email: '' }) }
}, [open])

// Correct
useEffect(() => {
  if (open) { setForm({ name: '', email: '' }) }
}, [open])
```

**Rule:** Any code that must re-run when props/state changes is a side effect → `useEffect`. Initial state setup → `useState`. The confusion arises because both accept a function as first arg.

---

## Bug 3: `position: absolute` modal overlay breaks in SPA

**Symptom:** Modal background covered only a portion of the screen in the SPA, but had worked fine in the multi-page HTML prototype.

**Root cause:** `position: absolute` is relative to the nearest positioned ancestor. In a multi-page HTML file with no positioned ancestors, it happened to cover the whole viewport. In the SPA, the `pa-root` container has `position: relative`, making the absolute overlay relative to it rather than the viewport.

**Fix:**
```css
/* Wrong for SPA */
.pa-modal-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
}

/* Correct */
.pa-modal-bg {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
}
```

**Rule:** Full-screen overlays (modals, drawers, toasts) always use `position: fixed`. `absolute` is only appropriate when intentionally scoping to a container.

---

## Pattern: Removing UMD/CDN React

When migrating from CDN UMD to Vite:

1. Delete all `<script src="cdn...react...">` tags from HTML
2. Delete `<script src="babel...">` and change `type="text/babel"` to `type="module"`
3. Replace all `const { useState, useEffect } = React` → `import { useState, useEffect } from 'react'`
4. Replace all `Object.assign(window, {...})` → named ES exports
5. Replace all `window.ComponentName` usages → `import { ComponentName } from './path'`
6. `window.location.href = 'page.html'` → `useNavigate()` + `navigate('/route')`
7. `<a href="page.html">` → `<Link to="/route">`

---

## Pattern: `.gitignore` for Vite projects

```
node_modules
dist
```

Also ignore any editor/tool state files (`.design-canvas.state.json`, `.thumbnail`, `.claude`).
