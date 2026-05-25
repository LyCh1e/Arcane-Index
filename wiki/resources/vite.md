---
type: resource
title: "Vite — Frontend Build Tool"
tags: [resource, tool, vite, react, frontend, build-tool]
created: 2026-05-25
updated: 2026-05-25
---

# Vite

**Type:** Build tool / dev server  
**Domain:** web-development, frontend  
**URL:** https://vitejs.dev

## What It Is

Vite is the standard build tool for modern React (and Vue/Svelte) projects. It replaces the old Create React App (CRA) and Babel standalone approach. Key advantages:
- Near-instant dev server startup (serves ES modules natively, no bundling on start)
- Hot Module Replacement (HMR) — changes reflect in < 100 ms
- Production build via Rollup (fast, tree-shaken)
- Zero-config JSX support via `@vitejs/plugin-react`

## Minimal React Setup

```bash
npm install react react-dom react-router-dom
npm install -D vite @vitejs/plugin-react
```

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
export default defineConfig({ plugins: [react()] })
```

```html
<!-- index.html (project root, not inside src/) -->
<!DOCTYPE html>
<html lang="en">
  <head>...</head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

```json
// package.json scripts
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

## Common Commands

| Command | What it does |
|---------|-------------|
| `npm run dev` | Start dev server (usually http://localhost:5173) |
| `npm run build` | Build for production into `dist/` |
| `npm run preview` | Preview the production build locally |

## .gitignore

```
node_modules
dist
```

## When to Use vs Alternatives

| Scenario | Tool |
|----------|------|
| New React app | Vite (`npm create vite@latest`) |
| React + SSR / file-based routing | Next.js |
| Quick prototype (no build step) | UMD CDN + Babel standalone (throwaway only) |
| Full-stack React + server | Remix |

## Notes

- `index.html` lives at the **project root**, not inside `src/` — Vite uses it as the entry point directly
- CSS files imported in `main.jsx` are bundled automatically — no `<link>` tag needed in HTML
- CSS custom properties (`:root { --color: ... }`) work exactly the same as in plain HTML
