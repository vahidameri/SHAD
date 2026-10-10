# CONTENT.md — Story, copy and data for the Shad landing page

> Version 2.0 · October 2026
> Companion files: `DESIGN.md` (art direction) · `PROMPT.md` (how to work)

---

## 0. How to use this file

- **Facts are locked** (section 2): links, numbers, version, phone. Read them from a `CONFIG` object; never invent new stats, claims, quotes or testimonials.
- **Copy is a strong draft, not a cage.** You may tighten, shorten, split or re-rhythm any line so it works in the layout, as long as the meaning stays and the Persian is natural and correct. You may write extra microcopy (labels, chips, UI-fragment text, aria labels) in the same voice.
- **Section order is the recommended story** (section 4). You may merge, split or reorder sections if the page gets clearly better — keep the narrative arc.
- Headlines are written as **two lines** for the two-tone treatment: `line 1` (light) / `line 2` (strong). Several options are given where useful — pick the best for your composition.
- All digits in Persian copy are Persian (۰–۹). Preserve ZWNJ (نیم‌فاصله) exactly. Wrap brand names in `translate="no"`.
- Sections marked `new` are additions beyond the current shad.ir; add `data-source="new"` on their wrapper so the client can find them.

---

## 1. The story in one breath

Shad is not "an app download". It's **a whole school in one app** — and 34 million people already use it. The page should make a student think «همه‌چیز مدرسه‌ام اینجاست», make a parent think «رسمی و امن است», make a teacher think «کلاسم را ساده می‌کند» — and make all three press the right install button within seconds.

| | |
|---|---|
| Page job | Get each visitor to the right install/open action for their device |
| Audiences | Students & families (mostly Android phones) → teachers & school staff → institutions & press |
| Feeling | The excitement of the first day of school + the trust of an official national platform |
| Voice | Warm, clear, confident. Friendly to a teenager, credible to a parent. Address the reader as «شما». No slang, no bureaucratic tone. |

---

## 2. CONFIG — locked facts

```js
const CONFIG = {
  links: {
    bazaar:   "https://cafebazaar.ir/app/ir.medu.shad",
    myket:    "https://myket.ir/app/ir.medu.shad",
    apk:      "https://shad.ir/static/apk/Shad_v3_8_2.apk",
    pwa:      "https://my.shad.ir/",   // iPhone / iPad (web app)
    web:      "https://my.shad.ir/",   // desktop web version
    landing:  "https://shad.ir/",      // QR code target
    privacy:  "#", terms: "#", campaign: "#"   // placeholders
  },
  apk:      { version: "۳.۸.۲", size: "۴۵ مگابایت", minOs: "اندروید ۵ به بالا" }, // size/minOs are placeholders
  support:  { phoneDisplay: "۰۲۱-۴۳۰۸۱", phoneHref: "tel:+982143081" },
  stats: [                                   // from current shad.ir
    { value: "+۳۴", unit: "میلیون",  label: "نصب یکتا" },
    { value: "+۸۷", unit: "میلیارد", label: "پیام ارسال‌شده" },
    { value: "+۱۲", unit: "میلیارد", label: "فایل جابه‌جاشده" }
  ],
  activeUsers: { daily: "۱۲ میلیون", weekly: "۱۵ میلیون", monthly: "۲۰ میلیون" }, // peak, from shad.ir
  campaign: { enabled: true, text: "انیمیشن «ببعی قهرمان» در شاد رایگان شد", linkText: "تماشا کنید" },
  year: "۱۴۰۵"
};
```

---

## 3. The smart CTA (behavior that matters everywhere)

Detect the platform and lead with the right action. Every CTA area on the page (header, hero, sticky bar, final CTA) follows this.

