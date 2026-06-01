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
await page.addStyleTag({
  content: `
    .phone { transform: none !important; }
    .phone-tag, .phone-stage::before, .phone-stage::after { display: none !important; }
    body { background: #FBF8F3 !important; }
    .phone-stage { padding: 40px; background: #FBF8F3 !important; }
  `,
});
const phone = await page.$('.phone');
if (!phone) throw new Error('.phone not found');
await phone.screenshot({ path: outPath, omitBackground: false });
await browser.close();
console.log('saved', outPath);
