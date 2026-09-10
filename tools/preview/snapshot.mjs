#!/usr/bin/env node
// Render the Archbee docs into a static HTML snapshot for PR previews.
//
// `archbee dev` serves a client-rendered Next.js SPA: fetching a page URL
// returns an empty shell, and the markdown is rendered in the browser.
// There is no static-export command in the CLI, so this script starts the
// dev server, renders every page in headless Chrome, and saves the hydrated
// DOM as plain HTML.
//
// The output is deliberately static and script-free:
//   * every <script> tag and inline on* handler is stripped, so contributor
//     markdown cannot execute JS on the preview host (github.io is a shared
//     origin across an org's project Pages — serving untrusted JS there
//     would let one PR script against other previews and project sites);
//   * all root-absolute URLs are rewritten to *relative* ones, so the
//     snapshot works from any base path (gh-pages/pr/<n>/) without a
//     basePath knob — the Archbee CLI has none;
//   * same-origin assets (/_next CSS, /api/assets images) are mirrored into
//     the output; external assets (cdn.flipper.net, api.archbee.com fonts/
//     CDN styles) are left as absolute https URLs.
//
// Usage:
//   node tools/preview/snapshot.mjs --out dist [--port 4173]
//       [--concurrency 4] [--banner "PR #123 · abc1234"]
//
// Requires: @archbee/cli on PATH, Chrome/Chromium (PUPPETEER_EXECUTABLE_PATH
// or a standard install location), puppeteer-core (npm ci in this dir).

import { spawn, execSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer-core';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..', '..');

// --- CLI args ---------------------------------------------------------------
const args = process.argv.slice(2);
function arg(name, dflt) {
  const i = args.indexOf(`--${name}`);
  return i >= 0 ? args[i + 1] : dflt;
}
const outDir = path.resolve(arg('out', 'preview-dist'));
const port = Number(arg('port', '4173'));
const concurrency = Number(arg('concurrency', '4'));
const banner = arg('banner', '');
// The dev server advertises (and the SPA generates asset URLs against)
// http://localhost:<port>, so render through the same host name — otherwise
// the in-page URL rewriting would see those URLs as cross-origin.
const origin = `http://localhost:${port}`;

// --- Page enumeration -------------------------------------------------------
// The dev server routes pages by file path relative to docs/, without the
// .md extension and case-sensitive (docs/general/Tech-Specs.md ->
// /general/Tech-Specs). Frontmatter slugs are NOT used by the dev server.
function listRoutes(dir, prefix = '') {
  const routes = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
    if (entry.isDirectory()) {
      if (entry.name === 'files') continue; // assets, not pages
      routes.push(...listRoutes(path.join(dir, entry.name), `${prefix}${entry.name}/`));
    } else if (entry.name.endsWith('.md')) {
      routes.push(prefix + entry.name.slice(0, -3));
    }
  }
  return routes;
}
const routes = listRoutes(path.join(repoRoot, 'docs'));
// Sidebar order from archbee.json, used to pick category landing pages.
const archbeeConfig = JSON.parse(fs.readFileSync(path.join(repoRoot, 'archbee.json'), 'utf8'));
const orderedRoutes = [];
(function walk(nodes) {
  for (const n of nodes ?? []) {
    if (n.path) orderedRoutes.push(n.path.replace(/\.md$/, ''));
    walk(n.children);
  }
})(archbeeConfig.structure?.docsTree);
if (routes.length === 0) {
  console.error('No markdown pages found under docs/');
  process.exit(1);
}
const readme = archbeeConfig.structure?.readme?.replace(/\.md$/, '') ?? routes[0];
console.log(`Found ${routes.length} pages; landing page: ${readme}`);

// --- Start archbee dev ------------------------------------------------------
// Refuse to reuse a server that is already squatting the port: it may serve
// different content (stale checkout, another working copy).
try {
  await fetch(origin + '/', { redirect: 'manual' });
  console.error(`Port ${port} is already in use — stop the other server or pass a different --port.`);
  process.exit(1);
} catch { /* free, good */ }
console.log(`Starting archbee dev on :${port} ...`);
// detached: own process group, so stopDev can kill the whole tree —
// the CLI wraps a next-server child that would otherwise outlive it.
const dev = spawn('archbee', ['dev', '--port', String(port)], {
  cwd: repoRoot,
  stdio: ['ignore', 'pipe', 'pipe'],
  detached: true,
  env: { ...process.env, BROWSER: 'none', CI: 'true' },
});
let devLog = '';
dev.stdout.on('data', d => { devLog += d; });
dev.stderr.on('data', d => { devLog += d; });
dev.on('exit', code => {
  if (!shuttingDown) {
    console.error(`archbee dev exited early (code ${code}):\n${devLog}`);
    process.exit(1);
  }
});
let shuttingDown = false;
function stopDev() {
  shuttingDown = true;
  try { process.kill(-dev.pid, 'SIGTERM'); } catch { /* already gone */ }
  try { dev.kill('SIGTERM'); } catch { /* already gone */ }
}
process.on('exit', stopDev);