| Platform | Primary | Secondary | Extra |
|---|---|---|---|
| **Android** | «دریافت از بازار» → bazaar | «دریافت از مایکت» → myket | Text link «دانلود مستقیم فایل نصبی (APK)» + version and size |
| **iPhone / iPad** | «ورود به شاد در آیفون» → pwa | — | «بدون نیاز به اپ‌استور؛ شاد را به صفحه اصلی گوشی اضافه کنید.» + link to the iPhone guide |
| **Desktop** | «ورود به نسخه وب شاد» → web | — | QR card: «نصب روی گوشی» / «این کد را با دوربین گوشی اسکن کنید.» |
| **Unknown / no JS** | Show Bazaar, iPhone and Web side by side | | |

Always available near the hero CTA: «دستگاه دیگری دارید؟ همه روش‌های نصب» → install section.

---

## 4. The story, section by section

### [0] Campaign bar — existing (optional)
Slim dismissible bar for the current campaign: `{{campaign.text}}` + `{{campaign.linkText}}`. Must never overpower the hero (on the current site it does).

### [1] Header — new
Logo · «قابلیت‌ها» · «راهنمای نصب» · «سؤالات متداول» · «پشتیبانی» · secondary «ورود به نسخه وب» · primary «دریافت شاد». On mobile: logo + compact «دریافت» + menu.

### [2] Hero — existing + new
**Headline options (line 1 / line 2):**
1. «مدرسه‌ای به وسعت ایران» / «در گوشی شما»
2. «کلاس، کتاب و معلم» / «همه در یک اپ»
3. «یک اپ،» / «یک مدرسه کامل»

**Subheading:**
> کلاس آنلاین، کتاب درسی دیجیتال، پیام‌رسان و هرچه برای درس و مدرسه لازم دارید؛ رایگان، برای دانش‌آموزان، معلم‌ها و خانواده‌ها.

**Trust micro-line (near CTA):** «رایگان، با بیش از ۳۴ میلیون نصب»
**Optional pill above headline:** «بزرگ‌ترین اپلیکیشن آموزشی ایران»
**CTA:** smart CTA (§3).
**Visual:** see `DESIGN.md` §7 — phone + subject cards + floating UI fragments (§6).

### [3] Partners — existing
Label: «همکاران شاد»
Logos: وزارت آموزش و پرورش · وزارت ارتباطات و فناوری اطلاعات · مرکز ملی فضای مجازی · همراه اول · پلیس فتا

### [4] Super-app ecosystem — existing (stats) + new (framing)
**Pill:** «سوپراپلیکیشن شاد»
**Headline:** «همه‌چیز مدرسه،» / «در یک اپلیکیشن»
**Text:** «از کلاس و تکلیف تا پیام‌رسان، کتاب، رویداد و سرگرمی؛ شاد همه زندگی مدرسه را یک‌جا جمع کرده است.»
**Stats:** `CONFIG.stats` (value + unit on one line, label below).
**Services on the orbit** (use names + icons; tiles like the app):
شاد من · پیام‌رسان · کلاس و تکالیف · پخش زنده · گفت‌وگوی صوتی · رمزینه‌خوان · نمونه تدریس‌ها · شادبین · شادبوم · شاد رویداد · تماشا · فیلم و سریال

### [5] How it works — new
**Pill:** «چطور شروع کنم؟»
**Headline:** «از نصب تا کلاس،» / «فقط سه قدم»

| # | Title | Text |
|---|---|---|
| ۱ | «نصب کنید» | «شاد را از بازار یا مایکت دریافت کنید؛ در آیفون، نسخه وب را به صفحه اصلی اضافه کنید.» |
| ۲ | «ثبت‌نام کنید» | «با شماره موبایل ثبت‌نام کنید و کد تأیید پیامکی را وارد کنید.» |
| ۳ | «وارد کلاس شوید» | «نقش خود را انتخاب کنید و به کلاس و مدرسه‌تان بپیوندید.» |

### [6] Features — existing (rewritten)
**Pill:** «قابلیت‌ها»
**Headline:** «هرچه برای درس لازم است،» / «همین‌جاست»

