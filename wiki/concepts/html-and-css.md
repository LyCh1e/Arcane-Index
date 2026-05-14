---
type: concept
title: "HTML and CSS"
domain: web-development
source: [[sources/INF1005-web-systems-technologies]]
complexity: medium
updated: 2026-05-14
tags: [concept, web-development, html, css, flexbox, grid, responsive-design, accessibility]
---

# HTML and CSS

Covers HTML5 document structure, semantic elements, tables, forms, CSS selectors, the cascade, the box model, Flexbox, Grid, responsive design, animations, and accessibility.

---

## Part A: HTML

### 1. HTML Document Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Page Title</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Visible content here -->
</body>
</html>
```

- `<!DOCTYPE html>` — tells the browser the document type (not the HTML version)
- `<html lang="en">` — root element; optional but useful `lang` attribute
- `<head>` — metadata: title, charset, stylesheets, scripts
- `<body>` — all visible content

### 2. Key HTML Elements

#### Semantic Markup Philosophy

HTML should describe **structure and meaning**, not presentation. Appearance belongs in CSS.

**Benefits**: maintainability, performance (smaller files), accessibility (screen readers), SEO.

#### Text and Inline Elements

| Element | Purpose |
|---------|---------|
| `<p>` | Paragraph (block) |
| `<div>` | Generic block container (no semantic meaning) |
| `<span>` | Generic inline container |
| `<strong>` | Strong importance |
| `<em>` | Emphasis |
| `<br>` | Line break |
| `<hr>` | Thematic break |
| `<a href="url">` | Hyperlink |
| `<abbr>`, `<cite>`, `<code>`, `<mark>`, `<time>` | Semantic inline elements |

#### Links

```html
<!-- External (absolute URL) -->
<a href="https://www.example.com">External</a>

<!-- Internal (relative URL) -->
<a href="about.html">About</a>

<!-- Same-page anchor -->
<a href="#section2">Jump</a>

<!-- Email -->
<a href="mailto:user@example.com">Email Us</a>
```

#### Images

```html
<img src="photo.jpg" alt="Descriptive text" width="300" height="200">
```

`alt` is **required** for accessibility. Never omit it.

#### Lists

```html
<ul><li>Unordered item</li></ul>
<ol><li>Ordered item</li></ol>
<dl><dt>Term</dt><dd>Definition</dd></dl>
```

#### Character Entities

| Entity | Character |
|--------|-----------|
| `&nbsp;` | Non-breaking space |
| `&lt;` / `&gt;` | `<` / `>` |
| `&copy;` | © |
| `&euro;` | € |

### 3. HTML5 Semantic Structure Elements

| Element | Purpose |
|---------|---------|
| `<header>` | Page or section header |
| `<nav>` | Navigation links |
| `<main>` | Primary page content |
| `<section>` | Thematic grouping |
| `<article>` | Self-contained content |
| `<aside>` | Related but tangential content |
| `<figure>` / `<figcaption>` | Illustration with caption |
| `<footer>` | Page or section footer |
| `<details>` / `<summary>` | Accordion/disclosure (no JS needed) |
| `<address>` | Contact information |
| `<blockquote>` | Quotation from another source |

### 4. HTML Tables

```html
<table>
  <caption>Sales Data</caption>
  <thead>
    <tr><th scope="col">Product</th><th scope="col">Sales</th></tr>
  </thead>
  <tbody>
    <tr><td>Widget A</td><td>100</td></tr>
  </tbody>
  <tfoot>
    <tr><td>Total</td><td>100</td></tr>
  </tfoot>
</table>
```

- `colspan` — cell spans multiple columns; `rowspan` — multiple rows
- `border-collapse: collapse` — adjacent cells share borders
- **Tables are for data, not for layout**

### 5. HTML Forms

#### How Forms Work

1. User fills in fields
2. Browser encodes data as a query string (`name=value&name2=value2`)
3. Sends via HTTP GET or POST
4. Server processes and returns response

```html
<form action="process.php" method="post">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" required>
  <input type="submit" value="Submit">
