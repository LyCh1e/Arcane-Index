---
type: example
title: "ICT2216 Project — UMD Prototype to Vite + React SPA Refactor"
course: ICT2216
tags: [example, lab, ict2216, vite, react, react-router, spa, refactor]
created: 2026-05-25
updated: 2026-05-25
---

# ICT2216 Project — UMD Prototype to Vite + React SPA Refactor

**Project:** TrialGuard — Secure Clinical Trial Participant Portal  
**Relates to:** [[concepts/security-by-design-principles]], [[concepts/server-side-web-development]], [[resources/vite]]

## Starting State

A vanilla multi-page HTML prototype using:
- UMD React + ReactDOM loaded via CDN `<script>` tags
- Babel standalone for in-browser JSX transpilation
- `Object.assign(window, {...})` to share components across pages
- `<a href="page.html">` for navigation between 6 pages
- Inline `const { useState } = React` destructuring throughout
- A tweaks-panel design tool bundled into the prototype

## Target State

A proper Vite + React 18 + React Router v6 SPA launchable with `npm run dev`.

## Resulting Folder Structure

```
index.html              ← Vite entry (just <div id="root"> + module script)
vite.config.js
package.json
.gitignore              ← node_modules, dist, .claude
src/
  main.jsx              ← ReactDOM.createRoot + BrowserRouter
  App.jsx               ← Routes: /, /login, /signup, /patient, /admin, /researcher
  styles/
    global.css          ← CSS tokens (--sage, --coral, --cream…) + reset + landing styles
    portal.css          ← Portal component styles (.pa-root, .pa-card, .pa-btn…)
  data/
    landing.js          ← TG_TRIALS, TG_STEPS, TG_FAQ, TG_STATS, TG_QUOTES
    portal.js           ← PORTAL_TRIALS, PORTAL_COHORT, PORTAL_REPORTS, PORTAL_AUDIT…
  components/
    shared.jsx          ← TgLogo, Icon, FaqList, EmailCapture, EligibilityQuiz, TrialCard
    portal-shell.jsx    ← PortalTopbar, PortalSide, PortalHead, PortalModal, PortalConfirm
  pages/
    Landing.jsx
    Login.jsx           ← AuthFrame + AuthField local; useNavigate for redirect
    Signup.jsx          ← 3-step wizard; Fragment named import for keyed steps
    PatientPortal.jsx
    AdminPortal.jsx     ← useEffect for modal-open form reset
    ResearcherPortal.jsx
```

## Key Migration Patterns

### 1. Replace UMD + Babel with Vite

**Before (in every HTML file):**
```html
<script src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<script type="text/babel" src="shared.jsx"></script>
```

**After:**
```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
export default defineConfig({ plugins: [react()] })
```
```html
<!-- index.html -->
<script type="module" src="/src/main.jsx"></script>
```

### 2. Replace Global Window Exposure with ES Modules

**Before:**
```js
// shared.jsx
function TgLogo() { ... }
function Icon() { ... }
Object.assign(window, { TgLogo, Icon })
```

**After:**
```js
// src/components/shared.jsx
export function TgLogo() { ... }
export function Icon() { ... }
```

### 3. Replace HTML Navigation with React Router

**Before:**
```jsx
<a href="login.html">Sign in</a>
<button onClick={() => window.location.href = 'patient.html'}>Go</button>
```

**After:**
```jsx
import { Link, useNavigate } from 'react-router-dom'
// ...
<Link to="/login">Sign in</Link>
// ...
const navigate = useNavigate()
navigate('/patient')
```

### 4. Replace React Destructuring with ES Imports

**Before (in every file):**
```js
const { useState, useEffect } = React
```

**After:**
```js
import { useState, useEffect } from 'react'
```

## Bugs Found During Migration

See [[learning/vite-react-spa-migration]] for full details. Summary:
1. `React.Fragment` with `key` requires named `Fragment` import — not namespace access
2. `useState` mistakenly used instead of `useEffect` for side-effect-on-open pattern
3. `position: absolute` on modal overlay breaks in SPA — must use `position: fixed`

## Build Output

```
vite v6.4.2 building for production...
✓ 42 modules transformed
dist/index.html        0.78 kB │ gzip:  0.44 kB
dist/assets/*.css     18.08 kB │ gzip:  3.79 kB
dist/assets/*.js     274.08 kB │ gzip: 78.78 kB
✓ built in 1.53s
```