| Feature | Product name | Copy |
|---|---|---|
| **کلاس و تکالیف** (lead) | سامانه مدیریت یادگیری | «کلاس مجازی، تکلیف و آزمون در یک‌جا؛ ساخته‌شده برای آموزش و یادگیری معلم‌ها و دانش‌آموزان.» |
| **کلاس زنده** | پخش زنده | «کلاس تصویری زنده در کانال‌ها و گروه‌ها، با امکان مرور درس و برگزاری جلسه.» |
| **کتاب درسی دیجیتال** | رمزینه‌خوان | «نسخه دیجیتال کتاب‌های درسی همه مقاطع؛ رمزینه کتاب را اسکن کنید و به محتوای آموزشی برسید.» |
| **گفت‌وگو با معلم و مدرسه** | گفت‌وگوی صوتی | «پیام، کانال و تماس صوتی گروهی؛ برای کلاس مجازی و ارتباط هرروزه با مدرسه.» |
| **نمونه تدریس‌ها** | — | «محتوای آموزشی همه درس‌ها، از پیش‌دبستانی تا دوازدهم.» |
| **شادبین** | — | «جست‌وجوی سریع، هدفمند و پاک برای اهالی مدرسه.» |
| **شادبوم** | — | «بازی‌های آموزشی و سرگرمی سالم.» |
| **شاد رویداد** | — | «رویدادهای پرورشی و فرهنگی در مقیاس ملی.» |

### [7] Who it's for — new
**Pill:** «برای همه اهالی مدرسه»
**Headline:** «یک اپ،» / «برای همه اهالی مدرسه»

**«دانش‌آموزان»** — «همه درس‌ها، همیشه همراه شما»
- «در کلاس زنده شرکت کنید و تکلیف‌ها را همان‌جا تحویل دهید.»
- «کتاب‌های درسی و محتوای آموزشی را هر وقت خواستید مرور کنید.»
- «با معلم و هم‌کلاسی‌ها در گروه کلاس در ارتباط باشید.»

**«معلم‌ها»** — «کلاستان را ساده‌تر اداره کنید»
- «کلاس زنده برگزار کنید و جلسه‌ها را برای مرور در دسترس بگذارید.»
- «تکلیف و آزمون بدهید و پاسخ‌ها را یک‌جا ببینید.»
- «با دانش‌آموزان و خانواده‌ها در کانال کلاس در ارتباط باشید.»

**«خانواده‌ها»** — «در جریان درس فرزندتان باشید»
- «اطلاعیه‌های مدرسه و کلاس را مستقیم دریافت کنید.»
- «از تکلیف‌ها و برنامه کلاس فرزندتان باخبر شوید.»
- «فضایی آموزشی و امن برای فرزندتان.»

### [8] Install on any device — existing + new
**Pill:** «نصب شاد»
**Headline:** «روی هر دستگاهی،» / «شاد همراه شماست»

- **«اندروید»** — «دریافت از بازار» · «دریافت از مایکت» · «دانلود مستقیم فایل نصبی (APK)» · version / size / minimum Android · note: «با نصب از بازار یا مایکت، شاد خودکار به‌روز می‌شود.»
- **«آیفون و آیپد»** — «ورود به شاد در آیفون» · guide «افزودن شاد به صفحه اصلی آیفون»:
  1. «آدرس my.shad.ir را در مرورگر Safari باز کنید.»
  2. «دکمه اشتراک‌گذاری (مربع با فلش رو به بالا) را بزنید.»
  3. «گزینه «Add to Home Screen» یا «افزودن به صفحه اصلی» را انتخاب کنید.»
  4. «دکمه «Add» را بزنید؛ آیکون شاد روی صفحه اصلی ظاهر می‌شود.»
