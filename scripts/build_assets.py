"""Regenerate the README cards in assets/ so they match amankumarchhari.vercel.app.

    python3 scripts/build_assets.py

Builds hero.svg, about.svg and the four project cards, and adds the Apache JMeter
tile to skills.svg (once). Avatar and project art are inlined from ../portfolio/public
(needs Pillow).
"""
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

SANS = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', SFMono-Regular, Menlo, Consolas, monospace"
BRIGHT, FG, MUTED, LINE, MOSS = "#111111", "#2b2b2b", "#6e6e6e", "#dadada", "#2fa35a"

DEFS = """<defs>
  <radialGradient id="canvas" cx="50%" cy="0%" r="90%"><stop offset="0%" stop-color="#fbfbfb"/><stop offset="70%" stop-color="#ececec"/></radialGradient>
  <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1"><stop offset="30%" stop-color="#1d1d1f"/><stop offset="100%" stop-color="#5a5a5f"/></linearGradient>
  <filter id="sh" x="-5%" y="-5%" width="110%" height="120%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.06"/></filter>
  {extra}
</defs>"""


def text(x, y, s, size, weight=400, fill=FG, mono=False, anchor="start", spacing=None, extra=""):
    family = MONO if mono else SANS
    spacing = spacing if spacing is not None else ("0.08em" if mono else "-0.01em")
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" letter-spacing="{spacing}" text-anchor="{anchor}"{extra}>{escape(s)}</text>')


# Rough advance widths, enough to size pills (same numbers the old cards used).
def sans_w(s, size=12.5): return len(s) * size * 0.556
def mono_w(s, size=11): return len(s) * size * 0.645


def pill(x, y, label, dark=False, dot=False):
    w = sans_w(label) + 28 + (12 if dot else 0)
    fill, stroke, color = (BRIGHT, BRIGHT, "#fff") if dark else ("#fff", LINE, FG)
    out = f'<rect x="{x}" y="{y}" width="{w:.0f}" height="28" rx="14" fill="{fill}" stroke="{stroke}"/>'
    tx = x + 14
    if dot:
        out += f'<circle cx="{x + 16}" cy="{y + 14}" r="4" fill="{MOSS}"/>'
        tx = x + 28
    return out + text(tx, y + 18.5, label, 12.5, 500, color), w


