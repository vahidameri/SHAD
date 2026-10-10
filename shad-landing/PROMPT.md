# PROMPT.md — Build instructions for the Shad landing page

> Two prompts below: **A) Claude Code** (production HTML, recommended) and **B) Claude Design** (visual exploration).
> Put `CONTENT.md`, `DESIGN.md`, `PROMPT.md` and the `assets/` folder in the project root before starting.

---

## A) Prompt for Claude Code

Copy everything inside the block below as your first message.

````markdown
You are a senior product designer and front-end engineer. You are rebuilding the download landing page of **Shad (شاد)**, Iran's national school super-app used by ~34 million students, teachers and families. The page is Persian (RTL), mobile-first, and its single job is to get each visitor to the right install/open action for their device.

## Source files (read all three fully before writing any code)
- `CONTENT.md` — page structure, section order and ALL copy. Source of truth for text. Use Persian copy verbatim.
- `DESIGN.md` — visual system: tokens, type, layout, components, motion, accessibility, performance.
- `assets/` — brand logos, app screenshots, partner placeholders, fonts.

If the two files ever conflict: `CONTENT.md` wins on words and order, `DESIGN.md` wins on look and behavior. If something is missing, choose the simplest option consistent with both files and list it in your final report. Never invent copy.

## Deliverable
- `index.html` — one file, inline `<style>` and `<script>`, no framework, no build step required to view it.
- Uses only local files from `assets/`. **Zero external network requests** (no CDNs, no Google Fonts, no analytics). The page must work on Iran's domestic network.
- `qa/` — screenshots from your QA pass (see Step 6).
- A short final report (see Step 7).

## Hard constraints
1. `<html lang="fa" dir="rtl">`. Use CSS logical properties only (`margin-inline-start`, `inset-inline-end`, `text-align: start`…). No `left`/`right` for layout.
2. Mobile-first CSS: base styles target 360px; enhance with `min-width` queries at 600, 1024, 1280. No horizontal scroll at 320px.
3. All color, type, spacing and radius values come from the CSS custom properties defined in `DESIGN.md`. No ad-hoc hex values in component CSS.
4. All links, numbers, versions and campaign settings come from a single `CONFIG` object (defined in `CONTENT.md` §2) at the top of the script, and are injected into the DOM. Markup must still contain sensible server-rendered defaults so the page is complete without JS.
5. Persian digits as typed in `CONTENT.md`. Preserve ZWNJ characters exactly. Never add `letter-spacing` to Persian text.
6. Use the provided logo SVG files as `<img>`/`<picture>`. Never redraw, recolor or recreate the logo. The Shad Wave and three dots are separate decorative inline SVGs derived from the logo mark (see `DESIGN.md` §5.1).
7. Avoid every pattern listed in `DESIGN.md` §1.3.
8. Mark every block tagged `new` in `CONTENT.md` with `data-source="new"` on its wrapper.

## Fonts
- Check `assets/fonts/` for Yekan Bakh WOFF2 files. If present, declare `@font-face` for weights 400/500/700/900 and preload 400 + 900.
- If absent, install Vazirmatn locally (`npm i vazirmatn`), copy the needed WOFF2 weights into `assets/fonts/`, and use it via `@font-face`. Keep `"Yekan Bakh"` first in the font stack so dropping the files in later just works.

## Platform detection (progressive enhancement)
Default `data-platform="unknown"` on `<html>` (fallback layout). Then, inline in `<head>` so there is no layout flash:
```js
(function () {
  var ua = navigator.userAgent || "";
  var p = "desktop";
  if (/android/i.test(ua)) p = "android";
  else if (/iphone|ipad|ipod/i.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1)) p = "ios";
  else if (/mobile/i.test(ua)) p = "unknown";
  document.documentElement.dataset.platform = p;
})();
```
CSS shows the matching smart-CTA state, reorders the install panels (current device first + «دستگاه شما» badge), opens the iOS guide on iOS, and shows the QR card only on desktop ≥1024px.

## Theme
Light by default; dark ("chalkboard") via `prefers-color-scheme`, plus a manual toggle in the header that sets `data-theme="light|dark"` on `<html>` and stores the choice in `localStorage` (wrap in try/catch). Swap logo and hero screenshot per theme.

## QR code
Generate a static SVG QR for `CONFIG.links.landing` at build time (e.g. `npx qrcode -t svg`, or the `qrcode` npm package in a small Node script) and inline it. No runtime QR library.

## Analytics hooks (no tracking script — attributes only)
Add to every CTA: `data-track="cta_click"`, `data-channel="bazaar|myket|apk|pwa|web"`, `data-location="header|hero|sticky|audiences|install|final"`. Also `data-track="faq_open"` on FAQ items and `data-track="ios_guide_open"` on the iOS guide.

## Process — follow these steps in order, and do not skip ahead

**Step 1: Read & plan.** Read the three files. Then write a short build plan (in chat, not a file): section list, component list, and any gaps or conflicts you found. Continue without waiting.

**Step 2: Foundation.** Document skeleton, `<head>` (meta, SEO, Open Graph, two `theme-color` tags, JSON-LD `MobileApplication` + `FAQPage`), fonts, all design tokens for light and dark, base typography, layout container, focus styles, skip link, reduced-motion rules.