- **«کامپیوتر و لپ‌تاپ»** — «ورود به نسخه وب شاد» · «بدون نصب، در هر مرورگری.» · QR: «برای نصب روی گوشی، کد را اسکن کنید.»
- Badge on the visitor's own device: «دستگاه شما»

### [9] FAQ — new
**Pill:** «سؤالات متداول»
**Headline:** «سؤالی دارید؟» / «جواب‌ها اینجاست»
**Support card:** «هنوز سؤال دارید؟» · «کارشناسان پشتیبانی شاد پاسخ‌گوی شما هستند.» · `{{support.phoneDisplay}}`

1. «استفاده از شاد هزینه دارد؟» — «نه. نصب و استفاده از شاد رایگان است.»
2. «چطور شاد را روی آیفون نصب کنم؟» — «شاد در آیفون از طریق نسخه وب در دسترس است. my.shad.ir را در Safari باز کنید، دکمه اشتراک‌گذاری را بزنید و «افزودن به صفحه اصلی» را انتخاب کنید.»
3. «از بازار نصب کنم، مایکت یا فایل مستقیم؟» — «فرقی ندارد؛ هر سه همان اپلیکیشن رسمی شاد است. نصب از بازار یا مایکت بهتر است، چون شاد خودکار به‌روز می‌شود.»
4. «گوشی اجازه نصب فایل APK را نمی‌دهد. چه کنم؟» — «در تنظیمات گوشی، اجازه نصب از منابع ناشناس را برای مرورگر یا مدیر فایل فعال کنید و دوباره فایل را باز کنید. فایل را فقط از سایت رسمی شاد دریافت کنید.»
5. «چطور شاد را به‌روزرسانی کنم؟» — «اگر از بازار یا مایکت نصب کرده‌اید، از همان‌جا به‌روزرسانی کنید؛ در غیر این صورت آخرین نسخه را از همین صفحه دریافت کنید.»
6. «کد تأیید پیامکی برایم نمی‌آید.» — «چند دقیقه صبر کنید و شماره موبایل را بررسی کنید. اگر باز هم پیامک نرسید، با پشتیبانی شاد تماس بگیرید.»
7. «کلاس یا مدرسه‌ام را در شاد پیدا نمی‌کنم.» — «عضویت در کلاس‌ها از طرف مدرسه انجام می‌شود. از معلم یا مدیر مدرسه بخواهید عضویت شما را بررسی کند.»
8. «روی کامپیوتر هم می‌شود از شاد استفاده کرد؟» — «بله. نسخه وب شاد در my.shad.ir بدون نصب و در هر مرورگری در دسترس است.»

### [10] Final CTA — new
**Headline options:** «کلاس شما در شاد» / «منتظر شماست» — or — «همین حالا» / «به شاد بپیوندید»
**Text:** «به میلیون‌ها دانش‌آموز، معلم و خانواده در سراسر ایران بپیوندید.»
**CTA:** smart CTA (§3).

### [11] Footer — existing + new
- **About** (existing): «پلتفرمی که بزرگ‌ترین زیست‌بوم آموزشی کشور شد» — «شاد، مدرسه‌ای به وسعت ایران و بزرگ‌ترین اپلیکیشن آموزشی کشور است. تاکنون بیش از ۳۴ میلیون نصب یکتا داشته و در بیشینه حالت، {{activeUsers.daily}} کاربر فعال روزانه، {{activeUsers.weekly}} کاربر فعال هفتگی و {{activeUsers.monthly}} کاربر فعال ماهانه داشته است.»
- **Get Shad**: «اندروید از بازار» · «اندروید از مایکت» · «فایل نصبی APK» · «آیفون و آیپد» · «نسخه وب»
- **Help**: «راهنمای نصب» · «سؤالات متداول» · «حریم خصوصی» · «شرایط استفاده»
- **Support** (existing): «پشتیبانی تلفنی» · `{{support.phoneDisplay}}` (render LTR) · «تنها شماره رسمی مرکز پاسخ‌گویی شاد» · new: «پشتیبانی شاد هرگز کد تأیید پیامکی شما را نمی‌خواهد.»
- «© {{year}} شاد. همه حقوق محفوظ است.»

