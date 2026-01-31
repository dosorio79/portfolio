import fs from "node:fs";
import path from "node:path";

const distDir = path.resolve("dist");

if (!fs.existsSync(distDir)) {
  console.error("dist/ not found. Run `npm run build` first.");
  process.exit(1);
}

const htmlFiles = [];

function walk(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(fullPath);
      continue;
    }
    if (entry.isFile() && entry.name.endsWith(".html")) {
      htmlFiles.push(fullPath);
    }
  }
}

function isExternal(href) {
  return (
    href.startsWith("http://") ||
    href.startsWith("https://") ||
    href.startsWith("mailto:") ||
    href.startsWith("tel:") ||
    href.startsWith("javascript:")
  );
}

function normalizeHref(href) {
  const [noHash] = href.split("#");
  const [noQuery] = noHash.split("?");
  return noQuery;
}

function candidatePaths(resolved) {
  const candidates = [];
  if (path.extname(resolved)) {
    candidates.push(resolved);
    return candidates;
  }
  candidates.push(resolved);
  candidates.push(path.join(resolved, "index.html"));
  candidates.push(`${resolved}.html`);
  return candidates;
}

walk(distDir);

const broken = [];

for (const filePath of htmlFiles) {
  const content = fs.readFileSync(filePath, "utf8");
  const hrefs = content.match(/href\s*=\s*["'][^"']+["']/gi) ?? [];
  for (const raw of hrefs) {
    const href = raw.replace(/href\s*=\s*["']/, "").replace(/["']$/, "");
    if (!href || href.startsWith("#") || isExternal(href)) {
      continue;
    }

    const normalized = normalizeHref(href);
    if (!normalized) {
      continue;
    }

    let resolved;
    if (normalized.startsWith("/")) {
      resolved = path.join(distDir, normalized);
    } else {
      resolved = path.resolve(path.dirname(filePath), normalized);
    }

    const ok = candidatePaths(resolved).some((candidate) =>
      fs.existsSync(candidate),
    );

    if (!ok) {
      broken.push({ file: filePath, href });
    }
  }
}

if (broken.length > 0) {
  console.error("Broken links found:");
  for (const item of broken) {
    console.error(`- ${path.relative(distDir, item.file)} -> ${item.href}`);
  }
  process.exit(1);
}

console.log(`Checked ${htmlFiles.length} HTML files, no broken links found.`);