**Step 3: Build at 360px first, section by section,** in `CONTENT.md` order: campaign bar → header → hero (with Shad Wave, phone, dots, smart CTA) → trust → features → more in Shad → audiences tabs → steps → install panels → FAQ → final CTA → footer → sticky CTA bar. After each section, check it against its spec in both files.

**Step 4: Expand to 600, 1024, 1280+.** Apply the desktop layouts from `DESIGN.md` §4.3. Desktop adds columns and space, never new content.

**Step 5: Behavior.** Platform detection, theme toggle, mobile menu (focus trap, Esc, close on link), WAI-ARIA tabs with RTL arrow keys, campaign dismiss (sessionStorage, try/catch), sticky bar show/hide via IntersectionObserver, the single hero load sequence (`DESIGN.md` §7.1), APK aria-live message.

**Step 6: QA pass with real screenshots.** Use Playwright (Chromium is available). Capture full-page screenshots into `qa/` for each combination:
- widths 360, 390, 768, 1024, 1440
- light and dark
- platforms android, ios, desktop (override `userAgent` per context)

Review every screenshot yourself as a critical senior designer. Fix problems and re-shoot until the checklist below fully passes. Also run an automated accessibility check (e.g. `npx @axe-core/cli` or axe via Playwright) and fix every violation.

**Step 7: Report.** Short summary: what was built, checklist results, any deviations from the spec with reasons, and open items (e.g. missing font files, placeholder partner logos).

## Quality checklist (Definition of Done)
**Hierarchy & content**
- [ ] At 360×640, the H1 and the primary button are visible without scrolling.
- [ ] Exactly one visually dominant action per view; nothing competes with it.
- [ ] Every string matches `CONTENT.md` exactly (no invented, translated or shortened copy).
- [ ] Stat value and unit never wrap apart.

**Visual**
- [ ] The hero reads as the logo at page scale: green wave + phone + three yellow dots.
- [ ] The Shad Wave and dots appear only in the hero and the final CTA.
- [ ] Yellow is never used for text or icons on light backgrounds.
- [ ] No pattern from `DESIGN.md` §1.3 appears anywhere.
- [ ] Dark mode is chalkboard green, all text readable, logo and screenshot swapped.

**RTL & typography**
- [ ] Text start-aligned (right) except final CTA and stats; directional icons mirrored.
- [ ] No broken Persian joining, no letter-spacing, ZWNJ preserved, Persian digits.
- [ ] Phone number renders left-to-right correctly.

**Responsive**
- [ ] No horizontal scroll at 320–1920px. Nothing overlaps or clips (except the intentional phone crop).
- [ ] Sticky bar appears only on mobile after the hero CTA leaves view, never covers content or focus.

**Accessibility**
- [ ] axe: 0 violations. All contrast ≥ 4.5:1 for normal text.
- [ ] Full keyboard path works: skip link, menu, tabs (arrow keys), accordions, all CTAs, visible focus everywhere.
- [ ] Touch targets ≥ 48px. Zoom not disabled. `prefers-reduced-motion` respected.

**Performance**
- [ ] Zero external requests (verify in Playwright network log).
- [ ] Images have width/height; hero image `fetchpriority="high"`, others lazy.
- [ ] HTML+CSS+JS < 60 KB gzipped.
````

---

## B) Prompt for Claude Design (visual exploration)

Use this when you want to explore and compare the visual direction before production. Upload `CONTENT.md`, `DESIGN.md`, the logo SVGs and the two screenshots, then send:

````markdown
Design the new download landing page for **Shad (شاد)**, Iran's national school super-app. Persian, RTL, mobile-first.

Attached:
- `CONTENT.md` — structure and all copy (use the Persian text verbatim; never invent copy)
- `DESIGN.md` — the visual system (colors, type, layout, components, rules)
- Shad logo SVGs and two real app screenshots (light and dark)

Please produce:
1. **Mobile frame (360px)** of the full page, light theme.
2. **Desktop frame (1440px)** of the full page, light theme.
3. **Hero only, both sizes, in dark ("chalkboard") theme.**
4. **Two alternative hero explorations** (mobile + desktop each) that keep the same concept — the Shad Wave, phone on the wave, three yellow dots — but vary composition and scale. Label them A / B / C.

Rules:
- Follow `DESIGN.md` tokens exactly; brand colors `#068F66` and `#FFBA0C` are fixed.
- Font: Vazirmatn as a stand-in for Yekan Bakh.
- Use the logo files as-is; never redraw the logo.
- Avoid every pattern in `DESIGN.md` §1.3 (pastel blobs, identical card grids, eyebrow labels, gradient washes, tilted phones, giant hero stats).
- Show the Android state of the smart CTA on mobile, and the desktop state (web button + QR) on desktop.
````

---

## C) Recommended workflow

1. **Claude Design first (optional, ~1 round):** pick the strongest hero direction (A/B/C). If you change anything, update `DESIGN.md` §6.3 before moving on.
2. **Claude Code:** run prompt A. Review the `qa/` screenshots yourself.
3. **Feedback rounds:** give feedback by section ID (e.g. "`#hero` on 360px: …") so changes stay scoped.
4. **Swap-ins later, no code changes needed:** Yekan Bakh files → `assets/fonts/`; real partner logos → `assets/partners/` (same filenames); numbers and links → `CONFIG`.