def card(w, h, body, extra_defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'{DEFS.format(extra=extra_defs)}'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="22" fill="url(#canvas)" stroke="{LINE}"/>{body}</svg>\n')


def logo(x, y, height, fill=BRIGHT):
    """The traced AA mark from logo-aa.svg (viewBox 146 220 355 188)."""
    paths = re.findall(r"<path[^>]*/>", (ASSETS / "logo-aa.svg").read_text())
    s = height / 188
    return f'<g transform="translate({x - 146 * s:.2f},{y - 220 * s:.2f}) scale({s:.4f})" fill="{fill}">{"".join(paths)}</g>', 355 * s


PORTFOLIO = ROOT.parent / "portfolio" / "public"


def embed(src, size, quality=82):
    """Portfolio image as a JPEG data URI (GitHub only renders images inlined in the SVG)."""
    from PIL import Image  # only dependency outside the standard library
    import base64, io
    im = Image.open(src).convert("RGB")
    im.thumbnail(size, Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def icon_path(slug):
    return re.search(r' d="([^"]+)"', (ROOT / "icons" / f"{slug}.svg").read_text()).group(1)


# Lucide outlines (24px grid), as used by the portfolio's dock and headline
LUCIDE = {
    "layers": '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/>'
              '<path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    "resume": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/>'
              '<path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    "github": '<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/>'
              '<path d="M9 18c-4.51 2-5-2-8-2"/>',
    "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
}

# site.stack tiles, then the link tiles, same order and colours as the portfolio dock
DOCK = [("nextdotjs", "#111111", "#ffffff"), ("react", "#20232a", "#61dafb"), ("typescript", "#3178c6", "#ffffff"),
        ("nodedotjs", "#3c9a4f", "#ffffff"), ("postgresql", "#d6e6f5", "#336791"), ("claude", "#d97757", "#ffffff"),
        None,
        ("resume", "#f2c94c", "#1a1a1a"), ("github", "#24292f", "#ffffff"), ("linkedin", "#2d6fb8", "#ffffff"), ("mail", "url(#mailbg)", "#ffffff")]


def hero():
    W, H, BAR, CX = 880, 590, 46, 440
    defs = (f'<clipPath id="cardclip"><rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="22"/></clipPath>'
            # glossy Tiger-style menu bar, same stops as the site's nav
            '<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fff" stop-opacity="0.95"/>'
            '<stop offset="50%" stop-color="#f3f3f3" stop-opacity="0.9"/><stop offset="51%" stop-color="#e2e2e2" stop-opacity="0.9"/>'
            '<stop offset="100%" stop-color="#ececec" stop-opacity="0.95"/></linearGradient>'
            '<linearGradient id="mailbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#5aa9ff"/><stop offset="100%" stop-color="#2f6fde"/></linearGradient>'
            f'<clipPath id="avatar"><circle cx="{CX}" cy="146" r="66"/></clipPath>'
            '<filter id="avsh" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity="0.22"/></filter>'
            '<filter id="tile" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.08"/></filter>')
    mark, mark_w = logo(26, 13, 20)
    b = [f'<g clip-path="url(#cardclip)"><rect x="0" y="0" width="{W}" height="{BAR}" fill="url(#gloss)"/>'
         f'<line x1="0" y1="{BAR - 0.5}" x2="{W}" y2="{BAR - 0.5}" stroke="#000" stroke-opacity="0.12"/></g>',
         mark, text(26 + mark_w + 12, 28.5, "Aman Kumar Chhari", 14, 700, BRIGHT)]
    x = 26 + mark_w + 12 + sans_w("Aman Kumar Chhari", 14) + 26
    for item in ["About", "Work", "Experience", "Hiring", "Contact"]:
        b.append(text(round(x), 28.5, item, 14, 500, "#262626"))
        x += sans_w(item, 14) + 24
    b.append(text(W - 26, 28.5, "Guna, MP · IST", 13, 500, MUTED, anchor="end"))
    right = W - 26 - sans_w("Guna, MP · IST", 13) - 22
    b.append(text(right, 28.5, "Open to work", 13, 500, "#262626", anchor="end"))
    b.append(f'<circle cx="{right - sans_w("Open to work", 13) - 10:.0f}" cy="24" r="4" fill="{MOSS}"/>')

    # avatar, name, two-line headline with the layers mark, tagline, availability
    b += [f'<circle cx="{CX}" cy="146" r="66" fill="#d9d9d9" filter="url(#avsh)"/>',
          f'<image x="{CX - 66}" y="80" width="132" height="132" clip-path="url(#avatar)" preserveAspectRatio="xMidYMid slice" '
          f'href="{embed(PORTFOLIO / "avatar-me.jpg", (264, 264), 86)}"/>',
          f'<circle cx="{CX}" cy="146" r="66" fill="none" stroke="#000" stroke-opacity="0.06"/>',
          text(CX, 238, "Aman Kumar Chhari", 14, 500, FG, anchor="middle"),
          # headline ends where the icon starts so the pair sits centred (icon 52 + gap 14)
          text(CX + 316 - 66, 322, "Applied AI Engineer", 66, 600, "url(#ink)", anchor="end", spacing="-0.035em"),
          f'<g transform="translate({CX + 316 - 52},{278}) scale(2.2)" fill="none" stroke="#2c2c2e" stroke-width="1.6" '
          f'stroke-linecap="round" stroke-linejoin="round">{LUCIDE["layers"]}</g>',
          text(CX, 396, "& full-stack", 66, 600, "url(#ink)", anchor="middle", spacing="-0.035em"),
          text(CX, 442, "I ship AI features inside real products, with the guardrails that make them safe to run.", 16.5, 400, MUTED, anchor="middle"),
          f'<circle cx="{CX - 98}" cy="471" r="3" fill="{MOSS}"/>',
          text(CX - 88, 475, "available immediately · open to relocate", 12, 400, MUTED)]

    # dock
    T, G, SEP = 46, 10, 21
    dw = 10 * T + 9 * G + SEP + 2 * 12
    x0, y0 = CX - dw / 2, 506
    b.append(f'<rect x="{x0:.1f}" y="{y0}" width="{dw}" height="{T + 20}" rx="22" fill="#fff" fill-opacity="0.75" stroke="{LINE}" filter="url(#sh)"/>')
    x = x0 + 12
    for item in DOCK:
        if item is None:
            b.append(f'<line x1="{x + 5:.1f}" y1="{y0 + 14}" x2="{x + 5:.1f}" y2="{y0 + T + 6}" stroke="{LINE}"/>')
            x += SEP
            continue
        slug, bg, fg = item
        y = y0 + 10
        b.append(f'<rect x="{x:.1f}" y="{y}" width="{T}" height="{T}" rx="12" fill="{bg}" filter="url(#tile)"/>'
                 f'<rect x="{x + 0.5:.1f}" y="{y + 0.5}" width="{T - 1}" height="{T - 1}" rx="11.5" fill="none" stroke="#000" stroke-opacity="0.06"/>')
        if slug in LUCIDE:
            b.append(f'<g transform="translate({x + 11:.1f},{y + 11})" fill="none" stroke="{fg}" stroke-width="2" '
                     f'stroke-linecap="round" stroke-linejoin="round">{LUCIDE[slug]}</g>')
        else:
            b.append(f'<path transform="translate({x + 11:.1f},{y + 11})" d="{icon_path(slug)}" fill="{fg}"/>')
        x += T + G
    return card(W, H, "".join(b), defs)


PROJECTS = [
    # slug, number, title, line 1, line 2, footer (the card art comes from the portfolio's coverflow)
    ("stack", "01", "Stack", "A local-first reading app", "with spaced review of highlights", "JMETER · 500/500 WITH 2 ENGINES DOWN"),
    ("closeby", "02", "CloseBy", "AI-assisted hyperlocal marketplace", "for neighborhood shops", "LIVE · JMETER · 0 OVERSELLS IN 4/4 RUNS"),
    ("scancart", "03", "ScanCart.ai", "Parallel multi-agent trust scoring", "for Indian e-commerce", "DEMO · JMETER · 2.8× FASTER SCANS"),
    ("orderly", "04", "Orderly", "WhatsApp ordering", "for kirana shops", "LIVE · 45 S BOT HEARTBEAT"),
]


def project(slug, num, title, l1, l2, footer):
    W, H, IW, IH = 432, 362, 400, 225
    defs = (f'<clipPath id="art"><rect x="16" y="16" width="{IW}" height="{IH}" rx="14"/></clipPath>'
            '<filter id="artsh" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#000" flood-opacity="0.16"/></filter>')
    b = [f'<rect x="16" y="16" width="{IW}" height="{IH}" rx="14" fill="#ddd" filter="url(#artsh)"/>',
         f'<image x="16" y="16" width="{IW}" height="{IH}" clip-path="url(#art)" preserveAspectRatio="xMidYMid slice" '
         f'href="{embed(PORTFOLIO / "projects" / "cards" / f"{slug}.webp", (800, 450), 78)}"/>',
         f'<rect x="16.5" y="16.5" width="{IW - 1}" height="{IH - 1}" rx="13.5" fill="none" stroke="#000" stroke-opacity="0.08"/>',
         text(24, 274, title, 19, 600, BRIGHT, spacing="-0.03em"),
         text(408, 272, num, 11, 500, MUTED, mono=True, anchor="end"),
         text(24, 298, l1, 14.5, 400, FG),
         text(24, 318, l2, 14.5, 400, MUTED),
         f'<line x1="24" y1="331" x2="408" y2="331" stroke="{LINE}"/>',
         f'<circle cx="28" cy="346" r="3.5" fill="{MOSS}"/>',
         text(38, 350, footer, 11, 500, MUTED, mono=True),
         text(408, 350, "→", 15, 500, BRIGHT, anchor="end", spacing="0")]
    return card(W, H, "".join(b), defs)


# "used in" rows, same as site.stack on the portfolio (no self-rated skill bars)
DAILY = [("Nx", "#111111", "#ffffff", "Next.js", "Stack, CloseBy"), ("Re", "#20232a", "#61dafb", "React", "ScanCart, Orderly"),
         ("Ts", "#3178c6", "#ffffff", "TypeScript", "Stack, CloseBy"), ("Nd", "#3c9a4f", "#ffffff", "Node.js", "ScanCart, Orderly"),
         ("Pg", "#d6e6f5", "#336791", "Postgres", "CloseBy, Orderly"), ("Ai", "#d97757", "#ffffff", "Claude API", "CloseBy, ScanCart, Stack")]


def about():
    b = [text(32, 46, "WHAT I'M LOOKING FOR", 11, 500, MUTED, mono=True),
         text(32, 80, "Applied AI · Full-stack · SDE-1", 22, 600, BRIGHT, spacing="-0.03em")]
    for i, (k, v) in enumerate([("TYPE", "Full-time"), ("LEVEL", "Entry · B.Tech CSE 2026"), ("WHERE", "Open to relocate"), ("START", "Immediately")]):
        y = 116 + i * 30
        b += [text(32, y, k, 11, 500, MUTED, mono=True), text(110, y, v, 14, 400, FG),
              f'<line x1="32" y1="{y + 11}" x2="420" y2="{y + 11}" stroke="{LINE}"/>']
    b += [f'<rect x="452" y="28" width="396" height="194" rx="16" fill="#fff" fill-opacity="0.65" stroke="{LINE}" filter="url(#sh)"/>',
          text(474, 56, "DAILY STACK · USED IN", 11, 500, MUTED, mono=True)]
    for i, (short, bg, fg, name, used) in enumerate(DAILY):
        x, y = 474 + (i % 2) * 190, 76 + (i // 2) * 46
        b += [f'<rect x="{x}" y="{y}" width="34" height="34" rx="9" fill="{bg}"/>',
              text(x + 17, y + 22, short, 12, 700, fg, anchor="middle", spacing="0"),
              text(x + 44, y + 14, name, 13, 500, FG),
              text(x + 44, y + 30, used, 10.5, 400, MUTED)]
    return card(880, 250, "".join(b))


def add_jmeter_tile():
    """Add an Apache JMeter tile after Linux in the last skills row, once."""
    path = ASSETS / "skills.svg"
    s = path.read_text()
    if ">JMeter<" in s:
        return False
    icon = re.search(r'd="([^"]+)"', (ROOT / "scripts" / "apachejmeter.svg").read_text()).group(1)
    linux = re.search(r'<rect x="(\d+)" y="(\d+)" width="40" height="40" rx="11" fill="[^"]+"/>(?=<path[^>]*/><text[^>]*>Linux<)', s)
    x, y = int(linux.group(1)) + 84, int(linux.group(2))
    tile = (f'<rect x="{x}" y="{y}" width="40" height="40" rx="11" fill="#D22128"/>'
            f'<path transform="translate({x + 9},{y + 9}) scale(0.9167)" d="{icon}" fill="#ffffff"/>'
            + text(x + 20, y + 58, "JMeter", 11, 500, FG, anchor="middle", spacing="0"))
    s = re.sub(r">(\d+) TOOLS<", lambda m: f">{int(m.group(1)) + 1} TOOLS<", s)
    path.write_text(s.replace("</svg>", tile + "</svg>"))
    return True


if __name__ == "__main__":
    (ASSETS / "hero.svg").write_text(hero())
    (ASSETS / "about.svg").write_text(about())
    for slug, *rest in PROJECTS:
        (ASSETS / f"project-{slug}.svg").write_text(project(slug, *rest))
    print("skills.svg: added JMeter" if add_jmeter_tile() else "skills.svg: JMeter already there")
