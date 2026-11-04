#!/usr/bin/env python3
"""Profile README cards in the SOLOX look (amankumarchhari.vercel.app, Nov 2026).

    python3 scripts/build_solox.py

Each card is an HTML page rendered by headless Chrome at 2x into assets/solox/*.png, so the
Anton + Inter fonts and the real site images show exactly. Images come from the portfolio repo
(~/Desktop/combined-portfolio/public)."""
import base64, os, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "solox"
SITE = Path.home() / "Desktop/combined-portfolio/public"
ANTON = Path.home() / "Desktop/lets one more change/agency-pitch/assets/Anton.ttf"
INTER = Path.home() / ".local/share/fonts/Inter-Variable.ttf"

def uri(p):
    p = SITE / p
    mime = {"webp": "image/webp", "png": "image/png", "svg": "image/svg+xml", "jpg": "image/jpeg"}[p.suffix[1:]]
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()

CSS = f"""
@font-face{{font-family:Anton;src:url('file://{ANTON}')}}
@font-face{{font-family:Inter;src:url('file://{INTER}');font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}
html,body{{background:transparent}}
body{{font-family:Inter,sans-serif;color:#0a0a0a;-webkit-font-smoothing:antialiased}}
.card{{position:relative;background:#fff;border:1.5px solid #0a0a0a;border-radius:22px;overflow:hidden}}
.d{{font-family:Anton,Impact,sans-serif;text-transform:uppercase;line-height:.86;letter-spacing:-.01em}}
.lb{{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.06em}}
.mute{{color:#6b6b6b}}
.dot{{display:inline-block;width:9px;height:9px;margin-right:8px}}
"""
PAL = ["#ff6a3d", "#facc15", "#3b6bff", "#ef4444", "#22c55e"]

def render(name, w, h, body, scale=2):
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body style='width:{w}px;height:{h}px'>{body}</body></html>"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html); page = f.name
    out = OUT / f"{name}.png"
    subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000",
                    "--allow-file-access-from-files", f"--force-device-scale-factor={scale}", "--virtual-time-budget=5000",
                    f"--window-size={w},{h}", f"--screenshot={out}", f"file://{page}"], capture_output=True)
    os.remove(page)
    print(out)

def hero():
    W, H = 880, 560
    body = f"""<div class="card" style="width:{W}px;height:{H}px">
      <div style="position:absolute;left:28px;top:22px;height:58px"><img src="{uri('brand/solox-logo-hd.png')}" style="height:58px"></div>
      <div class="lb" style="position:absolute;right:30px;top:30px;text-align:right"><span class="dot" style="background:#ff6a3d"></span>2026 · Selected works</div>
      <div class="lb mute" style="position:absolute;right:30px;top:50px">Design Engineer · Applied AI</div>
      <div style="position:absolute;left:0;right:0;top:118px;text-align:center">
        <div style="position:relative;display:inline-block">
          <div class="d" style="font-size:250px">SOLOX</div>
          <img src="{uri('solox-cutout.webp')}" style="position:absolute;left:50%;bottom:-24%;height:126%;transform:translateX(-50%);filter:grayscale(1) contrast(1.08);
               -webkit-mask-image:linear-gradient(to bottom,#000 86%,transparent 100%)">
        </div>
      </div>
      <div style="position:absolute;left:30px;right:30px;bottom:26px;display:flex;justify-content:space-between;align-items:flex-end;gap:20px">
        <div><div style="font-weight:800;font-size:15px;letter-spacing:.04em">AMAN KUMAR CHHARI</div>
             <div style="font-weight:600;font-size:21px;line-height:1.15;text-transform:uppercase;margin-top:6px;max-width:520px">I build AI products, then design the brand story that sells them.</div></div>
        <div class="lb mute" style="text-align:right;line-height:1.6">Guna, MP · open to relocate<br>B.Tech CSE 2026</div>
      </div></div>"""
    render("hero", W, H, body)

def button(name, label, dark):
    w = 34 + len(label) * 11 + 34
    st = "background:#0a0a0a;color:#fff" if dark else "background:#fff;color:#0a0a0a"
    body = f"""<div style="width:{w}px;height:40px;border:1.5px solid #0a0a0a;border-radius:20px;{st};display:flex;align-items:center;justify-content:center;
      font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase">{label}</div>"""
    render(name, w, 40, body)

