# CONTENT.md — Shad download landing page (shad.ir)

> Version 0.2 · October 2026
> This file is the **single source of truth for page structure and all copy**.
> Companion files: `DESIGN.md` (visual system) · `PROMPT.md` (build instructions)

---

## 0. Rules for the builder

1. **Use the Persian copy verbatim.** Do not rewrite, shorten, translate or add copy. If a slot has no copy, leave an HTML comment `<!-- COPY MISSING -->` instead of inventing text.
2. **Never change numbers.** All stats, versions and phone numbers come from `CONFIG` (section 2). They are placeholders the client will update.
3. **Section order is fixed** (section 4). Mobile/desktop differences are stated per section.
4. **Source tags.** Every section and item is tagged:
   - `existing` — content that exists on the current shad.ir.
   - `new` — content added to improve the page. It is real, usable copy, but the client may swap it later. Mark each `new` block with `data-source="new"` on its wrapper so it can be found and replaced easily.
5. `{{path}}` means "read from `CONFIG`". Never hard-code these values in markup.
6. All digits in copy are already Persian (۰–۹). Keep them as typed. Do not convert to Latin digits. URLs stay Latin.
7. Wrap brand and product names that must not be machine-translated in `<span translate="no">`: شاد, بازار, مایکت, Safari, APK.

---

## 1. Page goal (context for design decisions)

| Item | Definition |
|---|---|
| Page type | Download & activation landing page, not a corporate "about" page |
| User's job | "Install Shad on this device with no hassle and get into my class." |
| Primary action | The platform-appropriate download / open button |
| Primary audience | Students and their families, mostly on Android phones |
| Secondary audience | Teachers and school staff (phone + desktop) |
| Tertiary audience | Institutions, press (mostly desktop) |
| 5-second test | A first-time visitor must understand: (1) Shad is the free school & class app, (2) which button to press |

---

## 2. CONFIG (single object at the top of the script)

```js
const CONFIG = {
  links: {
    bazaar:   "https://cafebazaar.ir/app/ir.medu.shad",
    myket:    "https://myket.ir/app/ir.medu.shad",
    apk:      "https://shad.ir/static/apk/Shad_v3_8_2.apk",
    pwa:      "https://my.shad.ir/",   // iPhone/iPad (PWA) — same URL as web
    web:      "https://my.shad.ir/",
    landing:  "https://shad.ir/",      // QR code target on desktop
    privacy:  "#",                     // placeholder
    terms:    "#",                     // placeholder
    campaign: "#"                      // placeholder
  },
  apk: {
    version: "۳.۸.۲",
    size:    "۴۵ مگابایت",             // placeholder
    minOs:   "اندروید ۵ به بالا"        // placeholder
  },
  support: {
    phoneDisplay: "۰۲۱-۴۳۰۸۱",
    phoneHref:    "tel:+982143081"
  },
  stats: [                              // existing numbers from shad.ir
    { value: "+۳۴", unit: "میلیون",  label: "نصب یکتا" },
    { value: "+۸۷", unit: "میلیارد", label: "پیام ارسال‌شده" },
    { value: "+۱۲", unit: "میلیارد", label: "فایل جابه‌جاشده" }
  ],
  activeUsers: {                        // existing, from shad.ir footer
    daily: "۱۲ میلیون", weekly: "۱۵ میلیون", monthly: "۲۰ میلیون"
  },
  campaign: {                           // existing banner, as an optional slot
    enabled: true,
    text: "انیمیشن «ببعی قهرمان» در شاد رایگان شد",
    linkText: "تماشا کنید"
  },
  year: "۱۴۰۵"
};
```

---

## 3. Voice & copy rules

- Tone: warm, clear, trustworthy. Friendly for teenagers, credible for parents and teachers. Never childish, never bureaucratic.
- Address the reader as «شما» with short, active verbs («نصب کنید»، «وارد شوید»). No slang.
- Headlines: max ~8 words. One idea per sentence.
- Persian punctuation: «» quotes, «،» comma, «؛» semicolon. Use the zero-width non-joiner (ZWNJ, U+200C) where the copy has it (e.g. «می‌شود»، «دانش‌آموز») — preserve it exactly.
- Button labels say exactly what happens («دریافت از بازار», not «کلیک کنید»).

---

## 4. Information architecture

