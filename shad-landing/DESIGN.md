# DESIGN.md — Art direction for the Shad landing page

> Version 2.0 · October 2026
> This is an **art direction**, not a spec sheet. It tells you what the page should feel like, what world it comes from, and what level of craft is expected. It gives you building blocks and ideas. **You are the designer: compose, combine and push them.**
> Only section 9 (Foundations that don't move) is fixed. Everything else is direction you may interpret, extend or improve, as long as the result is clearly better.

---

## 1. The ambition

Build a landing page that would sit comfortably next to the best app landing pages on Land-book, Mobbin or Awwwards, and **feels unmistakably like Shad**.

Bar to clear: if someone puts our page next to the references in `references/`, it must look like it came from the same tier of studio. Rich, layered, confident, polished down to the pixel — and still instantly clear about what to do (install Shad).

The current page (`references/current-shad-ir.png`) is the opposite of what we want: flat, empty, pastel blobs, no product, no people, no life.

---

## 2. Reference study — what to take from each

Open every image in `references/` and study it at full size before designing. Do not copy any of them. Extract the **craft**.

| Reference | What makes it great | What we take |
|---|---|---|
| `ref-1-momento-full-page` | Big centered hero with the phone as the hero object, flanked by **fanned, tilted cards**; two-tone two-line headlines (light line + strong line) on every section; small pill tags above headings; pastel "how it works" cards; alternating feature rows that pair phone screens with imagery; audience cards with overlay labels; immersive gradient final CTA with phone + floating UI chips | The fan composition, two-tone headlines, pill tags, pastel step cards, gradient CTA band with phone |
| `ref-2-reel-hero-orbit` | Phone at center **rising out of concentric arcs**; product UI broken into **floating chips/cards** around it (live badge, stats, product cards, rating); clean centered type; logo marquee right under the hero | Phone-in-orbit + floating UI fragments as "proof"; logo strip under hero |
| `ref-3-community-arcs-stats` | Stats placed **inside** concentric arcs with avatars and status chips riding the arcs — a living ecosystem diagram; pill tags with icons below | The **super-app ecosystem orbit**: Shad at the center, services riding the arcs, stats inside |
| `ref-4-paylio-bento-faq` | Hero mixes a real photo with UI overlays; **bento grid** where each tile contains a real UI fragment (converter, transfer receipt), not just an icon; testimonial rows; split FAQ (title + help card on one side, accordion on the other) | Bento tiles that each *show* the feature working; split FAQ with support card |
| `ref-5-mobit-feature-explorer` | Hand-held phone in concentric rings; stats row with big numerals; **interactive feature explorer**: list of features on one side, a live preview panel on the other that changes on select | Feature/audience explorer with live preview |
| `ref-6-finto-grid-cta` | Disciplined grid with faint dashed column lines; bento of real UI fragments; deep green final CTA band; very clean footer | Grid discipline, deep green CTA band (fits our chalkboard green perfectly) |

**Common DNA across all six (this is the quality bar):**
1. The **product UI is the hero imagery** — real screens plus UI pieces lifted out and floated as cards around it.
2. **Depth and layering**: phone in front, cards behind and around it, soft shadows, slight tilts, arcs/rings behind.
3. **Generous whitespace**, huge confident headlines, very small supporting text.
4. **Every section has a different composition** (fan, orbit, bento, split, explorer, band) — no two sections look alike, yet one system ties them together.
5. **Small craft details everywhere**: pill tags with icons, status dots, avatar stacks, counters, check badges, micro-labels.

---

## 3. The Shad world — where our visual language comes from

Shad is not a utility app. It's a **super-app**: a whole school in a phone — classes, live lessons, digital textbooks, messenger, voice calls, events, games, search, video (Tamasha), films. Look at `assets/screens/home-light.png`: it's colorful, playful and dense with life.

**The page must carry that super-app energy: a full, lively school day orbiting around one app.**

### 3.1 Concept: «یک اپ، یک مدرسه کامل» — the whole school, in orbit

The phone is the school. Around it, the life of the school moves: a math class going live, a teacher's message arriving, homework getting a check mark, a physics textbook card, an event trophy, an animation playing in Tamasha. Shad's three yellow dots are the sun these things orbit around.

This idea can drive the hero, the ecosystem section and the final CTA — but **how** you stage it is your call.

### 3.2 Visual ingredients taken from the real app

| Ingredient from the app | Where it appears in the app | How to use it on the page |
|---|---|---|
| **Subject cards** — vivid color blocks with 3D school objects (books, telescope, globe) and a white "grade" pill | «آموزشی» row | The page's most Shad-specific asset. Fan them around the phone like Momento's photo cards; use them in bento tiles; use their colors as section accents |
| **Service tiles** — rounded app tiles (شاد من، پیام‌رسان، تماشا، فیلم و سریال) with badges («جدید», a blue count) | Top row | Ecosystem orbit, super-app section, floating chips |
| **Chalkboard banner** — green board with Tehran skyline in chalk | Hero banner | Texture/inspiration for the final CTA band or dark mode; the chalk-line skyline is a great "به وسعت ایران" motif |
| **«مدرسه من» banner** — 3D school building, schoolbag, books | Promo banner | Imagery for "your school" moments |
| **Mint selected state** (`#C7FFF3` fill + green border) | Selected tile, active nav | Active tabs, selected device card, highlights |
| **Bottom nav** (خانه، رویدادها، پخش زنده، اعلانات، حساب من) | Bottom bar | Can be used as a recognizable UI fragment |

Pre-cut crops of these are in `assets/app-ui/` (light and dark). They are low-resolution crops from a phone screenshot — fine for small floating cards; for anything larger, **rebuild the UI in HTML/CSS** in the same style (this usually looks sharper and lets you animate it).

### 3.3 The UI-fragment kit (build this — it is the soul of the page)

Build a small kit of HTML/CSS components that look like they were lifted straight out of the Shad app. They are illustrations of the product, used as floating cards, bento content and preview panels. Suggested pieces (content in `CONTENT.md` §6):

- **Live class card** — red «زنده» badge with pulsing dot, class name, teacher, stacked avatars, «۲۸ نفر آنلاین».
- **Message bubble / notification** — teacher avatar, name, one-line message, time.
- **Homework checklist** — 2–3 items, one getting checked.
- **Subject card** — color block + 3D object + grade pill (use crops or rebuild).
- **Digital textbook + رمزینه scan** — a book cover with a QR scanning line sweeping across it.
- **Service tiles** — app-icon-like tiles with badges.
- **Event / trophy chip** — «شاد رویداد».
- **Grade/result chip** — e.g. «آزمون ادبیات — ۱۹٫۵».
- **Stat chip** — big number + label.
- **Search bar** — the Shadbin search with mic icon.

Avatars: use simple, friendly initial circles in subject colors (no faces needed), or person photos if they are supplied later.

---

## 4. Color

### 4.1 Brand (fixed values)

| Name | Hex | Role |
|---|---|---|
| Shad Green | `#068F66` | Brand color. Large surfaces, logo, wave, highlights |
| Shad Yellow | `#FFBA0C` | Joy and emphasis. The three dots, primary button on green, badges, glows |
| Ink | `#1C1C1C` | Text (from the logo file) |

### 4.2 The super-app palette (sampled from the app)

Use these as **accents**, especially for subject cards, bento tiles, step cards, avatars and chips. They are what makes the page feel like Shad and not like a generic green brand.

| Name | Hex | From |
|---|---|---|
| Chalkboard | `#256243` | Chalkboard banner — deep sections, final CTA, dark mode base |
| Mint | `#C7FFF3` | Selected state — highlights, active tabs, soft fills |
| App background | `#F9F9F9` | App canvas — page background |
| Math lime | `#8CD021` | Subject card |
| History teal | `#489883` | Subject card |
| Physics cobalt | `#3A4EED` | Subject card |
| Social violet | `#9471FE` | Subject card |
| Messenger blue | `#0F7FF9` | Messenger tile / count badge |
| Live red | `#CD1E1E` | «جدید» / live badges |

Use pale tints of these (8–15% on white) for pastel cards (as Momento's step cards). Soft gradients and glows are welcome — e.g. mint→white sky behind the hero, a warm yellow glow behind the phone, chalkboard→brand-green in the final CTA.

### 4.3 Accessibility facts (measured — keep in mind)

- White text on Shad Green `#068F66` = **4.09:1** → fine for large text only. For buttons/links with white text use a darker green such as `#057A57` (5.35:1) / hover `#045E43`.
- Yellow `#FFBA0C` on white = **1.71:1** → never for text or thin icons on light backgrounds. Ink on yellow = **9.97:1** ✅.
- Check every subject-color pairing you use for text (white on lime `#8CD021` fails — use ink there).

### 4.4 Dark mode

Optional but welcome. If you build it, base it on the **chalkboard** world (deep green, chalk-white text, glowing yellow dots), not on grey/black. Swap the logo (`logo-full-white.svg`) and screenshots (`*-dark`). Light mode is the priority and must be perfect first.

---

## 5. Typography

- **Typeface: Yekan Bakh** (FaNum variant if available) for everything. Until its files are in `assets/fonts/`, use **Vazirmatn** as a local stand-in. Font stack: `"Yekan Bakh", "Vazirmatn", Tahoma, sans-serif`.
- Go **big and confident** on headlines, the way the references do. Suggested range: hero 44–48px on mobile, 72–88px on desktop; section headlines 30–34px mobile, 48–56px desktop. Body small and calm (15–17px). Find the exact scale by looking at your screenshots.
- **Two-tone, two-line headlines** (from Momento): line 1 lighter in color and/or weight (e.g. muted grey-green, weight 300–400), line 2 strong (ink, weight 800–900). `CONTENT.md` writes headlines in this two-line form.
- Persian needs more line-height than Latin (body ~1.8–1.9, display ~1.2–1.35). Never use letter-spacing on Persian text — it breaks letter joining.
- Persian digits everywhere in copy. Numbers in stats can be the most expressive type on the page.
- Small pill tags with an icon above section headlines are welcome (they're in all the references).

---

## 6. Imagery

Four image sources, in this order of priority:

1. **Real app screens** (`assets/screens/`) inside a realistic, modern phone frame (built in CSS/SVG). The phone is the main hero object.
2. **HTML/CSS UI fragments** in Shad's style (§3.3). Unlimited, sharp, animatable. Use them generously.
3. **3D school-object illustrations** in the style the app already uses (books, schoolbag, telescope, globe, school building). Available now only inside the screenshot crops; the client may supply originals later.
4. **Photography** of real Iranian students, teachers and families. Not supplied yet. Design the layout so that photo slots look good with a placeholder now and great with photos later (`assets/photos/` — see `CONTENT.md` §7 for art direction). Do not use stock photos from the internet.

---

## 7. Composition ideas, section by section

These are **starting points, not instructions**. Pick, combine, or do something better. Every section should have its own composition, like the references.

**Hero** — the biggest design moment of the page. Some directions to explore:
- *Orbit* (ref 2 + 3): centered two-line headline and CTAs, phone rising from the bottom out of concentric mint arcs, the yellow dots glowing like a sun behind it, UI fragments (live class, teacher message, homework check, stat chip) floating on the arcs.
- *Subject fan* (ref 1): phone at center, the four subject cards (lime, teal, cobalt, violet) fanned and tilted on both sides of it like playing cards, chips floating in front.
- A blend of the two, or your own idea.
On mobile: stay centered and bold; phone + two peeking cards + one or two chips — rich but not cluttered. The primary CTA must be reachable without scrolling.

**Partner strip** — directly under the hero: «همکاران شاد» with institution logos, as a calm row or slow marquee.

**Super-app ecosystem** — the "whole school in one app" statement. Ref 3 is the model: Shad's mark at the center, service tiles and chips riding concentric arcs, the stats (+۳۴ میلیون…) set large inside the arcs. Could gently rotate or react to scroll.

**How it works (3 steps)** — Momento-style pastel cards, each tinted with a different subject color, numbered (it's a real sequence), each with an icon tile or a tiny UI fragment.

**Features** — a bento grid (ref 4, 6) or alternating rows (ref 1). Each tile *shows* the feature: the live class card, the homework checklist, the textbook with رمزینه scan line, the chat thread. Vary tile sizes; give the lead feature (کلاس و تکالیف) the biggest tile.

**Who it's for** — an interactive explorer (ref 5): three audiences (دانش‌آموزان / معلم‌ها / خانواده‌ها) on one side; a phone or UI panel on the other that changes per audience. On mobile: segmented control on top, preview below. Photo cards (ref 1 "Built for Nightlife Culture") are a great alternative once photos exist.

**Install on any device** — three platform cards (Android, iPhone, Computer). The visitor's own device is highlighted (mint selected state, «دستگاه شما» badge) and comes first. iPhone card includes the add-to-home-screen guide; computer card includes the QR code.

**FAQ** — split layout (ref 4): headline + support card with the phone number on one side, accordion on the other. Stacks on mobile.

**Final CTA** — an immersive band (ref 1, 6): chalkboard-to-green gradient, maybe the chalk Tehran skyline, the phone with floating chips, yellow primary button. This should feel like the hero's echo.

**Footer** — clean and organized (ref 6), with the support number given prominence.

**Mobile sticky CTA** — a slim bar that appears after the hero CTA scrolls away.

---

## 8. Motion & interaction

Motion is part of the "خفن". Make the page feel alive — but every movement must be smooth, purposeful and cheap to run.

Good candidates:
- An orchestrated **hero entrance**: phone rises, cards fan out, chips pop in with a stagger, dots glow.
- **Ambient float** on hero chips (slow, a few px, offset timings) and subtle **pointer/scroll parallax** on desktop.
- **Logo marquee**, **count-up** stats when they enter the viewport, a slow **orbit** drift.
- Living UI fragments: pulsing live dot, a message bubble typing in, a homework item ticking, the رمزینه scan line sweeping.
- Tactile states on buttons and cards (hover lift, press). Smooth tab/explorer transitions, accordion height animation.
- Tasteful scroll-reveal is fine — vary it per section rather than the same fade-up everywhere.

Rules: animate `transform`/`opacity` (and filters sparingly); respect `prefers-reduced-motion` (show final states, stop loops); never delay the CTA; no jank on a mid-range Android phone.

---

## 9. Foundations that don't move

These are the only hard rules.

1. **Persian, RTL**: `<html lang="fa" dir="rtl">`, logical CSS properties, mirrored directional icons, no letter-spacing on Persian text, ZWNJ preserved.
2. **Mobile-first and flawless at 360–430px.** Most visitors are students on Android phones. Desktop must be equally impressive, but mobile is never a shrunken desktop. No horizontal scroll from 320px up.
3. **Brand**: the brand hex values in §4.1 are exact. Use the logo SVG files as-is; never redraw or recolor the logo.
4. **The job**: the platform-appropriate install/open action (`CONTENT.md` §3) is always the clearest thing on screen. All richness serves it, never competes with it.
5. **Facts come from `CONFIG`**: links, numbers, versions, phone number. Never invent stats, claims or testimonials.
6. **Accessibility**: WCAG 2.2 AA contrast for all text, visible keyboard focus, touch targets ≥ 44px, meaningful `alt`, decorative elements `aria-hidden`, works without motion.
7. **Self-contained**: no runtime requests to external domains (no CDNs, Google Fonts or third-party scripts) — the page must work on Iran's domestic network. Libraries installed locally and bundled/inlined are fine.
8. **Performance**: hero assets optimized (WebP, explicit dimensions, priority loading); everything below the fold lazy. Smooth on a mid-range phone.

---

## 10. Brand asset map

| File | Use |
|---|---|
| `assets/brand/logo-full-color.svg` | Logo on light backgrounds |
| `assets/brand/logo-full-white.svg` | Logo on dark / green backgrounds |
| `assets/brand/logo-full-black.svg` | Monochrome only |
| `assets/brand/icon-flat.svg` | App mark (three dots + wave) — favicon, sticky bar, ecosystem center, app-icon tiles |
| `assets/brand/icon-outlined.svg` | App mark with outline — playful uses |
| `assets/screens/home-{light,dark}.{webp,png}` | Real app home screen (824×1834) |
| `assets/app-ui/*-{light,dark}.png` | Crops of app UI pieces (subject cards, service tiles, banners, search, bottom nav) |
| `assets/partners/*.svg` | Placeholder partner logos — real files will replace them with the same names |
| `assets/photos/` | Empty — future photography |
| `assets/fonts/` | Yekan Bakh goes here; Vazirmatn as stand-in until then |
| `references/` | The six reference pages + the current shad.ir |