def project(slug, n, name, kind, tag, big, big_l, color, art):
    W, H = 432, 330
    body = f"""<div class="card" style="width:{W}px;height:{H}px">
      <img src="{uri(art)}" style="width:100%;height:118px;object-fit:cover;object-position:left center;filter:grayscale(1) contrast(1.05);border-bottom:1.5px solid #0a0a0a">
      <div style="position:absolute;left:22px;top:136px;right:22px;display:flex;justify-content:space-between" class="lb mute"><span>0{n} · {kind}</span><span>2026</span></div>
      <div class="d" style="position:absolute;left:20px;top:160px;font-size:62px">{name}</div>
      <div style="position:absolute;left:22px;top:222px;font-size:14.5px;color:#2a2a2a;max-width:390px">{tag}</div>
      <div style="position:absolute;left:22px;right:22px;bottom:18px;display:flex;align-items:flex-end;gap:12px;border-top:1px solid #e0e0dc;padding-top:10px">
        <span class="dot" style="background:{color};margin:0 0 8px;flex:none"></span>
        <span class="d" style="font-size:34px">{big}</span><span class="mute" style="font-size:12.5px;padding-bottom:4px;white-space:nowrap">{big_l}</span>
        <span class="lb" style="margin-left:auto;padding-bottom:5px;white-space:nowrap">Case study →</span></div></div>"""
    render(f"project-{slug}", W, H, body)

def more():
    W, H = 432, 330
    icons = "".join(f'<img src="{uri("icons/" + i)}" style="width:46px;height:46px;border-radius:11px;border:1px solid #ddd">'
                    for i in ["wakeface.svg", "otg-switch.svg", "github-widgets.webp", "mac-bar.webp", "ubuntu-mac-kit.webp", "ubuntu-widgets.webp"])
    body = f"""<div class="card" style="width:{W}px;height:{H}px;background:#0a0a0a;color:#fff">
      <div class="lb" style="position:absolute;left:22px;top:22px;color:#999">Also built · used every day</div>
      <div class="d" style="position:absolute;left:20px;top:54px;font-size:62px">Tools<br>+ UI Kit</div>
      <div style="position:absolute;left:22px;top:180px;font-size:14.5px;color:#ccc;max-width:390px">Android apps, home-screen widgets, a GNOME extension and two open-source Ubuntu kits.</div>
      <div style="position:absolute;left:22px;bottom:22px;display:flex;gap:10px">{icons}</div></div>"""
    render("project-tools", W, H, body)

def about():
    W, H = 880, 300
    roles = ["Design Engineer", "Creative Technologist", "AI Product Engineer", "Forward Deployed Engineer"]
    rl = "".join(f'<div style="display:flex;align-items:center;gap:10px;border-top:1px solid #e0e0dc;padding:7px 0">'
                 f'<span class="dot" style="background:{PAL[i]}"></span><span class="d" style="font-size:30px">{r}</span></div>' for i, r in enumerate(roles))
    det = [("Type", "Full-time"), ("Level", "Entry · B.Tech CSE 2026"), ("Location", "Open to relocate"), ("Start", "Immediately"),
           ("Daily stack", "Next.js · React · TypeScript · Node.js · Postgres · Claude API · Figma")]
    dl = "".join(f'<div style="margin-bottom:12px"><div class="lb mute" style="font-size:11px">{k}</div><div style="font-weight:600;font-size:15px;margin-top:3px">{v}</div></div>' for k, v in det)
    body = f"""<div class="card" style="width:{W}px;height:{H}px;padding:24px 28px;display:grid;grid-template-columns:1.25fr 1fr;gap:34px">
      <div><div class="lb" style="margin-bottom:12px">(Hire me as)</div>{rl}</div>
      <div><div class="lb" style="margin-bottom:12px">(Looking for)</div>{dl}</div></div>"""
    render("about", W, H, body)

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    hero()
    for n, l, d in [("btn-portfolio", "Portfolio", True), ("btn-linkedin", "LinkedIn", False), ("btn-email", "Email", False), ("btn-resume", "Resume", False)]:
        button(n, l, d)
    project("closeby", 1, "CloseBy", "AI marketplace", "Your street's shops, online. One gateway guards every AI call.", "0", "oversells, 50 buyers vs 5 units", PAL[0], "cards/closeby-wide.webp")
    project("stack", 2, "Stack", "Web + Android", "A local-first reading app that brings your highlights back.", "500/500", "with 2 AI engines down", PAL[1], "cards/stack-wide.webp")
    project("scancart", 3, "ScanCart.ai", "Chrome extension", "7 parallel AI checks behind one Trust Score for any listing.", "7", "checks, one verdict", PAL[2], "cards/scancart-wide.webp")
    project("streetwise", 4, "Streetwise", "Multi-agent AI", "One QR on every shop, four Fetch.ai agents behind it.", "4", "AI agents, one shop QR", PAL[3], "cards/streetwise-wide.webp")
    project("orderly", 5, "Orderly", "WhatsApp bot", "Run your kirana shop on WhatsApp. Buyers install nothing.", "45 s", "bot heartbeat in the owner app", PAL[4], "cards/orderly-wide.webp")
    more()
    about()