```
[0]  Campaign bar             existing   optional, dismissible
[1]  Header                   new
[2]  Hero + smart CTA         existing+new
[3]  Trust: partners + stats  existing
[4]  Core features (4)        existing (rewritten)
[5]  More in Shad             existing
[6]  Who it's for (tabs)      new
[7]  Get started in 3 steps   new
[8]  All install options      existing+new
[9]  FAQ                      new
[10] Final CTA                new
[11] Footer                   existing+new
[*]  Sticky CTA bar           new        mobile only
```

Narrative logic: what do I do (hero) → why trust it (3) → what do I get (4–6) → how do I start (7–8) → what if I get stuck (9) → do it now (10).

---

## 5. Section content

### [0] Campaign bar — `#campaign` · existing

- Purpose: a controlled slot for current campaigns, so they never sit above the brand or break the hero (the current site's banner is cropped and dominates the page).
- Shown only when `CONFIG.campaign.enabled` is true.
- Content: `{{campaign.text}}` + link `{{campaign.linkText}}` → `{{links.campaign}}`.
- Close button, `aria-label="بستن اطلاعیه"`. Dismissal is remembered for the session.
- Must fit on one line at 360px; truncate with ellipsis rather than wrap.

---

### [1] Header — `<header>` · new

| Element | Content |
|---|---|
| Skip link (first focusable element) | «پرش به محتوای اصلی» → `#main` |
| Logo | Full Shad logo, links to top. `alt="شاد، مدرسه‌ای به وسعت ایران"` |
| Nav (≥1024px) | «قابلیت‌ها» → `#features` · «راهنمای نصب» → `#install` · «سؤالات متداول» → `#faq` · «پشتیبانی» → `#support` |
| Secondary action (≥1024px) | «ورود به نسخه وب» → `{{links.web}}` |
| Primary action (≥1024px) | «دریافت شاد» → scrolls to `#install` |
| Mobile (<1024px) | Logo + compact primary button «دریافت» (platform-aware, see Hero) + menu button (`aria-label` «باز کردن منو» / «بستن منو») |
| Mobile menu | The 4 nav links + «ورود به نسخه وب» |
| Theme toggle | Icon button, `aria-label="تغییر حالت روشن و تاریک"` |

---

### [2] Hero — `#hero` · existing + new

**H1:**
> کلاس، کتاب و معلم؛ همه یک‌جا در شاد

**Subheading:**
> بزرگ‌ترین اپلیکیشن آموزشی ایران؛ کلاس آنلاین، کتاب درسی دیجیتال و ارتباط با معلم و مدرسه، برای دانش‌آموزان، معلم‌ها و خانواده‌ها.

**Smart CTA block.** Detect the platform and render exactly one of these states:

**State A: Android**

| Role | Copy | Target |
|---|---|---|
| Primary button | «دریافت از بازار» | `{{links.bazaar}}` |
| Secondary button | «دریافت از مایکت» | `{{links.myket}}` |
| Text link | «دانلود مستقیم فایل نصبی (APK)» | `{{links.apk}}` |
| Meta under link | «نسخه {{apk.version}}، {{apk.size}}» | — |

**State B: iPhone / iPad**

| Role | Copy | Target |
|---|---|---|
| Primary button | «ورود به شاد در آیفون» | `{{links.pwa}}` |
| Helper text | «بدون نیاز به اپ‌استور؛ شاد را به صفحه اصلی گوشی اضافه کنید.» | — |
| Text link | «راهنمای نصب روی آیفون» | `#install-ios` (and open that guide) |

**State C: Desktop**

| Role | Copy | Target |
|---|---|---|
| Primary button | «ورود به نسخه وب شاد» | `{{links.web}}` |
| QR card title | «نصب روی گوشی» | — |
| QR card text | «این کد را با دوربین گوشی اسکن کنید.» | QR encodes `{{links.landing}}` |

**Fallback (no JS / unknown platform):** show three equal buttons: «دریافت از بازار», «ورود به شاد در آیفون», «ورود به نسخه وب شاد».

**Below the CTA block (all states):**
- Link: «دستگاه دیگری دارید؟ همه روش‌های نصب» → `#install`
- Trust line: «رایگان، با بیش از ۳۴ میلیون نصب»

**Hero visual:** the real app home screen in a phone frame. Light theme → `home-light`, dark theme → `home-dark`. `alt="صفحه اصلی اپلیکیشن شاد"`.

**Order:**
- Mobile: H1 → subheading → CTA block → link + trust line → phone visual (top portion visible, cropped at the bottom by the section edge).
- Desktop: text + CTA in the start column (right side, RTL), phone visual in the end column (left side).
- H1 and the primary button must be visible without scrolling at 360×640.

---

### [3] Trust — `#trust` · existing

**Visually hidden H2 (screen readers only):** «شاد در یک نگاه»

**Partner logos.** Small heading:
> همکاران شاد

1. وزارت آموزش و پرورش
2. وزارت ارتباطات و فناوری اطلاعات
3. مرکز ملی فضای مجازی
4. همراه اول
5. پلیس فتا

Each logo has `alt` = the institution's full name above. Files are placeholders (see `DESIGN.md`).

**Stats** from `{{stats}}`. Render the value and unit together on one line (e.g. «+۳۴ میلیون») and the label beneath. Never split value and unit across lines.

---

### [4] Core features — `#features` · existing (rewritten)

**H2:**
> هرچه برای درس و مدرسه لازم دارید

**Lead:**
> از کلاس زنده تا کتاب درسی، همه در یک اپلیکیشن.

Four features, in priority order. Feature 1 is the lead feature and gets more space on desktop.

**1. کلاس و تکالیف** — product label: «سامانه مدیریت یادگیری»
> کلاس مجازی، تکلیف و آزمون در یک‌جا؛ طراحی‌شده برای نیازهای آموزش و یادگیری معلم‌ها و دانش‌آموزان.

**2. کلاس زنده** — product label: «پخش زنده»
> کلاس تصویری زنده در کانال‌ها و گروه‌ها، با امکان مرور درس و برگزاری جلسه.

**3. کتاب درسی دیجیتال** — product label: «رمزینه‌خوان»
> نسخه دیجیتال کتاب‌های درسی همه مقاطع؛ رمزینه‌های کتاب را اسکن کنید و به محتوای آموزشی برسید.

**4. گفت‌وگو با معلم و مدرسه** — product label: «گفت‌وگوی صوتی»
> پیام، کانال و تماس صوتی گروهی؛ برای کلاس مجازی و ارتباط روزانه با مدرسه.

Each feature: icon (or screenshot) + title (H3) + product label (small, muted) + text. Features are not links.

---

### [5] More in Shad — `#more` · existing

**H3:**
> و بیشتر در شاد

| Name | One-line description |
|---|---|
| نمونه تدریس‌ها | محتوای آموزشی همه درس‌ها، از پیش‌دبستانی تا دوازدهم |
| شادبین | جست‌وجوی سریع، هدفمند و پاک برای اهالی مدرسه |
| شادبوم | بازی‌های آموزشی و سرگرمی سالم |
| شاد رویداد | رویدادهای پرورشی و فرهنگی در مقیاس ملی |

Mobile: two-column grid. Desktop: one row of four.

---

### [6] Who it's for — `#audiences` · new

**H2:**
> برای همه اهالی مدرسه

Tabs, default = first tab. On mobile, render as a full-width segmented control.

**Tab 1: «دانش‌آموزان»**
- Title: «همه درس‌ها، همیشه همراه شما»
- «در کلاس زنده شرکت کنید و تکلیف‌ها را همان‌جا تحویل دهید.»
- «کتاب‌های درسی و محتوای آموزشی را هر وقت خواستید مرور کنید.»
- «با معلم و هم‌کلاسی‌ها در گروه کلاس در ارتباط باشید.»

**Tab 2: «معلم‌ها»**
- Title: «کلاستان را ساده‌تر اداره کنید»
- «کلاس زنده برگزار کنید و جلسه‌ها را برای مرور در دسترس بگذارید.»
- «تکلیف و آزمون بدهید و پاسخ‌ها را یک‌جا ببینید.»
- «با دانش‌آموزان و خانواده‌ها در کانال کلاس در ارتباط باشید.»

**Tab 3: «خانواده‌ها»**
- Title: «در جریان درس فرزندتان باشید»
- «اطلاعیه‌های مدرسه و کلاس را مستقیم دریافت کنید.»
- «از تکلیف‌ها و برنامه کلاس فرزندتان باخبر شوید.»
- «فضایی آموزشی و امن برای فرزندتان.»

**CTA under tabs:** «دریافت شاد» → platform-aware primary action.

---

### [7] Get started — `#get-started` · new

**H2:**
> در سه قدم وارد کلاس شوید

This is a real sequence, so numbered markers are appropriate.

| Step | Title | Text |
|---|---|---|
| ۱ | نصب کنید | «شاد را از بازار یا مایکت دریافت کنید. در آیفون، نسخه وب را به صفحه اصلی اضافه کنید.» |
| ۲ | ثبت‌نام کنید | «با شماره موبایل ثبت‌نام کنید و کد تأیید پیامکی را وارد کنید.» |
| ۳ | به کلاس بپیوندید | «نقش خود را انتخاب کنید و وارد کلاس و مدرسه‌تان شوید.» |

---

### [8] All install options — `#install` · existing + new

**H2:**
> شاد را روی دستگاه خود نصب کنید

**Lead:**
> روی هر گوشی و کامپیوتری در دسترس است.

Three panels. The panel matching the visitor's platform comes first and carries the badge «دستگاه شما».

**Android — `#install-android`**
- Title: «اندروید»
- Buttons: «دریافت از بازار» · «دریافت از مایکت»
- Link: «دانلود مستقیم فایل نصبی (APK)»
- Meta (three separate items, not a dot-joined string): «نسخه {{apk.version}}» / «{{apk.size}}» / «{{apk.minOs}}»
- Note: «با نصب از بازار یا مایکت، شاد خودکار به‌روز می‌شود.»

**iPhone & iPad — `#install-ios`**
- Title: «آیفون و آیپد»
- Button: «ورود به شاد در آیفون» → `{{links.pwa}}`
- Guide title: «افزودن شاد به صفحه اصلی آیفون»
- Steps (ordered list):
  1. «آدرس my.shad.ir را در مرورگر Safari باز کنید.»
  2. «دکمه اشتراک‌گذاری (مربع با فلش رو به بالا) را بزنید.»
  3. «گزینه «Add to Home Screen» یا «افزودن به صفحه اصلی» را انتخاب کنید.»
  4. «دکمه «Add» را بزنید؛ آیکون شاد روی صفحه اصلی ظاهر می‌شود.»
- Guide is expanded by default on iOS, collapsed (disclosure) elsewhere.

**Desktop — `#install-desktop`**
- Title: «کامپیوتر و لپ‌تاپ»
- Button: «ورود به نسخه وب شاد» → `{{links.web}}`
- Text: «بدون نصب، در هر مرورگری. برای نصب روی گوشی، کد را اسکن کنید.»
- QR code → `{{links.landing}}` (shown only at ≥1024px).

---

### [9] FAQ — `#faq` · new

**H2:**
> سؤالات متداول

All collapsed by default. Also output as `FAQPage` JSON-LD.

1. **«استفاده از شاد هزینه دارد؟»**
   «نه. نصب و استفاده از شاد رایگان است.»

2. **«چطور شاد را روی آیفون نصب کنم؟»**
   «شاد در آیفون از طریق نسخه وب در دسترس است. my.shad.ir را در Safari باز کنید، دکمه اشتراک‌گذاری را بزنید و «افزودن به صفحه اصلی» را انتخاب کنید.» + link «راهنمای تصویری» → `#install-ios`

3. **«از بازار نصب کنم، مایکت یا فایل مستقیم؟»**
   «فرقی ندارد؛ هر سه همان اپلیکیشن رسمی شاد است. نصب از بازار یا مایکت بهتر است، چون شاد خودکار به‌روز می‌شود. اگر به این فروشگاه‌ها دسترسی ندارید، فایل نصبی را مستقیم دانلود کنید.»

4. **«گوشی اجازه نصب فایل APK را نمی‌دهد. چه کنم؟»**
   «در تنظیمات گوشی، اجازه نصب برنامه از منابع ناشناس را برای مرورگر یا مدیر فایل فعال کنید و دوباره فایل را باز کنید. فایل نصبی را فقط از سایت رسمی شاد دریافت کنید.»

5. **«چطور شاد را به‌روزرسانی کنم؟»**
   «اگر از بازار یا مایکت نصب کرده‌اید، از همان‌جا به‌روزرسانی کنید. در غیر این صورت، آخرین نسخه را از همین صفحه دریافت و نصب کنید.»

6. **«کد تأیید پیامکی برایم نمی‌آید.»**
   «چند دقیقه صبر کنید و درست بودن شماره موبایل را بررسی کنید. اگر باز هم پیامک نرسید، با پشتیبانی شاد تماس بگیرید.»

7. **«کلاس یا مدرسه‌ام را در شاد پیدا نمی‌کنم.»**
   «عضویت در کلاس‌ها از طرف مدرسه انجام می‌شود. از معلم یا مدیر مدرسه بخواهید عضویت شما را بررسی کند.»

8. **«روی کامپیوتر هم می‌شود از شاد استفاده کرد؟»**
   «بله. نسخه وب شاد در my.shad.ir بدون نصب و در هر مرورگری در دسترس است.»

---

### [10] Final CTA — `#final-cta` · new

**H2:**
> کلاس شما در شاد منتظر است

**Text:**
> همین حالا شاد را دریافت کنید و به میلیون‌ها دانش‌آموز و معلم بپیوندید.

**CTA:** the same smart CTA block as the hero (states A/B/C), compact version, without the QR card.

---

### [11] Footer — `<footer>` · existing + new

**Column 1: About** · existing
- Logo
- Heading: «پلتفرمی که بزرگ‌ترین زیست‌بوم آموزشی کشور شد»
- Text:
  > شاد، مدرسه‌ای به وسعت ایران و بزرگ‌ترین اپلیکیشن آموزشی کشور است. تاکنون بیش از ۳۴ میلیون نصب یکتا داشته و در بیشینه حالت، {{activeUsers.daily}} کاربر فعال روزانه، {{activeUsers.weekly}} کاربر فعال هفتگی و {{activeUsers.monthly}} کاربر فعال ماهانه داشته است.

**Column 2: Get Shad** · existing
- «اندروید از بازار» · «اندروید از مایکت» · «فایل نصبی APK» · «آیفون و آیپد» · «نسخه وب»

**Column 3: Help** · new
- «راهنمای نصب» → `#install` · «سؤالات متداول» → `#faq` · «حریم خصوصی» → `{{links.privacy}}` · «شرایط استفاده» → `{{links.terms}}`

**Column 4: Support — `#support`** · existing + new
- Heading: «پشتیبانی تلفنی»
- Phone: `{{support.phoneDisplay}}` as a `tel:` link. Wrap the number in `<span dir="ltr">`.
- Text: «تنها شماره رسمی مرکز پاسخ‌گویی شاد» (existing)
- Note: «پشتیبانی شاد هرگز کد تأیید پیامکی شما را نمی‌خواهد.» (new)

**Bottom row:** «© {{year}} شاد. همه حقوق محفوظ است.»

Mobile: columns stack; columns 2 and 3 become disclosures.

---

### [*] Sticky CTA bar — mobile only · new

- Appears when the hero CTA block leaves the viewport; hides while the final CTA or footer is visible.
- Content: Shad app icon + «شاد، رایگان» + platform button:
  - Android: «دریافت از بازار»
  - iOS: «ورود به شاد»
- Never shown at ≥1024px.

---

## 6. System microcopy

| Context | Copy |
|---|---|
| Skip link | «پرش به محتوای اصلی» |
| Menu button | «باز کردن منو» / «بستن منو» |
| Close campaign | «بستن اطلاعیه» |
| Theme toggle | «تغییر حالت روشن و تاریک» |
| Current-device badge | «دستگاه شما» |
| External link hint (visually hidden) | «(در صفحه جدید باز می‌شود)» |
| APK download started (aria-live) | «دانلود فایل نصبی شاد شروع شد.» |
| QR alt | «کد QR برای باز کردن صفحه دریافت شاد روی گوشی» |

---

## 7. SEO & metadata

| Field | Value |
|---|---|
| `html` | `lang="fa" dir="rtl"` |
| `<title>` | «دانلود شاد؛ اپلیکیشن آموزشی دانش‌آموزان ایران» |
| `meta description` | «شاد، بزرگ‌ترین اپلیکیشن آموزشی ایران: کلاس آنلاین، کتاب درسی دیجیتال و ارتباط با معلم و مدرسه. دریافت رایگان برای اندروید، آیفون و نسخه وب.» |
| `og:title` | «شاد، مدرسه‌ای به وسعت ایران» |
| `og:description` | same as meta description |
| `og:image` | `assets/og-image.png` (placeholder path) |
| `theme-color` | two tags, light and dark, values from `DESIGN.md` |
| JSON-LD | `MobileApplication` (name, operatingSystem: Android, iOS, Web; offers price 0) + `FAQPage` from section 9 |
