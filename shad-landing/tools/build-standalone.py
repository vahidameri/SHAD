"""Inline every local asset of index.html into one self-contained HTML file (dist/shad-landing-standalone.html)."""
import base64, pathlib, re, sys
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
MIME = {".svg": "image/svg+xml", ".webp": "image/webp", ".png": "image/png", ".woff2": "font/woff2"}
def data_uri(rel):
    p = root / rel
    if not p.exists():  # e.g. the og:image placeholder path: leave as-is
        return rel
    return f"data:{MIME[p.suffix]};base64," + base64.b64encode(p.read_bytes()).decode()
# preload hints are pointless once fonts are inline
html = re.sub(r'<link rel="preload"[^>]*>\n', "", html)
# PNG fallbacks -> WebP to keep the file small
html = re.sub(r'assets/screens/(home-(?:light|dark))\.png', r'assets/screens/\1.webp', html)
html = re.sub(r'(assets/[\w./-]+\.(?:svg|webp|png|woff2))', lambda m: data_uri(m.group(1)), html)
out = root / "dist" / "shad-landing-standalone.html"
out.write_text(html, encoding="utf-8")
print(out, round(out.stat().st_size / 1024), "KB")
