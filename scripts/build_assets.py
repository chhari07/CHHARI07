"""Regenerate the README cards in assets/ so they match amankumarchhari.vercel.app.

    python3 scripts/build_assets.py

Builds hero.svg, about.svg and the four project cards, and adds the Apache JMeter
tile to skills.svg (once). Standard library only.
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


def hero():
    W, H, BAR = 880, 376, 46
    defs = (f'<clipPath id="cardclip"><rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="22"/></clipPath>'
            # glossy Tiger-style menu bar, same stops as the site's nav
            '<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fff" stop-opacity="0.95"/>'
            '<stop offset="50%" stop-color="#f3f3f3" stop-opacity="0.9"/><stop offset="51%" stop-color="#e2e2e2" stop-opacity="0.9"/>'
            '<stop offset="100%" stop-color="#ececec" stop-opacity="0.95"/></linearGradient>')
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

    b += [text(30, 128, "Applied AI Engineer", 58, 600, "url(#ink)", spacing="-0.04em"),
          text(33, 168, "& full-stack", 28, 500, MUTED, spacing="-0.02em"),
          text(32, 212, "I ship AI features inside real products, with the guardrails that make them safe to run.", 15.5, 400, FG),
          text(32, 236, "One gateway for every model call, spend caps, tool use, human approval and evals, load-tested with JMeter.", 14, 400, MUTED)]
    x = 32
    for label, dark, dot in [("Open to work · Full-time", True, True), ("Open to relocate", False, False),
                             ("Available immediately", False, False), ("B.Tech CSE · 2026", False, False)]:
        p, w = pill(x, 268, label, dark, dot)
        b.append(p)
        x += w + 10
    b += [f'<line x1="32" y1="322" x2="848" y2="322" stroke="{LINE}"/>',
          text(32, 344, "AI DRAFTS, HUMANS CONFIRM · STATE MACHINES OVER VIBES · MONEY IN INTEGER PAISE · FAILED CHECKS LEFT OUT", 10.5, 500, MUTED, mono=True)]
    return card(W, H, "".join(b), defs)


PROJECTS = [
    # slug, letter, colour, number, title, line 1, line 2, tags, footer
    ("stack", "S", "#d97757", "01", "Stack", "A local-first reading app", "with spaced review of highlights",
     ["Next.js 16", "Capacitor", "Supabase", "5 LLMs"], "JMETER · 500/500 WITH 2 ENGINES DOWN"),
    ("closeby", "C", "#2fa35a", "02", "CloseBy", "AI-assisted hyperlocal marketplace", "for neighborhood shops",
     ["Next.js", "Supabase", "Claude API", "Razorpay"], "LIVE · JMETER · 0 OVERSELLS IN 4/4 RUNS"),
    ("scancart", "S", "#ee5a24", "03", "ScanCart.ai", "Parallel multi-agent trust scoring", "for Indian e-commerce",
     ["Chrome MV3", "Node.js", "Claude API", "React"], "DEMO · JMETER · 2.8× FASTER SCANS"),
    ("orderly", "O", "#2f6fde", "04", "Orderly", "WhatsApp ordering", "for kirana shops",
     ["React", "Supabase", "Node.js", "BuilderBot"], "LIVE · 45 S BOT HEARTBEAT"),
]


def project(letter, colour, num, title, l1, l2, tags, footer):
    b = [f'<rect x="24" y="24" width="40" height="40" rx="11" fill="{colour}"/>',
         text(44, 50, letter, 18, 700, "#fff", anchor="middle", spacing="0"),
         text(408, 40, num, 11, 500, MUTED, mono=True, anchor="end"),
         text(78, 51, title, 22, 600, BRIGHT, spacing="-0.03em"),
         text(24, 98, l1, 15, 400, FG),
         text(24, 120, l2, 15, 400, MUTED)]
    x = 24
    for t in tags:
        w = mono_w(t) + 16
        b.append(f'<rect x="{x:.1f}" y="140" width="{w:.0f}" height="22" rx="11" fill="#fff" stroke="{LINE}"/>')
        b.append(text(f"{x + 8:.1f}", 155, t, 11, 400, FG, mono=True, spacing="0"))
        x += w + 6
    b += [f'<circle cx="28" cy="181" r="3.5" fill="{MOSS}"/>',
          text(38, 185, footer, 11, 500, MUTED, mono=True),
          text(408, 185, "→", 15, 500, BRIGHT, anchor="end", spacing="0")]
    return card(432, 200, "".join(b))


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
        (ASSETS / f"project-{slug}.svg").write_text(project(*rest))
    print("skills.svg: added JMeter" if add_jmeter_tile() else "skills.svg: JMeter already there")
