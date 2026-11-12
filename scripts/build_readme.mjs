// Builds README.md from the SOLOX portfolio's own content files, so the profile and the site say the same thing.
// Text only: the one image is the portrait (assets/photo.png, copied from the site's solox-cutout.webp).
//   node scripts/build_readme.mjs            (Node 22.6+ reads the .ts files directly)
//   PORTFOLIO=/path/to/combined-portfolio node scripts/build_readme.mjs
import { writeFileSync, copyFileSync, existsSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { homedir } from "node:os";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const SRC = process.env.PORTFOLIO || join(homedir(), "Desktop/projects/combined-portfolio");
const C = (f) => import(join(SRC, "src/content", f));
const { site, projects, roleText, proof, guards, principles, experience, education, awards, skills, lookingFor } = await C("portfolio.ts");
const deep = (await C("fullstack.ts")).projects;
const { tools, kits } = await C("tools.ts");

const URL = "https://amankumarchhari.vercel.app";
const abs = (h) => (h.startsWith("/") ? URL + h : h);
const RESUME = `${URL}/Aman_Kumar_Chhari_Resume_Design_Engineer.pdf`;
const linkedin = site.links.find((l) => l.label === "LinkedIn").href;
const esc = (s) => String(s).replace(/\|/g, "\\|");
const out = [];
const w = (...l) => out.push(...l);

// Portrait: the only image. PNG so every GitHub client shows it.
const photo = join(ROOT, "assets/photo.png");
execFileSync("python3", ["-c", `from PIL import Image\nim=Image.open(${JSON.stringify(join(SRC, "public/solox-cutout.webp"))}).convert("RGBA")\nim.thumbnail((440,580))\nim.save(${JSON.stringify(photo)},optimize=True)`]);

// ── Header ──
w(`<p align="center"><img src="./assets/photo.png" width="200" alt="Portrait of ${site.name}, illustrated"/></p>`, "");
w(`<h1 align="center">${site.name}</h1>`, "");
w(`<p align="center"><b>${site.title}</b><br/>${site.line}</p>`, "");
w(`<p align="center">`,
  `  <a href="${URL}/">Portfolio</a> ·`,
  `  <a href="${linkedin}">LinkedIn</a> ·`,
  `  <a href="mailto:${site.email}">Email</a> ·`,
  `  <a href="${RESUME}">Resume</a>`,
  `</p>`, "");
w(`<p align="center"><sub>${site.location}</sub></p>`, "");
w(`> ${site.intro}`, "");

// ── How I work ──
w(`## How I work`, "");
w(`| | Step | What happens |`, `|---|---|---|`);
for (const s of site.steps) w(`| ${s.k} | **${s.t}** | ${esc(s.d)} |`);
w("");

// ── Proof ──
w(`## Measured, not estimated`, "");
for (const p of proof) w(`- **${p.v}**: ${p.l}`);
w("");

// ── Selected work ──
w(`## Selected work`, "");
projects.forEach((p, i) => {
  const d = deep.find((x) => x.slug === p.slug);
  w(`### ${String(i + 1).padStart(2, "0")} · [${p.name}](${URL}/work/${p.slug})`, "");
  w(`**${p.tagline}** <sub>${p.kind} · ${p.role} · ${p.year}</sub>`, "");
  w(p.problem, "");
  for (const b of p.built) w(`- ${b}`);
  w("");
  if (p.numbers?.length) w(p.numbers.map((n) => `**${n.v}** ${n.l}`).join(" · "), "");
  w(`<sub>Built with: ${p.stack}</sub>`, "");
  const links = [{ label: "Case study", href: `${URL}/work/${p.slug}` }, ...p.links];
  w(links.map((l) => `[${l.label}](${abs(l.href)})`).join(" · "), "");
  if (p.note) w(`<sub>${p.note}</sub>`, "");
});

// ── Load tests ──
const withTests = deep.filter((d) => d.loadTests);
if (withTests.length) {
  w(`## Load-tested with Apache JMeter`, "");
  w(`| Project | Test | Load | Result |`, `|---|---|---|---|`);
  for (const d of withTests) d.loadTests.rows.forEach((r, i) =>
    w(`| ${i ? "" : `[${d.name}](${URL}/work/${d.slug})`} | ${esc(r.test)} | ${esc(r.load)} | ${esc(r.result)} |`));
  w("", `<sub>${withTests.map((d) => `${d.name}: ${d.loadTests.caption}`).join(" ")}</sub>`, "");
}

// ── Tools ──
w(`## Tools I built for my own day`, "");
w(`| Tool | What it is | Status |`, `|---|---|---|`);
for (const t of tools) w(`| [${t.name}](${URL}/tools/${t.slug}) | ${esc(t.tagline)} <sub>${esc(t.kind)}</sub> | ${esc(t.status)} |`);
w("");

// ── Open source kits ──
w(`## Open source`, "");
for (const k of kits) {
  w(`### [${k.name}](${k.links[0].href})`, "", `${k.tagline} <sub>${k.meta}</sub>`, "");
  for (const x of k.includes) w(`- ${x}`);
  w("", "```bash", k.install, "```", `<sub>${k.installNote}</sub>`, "");
  w(k.links.map((l) => `[${l.label}](${abs(l.href)})`).join(" · "), "");
}

// ── How I ship AI ──
w(`## How I ship AI safely`, "");
for (const g of guards) w(`- **${g.t}.** ${g.d}`);
w("", principles.map((p) => `\`${p}\``).join(" · "), "");

// ── Hire me ──
w(`## Hire me`, "");
w(`| | |`, `|---|---|`);
for (const l of lookingFor) w(`| **${l.k}** | ${esc(l.v)} |`);
w("");
for (const r of site.roles) w(`- **${r}**: ${roleText[r]}`);
w("");

// ── Skills ──
w(`## Skills`, "");
for (const [k, v] of Object.entries(skills)) w(`- **${k}**: ${v.join(", ")}`);
w("");

// ── Experience & education ──
w(`## Experience`, "");
for (const e of experience) {
  w(`**${e.role}**, ${e.org} <sub>${e.when}</sub>`, "");
  for (const p of e.points) w(`- [${p.name}](${p.href}) <sub>${p.when}</sub>: ${p.text}`);
  if (e.points.length) w("");
}
w(`**${education.degree}**, ${education.school} <sub>${education.years}</sub>`, "");

// ── Achievements ──
w(`## Achievements`, "");
for (const a of awards) w(`- **${a.t}**, ${a.d} ([certificate](${abs(a.href)}))`);
w("");

w(`---`, "", `<sub>Text generated from the portfolio's content files by <code>node scripts/build_readme.mjs</code>, so it matches <a href="${URL}/">${URL.replace("https://", "")}</a>.</sub>`, "");

writeFileSync(join(ROOT, "README.md"), out.join("\n"));
console.log(`README.md: ${out.length} lines · ${projects.length} projects · ${tools.length} tools · ${kits.length} kits`);
