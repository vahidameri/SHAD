# DESIGN.md — Visual system for the Shad landing page

> Version 3.0 · October 2026 · Read `BRIEF.md` first.
> One idea, one system. Sections 2–7 define the system; inside it, compose freely. Section 8 (banned) and section 9 (foundations) are not negotiable.

---

## 1. Principles

1. **One idea, all the way.** The three dots and the wave (`BRIEF.md` §3) are the only graphic motif. No other decorative shapes, blobs, arcs, grids or textures.
2. **The product is the picture.** The real Shad app inside one phone is the main visual. Everything else is type and space.
3. **Calm is the luxury.** One focus per screen. Lots of air. Small, precise type. A page that breathes reads as premium; a crowded one reads as AI.
4. **Unity over variety.** Same grid, same radii, same colors, same motion everywhere. Sections differ by composition, never by switching styles.
5. **Craft is in the details**: optical alignment of Persian text, perfect spacing rhythm, crisp hairlines, a button that feels good to press, a dot that bounces with the right weight.

---

## 2. Color

A very small palette. Color is used with intent, mostly white space and ink, with green and yellow as the brand voice.

| Token | Hex | Use |
|---|---|---|
| `--paper` | `#FFFFFF` | Page background |
| `--mist` | `#F2F8F5` | The only tinted surface (FAQ, "also for", footer) |
| `--ink` | `#1C1C1C` | Headlines and body (from the logo file) |
| `--ink-2` | `#5A6662` | Secondary text (5.98:1 on white) |
| `--line` | `#E3ECE8` | 1px hairlines and borders |
| `--shad-green` | `#068F66` | Brand: the wave, logo, large shapes. White text on it only if ≥ 24px or ≥ 19px bold (4.09:1) |
| `--green-deep` | `#057A57` | Buttons, links, the install section background (white text 5.35:1) |
| `--green-press` | `#045E43` | Hover / pressed |
| `--shad-yellow` | `#FFBA0C` | The three dots; the primary button **on green**; the lit-dot state. Never text or thin icons on white (1.71:1). Ink on yellow is 9.97:1 |
| `--dot-off` | `#FFE3A1` | An unlit dot (story progress) |

**Inside the phone only:** the app's own colors (subject cards lime `#8CD021`, teal `#489883`, cobalt `#3A4EED`, violet `#9471FE`; mint `#C7FFF3` selection; messenger blue `#0F7FF9`; red badges `#CD1E1E`). They appear because the app has them — never as page decoration.

No gradients. No glows. No colored shadows. Light theme only for this round.

---

## 3. Typography

**Yekan Bakh** for everything (FaNum variant if available). Until its files are in `assets/fonts/`, use **Vazirmatn** as a stand-in. Stack: `"Yekan Bakh", "Vazirmatn", Tahoma, sans-serif`. Weights: **400, 500, 700, 800** only.

Persian letterforms have a large visual size and tall ascenders and descenders. Latin-style display sizes look shouty in Persian. Use this scale (fluid between 360px and 1280px):

| Role | Mobile | Desktop | Weight | Line-height |
|---|---|---|---|---|
| Display (hero H1) | 30–32px | 52–56px | 800 | 1.35 |
| Section title (H2) | 24px | 36–40px | 700 | 1.45 |
| Chapter title (H3) | 20px | 26–28px | 700 | 1.5 |
| Lead | 16px | 18px | 400 | 1.9 |
| Body | 15px | 16px | 400 | 1.9 |
| Small / meta | 13px | 14px | 500 | 1.8 |
| Button | 15px | 16px | 700 | 1 |

- Line length for body: ≤ 60 characters (`max-width: 32rem`).
- Headlines: single color (ink), single weight. `text-wrap: balance`.
- Never letter-spacing on Persian. Never all-caps tricks. Persian digits. Preserve ZWNJ.
- Optical check: Persian text sits visually higher in its line box; check vertical centering in buttons and adjust padding by eye.

---

## 4. Space, grid, shape

**Grid.** Mobile: 4 columns, 20px side margins, 16px gutters. Desktop (≥1024px): 12 columns, 1200px container, 24px gutters. Every element snaps to it.

**Spacing.** 8px base: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 160. Section spacing: 96px mobile / 160px desktop. Inside a block, related items sit close (8–16px); unrelated groups are far apart (48px or more). Proximity, not boxes, creates groups.

**Alignment.** Text is start-aligned (right). The hero may center on mobile only if it composes better. Logical CSS properties throughout.

