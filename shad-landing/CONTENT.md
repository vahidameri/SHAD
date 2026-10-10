# CONTENT.md — Copy, facts and phone-screen content

> Version 3.0 · October 2026 · Read `BRIEF.md` first.
> **Facts (§1–2) are locked.** Copy (§3) is final-draft quality: use it as written; small edits for rhythm and line breaks are fine, but keep meaning, voice and length. Don't add copy blocks that aren't here.

---

## 1. CONFIG — locked facts

```js
const CONFIG = {
  links: {
    bazaar:  "https://cafebazaar.ir/app/ir.medu.shad",
    myket:   "https://myket.ir/app/ir.medu.shad",
    apk:     "https://shad.ir/static/apk/Shad_v3_8_2.apk",
    pwa:     "https://my.shad.ir/",     // iPhone / iPad
    web:     "https://my.shad.ir/",     // computer
    landing: "https://shad.ir/",        // QR code target
    privacy: "#", terms: "#"            // placeholders
  },
  apk:     { version: "۳.۸.۲", size: "۸۲ مگابایت", minOs: "اندروید ۴٫۱ به بالا" }, // size/minOs to be confirmed by the team
  support: { phoneDisplay: "۰۲۱-۴۳۰۸۱", phoneHref: "tel:+982143081" },
  stats:   { installs: "۳۴ میلیون", messages: "۸۷ میلیارد", files: "۱۲ میلیارد" }, // from current shad.ir
  activeUsers: { daily: "۱۲ میلیون", weekly: "۱۵ میلیون", monthly: "۲۰ میلیون" }, // peak, from current shad.ir
  campaign: { enabled: false, text: "انیمیشن «ببعی قهرمان» در شاد رایگان شد", linkText: "تماشا کنید", href: "#" },
  year:    "۱۴۰۵"
};
```

---

## 2. What Shad really has (the only features you may mention)

From the live app and its store listing:

| Group | Features |
|---|---|
| Learning | کلاس آنلاین · تحویل تکلیف · ویدیوهای درسی (نمونه تدریس‌ها) · آزمون آنلاین · کارنامه و نمره‌ها · درس‌ها بر اساس پایه و رشته |
| Connecting | پیام‌رسان · گروه و کانال کلاس · پیام خصوصی · گفت‌وگوی صوتی · اعلان‌های مدرسه · پخش زنده |
| Beyond class | شاد من · رویدادها (شاد رویداد) · تماشا · فیلم و سریال · شادبوم (بازی و سرگرمی) · شادبین (جست‌وجوی امن) |
| Access | Android (Bazaar, Myket, APK) · iPhone/iPad and computer via the web version my.shad.ir |

**Never mention:** رمزینه / رمزینه‌خوان, حضور و غیاب, AI features, or anything not in this table.

---

## 3. Copy, block by block

Voice: speak to students with a warm, respectful «تو»; use «شما» where adults are addressed (teachers/families block, FAQ answers about setup, support).

### Header
- Logo (`alt`: «شاد»)
- Desktop links: «شاد چیست» → #story · «نصب» → #install · «سؤال‌ها» → #faq
- CTA: platform-aware (see Install). Short form for header/mobile: «دریافت شاد»

### Hero
- **H1:** «مدرسه‌ات، هر جا که باشی.»
  - Alternatives if the composition needs a different length: «کلاس، هم‌کلاسی‌ها و معلمت؛ همه در شاد.» / «همه مدرسه، در یک اپ.»
- **Lead:** «سر کلاس آنلاین برو، با معلم و هم‌کلاسی‌هایت در ارتباط باش و بعد از درس هم سرگرم شو؛ رایگان، روی گوشی و کامپیوتر.»
- **Primary CTA** (platform-aware):
  - Android: «دریافت از بازار»
  - iPhone/iPad: «ورود به شاد در آیفون»
  - Computer: «ورود به نسخه وب»
  - Unknown: «دریافت شاد» → scrolls to #install
- **Secondary link:** «دستگاه دیگری داری؟» → #install
- **Trust line:** «رایگان، با بیش از ۳۴ میلیون نصب»
- Phone `alt`: «صفحه اصلی اپلیکیشن شاد»

### Story — `#story`
- **Section title (H2):** «یاد بگیر، در ارتباط باش، کشف کن.»

