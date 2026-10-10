# BRIEF.md — Shad landing page (read this first)

> Version 3.0 · October 2026 · Kit: `BRIEF.md` → `DESIGN.md` → `CONTENT.md` → `PROMPT.md`
> This file holds the thinking: goal, audience, the idea, the story and what we learned from round 1. If anything in the other files conflicts with this one, this one wins.

---

## 1. One goal

**Get a student (or their parent/teacher) to install or open Shad on the device they're holding.**

Every section, element and animation must do one of two things: make the visitor want Shad, or make installing it easier. Anything that does neither is removed. When in doubt, cut it.

Success test (5 seconds, on a phone): a 14-year-old can say *what Shad is* and *which button to press*.

---

## 2. Audience

| Who | Share | What they need from this page |
|---|---|---|
| **Students, 7–18** (mostly 12–18) | Primary | "Is this cool or is this just homework?" Fast, clear, not childish, not boring. Usually on a mid-range Android phone. |
| **Parents** | Secondary | "Is it official and safe? How do I set it up for my kid?" |
| **Teachers & school staff** | Secondary | "Does it make my class easier?" Often on desktop too. |

What research says about teenagers on the web (Nielsen Norman Group): they skim; they hate dense text, tiny fonts, clutter, gimmicky glitz and **anything that talks down to them**; they love polished design, interactivity they control, and fast pages. They give up quickly when something is confusing.

So the page is **polished, calm, confident and fast** — the opposite of noisy. Delight comes from craft and one clever idea, not from quantity.

---

## 3. The idea: «سه نقطه» (the three dots)

Shad's logo is three yellow dots resting on a green wave.

- **The three dots are three people**: a student, a teacher, a family — anywhere in Iran.
- **The wave is Shad**, the thing that holds them together: «مدرسه‌ای به وسعت ایران».

This is the page's only visual idea, and it carries everything:
- The **hero** is built around the real app and the logo mark (dots + wave).
- The **story** has exactly **three chapters**, and the three dots are the progress indicator: one dot lights up per chapter. The logo literally tells the story.
- The **install moment** closes the loop: the dots and the wave come together.

The dots are abstract — no faces, no eyes, no mascot drawings. They show character only through **motion** (a little bounce, a hop to the next chapter, settling onto the wave). That keeps it playful for kids and still credible for teens and parents.

---

## 4. The story (page architecture)

```
HERO         «مدرسه‌ات، هر جا که باشی»  → real phone, logo mark, ONE platform-aware CTA
  │
STORY        one phone stays on screen; its screen changes per chapter; one dot lights per chapter
  ├─ ● ۱  یاد بگیر          class online · homework · lesson videos · tests & grades
  ├─ ● ۲  در ارتباط باش     class group · message the teacher · school announcements
  └─ ● ۳  کشف کن            events · Tamasha · films & series · Shadboom games · Shadbin search
  │
ALSO FOR     short: teachers / families (two quiet columns)
  │
PROOF        «۳۴ میلیون نصب» as one confident line + partner logos
  │
INSTALL      the climax: the visitor's device first, other devices one tap away
  │
FAQ          5 short answers + support phone
FOOTER
```

Seven blocks. Not more. No stats band, no feature grid, no bento, no testimonials, no "how it works" cards (installation steps live inside the install block).

---

## 5. Voice

- Speak to the student with a respectful, warm **«تو»**: short, direct, a little playful, never babyish. Example: «مدرسه‌ات، هر جا که باشی.»
- Switch to **«شما»** only where adults are addressed (families/teachers block, support, FAQ answers about setup).
- Short sentences. One idea per line. No marketing superlatives, no vague slogans ("بهترین", "انقلابی", "تجربه‌ای بی‌نظیر"). Say what Shad actually does.
- Only real features (see `CONTENT.md` §2). Never mention رمزینه or attendance (حضور و غیاب).

---

## 6. Round 1 feedback — what went wrong, and the rule that fixes it

The client reviewed the first build. Every point below is a rule for this round.

| # | Client feedback | Rule now |
|---|---|---|
| 1 | Too crowded | Seven blocks only. Generous whitespace. Max one visual focus per screen. |
| 2 | Hero not used well | The hero gets the real product (phone), the idea (dots + wave) and **one** primary action, composed with care. Nothing else. |
| 3 | Elements too big, wrong for Persian | Persian glyphs read large — use the type scale in `DESIGN.md`, headline weight ≤ 800. |
| 4 | Looks AI-made, repeated patterns | Banned list in `DESIGN.md` §8 (pill tags, two-tone headlines, floating chips, glows, bento, icon grids…). |
| 5 | Not Shad-like, not appealing to under-18s, confusing | Real app screens, Shad's own colors, a student-first voice, calm layout. |
| 6 | Goal unclear | One goal (§1). Platform-aware CTA always one tap away. |
| 7 | No storytelling | Three-chapter story (§4) with the dots as narrator. |
| 8 | No creativity, messy | One idea (§3), executed deeply and consistently, instead of many ideas. |
| 9 | No unity | One grid, one radius family, one motion language, one color story (`DESIGN.md`). |
| 10 | Features we don't have (رمزینه, attendance) | Only features from `CONTENT.md` §2. |
| 11 | Fake glows and shadows | No glows. Flat color and hairlines. One real shadow at most (the phone). |
| 12 | Doesn't fit Shad's world | Everything derives from the logo and the real app. |

---

## 7. What "excellent" means here

It should feel like a senior team spent weeks on it: every margin decided, every word earned, one idea pushed all the way. **Minimal but not empty; playful but not childish; rich in craft, poor in noise.** If a section could belong to any other app's landing page, it isn't finished.