### [*] Mobile sticky bar — new
Shad icon + «شاد، رایگان» + platform button («دریافت از بازار» on Android, «ورود به شاد» on iPhone).

---

## 5. Microcopy & SEO

| Context | Copy |
|---|---|
| Skip link | «پرش به محتوای اصلی» |
| Menu | «باز کردن منو» / «بستن منو» |
| Close campaign | «بستن اطلاعیه» |
| Theme toggle | «تغییر حالت روشن و تاریک» |
| APK download started (aria-live) | «دانلود فایل نصبی شاد شروع شد.» |
| QR alt | «کد QR برای باز کردن صفحه دریافت شاد روی گوشی» |
| `<title>` | «دانلود شاد؛ اپلیکیشن آموزشی دانش‌آموزان ایران» |
| meta description | «شاد، بزرگ‌ترین اپلیکیشن آموزشی ایران: کلاس آنلاین، کتاب درسی دیجیتال و ارتباط با معلم و مدرسه. دریافت رایگان برای اندروید، آیفون و نسخه وب.» |
| og:title | «شاد، مدرسه‌ای به وسعت ایران» |
| JSON-LD | `MobileApplication` (Android, iOS, Web; price 0) + `FAQPage` |

---

## 6. UI-fragment content library

Illustrative in-app content for floating cards, bento tiles and preview panels. These are depictions of the product UI, not claims. Use, adapt or add more in the same spirit. Names are generic and fictional.

| Fragment | Content |
|---|---|
| Live class | «زنده» badge · «ریاضی دهم» · «خانم رضایی» · «۲۸ نفر آنلاین» |
| Teacher message | «آقای کریمی» · «تکلیف فصل سوم را تا شنبه بفرستید.» · «۱۰:۳۲» |
| Class group | «گروه کلاس هفتم ب» · «۳ پیام جدید» |
| Homework | «تکلیف‌های امروز»: «حل تمرین صفحه ۴۲ ✓» · «خلاصه درس تاریخ ✓» · «آزمایش علوم» |
| Submitted | «تکلیف علوم تحویل شد» |
| Result | «آزمون ادبیات» · «نمره: ۱۹٫۵» |
| Textbook | «فیزیک دوازدهم» · «رمزینه اسکن شد» · «۶ ویدیوی آموزشی» |
| Subject cards (as in app) | «ریاضیات / دهم ریاضی» · «تاریخ / یازدهم تجربی» · «فیزیک / دوازدهم تجربی» · «جامعه‌شناسی / دوازدهم انسانی» |
| Event | «شاد رویداد» · «مسابقه کتاب‌خوانی» · «ثبت‌نام باز است» |
| Tamasha | «تماشا» · «انیمیشن ببعی قهرمان» |
| Search | «در شادبین جست‌وجو کنید» |
| Attendance | «حضور شما در کلاس ثبت شد» |
| Voice call | «تماس صوتی گروهی» · «۱۲ نفر» |
| Stat chip | «۱۲ میلیون کاربر فعال روزانه» (from CONFIG) |
| Service tile badges | «جدید» · count «۲» |

---

## 7. Photography brief (for later — design the slots now)

If/when photos are added to `assets/photos/`:
- Real Iranian students, teachers and parents; authentic, joyful, natural light. Not Western stock.
- Context-appropriate: school uniforms; girls with مقنعه in school settings; respectful family scenes at home.
- «به وسعت ایران»: show diversity of regions and settings — big city, small town, village school.
- Moments: a student on a phone in a live class, a teacher teaching to a phone/laptop, a parent and child checking homework together, friends looking at a phone and laughing.
- Suggested slots: hero side cards (2), audience explorer (3, one per audience), final CTA (1).
