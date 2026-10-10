"""Build the dot-matrix Iran map data and inline it into index.html (between /*MAP*/ markers).

Source: Natural Earth 10m admin-1 states/provinces (public domain):
  https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_1_states_provinces.geojson
Usage: python3 tools/build-map.py path/to/ne_10m_admin_1_states_provinces.geojson

Notes
- Greater Tunb and Lesser Tunb are missing from the 10m dataset; they are added to Hormozgan here.
- Every island polygon is guaranteed at least one dot so small Iranian islands always appear.
"""
import json, math, pathlib, re, sys

LON0, LON1, LAT0, LAT1 = 43.9, 63.5, 24.4, 39.9
K = math.cos(math.radians(32.0))
W = 640.0
S = W / ((LON1 - LON0) * K)
H = round((LAT1 - LAT0) * S)

def proj(lon, lat):
    return ((lon - LON0) * K * S, (LAT1 - lat) * S)

def box(lon, lat, r):  # small island polygon (degrees)
    return [[lon - r, lat - r * .7], [lon + r, lat - r * .7], [lon + r, lat + r * .7], [lon - r, lat + r * .7], [lon - r, lat - r * .7]]

EXTRA = {"Hormozgan": [box(55.303, 26.265, .03), box(55.145, 26.238, .015)]}  # Greater Tunb, Lesser Tunb

def inring(x, y, ring):
    c = False; n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]; x2, y2 = ring[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c

def inpoly(x, y, poly):  # poly = [outer, holes...]
    return inring(x, y, poly[0]) and not any(inring(x, y, h) for h in poly[1:])

def rdp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1e-9
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        d = abs(dy * pts[i][0] - dx * pts[i][1] + x2 * y1 - y2 * x1) / L
        if d > dmax: dmax, idx = d, i
    if dmax > eps:
        return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]

src = json.load(open(sys.argv[1], encoding="utf-8"))
provs = []
for f in src["features"]:
    p = f["properties"]
    if p.get("adm0_a3") != "IRN": continue
    g = f["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    polys = [[r for r in poly] for poly in polys] + [[r] for r in EXTRA.get(p["name"], [])]
    pp = [[[proj(*pt) for pt in ring] for ring in poly] for poly in polys]
    provs.append({"name": p["name_fa"].strip(), "en": p["name"], "polys": pp})

def grid(pitch):
    out = [[] for _ in provs]
    y = pitch / 2
    while y < H:
        row = int(y / pitch)
        x = pitch / 2 + (pitch / 2 if row % 2 else 0)  # staggered rows read as a finer halftone
        while x < W:
            for i, pr in enumerate(provs):
                if any(inpoly(x, y, poly) for poly in pr["polys"]):
                    out[i].append((round(x, 1), round(y, 1))); break
            x += pitch
        y += pitch
    # islands / tiny polygons: guarantee one dot each
    for i, pr in enumerate(provs):
        for poly in pr["polys"]:
            ring = poly[0]
            xs = [a for a, b in ring]; ys = [b for a, b in ring]
            if max(xs) - min(xs) < pitch * 2.2 and max(ys) - min(ys) < pitch * 2.2:
                if not any(inpoly(x, y, poly) for x, y in out[i]):
                    out[i].append((round(sum(xs) / len(xs), 1), round(sum(ys) / len(ys), 1)))
    return out

desk = grid(9.0); mob = grid(12.0)

def path(pr):
    parts = []
    for poly in pr["polys"]:
        ring = poly[0]
        xs = [a for a, b in ring]
        if max(xs) - min(xs) < 6:  # tiny island: a small square hit area
            cx = sum(xs) / len(xs); cy = sum(b for a, b in ring) / len(ring)
            parts.append(f"M{cx-5:.0f} {cy-5:.0f}h10v10h-10z"); continue
        # closed ring: split at the point farthest from the start, simplify both halves
        far = max(range(len(ring)), key=lambda k: (ring[k][0] - ring[0][0]) ** 2 + (ring[k][1] - ring[0][1]) ** 2)
        r = rdp(ring[:far + 1], 1.1)[:-1] + rdp(ring[far:], 1.1)
        parts.append("M" + "L".join(f"{x:.1f} {y:.1f}".replace(".0 ", " ").replace(".0", "") for x, y in r) + "Z")
    return "".join(parts)

data = {
    "w": round(W), "h": H,
    "tehran": [round(v, 1) for v in proj(51.389, 35.689)],
    "labels": {"خلیج فارس": [round(v) for v in proj(51.9, 26.75)], "دریای عمان": [round(v) for v in proj(59.6, 24.95)], "دریای خزر": [round(v) for v in proj(50.9, 38.2)]},
    "p": [{"n": pr["name"], "d": path(pr),
           "a": [c for xy in desk[i] for c in xy], "b": [c for xy in mob[i] for c in xy]} for i, pr in enumerate(provs)],
}
js = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
js = re.sub(r"(\d)\.0(?=[,\]])", r"\1", js)
root = pathlib.Path(__file__).resolve().parent.parent
f = root / "index.html"; html = f.read_text(encoding="utf-8")
html = re.sub(r"/\*MAP\*/.*?/\*/MAP\*/", lambda m: "/*MAP*/" + js + "/*/MAP*/", html, flags=re.S)
f.write_text(html, encoding="utf-8")
print("provinces", len(provs), "dots desk", sum(map(len, desk)), "mob", sum(map(len, mob)), "bytes", len(js.encode()))
