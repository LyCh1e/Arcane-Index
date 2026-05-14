# INF1005 Web Systems & Technologies — Complete Notes
> *Based on Connolly & Hoar, "Fundamentals of Web Development" (3rd Edition) and lecture slides*

---

## Table of Contents

1. [The Internet](#1-the-internet)
2. [The World Wide Web](#2-the-world-wide-web)
3. [HTML5 and the Semantic Web](#3-html5-and-the-semantic-web)
4. [How the Web Works (Protocols, DNS, HTTP)](#4-how-the-web-works)
5. [HTML Introduction](#5-html-introduction)
6. [CSS — Selectors and Basic Styling](#6-css--selectors-and-basic-styling)
7. [HTML — Tables and Forms](#7-html--tables-and-forms)
8. [CSS — Layout](#8-css--layout)
9. [Web Validation and Accessibility](#9-web-validation-and-accessibility)
10. [JavaScript — Language Fundamentals](#10-javascript--language-fundamentals)
11. [JavaScript — Using JavaScript (DOM & Events)](#11-javascript--using-javascript-dom--events)
12. [JavaScript — Additional Features](#12-javascript--additional-features)
13. [Server-Side Development: PHP](#13-server-side-development-php)
14. [Form Processing](#14-form-processing)
15. [LAMP Stack](#15-lamp-stack)
16. [Database Operations with MySQL](#16-database-operations-with-mysql)
17. [Working with Databases (SQL & NoSQL)](#17-working-with-databases-sql--nosql)
18. [Server-Side Development: Node.js](#18-server-side-development-nodejs)
19. [Security](#19-security)
20. [DevOps and Hosting](#20-devops-and-hosting)
21. [Modern Web Technologies](#21-modern-web-technologies)

---

## 1. The Internet

### History
- The Internet originated in **1969 as ARPANET**, a project of the US Department of Defense.
- ARPANET used **packet switching** (not circuit switching): data is broken into packets that travel independently across the network and are reassembled at the destination.
- In January 1983, **TCP/IP** was adopted across all of ARPANET, unifying disparate networks.

### Circuit Switching vs Packet Switching
| Circuit Switching | Packet Switching |
|---|---|
| A continuous dedicated path is established | No continuous connection needed |
| Inefficient use of bandwidth | Efficient — packets share links |
| Like a traditional phone call | Like email or web browsing |

### TCP/IP 5-Layer Model (simplified as 4)
| Layer | Role |
|---|---|
| **Application** | HTTP, FTP, SSH, DNS, SMTP |
| **Transport** | TCP (reliable, ordered), UDP (unreliable, fast) |
| **Internet (IP)** | Routing packets between networks |
| **Link** | Physical transmission; MAC addresses |

- **TCP** (Transmission Control Protocol): guarantees arrival and ordering of packets via sequence numbers and ACKs.
- **UDP** (User Datagram Protocol): no guarantee; used in streaming, VoIP, gaming, DNS.

### ARPANET Design Goals
- **Survivable** — tolerant of network failures
- **Simple** — easy to implement
- **Scalable** — able to grow
- **Selectable** — multiple paths available

### Benefits of the Internet
- Fully decentralized — no single point of failure.
- Intelligence at the edge; routing is simple and scalable.
- Low cost — affordable connectivity; VPNs create private networks over public infrastructure.
- Supports client-server and peer-to-peer models.

### Domain Name Service (DNS)
- Translates human-readable **hostnames** (e.g., `www.amazon.com`) to **IP addresses**.
- **Hostnames** are easy to remember, relocatable, and can map to multiple hosts.
- DNS resolvers perform two functions:
  - `gethostbyname()` — converts name → IP
  - `gethostbyaddr()` — converts IP → name
- A database of mappings is **cached** locally.

| Hostname | IP Address |
|---|---|
| singaporetech.edu.sg | 158.122.11.23 (IPv4) |
| apple.com | 2620:149:af0::10 (IPv6) |

> **Internet ≠ World Wide Web**: The Internet (1969) is the global network infrastructure. The Web (1989) is an application that runs *over* the Internet.

---

## 2. The World Wide Web

### History
- Developed in **1989 by Tim Berners-Lee** at CERN.
- Berners-Lee defined the core technologies:
  - **URL** — Uniform Resource Locator, uniquely identifies a web resource.
  - **HTTP** — Hypertext Transfer Protocol, defines request/response behavior.
  - **HTML** — Hypertext Markup Language, for publishing documents.
  - A **web server** to respond to HTTP requests.
  - A **browser** to make requests and display HTML.

### Client-Server Model
- **Clients**: desktops, laptops, phones, tablets — vary in OS, speed, screen size, memory.
- **Servers**: powerful machines that listen for and respond to HTTP requests.
  - Types: Web servers, Application servers, Database servers, Mail servers, Media servers, Authentication servers.
- Real-world deployments use **server farms**, **load balancers**, **failover redundancy**, and **cloud services** (elastic provisioning).

### Web 2.0
- Shifted the web from read-only (static) to interactive (dynamic) — users can both consume and contribute content.
- Programming logic began migrating from the server to the browser (requiring JavaScript).

### Web Applications vs. Desktop Applications
**Advantages of Web Apps:**
- Accessible from any Internet-enabled device.
- Cross-platform (different OSes and browsers).
- Easier software updates (only server-side update needed).
- Centralized data storage reduces local security concerns.

**Disadvantages of Web Apps:**
- Requires active Internet connection.
- Security concerns about data in transit.
- Cross-browser compatibility issues.
- Plugin restrictions (e.g., Flash on iOS).

---

## 3. HTML5 and the Semantic Web

### Three Main Goals of HTML5
1. **Improve the Native Web** — new elements like `<audio>`, `<video>`, `<canvas>` replace proprietary plugins.
2. **Do More with Less Code** — standardize common patterns (placeholder text, autofocus, client-side validation, date pickers).
3. **Realize the Semantic Web** — content that machines can understand, not just humans (Tim Berners-Lee's long-held vision).

### History of HTML
- **1990–1991**: Initial HTML and HTTP by Berners-Lee and Cailliau.
- **1995–1997**: W3C codifies HTML.
- **Mid-1990s "Browser Wars"**: Netscape vs IE — rapid but incompatible feature growth.
- **1998**: W3C freezes HTML at version 4.01.
- **XHTML**: Stricter XML-based version; XHTML 2.0 development dragged and was abandoned.
- **WHATWG** (Web Hypertext Application Technology Working Group) formed at Opera and Mozilla.
- **2009**: W3C adopts WHATWG's work as **HTML5**.
- **2014**: Major W3C endorsement of HTML5.

---

## 4. How the Web Works

### Internet Protocols
A **protocol** is a set of rules partners use when communicating. TCP/IP makes web development possible by handling low-level concerns (packet routing, transmission, checksums) automatically.

### The 4-Layer Network Model

#### Link Layer
- Lowest layer: physical transmission and logical link establishment.
- Handles packet creation, transmission, error detection, collisions.
- Uses **MAC (Media Access Control) addresses**.

#### Internet Layer (IP Layer)
- Routes packets between networks. Provides "best effort" — no guarantee.
- Uses **IP addresses** (numeric codes uniquely identifying destinations).
- **IPv4**: four 8-bit integers (e.g., `192.168.1.1`) — address space depleted in 2011.
- **IPv6**: eight 16-bit integers — vastly larger address space.
- **PAT (Port Address Translation)**: allows multiple devices to share one IPv4 address.

#### Transport Layer
- Ensures data arrives in order and without error (TCP).
- TCP breaks data into packets with sequence numbers; receiver sends ACKs; lost packets are retransmitted.
- **UDP**: no guarantee, used for streaming, VoIP, gaming, DNS.

#### Application Layer
- Familiar to web developers. Common protocols:
  - **HTTP** — web communication
  - **SSH** — remote command-line access to servers
  - **FTP** — file transfer
  - **POP/IMAP/SMTP** — email
  - **DNS** — domain name resolution

### Domain Name System (DNS)
- DNS maps domain names to IP addresses, separating the name from the host.
- Evolved from a simple `hosts` file to a distributed, hierarchical system.

#### Domain Name Structure
- **Top-Level Domains (TLDs)**:
  - **gTLD** (Generic): `.com`, `.net`, `.org`, `.info` (unrestricted); `.gov`, `.mil`, `.edu` (sponsored); new TLDs since 2012 (`.art`, `.cash`, etc.)
  - **ccTLD** (Country Code): `.sg`, `.uk`, `.ca` etc.
  - **IDN** (Internationalized): non-ASCII characters, deployed since 2009.
- **ICANN** oversees TLD management and accredits registrars.

#### DNS Address Resolution (10-step process)
1. Client makes domain request.
2. Check local DNS cache.
3. If not cached, request to primary DNS server.
4. Primary DNS server queries Root Name Server.
5. Root returns address of relevant TLD server.
6. DNS server queries TLD server.
7. TLD returns Authoritative DNS Server addresses.
8. DNS server queries Authoritative DNS Server.
9. IP address returned to DNS server.
10. Client makes request to the domain.

### Uniform Resource Locators (URLs)
Structure: `protocol://domain[:port][/path][?query][#fragment]`

| Component | Description | Example |
|---|---|---|
| Protocol | Connection type | `https://` |
| Domain | Server address | `www.example.com` |
| Port | Software connection point (optional) | `:8080` |
| Path | File/directory on server | `/blog/post` |
| Query String | Key-value pairs | `?id=42&lang=en` |
| Fragment | Page section | `#section2` |

- **Default ports**: HTTP = 80, HTTPS = 443.
- **Relative URLs**: used when referencing resources on the same server.

### HTTP (Hypertext Transfer Protocol)

#### HTTP Request Methods
| Method | Use |
|---|---|
| **GET** | Retrieve a resource; data sent via URL query string |
| **POST** | Send data to server (forms); data in request body |
| **HEAD** | Like GET but returns headers only |
| **PUT** | Update a resource |
| **DELETE** | Delete a resource |

#### HTTP Response Codes
| Code | Meaning |
|---|---|
| 200 OK | Successful request |
| 301 Moved Permanently | Resource permanently moved |
| 304 Not Modified | Cached version is up to date |
| 401 Unauthorized | Authentication required |
| 404 Not Found | Resource not found |
| 414 URI Too Long | Too much data in URL |
| 500 Internal Server Error | Server-side error |

#### HTTP Headers
- **Request headers**: Host, User-Agent, Cache settings.
- **Response headers**: Server, Last-Modified, Content-Type, Encoding.

### Web Browsers
- Request the initial HTML, then parse it to find all referenced resources (images, CSS, JS).
- The process of downloading, parsing, layout, and rendering is called **rendering**.

#### Browser Rendering Performance Metrics
- **TTFB** — Time to First Byte
- **FP** — First Paint
- **FCP** — First Contentful Paint
- **LCP** — Largest Contentful Paint
- **TTI** — Time to Interactive
- **CLS** — Cumulative Layout Shift

### Web Servers & Application Stacks
| Stack | Components |
|---|---|
| **LAMP** | Linux, Apache, MySQL, PHP |
| **MAMP** | macOS, Apache, MySQL, PHP |
| **WAMP** | Windows, Apache, MySQL, PHP |
| **MERN** | MongoDB, Express, React, Node.js |
| **WISA** | Windows, IIS, SQL Server, ASP.NET |
| **JAM** | JavaScript, APIs, Markup |

---

## 5. HTML Introduction

### What is HTML?
- A **markup language** — annotates content with structural meaning.
- HTML elements are identified by **tags** (e.g., `<p>`, `</p>`).
- Elements can have **attributes** (`name="value"` pairs).

### HTML Document Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Page Title</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Content goes here -->
</body>
</html>
```

- **DOCTYPE**: Tells the browser the document type (not the HTML version).
- **`<html>`**: Root element; optional `lang` attribute.
- **`<head>`**: Descriptive metadata — title, encoding, stylesheets, scripts.
- **`<body>`**: Visible content.

### Key HTML Elements

#### Headings
- Six levels: `<h1>` through `<h6>`.
- Choose semantically, not for visual size — use CSS for appearance.

#### Text Elements
- `<p>` — Paragraph (block-level)
- `<div>` — Generic block container (no semantic meaning)
- `<span>` — Generic inline container
- `<strong>` — Strong importance
- `<em>` — Emphasis
- `<br>` — Line break
- `<hr>` — Thematic break
- `<a href="url">` — Hyperlink (anchor)
- `<abbr>`, `<cite>`, `<code>`, `<mark>`, `<small>`, `<time>`

#### Links
```html
<!-- Absolute URL (external) -->
<a href="https://www.example.com">External Link</a>

<!-- Relative URL (internal) -->
<a href="about.html">About</a>

<!-- Fragment link (same page) -->
<a href="#section2">Jump to Section 2</a>

<!-- Email link -->
<a href="mailto:user@example.com">Email Us</a>
```

#### Relative URL Types
| Type | Syntax |
|---|---|
| Same directory | `file.html` |
| Child directory | `subdir/file.html` |
| Parent directory | `../file.html` |
| Root reference | `/path/file.html` |

#### Images
```html
<img src="photo.jpg" alt="Description" width="300" height="200" title="Tooltip">
```
- `alt` is required for accessibility.

#### Lists
```html
<!-- Unordered -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- Ordered -->
<ol>
  <li>First</li>
  <li>Second</li>
</ol>

<!-- Description list -->
<dl>
  <dt>Term</dt>
  <dd>Definition</dd>
</dl>
```

#### Character Entities
| Entity Name | Entity Number | Character |
|---|---|---|
| `&nbsp;` | `&#160;` | Non-breaking space |
| `&lt;` | `&#60;` | `<` |
| `&gt;` | `&#62;` | `>` |
| `&copy;` | `&#169;` | © |
| `&euro;` | `&#8364;` | € |
| `&trade;` | `&#8482;` | ™ |

### Semantic Markup
- HTML documents should describe **structure and meaning**, not presentation.
- Appearance is handled by CSS.

**Advantages:**
- **Maintainability** — easier to update.
- **Performance** — smaller files, faster downloads.
- **Accessibility** — screen readers work better.
- **SEO** — search engines understand the content.

### HTML5 Semantic Structure Elements
| Element | Purpose |
|---|---|
| `<header>` | Page or section header |
| `<nav>` | Navigation links |
| `<main>` | Primary content |
| `<section>` | Thematic grouping of content |
| `<article>` | Self-contained content |
| `<aside>` | Related but tangential content |
| `<figure>` | Self-contained illustration/image |
| `<figcaption>` | Caption for `<figure>` |
| `<footer>` | Page or section footer |
| `<details>` / `<summary>` | Accordion/disclosure widget (no JS needed) |
| `<blockquote>` | Quotation from another source |
| `<address>` | Contact information |

---

## 6. CSS — Selectors and Basic Styling

### What is CSS?
- **Cascading Style Sheets** — W3C standard for describing the appearance of HTML elements.
- Can assign fonts, colors, sizes, borders, backgrounds, positioning, and animations.

### Benefits of CSS
- Improved control over formatting.
- Improved site maintainability (centralized styles).
- Improved accessibility (separation of content and presentation).
- Improved page download speed (smaller HTML files).
- Enables **responsive design** (same content, different layouts).

### CSS Syntax
```css
selector {
  property: value;
  property: value;
}
```
A **rule** = selector + declaration block (one or more `property: value` declarations).

### CSS Versions
- CSS Level 1 (1996) → CSS2 (1997) → CSS2.1 (2011) → CSS3 (modular, ongoing).

### Where to Place CSS

| Location | Syntax | Notes |
|---|---|---|
| **Inline** | `style="..."` attribute | Only affects that element; highest specificity |
| **Embedded** | `<style>` in `<head>` | Applies to one HTML page |
| **External** | `<link rel="stylesheet" href="file.css">` | Recommended; reusable; cacheable |

### Selectors

#### Basic Selectors
| Selector | Description | Example |
|---|---|---|
| Element | All instances of that element | `p { }` |
| Universal | All elements | `* { }` |
| Class | Elements with that class | `.highlight { }` |
| ID | Element with that ID | `#header { }` |
| Group | Multiple selectors | `h1, h2, h3 { }` |

#### Attribute Selectors
| Pattern | Matches |
|---|---|
| `[attr]` | Has the attribute |
| `[attr="val"]` | Exact value match |
| `[attr~="val"]` | Word in space-separated list |
| `[attr^="val"]` | Starts with value |
| `[attr*="val"]` | Contains value |
| `[attr$="val"]` | Ends with value |

#### Pseudo-Class and Pseudo-Element Selectors
| Selector | Meaning |
|---|---|
| `a:link` | Unvisited link |
| `a:visited` | Visited link |
| `:hover` | Mouse pointer over element |
| `:active` | Element being clicked |
| `:first-child` | First child of its parent |
| `::first-letter` | First letter of element |
| `::first-line` | First line of element |
| `:nth-child(n)` | nth child |

#### Contextual (Combinator) Selectors
| Combinator | Character | Selects |
|---|---|---|
| Descendant | ` ` (space) | All descendants |
| Child | `>` | Direct children only |
| Adjacent Sibling | `+` | Immediately following sibling |
| General Sibling | `~` | All following siblings |

### The Cascade
When style rules conflict, CSS resolves using three principles:

1. **Inheritance** — font, color, list, text properties inherit; layout, sizing, border, background do not.
2. **Specificity** — more specific selectors win. ID > Class > Element.
3. **Location** — when specificity is equal, later rules win. Inline > Embedded > External.

### The CSS Box Model
Every HTML element lives inside a box:
```
[ margin ]
  [ border ]
    [ padding ]
      [ content ]
    [ padding ]
  [ border ]
[ margin ]
```
- **Content** — the element's actual text/images.
- **Padding** — space inside the border.
- **Border** — the border around padding and content.
- **Margin** — space outside the border.

**Collapsing Margins**: When vertical margins of two elements touch, only the larger margin is shown. Horizontal margins never collapse.

**Box sizing (border-box)**: More intuitive sizing where `width` and `height` include padding and border:
```css
* { box-sizing: border-box; }
```

### Block vs. Inline Elements
- **Block**: Each on its own line (`<p>`, `<div>`, `<h1-6>`, `<ul>`, `<table>`).
- **Inline**: Flow within text (`<span>`, `<a>`, `<em>`, `<img>`).

### CSS Text Styling

#### Font Properties
- `font-family` — font stack (fallbacks).
- `font-size` — `px`, `em`, `rem`, `%`.
- `font-weight` — `normal`, `bold`, 100–900.
- `font-style` — `normal`, `italic`.

**Web Font Stack**:
```css
font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
```

**Google Fonts**:
```html
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
```

#### Paragraph Properties
- `text-align` — `left`, `center`, `right`, `justify`.
- `text-decoration` — `none`, `underline`, `line-through`.
- `line-height` — spacing between lines.
- `letter-spacing` — space between characters.
- `text-transform` — `uppercase`, `lowercase`, `capitalize`.

### Color Values
| Method | Example |
|---|---|
| Named | `color: red;` |
| RGB | `color: rgb(255, 0, 0);` |
| Hex | `color: #FF0000;` |
| RGBa | `color: rgba(255, 0, 0, 0.5);` |
| HSL | `color: hsl(0, 100%, 50%);` |

### CSS Frameworks
- **Bootstrap** — comprehensive grid, components, and utilities.
- **Foundation** — flexible alternative.

### CSS Variables (Custom Properties)
```css
:root {
  --primary-color: #431c5d;
  --spacing: 20px;
}

.box {
  background-color: var(--primary-color);
  padding: var(--spacing);
}
```

---

## 7. HTML — Tables and Forms

### HTML Tables
Used for representing two-dimensional data.

```html
<table>
  <caption>Sales Data</caption>
  <thead>
    <tr>
      <th scope="col">Product</th>
      <th scope="col">Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Widget A</td>
      <td>100</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td>100</td>
    </tr>
  </tfoot>
</table>
```

- `colspan` — cell spans multiple columns.
- `rowspan` — cell spans multiple rows.
- **Borders**: assigned to `<table>` and `<td>`; not to `<tr>`, `<thead>`, `<tfoot>`, `<tbody>`.
- `border-collapse: collapse` — adjacent cells share borders.
- Tables should **not** be used for layout.

### HTML Forms

#### How Forms Work
1. User fills in form fields.
2. Browser encodes data as a **query string** (`name=value&name2=value2`).
3. Browser sends data to server via HTTP GET or POST.
4. Server processes data and returns a response.

#### The `<form>` Element
```html
<form action="process.php" method="post">
  <!-- form controls -->
</form>
```

- `action` — URL of the server-side processor.
- `method` — `GET` or `POST`.

#### GET vs POST
| GET | POST |
|---|---|
| Data visible in URL | Data hidden from URL |
| Can be bookmarked | Cannot be bookmarked |
| Stays in browser history | Not cached |
| Character limit on data | Supports binary data |
| Use for search/filtering | Use for login/form submission |

**Note**: POST does not encrypt data — use HTTPS for security.

#### Form Controls
| Element | Purpose |
|---|---|
| `<input type="text">` | Single-line text |
| `<input type="password">` | Masked text |
| `<input type="email">` | Email with validation |
| `<input type="number">` | Numeric input |
| `<input type="date">` | Date picker |
| `<input type="checkbox">` | Boolean option |
| `<input type="radio">` | Single choice from group |
| `<input type="file">` | File upload |
| `<input type="hidden">` | Hidden data |
| `<input type="submit">` | Submit button |
| `<input type="reset">` | Reset form |
| `<select>` | Dropdown list |
| `<textarea>` | Multi-line text |
| `<button>` | Custom button |
| `<datalist>` | Predefined options for input |

#### Form Accessibility
- Use `<fieldset>` and `<legend>` to group related inputs.
- Use `<label for="inputId">` to associate labels with inputs.
- Use `scope` attribute on `<th>` elements in tables.

### Input Validation
Validation can occur at three levels:
1. **HTML5 validation** — browser performs basic checks (`required`, `type`, `min`, `max`).
2. **JavaScript validation** — improves UX but **cannot be relied upon** (can be bypassed).
3. **Server-side validation** — the **only guaranteed validation**; always required.

**Types of validation:**
- Required fields
- Correct data type
- Correct format (patterns)
- Range checks
- Comparison (password confirmation)

---

## 8. CSS — Layout

### Older Layout Approaches
- **Float**: displaces element from normal flow, content reflows around it. A floated block element should have a width specified.
- **Positioning**: `position` property values:
  - `static` — default (normal flow)
  - `relative` — offset from normal position
  - `absolute` — positioned relative to nearest positioned ancestor; removed from flow
  - `fixed` — fixed in viewport; doesn't scroll
  - `sticky` — scrolls then sticks in place

### Flexbox Layout
Flexbox works on one axis at a time (row or column).

```css
.container {
  display: flex;
  flex-direction: row;    /* or column */
  flex-wrap: wrap;
  justify-content: space-between; /* main axis alignment */
  align-items: center;   /* cross axis alignment */
}

.item {
  flex: 1;               /* grow/shrink equally */
}
```

**Common flexbox container properties:**
- `flex-direction`: `row`, `column`, `row-reverse`, `column-reverse`
- `flex-wrap`: `nowrap`, `wrap`
- `justify-content`: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`
- `align-items`: `stretch`, `flex-start`, `flex-end`, `center`

### CSS Grid Layout
Grid works on two axes (rows and columns).

```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: 100px auto;
  gap: 10px;
}

.item {
  grid-column: 1 / 3;    /* span from column line 1 to 3 */
  grid-row: 1 / 2;
}
```

- `fr` unit — fraction of available space.
- `repeat()` function — `grid-template-columns: repeat(3, 1fr)`.
- **Grid areas** — named regions for explicit placement.
- **Best practice**: Use Grid for page layout structure; Flexbox for aligning contents within a cell.

### Responsive Design
Page "responds" to browser/device size, going beyond simple percentage scaling.

#### Mobile-First Design
Design the mobile version first, then progressively enhance for larger screens. Forces focus on essential content.

#### Viewport Meta Tag
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
Without this, mobile browsers scale down the desktop page.

#### Media Queries
```css
/* Mobile first (default styles) */
.container { flex-direction: column; }

/* Tablet */
@media (min-width: 768px) {
  .container { flex-direction: row; }
}

/* Desktop */
@media (min-width: 1024px) {
  .container { max-width: 1200px; }
}
```

#### Responsive Images
```css
img { max-width: 100%; }
```
The `<picture>` element allows serving different images at different sizes.

### CSS Effects

#### Transforms
Rotate, skew, scale, and translate elements:
```css
.box {
  transform: rotate(45deg) scale(1.2) translateX(20px);
}
```

#### Filters
```css
.grayscale { filter: grayscale(100%); }
.blur { filter: blur(5px) hue-rotate(60deg); }
```

#### Transitions
```css
.button {
  background-color: blue;
  transition: background-color 0.3s ease 0s;
}
.button:hover {
  background-color: darkblue;
}
```
Properties: `transition-property`, `transition-duration`, `transition-timing-function`, `transition-delay`.

#### Animations (Keyframes)
```css
@keyframes slideIn {
  from { transform: translateX(-100%); }
  to   { transform: translateX(0); }
}

.element {
  animation: slideIn 0.5s ease-out;
}
```

### CSS Preprocessors (Sass)
CSS has limitations (no variables pre-2018, no encapsulation, no modularity). **Sass** addresses these.

```scss
$primary-color: #647ACB;
$spacing: 20px;

.container {
  .sidebar {
    color: $primary-color;
    h2 { font-size: 18px; }
  }
}

@mixin button-style($bg) {
  background: $bg;
  border-radius: 5px;
}
```
Sass is compiled to regular CSS via command line or GUI tool.

---

## 9. Web Validation and Accessibility

### Web Validation

#### W3C (World Wide Web Consortium)
- Governs web standards; develops recommendations.
- Founded in 1994 by Tim Berners-Lee.

#### W3C Markup Validation Service
- Validates HTML documents against the specification.
- Catches syntax errors, missing attributes, improper nesting.
- URL: `validator.w3.org`

### Web Accessibility

#### W3C Web Accessibility Initiative (WAI)
- Created in 1997 to improve accessibility of websites.
- Developed the **Web Content Accessibility Guidelines (WCAG)**.

#### WCAG Four Principles (POUR)
| Principle | Meaning |
|---|---|
| **Perceivable** | Users can perceive all content (e.g., text alternatives for images) |
| **Operable** | All functionality usable via keyboard |
| **Understandable** | Content and operation must be understandable |
| **Robust** | Works with current and future assistive technologies |

#### Key Accessibility Practices
- Provide `alt` text for all images.
- Use semantic HTML (`<nav>`, `<header>`, `<main>`, etc.).
- Associate form `<label>` with inputs using `for` attribute.
- Use `<caption>` and `scope` in tables.
- Ensure sufficient colour contrast.
- Keyboard navigable interfaces.

#### Testing Tools
- **Deque's axe browser plugin** — automated accessibility testing.

---

## 10. JavaScript — Language Fundamentals

### What is JavaScript?
- **Object-oriented, dynamically typed scripting language**.
- Primarily a **client-side** scripting language (runs in the browser).
- Variables are objects with properties and methods.
- Functions are also objects.
- **Dynamically typed** (weakly typed) — variables can hold any type.

### History
- Introduced by Netscape in Navigator browser, 1996.
- Submitted to Ecma International in 1997 → **ECMAScript**.
- **ES6 (2015)**: Major additions — classes, arrow functions, promises, iterators, let/const.
- Latest: ES2020 (ES11) and beyond.

### Where JavaScript Goes
| Type | Syntax | Notes |
|---|---|---|
| Inline | `onclick="..."` attribute | Discouraged |
| Embedded | `<script>` in HTML | Works but mixes concerns |
| External | `<script src="file.js">` | Recommended |

### Variables and Data Types

#### Declaration
```javascript
var x = 5;    // function-scoped, hoisted (old style)
let y = 10;   // block-scoped
const z = 15; // block-scoped, constant
```

#### Primitive Types
| Type | Description |
|---|---|
| `Boolean` | `true` or `false` |
| `Number` | 64-bit float (integers and decimals) |
| `String` | Text, single or double quotes |
| `Null` | Intentional absence of value |
| `Undefined` | Variable declared but not assigned |
| `Symbol` | Unique key (ES2015) |

#### Truthy and Falsy
- **Falsy**: `false`, `null`, `""`, `''`, `0`, `NaN`, `undefined`.
- **Truthy**: everything else.

### Output Methods
```javascript
alert("message");           // Browser popup
prompt("question");         // User input popup
console.log("message");     // Browser console
document.write("markup");   // Write to document (use sparingly)
```

### Operators and Control Flow

#### Comparison Operators
- `==` loose equality (type coercion)
- `===` strict equality (no coercion) — **preferred**
- `!=`, `!==`, `<`, `>`, `<=`, `>=`

#### Conditionals
```javascript
if (x > 0) {
  // ...
} else if (x === 0) {
  // ...
} else {
  // ...
}

// Switch
switch (value) {
  case "A": result = "Alpha"; break;
  case "B": result = "Beta"; break;
  default: result = "Other";
}

// Ternary (conditional) operator
let label = x > 0 ? "positive" : "non-positive";
```

#### Loops
```javascript
while (count < 10) { count++; }
do { count++; } while (count < 10);
for (let i = 0; i < 10; i++) { /* ... */ }
for (let item of array) { /* ... */ }  // ES6
```

### Arrays
```javascript
const years = [1855, 1648, 1420];
const countries = ["Canada", "France", "Germany"];

// Access
console.log(countries[0]);   // "Canada"

// Destructuring
let [first, second, third] = countries;

// Common array methods
years.push(2024);            // Add to end
years.pop();                 // Remove from end
years.length;                // Length
```

### Objects
```javascript
// Object literal notation
const photo = {
  id: 1,
  title: "Central Library",
  location: {
    country: "Canada",
    city: "Calgary"
  }
};

// Access properties
photo.title;
photo["title"];

// Destructuring
let { id, title } = photo;
let { country, city } = photo.location;

// Spread
const copy = { ...photo, extra: "value" };
```

### JSON (JavaScript Object Notation)
- Language-independent data interchange format.
- Property names must be in **double quotes**.
```javascript
const jsonString = '{"name": "Alice", "age": 30}';
const obj = JSON.parse(jsonString);   // string → object
const str = JSON.stringify(obj);      // object → string
```

### Functions
```javascript
// Function declaration (hoisted)
function subtotal(price, quantity) {
  return price * quantity;
}

// Function expression (anonymous)
const calc = function(price, qty) { return price * qty; };

// Arrow syntax (ES6)
const tax = () => 0.05;
const add = (a, b) => a + b;

// Default parameters
function greet(name = "World") { return "Hello " + name; }

// Rest parameters
function sum(...args) {
  return args.reduce((a, b) => a + b, 0);
}
```

### Scope
| Scope | Keyword | Accessible |
|---|---|---|
| Global | `var` (outside functions) | Everywhere |
| Function (Local) | `var`, `let`, `const` | Within the function |
| Block | `let`, `const` | Within `{}` block |
| Module | — | Within the module file |

> **Hoisting**: Function declarations are moved to the top of their scope. Variable declarations (not assignments) with `var` are also hoisted.

### Closures
A closure is a function that retains access to its enclosing scope even after that scope has finished executing.

```javascript
function makeCounter() {
  let count = 0;
  return function() { return ++count; };
}
const counter = makeCounter();
counter(); // 1
counter(); // 2
```

### Classes (ES6)
```javascript
class Customer {
  constructor(name, address) {
    this.name = name;
    this.address = address;
  }
  output() {
    return `${this.name}, ${this.address}`;
  }
}

class PremiumCustomer extends Customer {
  constructor(name, address, discount) {
    super(name, address);
    this.discount = discount;
  }
}
```

---

## 11. JavaScript — Using JavaScript (DOM & Events)

### The Document Object Model (DOM)
The DOM is how the browser represents an HTML page internally — as a **tree** of **nodes**.

- **document** — root object representing the entire HTML document.
- **nodes** — each element, attribute, or text in the HTML.
- **NodeList** — a collection of nodes (like an array).

### Selecting DOM Elements
```javascript
// By ID
document.getElementById("myId");

// By class name
document.getElementsByClassName("myClass");

// By tag name
document.getElementsByTagName("p");

// CSS selector (first match)
document.querySelector("#main .highlight");

// CSS selector (all matches)
document.querySelectorAll("ul li");
```

### Key Element Properties
| Property | Description |
|---|---|
| `innerHTML` | All content (text + tags) — use carefully (XSS risk) |
| `textContent` | Text only (no tags) — safer |
| `id` | Element's id |
| `className` | Element's class attribute |
| `classList` | List of classes; methods: `add()`, `remove()`, `toggle()` |
| `style` | Access inline CSS properties |
| `value` | For form inputs |
| `href` | For `<a>` elements |
| `src` | For `<img>`, `<script>` elements |

### Modifying the DOM

#### Changing Style
```javascript
const el = document.getElementById("box");
el.style.backgroundColor = "#ff0000";
el.classList.add("highlight");
el.classList.toggle("active");
```

#### Changing Content
```javascript
element.textContent = "New text";         // Safe
element.innerHTML = "<strong>Bold</strong>"; // Use cautiously
```

#### DOM Manipulation Methods
```javascript
// Create new elements
const div = document.createElement("div");
const text = document.createTextNode("Hello");

// Add to DOM
parent.appendChild(child);
parent.insertBefore(newChild, referenceChild);

// Remove from DOM
parent.removeChild(child);
```

### Event Handling
```javascript
// Modern approach
element.addEventListener("click", function(e) {
  console.log("Clicked!", e.target);
});

// Arrow syntax
element.addEventListener("click", (e) => { /* ... */ });
```

#### Waiting for DOM to Load
```javascript
document.addEventListener("DOMContentLoaded", function() {
  // DOM is ready — safe to manipulate
});
```

#### Event Types
| Category | Events |
|---|---|
| **Mouse** | `click`, `dblclick`, `mousedown`, `mouseup`, `mouseover`, `mouseout`, `mousemove` |
| **Keyboard** | `keydown`, `keyup` |
| **Form** | `blur`, `focus`, `change`, `submit`, `reset`, `select` |
| **Frame** | `load`, `DOMContentLoaded`, `resize`, `scroll`, `unload` |
| **Media** | `play`, `pause`, `ended`, `volumechange` |

#### Event Object
```javascript
element.addEventListener("click", function(e) {
  e.preventDefault();     // Prevent default action (e.g., form submit)
  e.stopPropagation();    // Stop bubbling/capturing
  console.log(e.target);  // Element that triggered event
});
```

#### Event Propagation
1. **Capturing phase**: Event travels from root down to the target.
2. **Bubbling phase**: Event travels from target back up to root.

#### Event Delegation
Instead of adding listeners to each child, add one to the parent:
```javascript
document.querySelector("#list").addEventListener("click", function(e) {
  if (e.target && e.target.nodeName === "LI") {
    handleItem(e.target);
  }
});
```

### Forms in JavaScript

#### Validating a Form
```javascript
document.querySelector("#myForm").addEventListener("submit", (e) => {
  const val = document.querySelector("#username").value;
  if (!val) {
    e.preventDefault();  // Stop submission
    alert("Username required");
  }
});
```

### Regular Expressions
```javascript
let pattern = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
if (pattern.test(email)) { /* valid */ }
```
- Contained in forward slashes.
- Case sensitive.
- Metacharacters: `. [ ] \ ( ) ^ $ | * ? { } +`

---

## 12. JavaScript — Additional Features

### Array Functions (ES6+)
```javascript
const paintings = [
  { artist: "Van Gogh", title: "Starry Night", year: 1889, value: 100 },
  { artist: "Courbet",  title: "Burial at Ornans", year: 1849, value: 80 }
];

// forEach — iterate
paintings.forEach(p => console.log(p.title));

// find — first match
const courbet = paintings.find(p => p.artist === "Courbet");

// filter — all matches
const vangoghs = paintings.filter(p => p.artist === "Van Gogh");

// map — transform each element
const titles = paintings.map(p => p.title);

// reduce — single accumulated value
const total = paintings.reduce((prev, p) => prev + p.value, 0);

// sort — sort (provide compare function for objects)
const sorted = paintings.sort((a, b) => a.year - b.year);
```

### Prototypes and Classes
- JavaScript is **prototype-based**: objects inherit from other objects.
- **ES6 classes** provide syntactic sugar over prototypes.

```javascript
// Prototype approach
function Card(title, src) { this.title = title; this.src = src; }
Card.prototype.display = function() { return this.title; };

// Class approach (equivalent)
class Card {
  constructor(title, src) {
    this.title = title;
    this.src = src;
  }
  display() { return this.title; }
}
```

### Modules (ES6)
```javascript
// art.js — exporting
export function getAll() { /* ... */ }
export const data = [];

// main.js — importing
import { getAll, data } from "./art.js";
```
In HTML:
```html
<script src="main.js" type="module"></script>
```

### Asynchronous JavaScript

#### The Fetch API
```javascript
fetch("/api/data")
  .then(response => response.json())
  .then(data => { /* use data */ })
  .catch(error => console.error(error));
```

#### Promises
```javascript
const p = new Promise((resolve, reject) => {
  if (success) resolve(data);
  else reject(new Error("Failed"));
});

p.then(data => { /* success */ })
 .catch(err => { /* error */ });
```

#### Async/Await (ES7)
```javascript
async function loadData() {
  try {
    const response = await fetch("/api/data");
    const data = await response.json();
    return data;
  } catch (err) {
    console.error(err);
  }
}
```

#### CORS (Cross-Origin Resource Sharing)
- Browsers restrict cross-origin requests by default.
- Server must include `Access-Control-Allow-Origin: *` header to allow cross-origin access.

### Browser APIs

#### Web Storage API
```javascript
// localStorage — persists until cleared
localStorage.setItem("key", JSON.stringify(value));
const val = JSON.parse(localStorage.getItem("key"));

// sessionStorage — lasts for the session
sessionStorage.setItem("key", "value");
```

#### Geolocation API
```javascript
navigator.geolocation.getCurrentPosition(
  pos => { console.log(pos.coords.latitude, pos.coords.longitude); },
  err => { console.error(err); }
);
```

#### Web Speech API
```javascript
const utterance = new SpeechSynthesisUtterance("Hello world");
speechSynthesis.speak(utterance);
```

---

## 13. Server-Side Development: PHP

### What is Server-Side Development?
- Programs run on the **server** and generate HTML dynamically.
- Provides access to databases, handles security, interacts with external services.

### Common Server-Side Technologies
- **PHP** — most common; embeds in HTML; powers ~80% of websites (including WordPress).
- **Node.js** — JavaScript on the server.
- **Python** — Django, Flask.
- **Ruby on Rails** — Ruby-based framework.
- **ASP.NET** — Microsoft; C#.
- **JSP** — Java Server Pages.

### PHP Basics

#### PHP Tags
```php
<?php
$user = "Randy";
?>
<!DOCTYPE html>
<html>
<body>
  <h1>Welcome <?php echo $user; ?></h1>
</body>
</html>
```
- Files use `.php` extension.
- Code inside `<?php ... ?>` is executed; HTML outside is echoed directly.
- Comments: `//` (single-line), `/* ... */` (multi-line).

#### Variables and Data Types
```php
$name = "Alice";       // String
$age = 25;             // Integer
$price = 9.99;         // Float
$active = true;        // Boolean
$nothing = null;       // Null
```
- Variables prefixed with `$`.
- Dynamically typed.

#### Constants
```php
define("MAX_SIZE", 100);
echo MAX_SIZE;  // No $ sign
```

#### Output
```php
echo "Hello " . $name;   // Concatenation with .
echo "<em>$name</em>";   // Variables in double-quoted strings
printf("Price: %.2f", $price);
```

#### Control Flow
```php
if ($x > 0) { echo "positive"; }
else if ($x === 0) { echo "zero"; }
else { echo "negative"; }

switch ($type) {
  case "A": echo "Alpha"; break;
  default: echo "Other";
}

while ($i < 10) { $i++; }
for ($i = 0; $i < 10; $i++) { echo $i; }
foreach ($array as $value) { echo $value; }
foreach ($array as $key => $value) { echo "$key: $value"; }
```

#### Include Files
```php
include "header.php";
require "config.php";           // Fatal error if not found
include_once "functions.php";   // Include only once
require_once "db.php";
```

### PHP Functions
```php
function getNiceTime($showSeconds = true) {
  return $showSeconds ? date("H:i:s") : date("H:i");
}

// Type declarations (PHP 7+)
function greet(string $name): string {
  return "Hello $name";
}

// Pass by reference
function addTen(&$num) { $num += 10; }
```

### PHP Arrays
```php
// Indexed arrays
$days = ["Mon", "Tue", "Wed", "Thu", "Fri"];
echo $days[0];  // "Mon"

// Associative arrays (key-value)
$person = ["name" => "Alice", "age" => 30];
echo $person["name"];  // "Alice"

// Multidimensional
$cart = [
  ["id" => 37, "title" => "Widget A", "quantity" => 2],
  ["id" => 38, "title" => "Widget B", "quantity" => 1],
];

// Dynamic sizing
$days[] = "Sat";          // Append
unset($days[0]);           // Delete
isset($days[0]);           // Check existence
count($days);              // Length
```

### PHP Classes and Objects
```php
class Artist {
  public $firstName;
  public $lastName;
  private $secret;
  
  function __construct($firstName, $lastName) {
    $this->firstName = $firstName;
    $this->lastName = $lastName;
  }
  
  public function getName() {
    return $this->firstName . " " . $this->lastName;
  }
}

$artist = new Artist("Pablo", "Picasso");
echo $artist->getName();

// Inheritance
class Painter extends Artist {
  public $style;
  function __construct($first, $last, $style) {
    parent::__construct($first, $last);
    $this->style = $style;
  }
}
```

**Visibility**: `public` — accessible anywhere; `private` — only within class; `protected` — within class and subclasses.

### PHP Superglobal Arrays
| Superglobal | Contents |
|---|---|
| `$_GET` | URL query string parameters |
| `$_POST` | HTTP POST data |
| `$_REQUEST` | Combined GET, POST, COOKIES |
| `$_SESSION` | Session data |
| `$_COOKIE` | Cookie data |
| `$_FILES` | Uploaded file data |
| `$_SERVER` | Server and request info |
| `$_ENV` | Environment variables |
| `$GLOBALS` | All global variables |

```php
// Reading GET data
$id = $_GET["id"];

// Reading POST data
$username = $_POST["username"];

// Check request method
if ($_SERVER["REQUEST_METHOD"] === "POST") { /* ... */ }
```

### HTTP Headers in PHP
```php
// Redirect
header("Location: error.php");

// Return JSON
header("Content-Type: application/json");
echo json_encode($data);
```

---

## 14. Form Processing

### Where to Perform Validation
1. **HTML5** — browser performs basic checks.
2. **JavaScript** — dramatically improves UX but **cannot be relied on** (can be disabled/bypassed).
3. **Server-side** — the **most important** and only guaranteed validation.

### Security Concerns
- **XSS (Cross-Site Scripting)** — malicious scripts injected into forms/pages.
- **SQL Injection** — SQL commands entered into form fields.

### Sanitizing Form Data

#### `htmlspecialchars()`
Converts HTML special characters to entities, preventing XSS:
```php
$safe = htmlspecialchars($_POST["comment"]);
```

#### `filter_var()`
```php
// Validate email
if (filter_var($email, FILTER_VALIDATE_EMAIL)) { /* valid */ }

// Sanitize string
$clean = filter_var($input, FILTER_SANITIZE_STRING);
```

### POST vs GET in Forms
- Use **GET** for idempotent requests (search, filtering).
- Use **POST** for state-changing operations (login, purchase, data entry).

---

## 15. LAMP Stack

### What is LAMP?
A popular open-source web development stack:
- **L** — Linux (operating system)
- **A** — Apache (web server)
- **M** — MySQL (database)
- **P** — PHP (scripting language)

### Setting Up LAMP on Ubuntu (Google Cloud)
1. Configure Ubuntu virtual machine on Google Cloud.
2. Update package list: `sudo apt-get update`
3. Install Apache: `sudo apt-get install apache2`
4. Install MySQL: `sudo apt-get install mysql-server`
5. Install PHP: `sudo apt-get install php libapache2-mod-php php-mysql`
6. Restart Apache: `sudo systemctl restart apache2`
7. Deploy website files to `/var/www/html/`.

**Alternatives:**
- **MAMP** — macOS version
- **WAMP** — Windows version
- **XAMPP** — Cross-platform (Windows/Mac/Linux)

---

## 16. Database Operations with MySQL

### MySQL with PHP
Basic workflow:
1. Connect to the database.
2. Create schema and tables.
3. Implement database operations (CRUD).

### MySQL Workbench
- GUI tool for establishing database connections.
- Creating schemas and tables visually.

### PHP Data Objects (PDO)
```php
// Connect
$pdo = new PDO("mysql:host=localhost;dbname=mydb", "user", "pass");

// Create tables
$pdo->exec("CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  email VARCHAR(100)
)");

// Insert
$stmt = $pdo->prepare("INSERT INTO users (username, email) VALUES (?, ?)");
$stmt->execute([$username, $email]);

// Select
$result = $pdo->query("SELECT * FROM users");
while ($row = $result->fetch()) {
  echo $row["username"];
}
```

---

## 17. Working with Databases (SQL & NoSQL)

### Relational Databases
- **Table** — 2D container for data (rows and columns).
- **Record (row)** — one data entry.
- **Field (column)** — data attribute.
- **Primary key** — uniquely identifies each record.
- **Foreign key** — links to the primary key of another table.

### Table Relationships
- **One-to-many**: one record relates to many in another table.
- **One-to-one**: one record relates to exactly one in another table.
- **Many-to-many**: requires an intermediate/junction table with a **composite key**.

### SQL Commands

#### SELECT
```sql
SELECT * FROM Paintings ORDER BY Title;
SELECT Title, Artist FROM Paintings WHERE Year > 1900;
SELECT * FROM Paintings WHERE Artist = 'Van Gogh';
```

#### JOIN
```sql
SELECT Paintings.Title, Artists.LastName
FROM Paintings
INNER JOIN Artists ON Paintings.ArtistID = Artists.ArtistID;
```

#### Aggregate Functions with GROUP BY
```sql
SELECT Artist, COUNT(*) AS PaintingCount
FROM Paintings
GROUP BY Artist;
```

#### INSERT
```sql
INSERT INTO Artists (FirstName, LastName) VALUES ('Pablo', 'Picasso');
```

#### UPDATE
```sql
UPDATE Artists SET City = 'Paris' WHERE ArtistID = 5;
```

#### DELETE
```sql
DELETE FROM Artists WHERE ArtistID = 5;
```

#### Transactions
```sql
START TRANSACTION;
INSERT INTO orders ...;
INSERT INTO orderDetails ...;
UPDATE inventory ...;
COMMIT;  -- or ROLLBACK on error
```

### Working with SQL in PHP (PDO)

```php
// Connection with error handling
try {
  $pdo = new PDO("mysql:host=localhost;dbname=mydb", USER, PASS);
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
  die($e->getMessage());
}

// Prepared statement (safe from SQL injection)
$stmt = $pdo->prepare("SELECT * FROM Books WHERE ID = :id");
$stmt->bindValue(':id', $_GET['id']);
$stmt->execute();
while ($row = $stmt->fetch()) {
  echo $row['Title'];
}

// Close connection
$pdo = null;
```

### NoSQL Databases
Not-only-SQL — doesn't use the relational table model. Optimized for fast retrieval, large datasets, and horizontal scaling.

| Type | Description | Examples |
|---|---|---|
| **Key-Value Store** | Value associated with a unique key | Redis, DynamoDB |
| **Document Store** | Value is a document (JSON/XML) | MongoDB, Firebase |
| **Column Store** | Stores data by column, not row | Cassandra |
| **Graph Store** | Data as nodes and relationships | Neo4j |

**When to use NoSQL**: large datasets, high write volume, flexible schemas, distributed systems.
**When NOT to use NoSQL**: when data consistency and integrity are critical (use SQL).

### MongoDB with Node.js (Mongoose)
```javascript
const mongoose = require('mongoose');
mongoose.connect(process.env.MONGO_URL);

const bookSchema = new mongoose.Schema({
  isbn: String,
  title: String,
  year: Number
});
const Book = mongoose.model('Book', bookSchema, 'books');

// Query
Book.find({}, (err, data) => { res.json(data); });
Book.find({ isbn: "12345" }, (err, data) => { res.json(data); });
```

---

## 18. Server-Side Development: Node.js

### What is Node.js?
- **Server-side JavaScript runtime** built on Google Chrome's V8 engine.
- **Asynchronous, event-driven, non-blocking** architecture.
- Designed for scalable network applications.

### Node Advantages
- **JavaScript Everywhere** — same language on client and server; easier code sharing.
- **Push Architectures** — can push data from server to client (e.g., chat apps).
- **Non-blocking** — single-threaded event loop; handles many connections concurrently.
- **Rich Ecosystem** — npm has hundreds of thousands of packages.
- **Broad Adoption** — Netflix, Uber, PayPal, LinkedIn all use Node.

### Blocking vs Non-Blocking
| Blocking (PHP/Apache) | Non-Blocking (Node.js) |
|---|---|
| Each request gets its own thread | Single event loop thread |
| Waiting blocks the thread | Waiting is delegated; event loop continues |
| Simpler model, less scalable | More complex, highly scalable |

### Node Disadvantages
- Complex to develop and maintain for some use cases.
- Less suited for CPU-intensive tasks (video processing, scientific computing).
- Working with relational databases (MySQL) can be more complex.

### Basic Node Application
```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {"Content-Type": "text/plain"});
  res.write("Hello from Node.js!");
  res.end();
});

server.listen(8080);
console.log("Server running on port 8080");
```

### Express Framework
```javascript
const express = require('express');
const app = express();

// Static files
app.use('/static', express.static('public'));

// Routes
app.get('/', (req, res) => { res.send("Home page"); });
app.get('/users/:id', (req, res) => {
  const id = req.params.id;
  res.json({ id, name: "Alice" });
});

app.listen(8080);
```

### REST API with CRUD
```javascript
app.get('/items', (req, res) => { /* READ all */ });
app.get('/items/:id', (req, res) => { /* READ one */ });
app.post('/items', (req, res) => { /* CREATE */ });
app.put('/items/:id', (req, res) => { /* UPDATE */ });
app.delete('/items/:id', (req, res) => { /* DELETE */ });
```

### WebSockets (Socket.io)
- Enables **two-way communication** between browser and server.
- Used for chat, live updates, multiplayer games.

```javascript
// Server
const io = require('socket.io')(server);
io.on('connection', socket => {
  socket.on('chat message', msg => {
    io.emit('chat message', msg);  // Broadcast to all
  });
});
```

### View Engines (EJS)
```html
<!-- EJS template -->
<h1><%= title %></h1>
<% for (let p of paintings) { %>
  <div><%= p.artist %> — <%= p.title %></div>
<% } %>
```

### Serverless Computing
- Deploy applications using third-party cloud services — no server management.
- Types: **Databases-as-a-Service**, **Platform-as-a-Service (PaaS)**, **Functions-as-a-Service (FaaS)**.
- Benefits: reduced complexity, lower costs, better reliability and scalability.

---

## 19. Security

### Information Security Core Concepts

#### CIA Triad
- **Confidentiality** — protect data from unauthorized access.
- **Integrity** — ensure data is accurate and unaltered.
- **Availability** — ensure systems are accessible when needed.

### STRIDE Threat Model (Microsoft)
| Letter | Threat |
|---|---|
| **S**poofing | Attacker uses someone else's credentials |
| **T**ampering | Unauthorized modification of data |
| **R**epudiation | Removing traces of an attack |
| **I**nformation Disclosure | Unauthorized access to data |
| **D**enial of Service | Preventing legitimate access |
| **E**levation of Privilege | Gaining unauthorized system privileges |

### Authentication
**Authentication** = verifying who you are. **Authorization** = what you're allowed to do.

#### Authentication Factors
- **Knowledge** — something you know (password, PIN).
- **Ownership** — something you have (token, phone).
- **Inherence** — something you are (fingerprint, face).

**Multifactor Authentication (MFA)**: Requires two distinct factors.

#### Web Authentication Strategies
| Strategy | Description |
|---|---|
| **HTTP Basic Auth** | Browser pops up a dialog; credentials in request header |
| **Form-Based Auth** | Custom HTML form, data via POST; uses session cookies |
| **Token Auth (Bearer)** | Stateless JWT tokens; used for APIs |
| **Third-Party Auth** | OAuth, "Sign in with Google" |

### Cryptography

#### Symmetric Encryption
- Same key to encrypt and decrypt.
- AES (Advanced Encryption Standard) — current standard.

#### Public Key (Asymmetric) Cryptography
- Two keys: **public** (widely shared) and **private** (secret).
- Encrypts with public key, decrypts with private key (or vice versa for signatures).
- Solves the key distribution problem.

#### Digital Signatures
- Validates authenticity, integrity, and non-repudiation of a document.

#### SSL/TLS and HTTPS
- **TLS** (Transport Layer Security) — successor to SSL.
- **HTTPS** = HTTP over TLS — encrypts all data in transit.
- Requires an **SSL certificate** from a **Certificate Authority (CA)**.

**Certificate Types:**
- **DV (Domain-Validated)** — cheapest, fastest; just verifies domain ownership.
- **OV (Organization-Validated)** — verifies organization identity; more trusted.
- **EV (Extended-Validation)** — strictest verification; highest trust.

### Credential Storage
```php
// BAD: Storing plain text passwords
$password = "mypassword";

// BETTER: Hashing with MD5 (still insecure — rainbow tables)
$hash = md5($password);

// BEST: Use PHP's password_hash() with bcrypt
$hash = password_hash($password, PASSWORD_BCRYPT);
$valid = password_verify($inputPassword, $storedHash);
```

**Salting**: adding unique random noise to each password before hashing, preventing rainbow table attacks.

### Common Attack Vectors

#### SQL Injection
Malicious SQL embedded in user input:
```sql
-- Input: ' OR '1'='1
SELECT * FROM users WHERE username='' OR '1'='1';
```
**Defense**: Use prepared statements / parameterized queries.

#### Cross-Site Scripting (XSS)
Malicious script injected into a trusted page.
- **Reflected XSS**: script returned immediately in server response.
- **Stored XSS**: script stored in database, affects all visitors.

**Defense**:
- Use `htmlspecialchars()` to escape output.
- Sanitize all user input.
- Use Content Security Policy (CSP) headers.

#### Cross-Site Request Forgery (CSRF)
Forces authenticated users to execute unwanted actions.

**Defense**: Include a unique one-time CSRF token in each form:
```html
<input type="hidden" name="csrf-token" value="randomToken123">
```

#### Brute-Force Attacks
Automated password guessing.

**Defense**: Rate limiting, account lockout, CAPTCHA, intrusion detection.

#### Denial of Service (DoS / DDoS)
Overloading server with illegitimate requests.

**Defense**: Rate limiting, CDN, load balancers, DDoS protection services.

#### Security Misconfiguration
- Out-of-date software.
- Default credentials not changed.
- Unnecessary services running.

---

## 20. DevOps and Hosting

### DevOps
Combining Development and Operations roles for better collaboration and deployment.

#### Continuous Integration/Delivery/Deployment (CI/CD)
- **CI**: Developers integrate code frequently; automated tests run.
- **CD (Delivery)**: Automated release process.
- **CD (Deployment)**: Automatic deployment to production when tests pass.

### Testing
| Type | Description |
|---|---|
| **Unit testing** | Tests individual functions/components |
| **Integration testing** | Tests units working together |
| **Functional testing** | Tests system against requirements |
| **Non-functional testing** | Security, performance, usability |
| **Penetration testing** | Security testing by simulating attacks |

**Selenium** — popular browser automation tool for functional testing.

### Infrastructure as Code (IoC)
Describe infrastructure in text files (e.g., Ansible, Vagrant) — version-controlled like code.

### Hosting Options
| Type | Description |
|---|---|
| **Shared Hosting** | Multiple sites on one server; limited control; cheapest |
| **Virtualized Shared** | Virtual server with root access |
| **Dedicated Hosting** | Entire physical server rented to you |
| **Collocated Hosting** | You own/manage the hardware in a data center |
| **Cloud Hosting** | Distributed, elastic provisioning |

### Cloud Service Models
- **IaaS** (Infrastructure as a Service) — rent servers, storage, networking.
- **PaaS** (Platform as a Service) — rent a platform to deploy apps.
- **SaaS** (Software as a Service) — rent finished software.

### Server Virtualization
- **Hypervisor** — software that creates virtual machines.
- **Docker** — container-based deployment; snapshot of OS + app.
- **Kubernetes** — container orchestration.

### DNS Administration
- **A record** — maps hostname to IPv4 address.
- **AAAA record** — maps hostname to IPv6 address.
- **CNAME** — alias pointing to another A record.
- **MX record** — specifies mail servers.
- **NS record** — specifies name servers.
- **TXT/SPF record** — anti-spam validation.
- **PTR record** — reverse DNS lookup.

### Apache Web Server Configuration
- Main config file: `httpd.conf`.
- Directory-level config: `.htaccess` files.
- Key directives: `Timeout`, `KeepAlive`, `DirectoryIndex`, `VirtualHost`.

**VirtualHost** — host multiple domains on one server:
```apache
<VirtualHost *:80>
  ServerName www.example.com
  DocumentRoot /var/www/example
</VirtualHost>
```

**URL Rewriting**:
```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### Microservices vs Monolithic Architecture
- **Monolithic**: All code in one codebase — harder to maintain/scale.
- **Microservices**: Disaggregated into many small, well-defined modules — easier to scale and maintain independently.

---

## 21. Modern Web Technologies

### Node.js
- Server-side, asynchronous, event-driven JavaScript runtime.
- Uses Google's V8 JavaScript engine.
- Handles concurrent connections via events and callbacks.

### React
- JavaScript framework for building user interfaces from components.
- Created at Facebook (2013), open-sourced on GitHub.
- Uses **JSX** — JavaScript syntax extension that looks like HTML.
- Components: functions that return markup; can be nested.
- Small as a button or as large as an entire page.

```jsx
function Button({ label, onClick }) {
  return <button onClick={onClick}>{label}</button>;
}
```

### Next.js
- Combines React with server-side functionality → **full-stack** web applications.
- Uses Node.js as the server.
- Abstracts React tooling (bundling, compiling).
- Features: routing, rendering, data fetching, styling, TypeScript support.

### Remix
- Full-stack web framework using React for UI.
- Uses **nested routing** and loads data in parallel on the server.
- Sends fully formed HTML to browser.
- Built on the Web Fetch API — runs in Node.js and non-Node environments.

### ASP.NET Core / Razor Pages
- **.NET** — free, cross-platform, open-source developer platform.
- **ASP.NET Core** — fast, secure, cross-platform web framework.
- Uses **C#** (or F# / Visual Basic).
- **Razor** — markup syntax for embedding .NET code in HTML.

### ASP.NET Core Blazor
- Full-stack .NET web framework supporting server-side and client-side rendering.
- Uses **C#** for both client and server development.
- Renders as HTML and CSS.
- Can run in browser via **WebAssembly**, or on server via **SignalR**.
- Component-based architecture similar to React.

---

## Quick Reference: Key Concepts

### HTML5 Form Input Types
`text`, `password`, `email`, `url`, `tel`, `number`, `range`, `date`, `time`, `datetime-local`, `month`, `week`, `color`, `file`, `hidden`, `submit`, `reset`, `button`, `image`, `checkbox`, `radio`

### CSS Specificity (highest to lowest)
1. `!important`
2. Inline styles
3. ID selectors (`#id`)
4. Class, attribute, pseudo-class (`.class`, `[attr]`, `:hover`)
5. Element, pseudo-element (`div`, `::before`)
6. Universal selector (`*`)

### HTTP Methods Summary
| Method | Action | Body | Safe | Idempotent |
|---|---|---|---|---|
| GET | Retrieve | No | Yes | Yes |
| POST | Create | Yes | No | No |
| PUT | Update (replace) | Yes | No | Yes |
| DELETE | Delete | No | No | Yes |

### PHP vs JavaScript Comparison
| Feature | PHP | JavaScript |
|---|---|---|
| Execution | Server | Browser (or Node.js) |
| Variables | `$var` | `var`, `let`, `const` |
| String concat | `.` (dot) | `+` or template literals |
| Arrays | Ordered maps | Arrays |
| OOP | Class-based | Prototype-based (class syntax available) |
| Typing | Dynamic | Dynamic |

### SQL CRUD Operations
| Operation | SQL Statement |
|---|---|
| Create | `INSERT INTO table (cols) VALUES (vals)` |
| Read | `SELECT cols FROM table WHERE condition` |
| Update | `UPDATE table SET col=val WHERE condition` |
| Delete | `DELETE FROM table WHERE condition` |

---

*End of INF1005 Web Systems & Technologies Notes*