</form>
```

#### Form Controls

| Element | Purpose |
|---------|---------|
| `<input type="text/password/email/number/date">` | Text input variants |
| `<input type="checkbox/radio">` | Boolean / single-choice |
| `<input type="file">` | File upload |
| `<input type="hidden">` | Hidden data passed to server |
| `<input type="submit/reset">` | Form actions |
| `<select>` | Dropdown list |
| `<textarea>` | Multi-line text |
| `<datalist>` | Predefined input suggestions |
| `<fieldset>` / `<legend>` | Group related inputs |

#### Input Validation Layers

| Layer | Guarantees | Notes |
|-------|------------|-------|
| HTML5 (`required`, `type`, `min/max`) | None — bypassed by disabling JS | Good UX hint |
| JavaScript | None — can be disabled | Improves UX |
| **Server-side** | **Only guaranteed validation** | **Always required** |

---

## Part B: CSS

### 6. CSS Fundamentals

```css
selector {
  property: value;
}
```

A **rule** = selector + declaration block. CSS is placed inline (highest specificity), embedded (`<style>`), or external (`<link>` — recommended, cacheable).

### 7. Selectors

#### Basic Selectors

| Selector | Description | Example |
|----------|-------------|---------|
| Element | All instances | `p { }` |
| Universal | All elements | `* { }` |
| Class | Elements with class | `.highlight { }` |
| ID | Single element | `#header { }` |
| Group | Multiple selectors | `h1, h2, h3 { }` |

#### Attribute Selectors

| Pattern | Matches |
|---------|---------|
| `[attr]` | Has the attribute |
| `[attr="val"]` | Exact match |
| `[attr^="val"]` | Starts with |
| `[attr$="val"]` | Ends with |
| `[attr*="val"]` | Contains |

#### Pseudo-Classes and Pseudo-Elements

| Selector | Meaning |
|----------|---------|
| `:hover` | Mouse over element |
| `:first-child` | First child of parent |
| `:nth-child(n)` | nth child |
| `a:link` / `a:visited` | Link states |
| `::first-letter` / `::first-line` | Part of text |

#### Combinators (Contextual Selectors)

| Combinator | Character | Selects |
|------------|-----------|---------|
| Descendant | ` ` (space) | All descendants |
| Child | `>` | Direct children only |
| Adjacent sibling | `+` | Immediately following sibling |
| General sibling | `~` | All following siblings |

### 8. The Cascade

When rules conflict, CSS resolves using:

1. **Inheritance** — font, colour, text properties inherit; layout, border, background do not
2. **Specificity** — ID `>` Class `>` Element. Full order (highest → lowest): `!important` → inline → ID → class/attribute/pseudo-class → element/pseudo-element → universal
3. **Location** — when specificity is equal, later rules win

### 9. The Box Model

```
[ margin ]
  [ border ]
    [ padding ]
      [ content ]
```

- **Content** — actual text/images
- **Padding** — space inside the border
- **Border** — around padding + content
- **Margin** — space outside the border

**Collapsing margins**: vertical margins between elements collapse to the larger value. Horizontal margins never collapse.

**Border-box sizing** (recommended):
```css
* { box-sizing: border-box; }
```
Makes `width`/`height` include padding and border.

### 10. Text and Colour Styling

```css
/* Font */
font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
font-size: 1rem;
font-weight: bold;
font-style: italic;

/* Text */
text-align: center;
text-decoration: underline;
line-height: 1.5;
text-transform: uppercase;

/* Colour */
color: #FF0000;           /* Hex */
color: rgb(255, 0, 0);   /* RGB */
color: rgba(255,0,0,0.5);/* RGBa — with transparency */
color: hsl(0, 100%, 50%);/* HSL */
```

**CSS Custom Properties (Variables)**:
```css
:root {
  --primary: #431c5d;
  --spacing: 20px;
}
.box { background: var(--primary); padding: var(--spacing); }
```

---

## Part C: CSS Layout

### 11. Positioning

| Value | Behaviour |
|-------|-----------|
| `static` | Default — normal document flow |
| `relative` | Offset from its normal position; stays in flow |
| `absolute` | Positioned relative to nearest positioned ancestor; removed from flow |
| `fixed` | Fixed in the viewport; does not scroll |
| `sticky` | Scrolls normally then sticks when it hits a threshold |

