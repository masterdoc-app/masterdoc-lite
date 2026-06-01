import puppeteer from 'puppeteer';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const landingUrl = process.argv[2] || 'http://127.0.0.1:8769/';
const outPath = process.argv[3] || join(__dirname, '../landing/assets/.phone-capture.png');

const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 1200, height: 900, deviceScaleFactor: 2 });
await page.goto(landingUrl, { waitUntil: 'networkidle0', timeout: 60000 });

// Voice screen for ads; let phone grow to full content height (no aspect-ratio crop).
await page.addStyleTag({
  content: `
    .phone { transform: none !important; aspect-ratio: auto !important; height: auto !important; width: 340px !important; }
    .screen { overflow: visible !important; height: auto !important; }
    .scr { display: none !important; }
    .scr[data-screen="3"] { display: flex !important; }
    .phone-tag, .phone-stage::before, .phone-stage::after, .phone-nav, .phone-hint { display: none !important; }
    body { background: #FBF8F3 !important; }
    .phone-stage { padding: 48px 48px 64px; background: #FBF8F3 !important; }
  `,
});

const phone = await page.$('.phone');
if (!phone) throw new Error('.phone not found');

const box = await phone.boundingBox();
const pad = { top: 24, right: 24, bottom: 48, left: 24 };
await page.screenshot({
  path: outPath,
  clip: {
    x: Math.max(0, box.x - pad.left),
    y: Math.max(0, box.y - pad.top),
    width: box.width + pad.left + pad.right,
    height: box.height + pad.top + pad.bottom,
  },
});

await browser.close();
console.log('saved', outPath);
