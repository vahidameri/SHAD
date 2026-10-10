// Generates the styled QR (CONFIG.links.landing) and inlines it into index.html at <!--QR-->.
// Usage: node tools/gen-qr.js   (needs the `qrcode` npm package)
const fs = require("fs"), path = require("path");
const QR = require(process.env.QRCODE_PATH || "qrcode");
const url = "https://shad.ir/";
const q = QR.create(url, { errorCorrectionLevel: "M" });
const n = q.modules.size, m = q.modules.data;
const finder = (x, y) => (x < 7 && y < 7) || (x >= n - 7 && y < 7) || (x < 7 && y >= n - 7);
let out = "";
for (let y = 0; y < n; y++) for (let x = 0; x < n; x++)
  if (m[y * n + x] && !finder(x, y)) out += `<rect x="${x + .08}" y="${y + .08}" width=".84" height=".84" rx=".32" fill="#1C1C1C"/>`;
for (const [fx, fy] of [[0, 0], [n - 7, 0], [0, n - 7]])
  out += `<rect x="${fx + .5}" y="${fy + .5}" width="6" height="6" rx="1.8" fill="none" stroke="#068F66" stroke-width="1"/><rect x="${fx + 2}" y="${fy + 2}" width="3" height="3" rx=".9" fill="#068F66"/>`;
const file = path.join(__dirname, "..", "index.html");
let html = fs.readFileSync(file, "utf8");
html = html.replace(/<symbol id="qr" viewBox="0 0 \d+ \d+">[\s\S]*?<\/symbol>/, `<symbol id="qr" viewBox="0 0 ${n} ${n}"><!--QR-->${out}<!--/QR--></symbol>`);
fs.writeFileSync(file, html);
console.log("QR", n + "x" + n, "modules");