**Radius family** (three values, used consistently):
- `28px` — the phone's screen corners (and the phone body scales with it), the install panel
- `16px` — buttons, inputs, small panels
- `999px` — dots, badges

**Lines & depth.** Separation by space first, then 1px `--line` hairlines. No card boxes around text. One shadow on the whole page: under the phone, realistic and soft (`0 40px 80px -40px rgb(28 28 28 / .35)`), nothing else.

---

## 5. The dots & the wave

Built from `assets/brand/icon-flat.svg` (viewBox 37.6 × 39.7):
- Three yellow dots, each ≈ 28% of the mark's width; one on top in the center, two below on the sides.
- The green wave below them.

Rules:
- Use the real logo files for the logo. For the animated motif, use the exact dot and wave geometry from that SVG (copy the paths). Never redraw them freehand.
- **Never more than three dots on screen.** They are characters, not decoration.
- **No faces or limbs.** Personality comes from motion only.
- States: `lit` (`--shad-yellow`), `off` (`--dot-off`). The wave is always `--shad-green`.
- They appear in exactly three places:
  1. **Hero:** the mark composed with the phone (e.g. the dots resting above the phone, the wave under it).
  2. **Story:** a three-dot progress indicator beside the phone; chapter 1 lights the first dot, and so on. It shows the logo's arrangement (one top, two below).
  3. **Install:** the dots settle onto the wave, and the full mark completes — the story is resolved.

---

## 6. The phone