**Chapter ۱ — H3:** «یاد بگیر»
- Body: «سر کلاس آنلاین سؤالت را بپرس، تکلیفت را بفرست، ویدیوهای درس را هر وقت خواستی دوباره ببین و نمره‌هایت را همان‌جا دنبال کن.»
- Feature words: «کلاس آنلاین» «تحویل تکلیف» «ویدیوهای درسی» «آزمون آنلاین» «کارنامه»

**Chapter ۲ — H3:** «در ارتباط باش»
- Body: «با گروه کلاس، هم‌کلاسی‌ها و معلمت گفت‌وگو کن؛ پیام خصوصی بفرست و اعلان‌های مدرسه را همان لحظه بگیر.»
- Feature words: «گروه کلاس» «پیام خصوصی» «گفت‌وگوی صوتی» «اعلان‌های مدرسه»

**Chapter ۳ — H3:** «کشف کن»
- Body: «بعد از کلاس هم شاد با توست: رویدادها و مسابقه‌ها، انیمیشن و فیلم در تماشا، بازی در شادبوم و جست‌وجوی امن با شادبین.»
- Feature words: «رویدادها» «تماشا» «فیلم و سریال» «شادبوم» «شادبین»

Dot indicator labels (for screen readers): «فصل ۱ از ۳: یاد بگیر» etc.

### Also for teachers & families
- **H2:** «برای معلم‌ها و خانواده‌ها هم»
- **«معلم‌ها»** — «کلاس آنلاین برگزار کنید، تکلیف و آزمون بدهید و نتیجه‌ها را یک‌جا ببینید. با دانش‌آموزان و خانواده‌ها در کانال کلاس در ارتباط باشید.»
- **«خانواده‌ها»** — «اعلان‌های مدرسه را مستقیم دریافت کنید و از تکلیف‌ها و نمره‌های فرزندتان باخبر شوید. شاد، بستر رسمی آموزش و پرورش است.»

