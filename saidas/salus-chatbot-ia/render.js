const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 2 });
  const fileUrl = 'file://' + path.resolve(__dirname, 'one-pager.html');
  await page.goto(fileUrl, { waitUntil: 'networkidle' });
  await page.waitForTimeout(800); // garantir fontes
  const el = await page.$('.page');
  await el.screenshot({ path: path.resolve(__dirname, 'one-pager.png') });
  await browser.close();
  console.log('OK -> one-pager.png');
})();
