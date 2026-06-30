#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const PADDING = 48;
const MAX_SIZE = 4096;

function usage() {
  console.error("Usage: node scripts/render_excalidraw_png.js <file.excalidraw> [out.png]");
}

function escapeXml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function activeElements(scene) {
  return (scene.elements || []).filter((element) => !element.isDeleted);
}

function elementBounds(element) {
  let minX = element.x;
  let minY = element.y;
  let maxX = element.x + (element.width || 0);
  let maxY = element.y + (element.height || 0);

  if (Array.isArray(element.points)) {
    for (const [x, y] of element.points) {
      minX = Math.min(minX, element.x + x);
      minY = Math.min(minY, element.y + y);
      maxX = Math.max(maxX, element.x + x);
      maxY = Math.max(maxY, element.y + y);
    }
  }

  const strokePad = Math.max(8, (element.strokeWidth || 1) * 3);
  return {
    minX: minX - strokePad,
    minY: minY - strokePad,
    maxX: maxX + strokePad,
    maxY: maxY + strokePad,
  };
}

function sceneBounds(elements) {
  if (elements.length === 0) {
    return { minX: 0, minY: 0, maxX: 640, maxY: 360 };
  }

  return elements.reduce(
    (bounds, element) => {
      const item = elementBounds(element);
      return {
        minX: Math.min(bounds.minX, item.minX),
        minY: Math.min(bounds.minY, item.minY),
        maxX: Math.max(bounds.maxX, item.maxX),
        maxY: Math.max(bounds.maxY, item.maxY),
      };
    },
    { minX: Infinity, minY: Infinity, maxX: -Infinity, maxY: -Infinity },
  );
}

function style(element) {
  const strokeWidth = element.strokeWidth || 1;
  const stroke = element.strokeColor || "#1e1e1e";
  const fill =
    element.backgroundColor && element.backgroundColor !== "transparent"
      ? element.backgroundColor
      : "none";
  const opacity =
    element.opacity === undefined || element.opacity === null
      ? 1
      : element.opacity / 100;

  return `stroke="${escapeXml(stroke)}" stroke-width="${strokeWidth}" fill="${escapeXml(fill)}" opacity="${opacity}" stroke-linecap="round" stroke-linejoin="round"`;
}

function rotateAttr(element) {
  if (!element.angle) {
    return "";
  }
  const cx = element.x + (element.width || 0) / 2;
  const cy = element.y + (element.height || 0) / 2;
  return ` transform="rotate(${(element.angle * 180) / Math.PI} ${cx} ${cy})"`;
}

function pointsPath(element) {
  const points = element.points || [];
  if (points.length === 0) {
    return "";
  }

  const [firstX, firstY] = points[0];
  const commands = [`M ${element.x + firstX} ${element.y + firstY}`];
  for (const [x, y] of points.slice(1)) {
    commands.push(`L ${element.x + x} ${element.y + y}`);
  }
  return commands.join(" ");
}

function renderText(element) {
  const fontSize = element.fontSize || 20;
  const lineHeight = (element.lineHeight || 1.25) * fontSize;
  const lines = String(element.text || element.rawText || "").split("\n");
  const color = element.strokeColor || "#1e1e1e";
  const family = element.fontFamily === 3 ? "monospace" : "Arial, sans-serif";
  const opacity =
    element.opacity === undefined || element.opacity === null
      ? 1
      : element.opacity / 100;

  const tspans = lines
    .map((line, index) => {
      const dy = index === 0 ? 0 : lineHeight;
      return `<tspan x="${element.x}" dy="${dy}">${escapeXml(line)}</tspan>`;
    })
    .join("");

  return `<text x="${element.x}" y="${element.y + fontSize}" font-family="${family}" font-size="${fontSize}" fill="${escapeXml(color)}" opacity="${opacity}"${rotateAttr(element)}>${tspans}</text>`;
}

function renderElement(element) {
  const common = `${style(element)}${rotateAttr(element)}`;

  if (element.type === "text") {
    return renderText(element);
  }

  if (element.type === "rectangle") {
    const radius = element.roundness ? 8 : 0;
    return `<rect x="${element.x}" y="${element.y}" width="${element.width || 0}" height="${element.height || 0}" rx="${radius}" ${common}/>`;
  }

  if (element.type === "diamond") {
    const cx = element.x + (element.width || 0) / 2;
    const cy = element.y + (element.height || 0) / 2;
    const points = [
      [cx, element.y],
      [element.x + (element.width || 0), cy],
      [cx, element.y + (element.height || 0)],
      [element.x, cy],
    ]
      .map(([x, y]) => `${x},${y}`)
      .join(" ");
    return `<polygon points="${points}" ${common}/>`;
  }

  if (element.type === "ellipse") {
    const cx = element.x + (element.width || 0) / 2;
    const cy = element.y + (element.height || 0) / 2;
    return `<ellipse cx="${cx}" cy="${cy}" rx="${Math.abs(element.width || 0) / 2}" ry="${Math.abs(element.height || 0) / 2}" ${common}/>`;
  }

  if (element.type === "line" || element.type === "arrow" || element.type === "freedraw") {
    const marker = element.type === "arrow" ? ' marker-end="url(#arrowhead)"' : "";
    return `<path d="${pointsPath(element)}" ${common}${marker}/>`;
  }

  return `<!-- Unsupported Excalidraw element: ${escapeXml(element.type)} -->`;
}

function buildSvg(scene) {
  const elements = activeElements(scene);
  const bounds = sceneBounds(elements);
  const rawWidth = Math.max(1, bounds.maxX - bounds.minX + PADDING * 2);
  const rawHeight = Math.max(1, bounds.maxY - bounds.minY + PADDING * 2);
  const scale = Math.min(1, MAX_SIZE / Math.max(rawWidth, rawHeight));
  const width = Math.ceil(rawWidth * scale);
  const height = Math.ceil(rawHeight * scale);
  const viewMinX = bounds.minX - PADDING;
  const viewMinY = bounds.minY - PADDING;

  const body = elements.map(renderElement).join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="${viewMinX} ${viewMinY} ${rawWidth} ${rawHeight}">
  <defs>
    <marker id="arrowhead" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
      <path d="M 0 0 L 12 6 L 0 12 z" fill="#1e1e1e"/>
    </marker>
  </defs>
  <rect x="${viewMinX}" y="${viewMinY}" width="${rawWidth}" height="${rawHeight}" fill="#ffffff"/>
  ${body}
</svg>`;
}

async function main() {
  const input = process.argv[2];
  const output = process.argv[3] || `${input}.png`;

  if (!input) {
    usage();
    process.exit(1);
  }

  const scene = JSON.parse(fs.readFileSync(input, "utf8"));
  const svg = buildSvg(scene);
  fs.mkdirSync(path.dirname(output), { recursive: true });
  await sharp(Buffer.from(svg)).png().toFile(output);
  console.log(`rendered ${input} -> ${output}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