### Proof
- **Line (H2-sized, one sentence):** «بیش از ۳۴ میلیون نصب؛ مدرسه‌ای به وسعت ایران.»
- **Small line under it:** «تا امروز ۸۷ میلیارد پیام و ۱۲ میلیارد فایل در شاد جابه‌جا شده است.»
- **Logos label:** «همکاران شاد» — وزارت آموزش و پرورش، وزارت ارتباطات و فناوری اطلاعات، مرکز ملی فضای مجازی، همراه اول، پلیس فتا (each logo's `alt` = the full name)

### Install — `#install`
- **H2:** «شاد را نصب کن»
- **Lead:** «رایگان است و چند دقیقه بیشتر طول نمی‌کشد.»
- **Switcher:** «اندروید» · «آیفون و آیپد» · «کامپیوتر» (preselect the visitor's device)

**اندروید**
- Primary: «دریافت از بازار» · Secondary: «دریافت از مایکت»
- Link: «دانلود مستقیم فایل نصبی» + meta: «نسخه ۳.۸.۲» / «۸۲ مگابایت» (separate items)
- Note: «با نصب از بازار یا مایکت، شاد خودکار به‌روز می‌شود.»

**آیفون و آیپد**
- Primary: «ورود به شاد در آیفون»
- Guide title: «شاد را به صفحه اصلی آیفون اضافه کن»
  1. «my.shad.ir را در Safari باز کن.»
  2. «دکمه اشتراک‌گذاری را بزن.»
  3. «گزینه «Add to Home Screen» را انتخاب کن.»
  4. ««Add» را بزن؛ آیکون شاد روی صفحه اصلی می‌آید.»

**کامپیوتر**
- Primary: «ورود به نسخه وب»
- Text: «بدون نصب، در هر مرورگری. برای نصب روی گوشی، این کد را اسکن کن.» + QR → `links.landing`

**Under all panels:** «بعد از نصب، با شماره موبایلت ثبت‌نام کن و وارد مدرسه‌ات شو.»

### FAQ — `#faq`
- **H2:** «سؤال‌های رایج»
- Support line under the title: «سؤال دیگری دارید؟ پشتیبانی شاد:» + phone (LTR, `tel:` link)

1. «شاد رایگان است؟» — «بله. نصب و استفاده از شاد رایگان است.»
2. «روی آیفون چطور از شاد استفاده کنم؟» — «شاد در آیفون و آیپد از طریق نسخه وب کار می‌کند. my.shad.ir را در Safari باز کنید و آن را به صفحه اصلی اضافه کنید.»
3. «از بازار نصب کنم، مایکت یا فایل مستقیم؟» — «هر سه همان اپ رسمی شاد است. بازار یا مایکت بهتر است، چون شاد خودکار به‌روز می‌شود. اگر گوشی اجازه نصب فایل مستقیم را نداد، در تنظیمات، نصب از منابع ناشناس را برای مرورگر فعال کنید.»
4. «کد تأیید پیامکی نمی‌آید.» — «چند دقیقه صبر کنید و شماره موبایل را دوباره بررسی کنید. اگر پیامک نرسید، با پشتیبانی شاد تماس بگیرید.»
5. «کلاس یا مدرسه‌ام را پیدا نمی‌کنم.» — «عضویت در کلاس‌ها را مدرسه انجام می‌دهد. از معلم یا مدیر مدرسه بخواهید عضویت شما را بررسی کند.»

### Footer
- Logo + «شاد، مدرسه‌ای به وسعت ایران و بزرگ‌ترین اپلیکیشن آموزشی کشور.»
- **«دریافت شاد»**: «بازار» · «مایکت» · «فایل نصبی» · «آیفون و آیپد» · «نسخه وب»
- **«راهنما»**: «سؤال‌های رایج» · «حریم خصوصی» · «شرایط استفاده»
- **«پشتیبانی»**: phone (prominent) + «تنها شماره رسمی پاسخ‌گویی شاد»
- «© ۱۴۰۵ شاد»

### Mobile sticky bar
- App icon + «شاد، رایگان» + platform button («دریافت از بازار» / «ورود به شاد»)

### Campaign slot (off by default)
- If `CONFIG.campaign.enabled`: one slim line above the header with `text` + `linkText`, dismissible («بستن»). It must never push the hero's CTA below the fold.

---

## 4. Phone-screen content (illustrative UI, fictional names)

Build these as HTML screens in the real app's style. Keep each screen simple; one moment of life per screen.

**Chapter ۱ — class channel**
- Header: «ریاضی دهم» / «خانم رضایی»
- Lesson video post: «جلسه ۱۲: معادله درجه دوم» (play icon, duration «۱۸:۴۰»)
- Teacher message: «تکلیف این جلسه: تمرین‌های صفحه ۴۲»
- Your message (moment of life): a photo file «تمرین صفحه ۴۲» → status changes to «ارسال شد» with a check
- Small result card: «آزمون فصل ۲» / «۱۹٫۵»

**Chapter ۲ — chat list**
- «گروه کلاس دهم ب» — «فردا امتحان داریم؟» — badge «۳»
- «خانم رضایی» — «آفرین، تمرینت عالی بود.»
- «اطلاعیه‌های مدرسه» — «برنامه امتحان‌های نوبت اول منتشر شد.»
- «سارا» — moment of life: a new message slides in: «جزوه را فرستادم.»
- Bottom nav as in the app: «خانه» «رویدادها» «پخش زنده» «اعلانات» «حساب من»

**Chapter ۳ — home / discover**
- Service row (as in the app): «شاد من» · «پیام‌رسان» · «تماشا» · «فیلم و سریال» (with the «جدید» badge)
- Event card: «شاد رویداد» / «مسابقه کتاب‌خوانی» / «ثبت‌نام باز است»
- Tamasha card: «ببعی قهرمان» / «انیمیشن»
- Search bar: «در شادبین جست‌وجو کنید»

---

## 5. Microcopy, accessibility & SEO

| Context | Copy |
|---|---|
| Skip link | «رفتن به محتوای اصلی» |
| Menu button | «منو» / «بستن منو» |
| APK download started (aria-live) | «دانلود فایل نصبی شاد شروع شد.» |
| QR `alt` | «کد QR برای باز کردن صفحه دریافت شاد روی گوشی» |
| `<title>` | «دانلود شاد؛ مدرسه‌ای به وسعت ایران» |
| meta description | «شاد، اپلیکیشن رسمی آموزش و پرورش: کلاس آنلاین، تکلیف و آزمون، پیام‌رسان کلاس و سرگرمی. دریافت رایگان برای اندروید، آیفون و کامپیوتر.» |
| JSON-LD | `MobileApplication` (Android, iOS via web, Web; price 0) + `FAQPage` |
