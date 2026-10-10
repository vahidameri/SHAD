# PROMPT.md — How to brief Claude for the Shad landing page

> Version 2.0 · October 2026
> Put this whole kit in an empty project folder: `PROMPT.md`, `DESIGN.md`, `CONTENT.md`, `assets/`, `references/`.
> **A)** Claude Code — builds the production page (recommended). **B)** Claude Design — explores the visual direction first (optional).

---

## A) Prompt for Claude Code

Copy everything inside the block as your first message.

````markdown
You are the design lead of a top-tier product design studio, and an excellent front-end engineer. Your studio's work regularly gets featured on Land-book, Mobbin and Awwwards. You've been hired to design and build the new download landing page for **Shad (شاد)** — Iran's national school super-app, used by more than 34 million students, teachers and families.

The client has seen safe, minimal, "clean" proposals and rejected them as weak. They want a page that is **stunning** — rich, layered, alive, crafted to the pixel — and that carries the energy of the Shad super-app. At the same time it must stay crystal clear about its one job: getting each visitor to install or open Shad on their device.

## Your materials
- `DESIGN.md` — art direction: the ambition, a study of the references, the Shad visual world, palette, type, imagery, composition ideas, motion, and the few hard rules (§9).
- `CONTENT.md` — the story, draft copy, locked facts (CONFIG), UI-fragment content.
- `references/` — six reference landing pages that set the quality bar, plus the current shad.ir (what we're replacing). **Open and study every image at full size.**
- `assets/` — logos, real app screenshots, UI crops from the app, partner logo placeholders, fonts folder.

Treat `DESIGN.md` and `CONTENT.md` as a creative brief, not a checklist. Only `DESIGN.md` §9 and the facts in `CONTENT.md` §2 are fixed. Everything else is direction: interpret it, combine it, improve on it. If you have a better idea than the brief, do it and explain why in your report.

## Deliverable
- `index.html` + the `assets/` it uses. Vanilla HTML/CSS/JS is preferred. You may use build tools or local npm libraries (e.g. for animation), as long as the final output is static files with **no runtime requests to external domains**.
- `qa/` — your screenshots from the critique rounds.
- A short report at the end.

## How to work — phase by phase

### Phase 1 — Immerse (no code yet)
1. Read `DESIGN.md` and `CONTENT.md` fully.
2. Open every image in `references/` and `assets/screens/`, and look at `assets/app-ui/`.
3. Write in chat:
   - A 3-sentence **art direction statement** for this page.
   - For each reference: the 1–2 specific craft moves you'll bring into this page (and where).
   - What in the Shad app itself (colors, subject cards, tiles, chalkboard, 3D objects) will make this page feel like Shad and not like a generic template.

### Phase 2 — Concepts
1. Sketch **three distinct hero concepts** (e.g. "orbit", "subject fan", your own). For each, build a quick rough HTML version and screenshot it at 390px and 1440px.
2. Compare them against the references honestly. Pick one (or merge), and explain the choice in two sentences.
3. Write a one-line composition idea for every other section — each section should have its own layout (no two sections look alike).

### Phase 3 — System
Define the design tokens (colors including the super-app palette, type scale, spacing, radii, shadows, motion curves) and build the **UI-fragment kit** from `DESIGN.md` §3.3 — the live class card, message bubbles, homework checklist, subject cards, textbook + رمزینه scan, service tiles, chips. They should look as if lifted out of the real Shad app. Screenshot the kit and refine it until each piece looks polished on its own.

### Phase 4 — Build, mobile first
Build every section at 390px first, then compose the desktop version (1280–1440px) as its own deliberate layout — not a stretched mobile. Wire up the smart CTA (`CONTENT.md` §3), the audience explorer, the install cards, the FAQ, the sticky mobile bar.

### Phase 5 — Motion & interaction
Add the hero entrance, ambient motion, count-ups, living UI fragments, hover/press states and transitions (`DESIGN.md` §8). Check that everything still feels smooth with CPU throttling and that `prefers-reduced-motion` gives a clean static page.

### Phase 6 — Critique loop (do at least 3 rounds)
Each round:
1. Use Playwright (Chromium is available) to take full-page screenshots at **390, 768, 1440** px, plus a viewport-only shot of the hero at 390×844 and 1440×900. Emulate Android, iPhone and desktop user agents to check each CTA state. Save to `qa/round-N/`.
2. **Look at your screenshots next to the reference images.** Be a harsh creative director. Score each section 1–10 on: visual hierarchy, composition & depth, typography, craft & detail, "feels like Shad", clarity of the CTA, and mobile quality.
3. Write the scores and the top problems in chat. Fix everything below 8. Then start the next round.

Typical things to catch: empty or flat areas, sections that look like each other, weak headline scale, crowded mobile hero, UI fragments that look fake or blurry, misaligned grids, inconsistent radii/shadows, Persian text rendering issues, CTA not obvious.

### Phase 7 — QA & report
- Accessibility: run axe (e.g. via `@axe-core/playwright`) and fix violations; check keyboard navigation and visible focus.
- RTL: check the rendering and joining of Persian text, digits and the LTR phone number.
- Network: confirm zero external requests in the Playwright network log.
- Performance: optimized images, lazy loading below the fold, smooth scrolling on a throttled mobile profile.
- Report: final scores per section, what you changed from the brief and why, and open items (e.g. Yekan Bakh files, real partner logos, photography).

## Fonts
If Yekan Bakh WOFF2 files are in `assets/fonts/`, use them. Otherwise install Vazirmatn locally (`npm i vazirmatn`), copy the WOFF2 files you need into `assets/fonts/`, and keep "Yekan Bakh" first in the font stack.

## QR code
Generate it at build time (e.g. the `qrcode` npm package) as an inline SVG pointing to `CONFIG.links.landing`. Style it to match the page.

## Platform detection
Set `data-platform` on `<html>` early (inline script in `<head>`): `android` (`/android/i`), `ios` (`/iphone|ipad|ipod/i`, or Mac with touch), otherwise `desktop`. Fallback when unknown: show the three main options together.

## Analytics hooks
Add `data-track` attributes on every CTA (`cta_click`, plus `data-channel` = bazaar|myket|apk|pwa|web and `data-location` = header|hero|sticky|explorer|install|final). No tracking scripts.
````

---

## B) Prompt for Claude Design (optional visual exploration)

Upload `DESIGN.md`, `CONTENT.md`, all images from `references/`, the logo SVGs, the two screenshots and the `assets/app-ui/` crops. Then send:

````markdown
Design the new download landing page for **Shad (شاد)**, Iran's national school super-app (34M+ installs). Persian, RTL, mobile-first.

The attached `DESIGN.md` is the art direction and `CONTENT.md` holds the story and copy. The reference images set the quality bar: study their craft (layered phone + floating UI fragments, orbit/arc compositions, fanned cards, bento tiles with real UI, two-tone headlines, immersive CTA bands) — don't copy them. The page must feel like the Shad app itself: its subject cards (lime, teal, cobalt, violet with 3D school objects), service tiles, mint selected state, chalkboard green, and the three yellow dots of the logo.

Please produce:
1. Three distinct hero concepts, each as a mobile (390px) and a desktop (1440px) frame. Label them A / B / C with a one-line rationale.
2. For your favorite concept, the full page at 390px and at 1440px.
3. A sheet of the UI-fragment components (live class card, teacher message, homework checklist, subject cards, textbook with رمزینه scan, service tiles, chips).

Fixed: brand colors #068F66 and #FFBA0C, the logo files as-is, Vazirmatn as stand-in font, facts from CONTENT.md §2. Everything else is yours to push.
````

---

## C) Working rhythm with the client

1. *(Optional)* Run B in Claude Design, pick a hero concept, and add a line about it to the top of `DESIGN.md` §7 ("Chosen hero: …").
2. Run A in Claude Code. Review `qa/` yourself.
3. Give feedback per section and breakpoint (e.g. "Hero @390: the chips cover the headline"). Ask for another critique round after each batch of feedback.
4. Later swap-ins need no redesign: Yekan Bakh → `assets/fonts/`; real partner logos → `assets/partners/` (same filenames); photos → `assets/photos/`; numbers and links → `CONFIG`.
