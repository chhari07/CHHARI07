"""Generates the README's SVG cards in the portfolio theme (soft monochrome, colour only on icons)."""
from pathlib import Path
from html import escape as e

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', SFMono-Regular, Menlo, Consolas, monospace"
BG, SURFACE, LINE, DIM, MUTED, FG, BRIGHT = "#ececec", "#f7f7f7", "#dadada", "#a6a6a6", "#6e6e6e", "#2b2b2b", "#111111"
MOSS, RUST, NAVY = "#2fa35a", "#ee5a24", "#2f6fde"

DEFS = f"""<defs>
  <radialGradient id="canvas" cx="50%" cy="0%" r="90%"><stop offset="0%" stop-color="#fbfbfb"/><stop offset="70%" stop-color="{BG}"/></radialGradient>
  <linearGradient id="ink" x1="0" y1="0" x2="0" y2="1"><stop offset="30%" stop-color="#1d1d1f"/><stop offset="100%" stop-color="#5a5a5f"/></linearGradient>
  <filter id="sh" x="-5%" y="-5%" width="110%" height="120%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.06"/></filter>
</defs>"""


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f"{DEFS}{body}</svg>\n")


def canvas(w, h):
    return f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="22" fill="url(#canvas)" stroke="{LINE}"/>'


def card(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#fff" fill-opacity="0.65" stroke="{LINE}" filter="url(#sh)"/>'


def text(x, y, s, size=14, fill=FG, weight=400, font=SANS, ls="-0.01em", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" letter-spacing="{ls}" text-anchor="{anchor}">{e(s)}</text>')


def eyebrow(x, y, s, fill=MUTED):
    return text(x, y, s.upper(), 11, fill, 500, MONO, "0.08em")


def pill(x, y, label, w, dot=None, solid=False):
    bg, fg, st = (BRIGHT, "#fff", BRIGHT) if solid else ("#fff", FG, LINE)
    out = f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="14" fill="{bg}" stroke="{st}"/>'
    tx = x + 14
    if dot:
        out += f'<circle cx="{x+16}" cy="{y+14}" r="4" fill="{dot}"/>'
        tx = x + 28
    return out + text(tx, y + 18.5, label, 12.5, fg, 500)


# ---------- hero ----------
W, H = 880, 360
hero = canvas(W, H)
hero += pill(32, 30, "amankumarchhari.vercel.app", 214, MOSS)
hero += eyebrow(W - 32, 49, "Guna, MP · India").replace('text-anchor="start"', 'text-anchor="end"')
hero += text(30, 128, "Aman Kumar Chhari", 60, "url(#ink)", 600, SANS, "-0.04em")
hero += text(32, 166, "Full-stack & applied AI engineer", 22, MUTED, 500, SANS, "-0.02em")
hero += text(32, 214, "I design, build and ship full-stack applications end to end:", 15, FG)
hero += text(32, 238, "frontend, APIs, databases, auth, payments and AI features.", 15, FG)
x = 32
for label, w, dot, solid in [("Open to work · SDE-1", 170, MOSS, True), ("Gurgaon · Bengaluru · Remote", 222, None, False), ("B.Tech CSE · 2026", 146, None, False)]:
    hero += pill(x, 272, label, w, dot, solid)
    x += w + 10
hero += f'<line x1="32" y1="326" x2="{W-32}" y2="326" stroke="{LINE}"/>'
hero += eyebrow(32, 345, "AI drafts, humans confirm · State machines over vibes · Money in integer paise")
(OUT / "hero.svg").write_text(svg(W, H, hero))

# ---------- link buttons ----------
ICONS = {
    "globe": f'<circle cx="0" cy="0" r="6.5" fill="none" stroke="{{c}}" stroke-width="1.4"/><ellipse cx="0" cy="0" rx="2.8" ry="6.5" fill="none" stroke="{{c}}" stroke-width="1.2"/><line x1="-6.5" y1="0" x2="6.5" y2="0" stroke="{{c}}" stroke-width="1.2"/>',
    "in": '<rect x="-7" y="-7" width="14" height="14" rx="3" fill="#0a66c2"/><text x="0" y="4" font-family="Arial" font-weight="700" font-size="10" fill="#fff" text-anchor="middle">in</text>',
    "mail": f'<rect x="-7" y="-5" width="14" height="10" rx="2" fill="none" stroke="{RUST}" stroke-width="1.4"/><path d="M-7 -4 L0 1 L7 -4" fill="none" stroke="{RUST}" stroke-width="1.4"/>',
    "doc": f'<path d="M-5 -7 H2 L5 -4 V7 H-5 Z" fill="none" stroke="{NAVY}" stroke-width="1.4"/><line x1="-2.5" y1="0" x2="2.5" y2="0" stroke="{NAVY}" stroke-width="1.2"/><line x1="-2.5" y1="3" x2="2.5" y2="3" stroke="{NAVY}" stroke-width="1.2"/>',
}
for name, label, icon, w, solid in [("portfolio", "Portfolio", "globe", 128, True), ("linkedin", "LinkedIn", "in", 120, False),
                                     ("email", "Email", "mail", 98, False), ("resume", "Resume", "doc", 112, False)]:
    bg, fg, st = (BRIGHT, "#fff", BRIGHT) if solid else ("#fff", FG, LINE)
    ic = ICONS[icon].replace("{c}", "#fff" if solid else FG)
    b = (f'<rect x="1" y="1" width="{w-2}" height="38" rx="19" fill="{bg}" stroke="{st}"/>'
         f'<g transform="translate(24,20)">{ic}</g>' + text(40, 25, label, 14, fg, 500))
    (OUT / f"btn-{name}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="40" viewBox="0 0 {w} 40">{b}</svg>\n')

# ---------- project cards ----------
PROJECTS = [
    ("closeby", "CloseBy", "01", "AI-assisted marketplace", "for neighbourhood shops", ["Next.js", "Supabase", "Claude API", "Razorpay"], MOSS, "Live · case study"),
    ("scancart", "ScanCart.ai", "02", "Counterfeit & fake-review checks", "for Indian e-commerce", ["Chrome MV3", "Node.js", "Claude API"], RUST, "Demo · case study"),
    ("orderly", "Orderly", "03", "WhatsApp ordering", "for kirana shops", ["React", "Supabase", "Node.js", "BuilderBot"], NAVY, "Live · case study"),
    ("stack", "Stack", "04", "Read it, keep it, build on it:", "news, PDFs, notes & focus", ["Next.js", "Capacitor", "Android", "Supabase"], "#d97757", "Android · closed test"),
]
PW, PH = 432, 200
for slug, name, num, l1, l2, stack, accent, status in PROJECTS:
    p = canvas(PW, PH)
    p += f'<rect x="24" y="24" width="40" height="40" rx="11" fill="{accent}"/>' + text(44, 50, name[0], 18, "#fff", 700, SANS, "0", "middle")
    p += eyebrow(PW - 24, 40, num).replace('text-anchor="start"', 'text-anchor="end"')
    p += text(78, 51, name, 22, BRIGHT, 600, SANS, "-0.03em")
    p += text(24, 98, l1, 15, FG) + text(24, 120, l2, 15, MUTED)
    x = 24
    for s in stack:
        w = 16 + len(s) * 7.1
        p += f'<rect x="{x}" y="140" width="{w:.0f}" height="22" rx="11" fill="#fff" stroke="{LINE}"/>'
        p += text(x + 8, 155, s, 11, FG, 400, MONO, "0")
        x += w + 6
    p += f'<circle cx="28" cy="181" r="3.5" fill="{accent}"/>' + eyebrow(38, 185, status)
    p += text(PW - 24, 185, "→", 15, BRIGHT, 500, SANS, "0", "end")
    (OUT / f"project-{slug}.svg").write_text(svg(PW, PH, p))

# ---------- looking for + stack ----------
W2, H2 = 880, 250
s = canvas(W2, H2)
s += eyebrow(32, 46, "What I'm looking for")
s += text(32, 80, "Full-stack · Applied AI · SDE-1", 22, BRIGHT, 600, SANS, "-0.03em")
rows = [("Type", "Full-time"), ("Level", "Entry · B.Tech CSE 2026"), ("Where", "Gurgaon, Bengaluru, remote"), ("Start", "Immediately")]
for i, (k, v) in enumerate(rows):
    y = 116 + i * 30
    s += eyebrow(32, y, k) + text(110, y, v, 14, FG)
    s += f'<line x1="32" y1="{y+11}" x2="420" y2="{y+11}" stroke="{LINE}"/>'
s += card(452, 28, 396, 194)
s += eyebrow(474, 56, "Daily stack")
DOCK = [("Nx", "#111111", "#ffffff", "Next.js", 90), ("Re", "#20232a", "#61dafb", "React", 90), ("Ts", "#3178c6", "#ffffff", "TypeScript", 85),
        ("Nd", "#3c9a4f", "#ffffff", "Node.js", 80), ("Pg", "#d6e6f5", "#336791", "Postgres", 75), ("Ai", "#d97757", "#ffffff", "Claude API", 80)]
for i, (short, bg, fg, label, lvl) in enumerate(DOCK):
    col, row = i % 2, i // 2
    x, y = 474 + col * 190, 76 + row * 46
    s += f'<rect x="{x}" y="{y}" width="34" height="34" rx="9" fill="{bg}"/>' + text(x + 17, y + 22, short, 12, fg, 700, SANS, "0", "middle")
    s += text(x + 44, y + 14, label, 13, FG, 500)
    s += f'<rect x="{x+44}" y="{y+22}" width="120" height="5" rx="2.5" fill="{LINE}"/><rect x="{x+44}" y="{y+22}" width="{120*lvl/100:.0f}" height="5" rx="2.5" fill="{BRIGHT}"/>'
(OUT / "about.svg").write_text(svg(W2, H2, s))
print("ok")
