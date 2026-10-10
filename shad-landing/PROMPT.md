# PROMPT.md — Prompts for Claude Design and Claude Code

> Version 3.0 · October 2026
> Kit: `BRIEF.md` · `DESIGN.md` · `CONTENT.md` · `PROMPT.md` · `assets/` · `references/`
> **A) Claude Design** — design exploration and the full page (recommended starting point).
> **B) Claude Code** — production HTML.
> **C)** Moving between the two.

---

## A) Claude Design

Upload: `BRIEF.md`, `DESIGN.md`, `CONTENT.md`, `assets/brand/*.svg`, `assets/screens/home-light.png`, the `assets/app-ui/*-light.png` crops, `assets/partners/*.svg`, `references/current-shad-ir.png`. Then send:

````markdown
You're the creative lead of a small senior design team. Design the new download landing page for **Shad (شاد)**, Iran's official school super-app (34M+ installs). Persian, RTL, mobile-first. Audience: students 12–18 first, then parents and teachers.

Read the attached files in this order: BRIEF.md (goal, idea, story, and the client's feedback from round 1 — treat it as hard-won lessons), DESIGN.md (the visual system and the banned list), CONTENT.md (final copy, real features, phone-screen content).

The idea is «سه نقطه»: the logo's three yellow dots are a student, a teacher and a family; the green wave is Shad, holding them together. One real phone carries a three-chapter story (یاد بگیر / در ارتباط باش / کشف کن) and the dots light up one per chapter. Calm, minimal, crafted — playful through motion and detail, never through clutter.

Round 1 was rejected as crowded, generic, AI-looking, too big for Persian, without story or unity. Avoid everything in DESIGN.md §8.

Deliver, in this order — and pause after step 1 so I can choose:
1. **Three hero directions** inside the system, each at 390px and 1440px. Same copy, different composition of phone + dots + wave + text. One-line rationale each.
2. For the chosen direction: the **full page at 390px**, then at **1440px**.
3. The **three chapter phone screens** at full size, matching the real app's style (use the screenshot and crops as the style source).

Before you show anything, review it against the 12 rules in BRIEF.md §6 and remove one unnecessary element from every section.

Fixed: brand colors #068F66 / #FFBA0C, logo files as-is, Vazirmatn as stand-in for Yekan Bakh, the type scale in DESIGN.md §3, facts in CONTENT.md §1–2.
````

**Feedback rounds in Claude Design:** reply per section and breakpoint (e.g. "Hero @390: the phone starts too low; dots too small"). After each round, ask it to re-check BRIEF.md §6.

---

## B) Claude Code

Put the whole kit in an empty folder and send:

````markdown
You're the design lead and front-end engineer of a senior studio. Build the new download landing page for **Shad (شاد)**, Iran's official school super-app, as production-quality static HTML.

## Read first, in order
1. `BRIEF.md` — the goal, audience, idea, story, and the client's round-1 feedback. This is the most important file. It wins over the others.
2. `DESIGN.md` — the visual system (color, type, grid, radii, dots & wave, phone, compositions, motion) plus §8 banned and §9 foundations.
3. `CONTENT.md` — locked facts (CONFIG), the only features allowed, final copy, phone-screen content.
4. Look at `assets/screens/home-light.png` and `assets/app-ui/` closely: the chapter screens you build must look like the real app.
5. `references/quality-bar/` is for finish quality only; read its README. Do not borrow its layouts.

## Before coding, write in chat (short)
- The idea and the story in your own words (3 sentences).
- How the hero, the story and the install moment use the dots and the wave.
- The three biggest risks of making this look crowded or generic, and how you'll avoid each.

## Build
- `index.html` with inline CSS/JS (vanilla), plus `assets/`. Local npm tools/libraries are fine if the final output is static files with **zero runtime requests to external domains**.
- Fonts: use Yekan Bakh from `assets/fonts/` if present; otherwise `npm i vazirmatn`, copy the WOFF2s into `assets/fonts/`, and keep "Yekan Bakh" first in the stack.
- Platform detection in an inline `<head>` script → `data-platform` on `<html>` = `android` | `ios` (iPhone/iPad, incl. iPad with a Mac UA + touch) | `desktop` | `unknown`. It drives the primary CTA everywhere and preselects the install switcher.
- Story: implement the sticky phone with `position: sticky` + IntersectionObserver per chapter; the active chapter updates the phone screen and lights its dot. Short-viewport (< 640px tall) and reduced-motion fallback = simple stacked chapters.
- Dots & wave: use the exact path geometry from `assets/brand/icon-flat.svg`. Spring motion as in DESIGN.md §10 (CSS `linear()` easing or a tiny spring function).
- QR code: generate at build time (`qrcode` npm) as inline SVG for `CONFIG.links.landing`.
- Analytics hooks only (no scripts): `data-track="cta_click"` with `data-channel` (bazaar|myket|apk|pwa|web) and `data-location` (header|hero|sticky|install).

## Build order
Header → hero → story (chapter screens first, as isolated components) → also-for → proof → install → FAQ → footer → sticky bar. Build at 390px first, then compose 1440px deliberately.

## Critique rounds (at least 3)
Each round: Playwright screenshots at 360, 390, 768, 1440 (full page + first viewport), with Android, iPhone and desktop user agents, saved to `qa/round-N/`. Then review them as a demanding creative director:
1. Go through BRIEF.md §6 point by point (all 12). Write pass/fail for each, with the reason.
2. AI-tell scan: anything from DESIGN.md §8? Anything that could appear on any other app's landing page?
3. Persian scale check: is any text or element shouting? Compare against the type scale.
4. Remove at least one unnecessary element per section in round 1 and 2.
5. Fix, re-shoot, repeat. Stop only when every point passes.

## Final QA
axe (via `@axe-core/playwright`) with zero violations; full keyboard path with visible focus; zero external requests in the network log; smooth on a 4× CPU-throttled mobile profile; complete and calm with `prefers-reduced-motion`.

## Report
What you built, the round-by-round pass/fail table, any deviation from the brief and why, open items (font files, real partner logos, APK size confirmation).
````

---

## C) Moving between Claude Design and Claude Code

- **Design → Code:** export or screenshot the approved Claude Design frames (390 and 1440, plus the chapter screens) into `references/approved/`. Add one line to the Claude Code prompt: "Match the approved design in `references/approved/` exactly; where it is silent, follow DESIGN.md." The kit stays the source for copy, facts and rules.
- **Code → Design:** take the Playwright screenshots from the final `qa/` round (and the `index.html` if Claude Design accepts it) into Claude Design with the kit files, and ask it to refine specific sections, again citing BRIEF.md §6.
- Whichever tool you're in, keep feedback in the same shape: *block @ breakpoint: what's wrong → what you want*.

---

## D) Swap-ins later (no redesign needed)
Yekan Bakh → `assets/fonts/` · real partner logos → `assets/partners/` (same filenames) · numbers and links → `CONFIG` · campaign → `CONFIG.campaign.enabled`.
