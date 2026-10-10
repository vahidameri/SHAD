# DESIGN.md — Shad landing page visual system

> Version 0.1 · October 2026
> Read together with `CONTENT.md` (structure + copy) and `PROMPT.md` (build steps).
> This file defines **how the page looks and behaves**. It never defines copy.

---

## 1. Design direction

### 1.1 Concept: «مدرسه‌ای به وسعت ایران» (a school as wide as Iran)

The page should feel like **the first morning of the school year**: bright, open, a little exciting, completely trustworthy. It must speak to a 12-year-old and to their parent at the same time.

The visual language comes from **Shad's own world**, not from generic SaaS landing pages:

| Source in Shad's world | How it becomes design |
|---|---|
| The logo mark: three yellow dots above a green wave | The **Shad Wave** and the **three dots** are the page's only decorative motifs |
| The app's chalkboard banner (green board, Tehran skyline in chalk) | Dark mode is a **chalkboard green**, not grey or black |
| Classroom & notebook | Calm, generous, well-ordered content areas; clear sequence where content is a sequence |
| Brand colors `#068F66` + `#FFBA0C` | Green carries trust and action; yellow carries joy and highlight |

### 1.2 Principles

1. **One bold moment.** The hero is the memorable thing: a large Shad Wave rising from the bottom of the hero, with the phone standing on it and the three yellow dots above it, recreating the logo at page scale. Everything after the hero is quiet, disciplined and content-first.
2. **The right button first.** Visual hierarchy always ends in the platform-appropriate primary action. Nothing on screen may compete with it in weight.
3. **Real product, not illustration.** Show real app screens. No stock illustrations, no 3D blobs, no random pastel circles (the current site's biggest visual problem).
4. **Mobile is the design; desktop is the expansion.** Every section is designed at 360px first. Desktop adds columns and space. It never adds content.
5. **Structure means something.** Borders, numbers, labels and dividers appear only where they encode information (e.g. numbers only for real steps).

### 1.3 What this page must NOT look like

Avoid these generic "AI landing page" patterns explicitly:

- Pastel blobs or circles floating in the background (the current site's look).
- Every section chopped into identical rounded cards with the same soft grey shadow.
- Gradient washes used as decoration.
- A small "eyebrow" label above every heading.
- Giant stat numbers as the hero's main element.
- Fade-and-slide-up animation on every section as it scrolls into view.
- Meta strings joined with middle dots («A · B · C»). Use separate elements.
- Arrows («→» / «←») appended to button text.
- Accenting one word of a headline in a different color or weight.
- Tilted 3D phone mockups.

---

## 2. Color

### 2.1 Brand colors (do not modify)

| Name | Hex | Use |
|---|---|---|
| Shad Green | `#068F66` | Logo, large brand surfaces (Shad Wave, final CTA band), decorative fills |
| Shad Yellow | `#FFBA0C` | The three dots, highlights, badges, primary button **on green surfaces** |
| Shad Ink | `#1C1C1C` | Body text, text on yellow (from the logo file) |

### 2.2 Accessibility facts (measured)

| Pair | Ratio | Rule |
|---|---|---|
| White on `#068F66` | 4.09 | ❌ for normal text. OK only for large text (≥24px, or ≥19px bold) |
| White on `#057A57` | 5.35 | ✅ use for buttons and links |
| `#FFBA0C` on white | 1.71 | ❌ **never** use yellow for text or icons on light backgrounds |
| `#1C1C1C` on `#FFBA0C` | 9.97 | ✅ text on yellow is always ink |
| `#FFBA0C` on `#068F66` | 2.39 | ❌ yellow text on green is forbidden (yellow *shapes* on green are fine) |

**Therefore:** `#068F66` is the brand surface color. Interactive green (buttons, links, focus) uses the darker `--green-action` token.

### 2.3 Tokens — light theme (default)

```css
:root {
  /* brand */
  --brand-green:        #068F66;
  --brand-yellow:       #FFBA0C;

  /* action */
  --green-action:       #057A57;  /* buttons, links — white text 5.35:1 */
  --green-action-hover: #045E43;  /* hover/pressed — white text 7.81:1 */
  --on-action:          #FFFFFF;

  /* surfaces */
  --bg:                 #FFFFFF;
  --surface-tint:       #EAF5EF;  /* soft green sections (trust, footer) */
  --surface-raised:     #FFFFFF;
  --line:               #D6E5DE;  /* borders, dividers */

  /* text */
  --text:               #1C1C1C;  /* 17.0:1 on white */
  --text-2:             #4A5551;  /* secondary, 7.75:1 */
  --text-3:             #5E6965;  /* meta / labels, minimum allowed, 5.7:1 */

  /* states */
  --focus-ring:         #045E43;
  --focus-ring-on-dark: #FFBA0C;
}
```

### 2.4 Tokens — dark theme ("chalkboard")

Dark mode is a deep chalkboard green, inspired by the app's own chalkboard banner. Not grey, not black.

```css
/* apply via both: @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {...} }
   and :root[data-theme="dark"] {...} */
{
  --bg:                 #0D2019;  /* chalkboard */
  --surface-tint:       #132B23;
  --surface-raised:     #17332A;
  --line:               #24443A;

  --text:               #EAF2EE;  /* 14.9:1 */
  --text-2:             #A9BCB4;  /* 8.5:1 */
  --text-3:             #8FA59C;  /* 6.5:1 */

  --green-action:       #2FBF8C;  /* buttons in dark mode */
  --green-action-hover: #3CCB97;
  --on-action:          #0D2019;  /* dark text on light-green button, 7.2:1 */

  --focus-ring:         #FFBA0C;
}
```

- `theme-color` meta: light `#FFFFFF`, dark `#0D2019`.
- Set `color-scheme: light dark` on `:root`; `color-scheme: dark` when dark is active.
- In dark mode the brand green `#068F66` is still used for the Shad Wave and large shapes (it is decoration there, not text).

### 2.5 Color proportions

Roughly **70% white / chalkboard background, 20% green, 10% yellow**. Yellow is precious: it is used for the three dots, the "دستگاه شما" badge, the primary button inside green bands, and focus rings in dark mode. Nothing else.

---

## 3. Typography

### 3.1 Typeface

**Yekan Bakh** (commercial, Fontiran) — one family for everything, using weight and size for hierarchy.

- Use the **FaNum** variant if available (Persian digits). Copy already contains Persian digits, so this is a safety net.
- **Fallback until font files are provided: Vazirmatn** (open source, OFL). Stack:
  ```css
  --font: "Yekan Bakh", "YekanBakh", "Vazirmatn", Tahoma, sans-serif;
  ```
- Self-host only (`assets/fonts/`), `font-display: swap`, preload the two most used weights (Regular, Heavy). **No Google Fonts or other CDN** in production — the page must work on Iran's domestic network.

Weights used: **400** Regular (body), **500** Medium (UI, labels), **700** Bold (H2, H3, buttons), **900** Heavy (H1, stat values). Do not use other weights.

### 3.2 Type scale (mobile → desktop, fluid with `clamp()`)

Persian script needs more line-height than Latin. Do not use negative letter-spacing. Do not use letter-spacing at all on Persian text (it breaks joining).

| Token | Mobile (360) | Desktop (≥1280) | Weight | Line-height | Use |
|---|---|---|---|---|---|
| `--fs-display` | 34px | 60px | 900 | 1.3 | H1 only |
| `--fs-h2` | 26px | 40px | 700 | 1.4 | Section titles |
| `--fs-h3` | 19px | 22px | 700 | 1.5 | Feature / card titles |
| `--fs-lead` | 17px | 19px | 400 | 1.9 | Hero subheading, section leads |
| `--fs-body` | 16px | 16px | 400 | 1.9 | Body |
| `--fs-small` | 14px | 14px | 500 | 1.8 | Labels, meta, helper text |
| `--fs-micro` | 13px | 13px | 500 | 1.7 | Legal only. Never smaller than 13px |
| `--fs-stat` | 26px | 34px | 900 | 1.2 | Stat values |

```css
--fs-display: clamp(2.125rem, 1.3rem + 3.6vw, 3.75rem);
--fs-h2:      clamp(1.625rem, 1.15rem + 2vw, 2.5rem);
--fs-h3:      clamp(1.1875rem, 1.1rem + .4vw, 1.375rem);
--fs-lead:    clamp(1.0625rem, 1rem + .3vw, 1.1875rem);
```

- Headings: `text-wrap: balance`. Paragraphs: `text-wrap: pretty`.
- Max line length: **~65 characters** for body (≈ `max-width: 34rem`), ~22 characters per line for H1 on desktop.
- The H1 is the typographic hero: Heavy weight, very large, set tight, in `--text`. It must not be colored, split or decorated.

---

## 4. Layout

### 4.1 Grid & spacing

| Breakpoint | Width | Columns | Gutter (side padding) | Column gap |
|---|---|---|---|---|
| base | 360–599 | 4 | 16px | 16px |
| `sm` | ≥600 | 8 | 24px | 20px |
| `md` | ≥1024 | 12 | 32px | 24px |
| `lg` | ≥1280 | 12 | auto (container 1200px) | 24px |

- Mobile-first CSS: base styles = 360px; use `min-width` media queries only.
- Must not horizontally scroll at 320px.
- Spacing scale (4px base): `4, 8, 12, 16, 24, 32, 48, 64, 96, 128`.
- Section vertical padding: `64px` mobile → `96px` desktop. Hero is the exception (see 6.3).

### 4.2 Alignment

- **Start-aligned (right in RTL) everywhere** — headings, text, buttons. This is how Persian readers scan.
- Center alignment only for: the final CTA band and the stats row.
- Use logical CSS properties throughout (`margin-inline-start`, `padding-inline`, `inset-inline-end`, `text-align: start`). Never `left`/`right` for layout.
- Directional icons (chevrons, arrows) must be mirrored for RTL.

### 4.3 Page wireframes

**Mobile (360px):**

```
┌──────────────────────────────┐
│ ▓ campaign bar (optional)  ✕ │
├──────────────────────────────┤
│ ☰   [دریافت]          شاد ●  │  header, 56px, sticky
├──────────────────────────────┤
│              H1 (2–3 lines)  │
│         subheading (3 lines) │
│ [██████ primary button ████] │  full-width, 52px
│ [──── secondary button ────] │
│        direct APK link · meta│
│     other devices link / free│
│          ● ● ●               │  three yellow dots
│        ┌────────┐            │
│        │ phone  │            │
│~~~~~~~~│ screen │~~~~~~~~~~~~│  Shad Wave (green), phone stands on it
│████████└────────┘████████████│
├──────────────────────────────┤
│  partners (logos, scroll/wrap)│  tint surface
│  +۳۴ میلیون | +۸۷ … | +۱۲ …  │  3 stats in one row
├──────────────────────────────┤
│ H2 features                  │
│ ┌ lead feature w/ screenshot ┐│
│ └────────────────────────────┘│
│ ◯ feature 2                  │  icon rows with dividers
│ ◯ feature 3                  │
│ ◯ feature 4                  │
│ more in Shad: 2×2 grid       │
├──────────────────────────────┤
│ [دانش‌آموزان|معلم‌ها|خانواده‌ها]│  segmented control
│ tab panel                    │
├──────────────────────────────┤
│ ۱ ── ۲ ── ۳  steps (vertical)│
├──────────────────────────────┤
│ install panels (your device  │
│ first, others collapsed)     │
├──────────────────────────────┤
│ FAQ accordion                │
├──────────────────────────────┤
│~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~│  inverted wave
│ ████ FINAL CTA (green) ██████│
├──────────────────────────────┤
│ footer (tint)                │
└──────────────────────────────┘
│ [● شاد، رایگان  [دریافت]]     │  sticky bottom bar (after hero)
```

**Desktop (1440px):**

```
┌──────────────────────────────────────────────────────────────┐
│ [دریافت شاد] [ورود به نسخه وب]   پشتیبانی  سؤالات  راهنما  قابلیت‌ها   شاد ● │
├──────────────────────────────────────────────────────────────┤
│                                   │                          │
│        ● ● ●                      │        H1 (2 lines)      │
│      ┌───────┐                    │       subheading         │
│      │ phone │                    │  [primary] [secondary]   │
│      │       │                    │   APK link / meta        │
│~~~~~~│       │~~~~~~~~~~~~~~      │   ┌ QR card (desktop) ┐  │
│██████└───────┘███████████████     │   └──────────────────┘   │
│███████████████████████████████████████████████████████████████│ wave bleeds full width
├──────────────────────────────────────────────────────────────┤
│   logo  logo  logo  logo  logo       │  +۳۴  │ +۸۷  │ +۱۲    │
├──────────────────────────────────────────────────────────────┤
│  ┌──────── lead feature (7 cols) ───────┐ ┌ feat 2 (5 cols) ┐ │
│  │  screenshot + text                   │ ├ feat 3          ┤ │
│  └──────────────────────────────────────┘ └ feat 4          ┘ │
│   more in Shad: one row of 4                                 │
├──────────────────────────────────────────────────────────────┤
│  tabs (start)        │  tab panel                             │
├──────────────────────────────────────────────────────────────┤
│   ۳ ─────────── ۲ ─────────── ۱   (horizontal, RTL order)     │
├──────────────────────────────────────────────────────────────┤
│  [desktop panel]   [iOS panel]   [Android panel]  ← your device first (rightmost) │
├──────────────────────────────────────────────────────────────┤
│  FAQ: H2 in 4 cols (start)   │   accordion in 8 cols          │
├──────────────────────────────────────────────────────────────┤
│ ███████████████ FINAL CTA band (centered) ████████████████████│
├──────────────────────────────────────────────────────────────┤
│  about (4 cols) │ get shad │ help │ support (phone)          │
└──────────────────────────────────────────────────────────────┘
```

---

## 5. Brand assets

| File | What it is | Use |
|---|---|---|
| `assets/brand/logo-full-color.svg` | Full logo, green + yellow, ink tagline | Header & footer, light theme |
| `assets/brand/logo-full-white.svg` | Full logo, all white | Header & footer, dark theme; on green surfaces |
| `assets/brand/logo-full-black.svg` | Full logo, all black | Print / monochrome only |
| `assets/brand/icon-flat.svg` | Logo mark (dots + wave), no outline | Sticky bar, favicon, small uses |
| `assets/brand/icon-outlined.svg` | Logo mark with dark outline | Optional, playful contexts |
| `assets/screens/home-light.webp` (+ `.png`) | App home screen, light | Hero (light theme) — 824×1834 |
| `assets/screens/home-dark.webp` (+ `.png`) | App home screen, dark | Hero (dark theme) — 824×1834 |
| `assets/partners/*.svg` | Partner logos | **Placeholders** — see 6.5 |
| `assets/fonts/` | Font files | Yekan Bakh (to be provided) / Vazirmatn fallback |

- Logos are never redrawn, recolored, stretched or rebuilt in CSS. Always use the files.
- Logo minimum height: 32px (header mobile), 40px (header desktop). Clear space around it = height of one yellow dot.
- Theme-swap the logo with `<picture>` + `prefers-color-scheme` or CSS, and with the manual theme toggle.

### 5.1 The Shad Wave (signature motif)

Extract the wave shape from the logo mark (`icon-flat.svg`, the green path) and scale it horizontally into a wide, gentle wave. Build it as an inline SVG with `preserveAspectRatio="none"` and fill `var(--brand-green)`.

Allowed uses (only these):
1. **Hero ground:** full-bleed wave at the bottom of the hero; the phone stands on it.
2. **Final CTA top edge:** the same wave, mirrored, as the top edge of the green final CTA band (bookends the page).

The **three yellow dots** (`--brand-yellow` circles, from the logo mark's proportions) appear in exactly two places: above the phone in the hero, and in the final CTA band. Nowhere else.

---

## 6. Components

All components: logical properties, visible focus, ≥48px touch targets, every state defined.

### 6.1 Buttons

| Variant | Background | Text | Border | Use |
|---|---|---|---|---|
| Primary | `--green-action` | `--on-action` | none | The one main action in a block |
| Secondary | transparent | `--green-action` | 1.5px `--green-action` | The second action (e.g. Myket) |
| On-green primary | `--brand-yellow` | `--text` (`#1C1C1C`) | none | Primary action inside green bands |
| On-green secondary | transparent | `#FFFFFF` | 1.5px white | Secondary inside green bands |
| Text link | none | `--green-action`, underline on hover | — | APK link, "other devices" |

- Height: 52px (mobile, full width in hero) / 48px (elsewhere). Padding-inline 24px. Radius **14px**.
- Font: 16px / 700.
- Optional leading icon (24px). **No trailing arrows.**
- States: hover = `--green-action-hover`; active = scale(0.98); focus-visible = 3px ring `--focus-ring`, 3px offset; disabled not needed on this page.
- Store buttons (Bazaar, Myket) are standard buttons with a generic store icon. Official store badges may replace them later — leave a class `.store-btn` so they can be swapped.

### 6.2 Header

- Height 56px mobile / 72px desktop. Sticky, background `--bg` at 92% opacity with `backdrop-filter: blur(12px)`; bottom border `--line` appears only after scroll.
- Mobile menu: full-width sheet from the top, `overscroll-behavior: contain`, traps focus, closes on Esc and on link tap.

### 6.3 Hero (the bold moment)

- Min height: content-driven on mobile (do **not** force 100vh). Desktop ~ `min(88vh, 820px)`.
- Background `--bg`. The Shad Wave occupies the bottom ~30% (mobile) / ~40% (desktop), full bleed.
- Phone: a simple, flat device frame built in CSS (rounded rect, radius ~44px at desktop size, 10px ink bezel, no notch drama, **no tilt**), containing the screenshot. Width: 220px mobile, 300px desktop. It sits on the wave crest and is cropped by the section bottom on mobile.
- Three yellow dots above the phone, arranged as in the logo (one on top, two below).
- Smart CTA block (see 6.4) in the text column.
- Desktop: QR card sits under the CTAs as a small raised panel (radius 20px, 1px `--line`), QR 112px.

### 6.4 Smart CTA block

- Renders one of states A/B/C from `CONTENT.md`. Platform stored as `document.documentElement.dataset.platform = "android" | "ios" | "desktop" | "unknown"`; CSS shows the matching state.
- Server/no-JS default = `unknown` → the fallback three-button layout.
- Mobile: buttons stacked, full width, 12px gap. Desktop: buttons inline, auto width.
- APK meta line: `--fs-small`, `--text-3`, separate items with spacing (not dots).

### 6.5 Trust section

- Background `--surface-tint`. Padding 48px mobile / 64px desktop.
- Partner logo **placeholders** (until real files are added): `assets/partners/{moe,ict,ncs,mci,fata}.svg` are provided as neutral placeholder SVGs showing each institution's name. Use them as normal `<img>` logos. Real logos will later replace these files with the same names, so swapping must require no HTML or CSS change.
- Partner logos: each in a fixed 120×56 box (mobile 96×48), `object-fit: contain`, grayscale + 70% opacity at rest, full color on hover (desktop only). Mobile: wrap into a centered grid of 3+2; no carousel.
- Stats: one row of three, centered, separated by 1px vertical `--line` dividers. Value+unit (`--fs-stat`, 900, `--text`) on one line, label (`--fs-small`, `--text-2`) under it. Not giant — the stats support, they don't headline.

### 6.6 Features

- Lead feature: a large panel (radius 28px, `--surface-tint` background) with a cropped real screenshot (use the "آموزشی" course row from `home-light`/`home-dark`, cropped via `object-position`) and text.
- Features 2–4: **not cards**. Rows with a 48px icon in a 56px circle (`--surface-tint`), title, product label, text; separated by 1px `--line` dividers.
- Icons: one consistent set — inline SVG, 24px grid, 1.75px stroke, round caps/joins, `currentColor` in `--green-action`. (Lucide-style geometry; copy the SVG paths inline.) `aria-hidden="true"`.
- "More in Shad": small items (icon 40px + name + one line), 2×2 mobile, 1×4 desktop. Use the same icon style; do **not** use the mismatched illustrations from the current site.

### 6.7 Tabs (Who it's for)

- WAI-ARIA tabs pattern: `role="tablist"`, arrow-key navigation (mirrored for RTL), `aria-selected`, panels with `role="tabpanel"`.
- Mobile: full-width segmented control, 48px, radius 999px, track `--surface-tint`, selected pill `--bg` with subtle shadow.
- Desktop: vertical tab list in the start column (4 cols), panel in 8 cols.
- Panel: title (H3) + 3 bullet items with check icons in `--green-action`.

### 6.8 Steps

- Real sequence → numbered markers are correct here.
- Marker: 40px circle, `--brand-yellow` fill, `--text` number, 900 weight.
- Mobile: vertical, markers connected by a 2px dashed `--line` line. Desktop: horizontal, RTL order (۱ on the right).

### 6.9 Install panels

- Three panels; radius 20px; 1px `--line` border; background `--surface-raised`.
- Current-device panel: 2px `--green-action` border + badge «دستگاه شما» (yellow pill, ink text, 13px/700).
- Mobile: current device panel open, the other two collapsed as disclosures (`<details>`). Desktop: three columns, all open.
- iOS guide: ordered list with step numbers in small ink circles; each step can show a small inline SVG of the iOS share icon where mentioned.

### 6.10 FAQ accordion

- Native `<details>/<summary>`. Summary 56px min height, 17px/700, chevron icon at the end (rotates 180° on open, 200ms).
- 1px `--line` dividers between items; no boxes.

### 6.11 Final CTA band

- Background `--brand-green`, wave top edge, three yellow dots, centered text.
- H2 in white (large text, allowed at 4.09:1), body in white at ≥19px.
- Buttons use the on-green variants (yellow primary).
- In dark mode the band stays brand green (it reads as a lit board on the chalkboard).

### 6.12 Footer

- Background `--surface-tint`. 4 columns desktop; stacked on mobile with columns 2–3 as disclosures.
- Phone number: `--fs-h3`, 900, `dir="ltr"`, as a `tel:` link — it is the one thing users look for here.

### 6.13 Sticky CTA bar (mobile)

- Fixed bottom, full width, 64px + `env(safe-area-inset-bottom)`, background `--bg` 96% + blur, top border `--line`.
- Slides in/out (transform only, 220ms). Must not cover focused elements (add bottom padding to `body` while visible).

### 6.14 Campaign bar

- 40px high. Background `--text` (ink `#1C1C1C`) with white text — deliberately **not** green, so it never competes with the brand green CTA. In dark mode use `--surface-raised` with `--text`.
- Link underlined. Close icon button 40×40 (`aria-label` from `CONTENT.md`).

---

## 7. Interaction & motion

### 7.1 The one orchestrated moment

On first load only (hero):
1. The Shad Wave rises from below (translateY 40px → 0, opacity 0 → 1), 600ms, `cubic-bezier(.2,.8,.2,1)`.
2. The phone rises onto the wave, 120ms after.
3. The three yellow dots pop in one by one (scale .6 → 1), 80ms stagger, like the logo assembling.

Total ≤ 1.1s. Text and buttons are visible immediately (never delay the CTA).

### 7.2 Responsive motion only

Everything else animates only in response to the user: accordion open, tab switch (cross-fade 150ms), menu sheet, sticky bar, button press. **No scroll-triggered entrance animations.**

### 7.3 Rules

- Animate `transform` and `opacity` only. List transitioned properties explicitly (never `transition: all`).
- `@media (prefers-reduced-motion: reduce)`: disable the hero sequence (show final state) and all slides; keep instant state changes.
- Touch: `touch-action: manipulation`; `-webkit-tap-highlight-color: transparent` with a visible `:active` state instead.

---

## 8. Accessibility (WCAG 2.2 AA)

- Contrast per section 2. Text never below 4.5:1 (3:1 only for ≥24px or ≥19px bold).
- Touch targets ≥ 48×48px (minimum 44px), 8px spacing between adjacent targets.
- Visible `:focus-visible` on every interactive element. Never remove outlines without a replacement.
- Landmarks: `header`, `nav`, `main#main`, `footer`; skip link first.
- Heading order: one H1 (hero), H2 per section, H3 inside sections.
- Images: meaningful `alt` from `CONTENT.md`; decorative SVGs (wave, dots, icons) `aria-hidden="true"`.
- External links: `rel="noopener"` + visually hidden «(در صفحه جدید باز می‌شود)» if `target="_blank"`. Store and APK links open in the same tab.
- Zoom must not be disabled (no `maximum-scale`, no `user-scalable=no`).
- Works with 200% text zoom without horizontal scroll.

---

## 9. Performance & delivery

- One `index.html` with inline CSS and JS (no framework), plus the `assets/` folder.
- **No external requests** (no CDNs, no Google Fonts, no analytics scripts) — domestic-network safe.
- Hero screenshot: WebP with PNG fallback via `<picture>`, explicit `width`/`height`, `fetchpriority="high"`; all other images `loading="lazy"`.
- Fonts: WOFF2, `font-display: swap`, preload 2 weights.
- QR code: pre-generated static inline SVG (no runtime library).
- Budget: HTML+CSS+JS < 60 KB gzipped; total first load < 400 KB excluding fonts.
- Lighthouse targets (mobile): Performance ≥ 90, Accessibility 100, Best Practices ≥ 95, SEO 100.

---

## 10. Radius & elevation (hierarchy, not uniformity)

| Element | Radius |
|---|---|
| Large panels (lead feature) | 28px |
| Install panels, QR card | 20px |
| Buttons, inputs | 14px |
| Pills, badges, segmented control | 999px |
| Phone frame | 44px (scale with size) |

Elevation: flat by default. Only two shadows exist:
- `--shadow-raised: 0 1px 2px rgb(13 32 25 / .06), 0 8px 24px rgb(13 32 25 / .08)` — QR card, selected segment.
- `--shadow-phone: 0 30px 60px -20px rgb(13 32 25 / .35)` — the phone only.