async function waitForServer(timeoutMs = 120000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    try {
      const res = await fetch(origin + '/', { redirect: 'manual' });
      if (res.status > 0) return;
    } catch { /* not up yet */ }
    await new Promise(r => setTimeout(r, 1000));
  }
  console.error(`archbee dev did not become ready in ${timeoutMs / 1000}s:\n${devLog}`);
  process.exit(1);
}
await waitForServer();
console.log('Dev server is up.');

// --- Browser ----------------------------------------------------------------
function findChrome() {
  if (process.env.PUPPETEER_EXECUTABLE_PATH) return process.env.PUPPETEER_EXECUTABLE_PATH;
  for (const p of [
    '/usr/bin/google-chrome',
    '/usr/bin/google-chrome-stable',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
  ]) {
    if (fs.existsSync(p)) return p;
  }
  try { return execSync('command -v google-chrome chromium', { encoding: 'utf8' }).split('\n')[0]; } catch { /* fallthrough */ }
  console.error('No Chrome/Chromium found; set PUPPETEER_EXECUTABLE_PATH.');
  process.exit(1);
}
const browser = await puppeteer.launch({
  executablePath: findChrome(),
  headless: 'new',
  args: ['--no-sandbox', '--disable-dev-shm-usage'],
});

// --- In-page sanitize + rewrite ----------------------------------------------
// Runs in the browser after hydration. `routeSet` distinguishes doc links
// (rewritten to <rel>/Route/ directory URLs) from asset paths.
function sanitizeAndRewrite(depth, routeList, bannerText) {
  const rel = depth === 0 ? './' : '../'.repeat(depth);
  const routeSet = new Set(routeList);
  const assets = new Set();
  const categories = new Set();

  const toLocal = (url) => {
    // returns {href, asset} for a root-absolute same-origin URL, else null
    let u;
    try { u = new URL(url, location.href); } catch { return null; }
    if (u.origin !== location.origin) return null;
    const p = u.pathname.replace(/^\//, '');
    const pBare = decodeURIComponent(p.replace(/\/$/, ''));
    if (p === '' || routeSet.has(pBare)) {
      return { href: rel + (pBare ? pBare + '/' : '') + u.hash, asset: null };
    }
    // Category link (e.g. /hardware/): the SPA 404s on these, the snapshot
    // gets a redirect index.html to the category's first page instead.
    if (pBare && routeList.some(r => r.startsWith(pBare + '/'))) {
      categories.add(pBare);
      return { href: rel + pBare + '/' + u.hash, asset: null };
    }
    if (p.startsWith('api/assets/')) {
      const ap = 'assets/' + decodeURIComponent(p.slice('api/assets/'.length));
      assets.add(u.pathname + u.search + '\u0000' + ap);
      return { href: rel + ap, asset: ap };
    }
    // _next CSS, favicons, anything else same-origin: mirror by path
    assets.add(u.pathname + u.search + '\u0000' + decodeURIComponent(p));
    return { href: rel + decodeURIComponent(p), asset: p };
  };

  // 1. Drop scripts and script-ish resource hints.
  for (const el of document.querySelectorAll('script, link[rel=preload], link[rel=modulepreload], link[rel=prefetch], link[rel=preconnect]')) el.remove();

  // 2. Strip inline handlers and javascript: URLs from contributor HTML.
  for (const el of document.querySelectorAll('*')) {
    for (const attr of [...el.attributes]) {
      if (/^on/i.test(attr.name)) el.removeAttribute(attr.name);
    }
    for (const name of ['href', 'src', 'xlink:href']) {
      const v = el.getAttribute(name);
      if (v && /^\s*javascript:/i.test(v)) el.setAttribute(name, '#');
    }
  }

  // 3. Rewrite URLs.
  for (const el of document.querySelectorAll('a[href], link[href], img[src], source[src], video[src], video[poster], audio[src], iframe[src]')) {
    for (const name of ['href', 'src', 'poster']) {
      const v = el.getAttribute(name);
      if (!v) continue;
      const r = toLocal(v);
      if (r) el.setAttribute(name, r.href);
    }
  }
  for (const el of document.querySelectorAll('img[srcset], source[srcset]')) {
    const rewritten = el.getAttribute('srcset').split(',').map(part => {
      const [url, ...desc] = part.trim().split(/\s+/);
      const r = toLocal(url);
      return [r ? r.href : url, ...desc].join(' ');
    }).join(', ');
    el.setAttribute('srcset', rewritten);
  }

  // 4. The app reveals <body> via JS; without scripts it would stay invisible.
  document.body.classList.remove('opacity-0', 'transition-opacity');

  // 5. Optional banner so reviewers know what they are looking at.
  if (bannerText) {
    const div = document.createElement('div');
    div.textContent = bannerText + ' — static preview; search and other interactive features are disabled.';
    div.setAttribute('style',
      'position:sticky;top:0;z-index:9999;background:#fff3cd;color:#664d03;' +
      'border-bottom:1px solid #ffe69c;padding:6px 12px;font:13px/1.4 sans-serif;text-align:center;');
    document.body.prepend(div);
  }

  return { assets: [...assets], categories: [...categories] };
}

// --- Render loop --------------------------------------------------------------
const assetMap = new Map(); // url path+query -> output path
const categorySet = new Set(); // category prefixes that need redirect indexes
const failures = [];
const queue = [...routes];

async function renderWorker() {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  for (;;) {
    const route = queue.shift();
    if (!route) break;
    const depth = route.split('/').length; // page is written to <route>/index.html
    try {
      await page.goto(`${origin}/${route}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await page.waitForFunction(() => !!document.querySelector('h1'), { timeout: 30000 });
      await new Promise(r => setTimeout(r, 1000)); // settle: client-rendered embeds/diagrams
      const { assets, categories } = await page.evaluate(sanitizeAndRewrite, depth, routes, banner);
      for (const pair of assets) {
        const [urlPath, outPath] = pair.split('\u0000');
        assetMap.set(urlPath, outPath);
      }
      for (const c of categories) categorySet.add(c);
      const html = await page.content();
      const file = path.join(outDir, route, 'index.html');
      fs.mkdirSync(path.dirname(file), { recursive: true });
      fs.writeFileSync(file, html);
      console.log(`  ok ${route}`);
    } catch (err) {
      failures.push(`${route}: ${err.message.split('\n')[0]}`);
      console.error(`  FAIL ${route}: ${err.message.split('\n')[0]}`);
    }
  }
  await page.close();
}

fs.rmSync(outDir, { recursive: true, force: true });
fs.mkdirSync(outDir, { recursive: true });
const t0 = Date.now();
await Promise.all(Array.from({ length: Math.min(concurrency, routes.length) }, renderWorker));
console.log(`Rendered ${routes.length - failures.length}/${routes.length} pages in ${((Date.now() - t0) / 1000).toFixed(1)}s`);

// --- Mirror same-origin assets -------------------------------------------------
// CSS may pull in more same-origin files (fonts, images) via url(...): fetch
// those too, rewriting the references relative to the CSS file's location.
const assetFailures = [];
async function mirrorAsset(urlPath, outPath) {
  const res = await fetch(origin + urlPath);
  if (!res.ok) {
    assetFailures.push(`${urlPath} -> HTTP ${res.status}`);
    return;
  }
  const file = path.join(outDir, outPath);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  if (outPath.endsWith('.css')) {
    let css = await res.text();
    const cssDepth = outPath.split('/').length - 1;
    const cssRel = cssDepth === 0 ? './' : '../'.repeat(cssDepth);
    const extra = [];
    css = css.replace(/url\(\s*(['"]?)(\/[^)'"]+)\1\s*\)/g, (_, q, p) => {
      const clean = p.replace(/^\//, '').split(/[?#]/)[0];
      extra.push([p.split('#')[0], clean]);
      return `url(${q}${cssRel}${clean}${q})`;
    });
    fs.writeFileSync(file, css);
    for (const [refPath, refOut] of extra) {
      if (!assetMap.has(refPath) && !fs.existsSync(path.join(outDir, refOut))) {
        assetMap.set(refPath, refOut); // picked up by the outer loop
      }
    }
  } else {
    fs.writeFileSync(file, Buffer.from(await res.arrayBuffer()));
  }
}
const mirrored = new Set();
while (mirrored.size < assetMap.size) {
  const batch = [...assetMap].filter(([u]) => !mirrored.has(u));
  for (const [u] of batch) mirrored.add(u);
  await Promise.all(batch.map(([u, o]) => mirrorAsset(u, o).catch(e => assetFailures.push(`${u}: ${e.message}`))));
}
console.log(`Mirrored ${mirrored.size - assetFailures.length}/${mirrored.size} same-origin assets`);
for (const f of assetFailures) console.warn(`  asset warning: ${f}`);

// --- Asset completeness pass ---------------------------------------------------
// The DOM-collected asset set can vary with render timing (lazy mounts,
// settle windows). Scan the written HTML for local asset references and
// fetch anything the mirror missed. /api/assets resolves docs-root-relative
// paths with just docsPath, so the original URL is reconstructible.
const docsPath = (archbeeConfig.docsPath ?? 'docs/').replace(/\/$/, '');
function* htmlFiles(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) yield* htmlFiles(p);
    else if (entry.name.endsWith('.html')) yield p;
  }
}
const missing = new Map(); // site-root-relative output path -> fetch url
for (const file of htmlFiles(outDir)) {
  const fromDir = path.dirname(file);
  const html = fs.readFileSync(file, 'utf8');
  const refs = [];
  for (const m of html.matchAll(/(?:src|href|poster)="((?:\.\.\/|\.\/)[^"]+)"/g)) refs.push(m[1]);
  for (const m of html.matchAll(/srcset="([^"]+)"/g)) {
    for (const part of m[1].split(',')) refs.push(part.trim().split(/\s+/)[0]);
  }
  for (const ref of refs) {
    if (!/^\.\.?\//.test(ref)) continue;
    const clean = ref.split(/[?#]/)[0];
    const sitePath = path.relative(outDir, path.resolve(fromDir, decodeURIComponent(clean)));
    if (sitePath.startsWith('..')) continue;
    if (sitePath.endsWith('/') || fs.existsSync(path.join(outDir, sitePath))) continue;
    if (fs.existsSync(path.join(outDir, sitePath, 'index.html'))) continue; // page link
    if (sitePath.startsWith('assets/')) {
      missing.set(sitePath, `/api/assets/${encodeURI(sitePath.slice('assets/'.length))}?docsPath=${docsPath}`);
    } else {
      missing.set(sitePath, '/' + encodeURI(sitePath));
    }
  }
}
let recovered = 0;
for (const [sitePath, urlPath] of missing) {
  try {
    const res = await fetch(origin + urlPath);
    if (!res.ok) {
      console.warn(`  missing asset: ${sitePath} (${urlPath} -> HTTP ${res.status})`);
      continue;
    }
    const file = path.join(outDir, sitePath);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, Buffer.from(await res.arrayBuffer()));
    recovered++;
  } catch (err) {
    console.warn(`  missing asset: ${sitePath} (${err.message})`);
  }
}
if (missing.size) console.log(`Completeness pass: recovered ${recovered}/${missing.size} referenced assets`);
else console.log('Completeness pass: all referenced assets present');

// --- Root redirect ---------------------------------------------------------------
fs.writeFileSync(path.join(outDir, 'index.html'),
  `<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=${readme}/">` +
  `<link rel="canonical" href="${readme}/"><title>Redirecting</title><a href="${readme}/">${readme}</a>\n`);

// --- Category redirects -----------------------------------------------------------
// Sidebar/category links point at directory paths the SPA cannot render;
// redirect each to its first page in sidebar (archbee.json) order.
for (const cat of categorySet) {
  const target = orderedRoutes.find(r => r.startsWith(cat + '/')) ?? routes.find(r => r.startsWith(cat + '/'));
  if (!target) continue;
  const restRel = target.slice(cat.length + 1) + '/';
  const file = path.join(outDir, cat, 'index.html');
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file,
    `<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=${restRel}">` +
    `<link rel="canonical" href="${restRel}"><title>Redirecting</title><a href="${restRel}">${target}</a>\n`);
}

// --- Done -------------------------------------------------------------------------
await browser.close();
stopDev();
if (failures.length) {
  console.error(`\n${failures.length} page(s) failed to render:`);
  for (const f of failures) console.error(`  ${f}`);
  process.exit(1);
}
console.log(`Snapshot written to ${outDir}`);
process.exit(0);