- One modern phone, front-facing, upright (no tilt, no 3D perspective), built in CSS/SVG with a thin ink bezel and the 28px screen radius. The **same phone** appears in the hero and continues as the story phone.
- Size: ~240px wide on mobile, ~300–320px on desktop.
- **Screens.** Every screen must look like the real Shad app (`assets/screens/home-light.png` is the style source: its header, tiles, cards, bottom nav, fonts, colors).
  - Hero: the real home screenshot (`home-light.webp`).
  - Chapter 1, «یاد بگیر»: a class screen built in HTML in the app's style — e.g. the «آموزشی» subject row (real crops in `assets/app-ui/`), a class channel with the teacher's lesson video, a homework message with a sent file and a check mark, a grade.
  - Chapter 2, «در ارتباط باش»: the chat list (class group, the teacher, the school's announcements channel) with unread badges; a new message arrives.
  - Chapter 3, «کشف کن»: the home's service row (شاد من، پیام‌رسان، تماشا، فیلم و سریال) plus events / Tamasha content, in the app's style.
- Screen transitions behave like the app itself (a short slide or cross-fade, 300–400ms).
- Pick one moment of life per screen (a message arriving, a check appearing). Not more.

---

## 7. Composition by block

These describe intent and a recommended composition. You may compose differently if it's clearly better and stays inside this system.

**Header.** Thin and quiet: logo (start), the primary CTA (end). On desktop, 3 small anchor links between them. 64px tall. Transparent over the hero, white with a hairline after scrolling.

**Hero.** Three things only: the message, the action, the product.
```
Mobile (360)                         Desktop (1440)
┌──────────────────────┐             ┌───────────────────────────────────────────┐
│ logo            [دریافت]│           │ logo        links                 [دریافت] │
│                      │             │                                           │
│ H1 (2 lines)         │             │   ● ● ●                 H1 (2 lines)      │
│ lead (2–3 lines)     │             │   ┌──────┐              lead              │
│ [██ primary CTA ███] │             │   │phone │              [primary] secondary│
│ secondary link       │             │   │      │              small trust line  │
│        ●             │             │ ~~│      │~~~~~~                          │
│       ● ●            │             │ ██└──────┘███                             │
│     ┌──────┐         │             └───────────────────────────────────────────┘
│ ~~~~│phone │~~~~     │
│ ████└──────┘████     │   (phone cropped by the fold; the wave in Shad Green behind its lower half)
└──────────────────────┘
```
At 360×640 the H1 and the primary button are fully visible without scrolling.

**Story (three chapters).** The heart of the page.
- Desktop: the phone is sticky in the end column (left), vertically centered; the three-dot indicator next to it. The start column scrolls three chapters, each roughly one viewport tall: a small chapter number (۱، ۲، ۳), the H3, two lines of body, and 3–5 feature words as a quiet list. When a chapter is active, its dot lights and the phone's screen changes.
- Mobile: the phone (smaller) stays pinned in the upper part of the viewport while each chapter's text passes beneath it; the dots sit beside the phone. If the viewport is short (< 640px) or reduced motion is on, fall back to a simple stack: chapter text, then its phone screen.
- The section title above the story is a single quiet line (see `CONTENT.md`).

**Also for teachers & families.** On `--mist`. Two columns on desktop, stacked on mobile; each is a title + 2–3 short lines. No icons, no cards.

**Proof.** White. One confident sentence with the big number set in the text («بیش از ۳۴ میلیون نصب»), then a single row of the five partner logos in grayscale, evenly spaced. Nothing else.

**Install (the climax).** Full-bleed `--green-deep`. The dots settle onto the wave here. White H2, short lead.
- A device switcher (Android / iPhone & iPad / Computer) as a segmented control, preselected to the visitor's device.
- The active panel shows only what that device needs: Android → «دریافت از بازار» (yellow, primary), «دریافت از مایکت» (secondary), the direct APK link with version and size; iPhone → «ورود به شاد در آیفون» + the 4 add-to-home-screen steps; Computer → «ورود به نسخه وب شاد» + a QR code to install on a phone.

**FAQ.** On `--mist`. Title in the start column, accordion in the end columns (desktop); stacked on mobile. Hairline dividers, no boxes. Support phone under the title.

**Footer.** White, small, orderly: logo + one-line about, link groups, support phone (prominent), copyright.

**Mobile sticky bar.** After the hero CTA scrolls away: a slim bar with the app icon, «شاد، رایگان» and the platform button. Hidden while the install section is on screen.

---

## 8. Banned (these made round 1 look AI-made)

- Pill/eyebrow tags above headlines
- Two-tone headlines, or one word highlighted in another color/weight
- Floating UI chips or cards around the phone, outside the phone
- Glows, blurs used as decoration, gradients, colored or stacked shadows
- Concentric arcs, orbits, rings, blobs, confetti, sparkles
- Bento grids, card grids of features, icons inside circles in rows
- Stats bands with big numbers, count-up counters
- Tilted or perspective phones, hands holding phones
- Testimonials (we have no real ones)
- Emojis, arrow characters appended to buttons, middle-dot (·) meta strings
- Scroll-reveal fade-ups on every block
- Any feature not listed in `CONTENT.md` §2 (especially رمزینه and حضور و غیاب)

---

## 9. Foundations (non-negotiable)

1. `<html lang="fa" dir="rtl">`, logical CSS properties, mirrored directional icons.
2. Mobile-first; flawless at 360–430px; no horizontal scroll from 320px.
3. Brand hex values exact; logo files used as-is.
4. Links, numbers, versions from `CONFIG` (`CONTENT.md` §1). No invented stats or claims.
5. WCAG 2.2 AA contrast; visible keyboard focus; touch targets ≥ 44px; `prefers-reduced-motion` respected (static, complete page); meaningful `alt`; decorative SVG `aria-hidden`.
6. No runtime requests to external domains (works on Iran's domestic network). Self-host fonts and any library.
7. Fast on a mid-range Android: WebP images with dimensions, the hero image prioritized, everything else lazy; motion only on `transform`/`opacity`.

---

## 10. Motion language

One language: **gentle spring physics**, like a small ball with a little weight.
- Hero load (once, ≤ 1.2s): the phone fades up a few px; the three dots drop in one after another and land with a small bounce. Text and CTA are visible immediately.
- Story: when a chapter activates, a dot hops from the previous position and lights up (≈ 450ms spring); the phone's screen transitions like the app does.
- Install: the dots settle onto the wave (completing the mark) when the section enters.
- UI: buttons press (scale .98), hover darkens; accordion and switcher animate height/position smoothly (200–250ms).
- Nothing loops forever. Nothing moves without a reason. Reduced motion: final states, no movement.

---

## 11. Asset map

| File | Use |
|---|---|
| `assets/brand/logo-full-color.svg` | The logo (header, footer) |
| `assets/brand/logo-full-white.svg` | Logo on the green install section if needed |
| `assets/brand/icon-flat.svg` | Source of the dots & wave geometry; favicon; sticky-bar icon |
| `assets/screens/home-light.{webp,png}` | Real home screen (hero phone), 824×1834 |
| `assets/app-ui/*-light.png` | Real crops for building chapter screens (subject cards, service tiles, search bar, bottom nav, banners) |
| `assets/partners/*.svg` | Partner logo placeholders (same filenames will be replaced) |
| `assets/fonts/` | Yekan Bakh here when supplied; Vazirmatn stand-in |
| `references/quality-bar/` | Finish-quality references only (see the README there) |
| `references/current-shad-ir.png` | The page we're replacing |