**Float**: displaces element from normal flow; content reflows around it. Requires a width. Mostly replaced by Flexbox/Grid.

### 12. Flexbox

For **one-dimensional** layout (row or column).

```css
.container {
  display: flex;
  flex-direction: row;          /* or column */
  flex-wrap: wrap;
  justify-content: space-between; /* main axis */
  align-items: center;          /* cross axis */
}
.item { flex: 1; }              /* grow/shrink equally */
```

| Property | Values |
|----------|--------|
| `flex-direction` | `row`, `column`, `row-reverse`, `column-reverse` |
| `flex-wrap` | `nowrap`, `wrap` |
| `justify-content` | `flex-start`, `center`, `space-between`, `space-around`, `flex-end` |
| `align-items` | `stretch`, `center`, `flex-start`, `flex-end` |

### 13. CSS Grid

For **two-dimensional** layout (rows and columns).

```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: 100px auto;
  gap: 10px;
}
.item {
  grid-column: 1 / 3;   /* span column lines 1 to 3 */
  grid-row: 1 / 2;
}
```

- `fr` unit — fraction of available space
- `repeat(3, 1fr)` — 3 equal columns
- **Best practice**: use Grid for page structure; Flexbox for aligning content within cells

### 14. Responsive Design

#### Viewport Meta Tag (required for mobile)

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Without this, mobile browsers shrink the desktop layout.

#### Mobile-First Approach

Write default styles for mobile; use `min-width` media queries to progressively enhance for larger screens.

```css
/* Mobile (default) */
.container { flex-direction: column; }

/* Tablet */
@media (min-width: 768px) { .container { flex-direction: row; } }

/* Desktop */
@media (min-width: 1024px) { .container { max-width: 1200px; } }
```

#### Responsive Images

```css
img { max-width: 100%; }
```

Use `<picture>` to serve different image files at different viewport sizes.

### 15. CSS Effects

#### Transitions

```css
.button {
  background: blue;
  transition: background-color 0.3s ease;
}
.button:hover { background: darkblue; }
```

#### Animations (Keyframes)

```css
@keyframes slideIn {
  from { transform: translateX(-100%); }
  to   { transform: translateX(0); }
}
.element { animation: slideIn 0.5s ease-out; }
```

#### Transforms

```css
.box { transform: rotate(45deg) scale(1.2) translateX(20px); }
```

#### Filters

```css
.grey { filter: grayscale(100%); }
.blur { filter: blur(5px); }
```

### 16. CSS Preprocessors (Sass)

Sass adds variables, nesting, and mixins — compiled to regular CSS.

```scss
$primary: #647ACB;

.container {
  .sidebar {
    color: $primary;
    h2 { font-size: 18px; }
  }
}

@mixin button-style($bg) {
  background: $bg;
  border-radius: 5px;
}
```

---

## Part D: Accessibility and Validation

### 17. WCAG — Web Content Accessibility Guidelines (POUR)

| Principle | Requirement |
|-----------|-------------|
| **Perceivable** | Text alternatives for non-text content (e.g., `alt` on images) |
| **Operable** | All functionality keyboard-accessible |
| **Understandable** | Content and UI must be understandable |
| **Robust** | Works with current and future assistive technologies |

**Key practices**:
- `alt` text on all images
- Semantic HTML (`<nav>`, `<header>`, `<main>`, etc.)
- `<label for="inputId">` for form inputs
- `<caption>` and `scope` in tables
- Sufficient colour contrast
- W3C validator at `validator.w3.org`

---

## See Also

- [[concepts/web-fundamentals|Web Fundamentals]] — HTTP, DNS, browser rendering
- [[concepts/javascript-fundamentals|JavaScript Fundamentals]] — client-side interactivity and DOM manipulation
- [[concepts/server-side-web-development|Server-Side Web Development]] — server generates the HTML these styles are applied to
- [[sources/INF1005-web-systems-technologies|INF1005 Source Page]]
