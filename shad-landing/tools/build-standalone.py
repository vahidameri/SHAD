"""Inline every local asset of index.html into one self-contained file: dist/shad-landing.html"""
import base64, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
MIME = {".svg": "image/svg+xml", ".webp": "image/webp", ".png": "image/png", ".woff2": "font/woff2"}
cache = {}
def uri(rel):
    p = root / rel
    if not p.exists():
        return rel
    if rel not in cache:
        cache[rel] = f"data:{MIME[p.suffix]};base64," + base64.b64encode(p.read_bytes()).decode()
    return cache[rel]
html = re.sub(r'<link rel="preload"[^>]*>\n', "", html)
html = re.sub(r'(assets/[\w./-]+\.(?:svg|webp|png|woff2))', lambda m: uri(m.group(1)), html)
(root / "dist").mkdir(exist_ok=True)
out = root / "dist" / "shad-landing.html"
out.write_text(html, encoding="utf-8")
print(out, round(out.stat().st_size / 1024), "KB")
