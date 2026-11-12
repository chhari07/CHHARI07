<p align="center"><img src="./assets/photo.png" width="200" alt="Portrait of Aman Kumar Chhari, illustrated"/></p>

<h1 align="center">Aman Kumar Chhari</h1>

<p align="center"><b>Design Engineer · Applied AI</b><br/>I build AI products, then design the brand story that sells them.</p>

<p align="center">
  <a href="https://amankumarchhari.vercel.app/">Portfolio</a> ·
  <a href="https://www.linkedin.com/in/aman-kumar-chhari-9613bb235/">LinkedIn</a> ·
  <a href="mailto:amankumarchhari@gmail.com">Email</a> ·
  <a href="https://amankumarchhari.vercel.app/Aman_Kumar_Chhari_Resume_Design_Engineer.pdf">Resume</a>
</p>

<p align="center"><sub>Guna, MP · open to relocate · B.Tech CSE 2026</sub></p>

> I start from the client's need, ship the full-stack AI tool or app, and then turn it into a brand story people can read in 30 seconds: a case study, a launch poster, a banner and a narrated explainer video. One person, from problem to launch.

## How I work

| | Step | What happens |
|---|---|---|
| 01 | **Listen** | Write the client's problem in one line, and who loses money or time because of it. |
| 02 | **Build** | Ship the AI tool, web app or Android app: UI, backend, AI layer, payments, deploy. |
| 03 | **Guard** | AI drafts, people decide. One gateway, spend caps, evals and load tests. |
| 04 | **Brand** | Name, colours, poster, banner and a QR code that opens the live demo. |
| 05 | **Tell** | Case study and narrated explainer video, so a buyer gets it in 30 seconds. |

## Measured, not estimated

- **500/500**: Stack: requests served with the top two AI providers down
- **100%**: CloseBy: over-cap AI calls blocked before any model call
- **27**: CloseBy: eval cases, Hindi aliases to gibberish
- **7**: ScanCart.ai: parallel checks behind one Trust Score
- **600+**: teams at Hacksagon 2025, where I was a finalist

## Selected work

### 01 · [CloseBy](https://amankumarchhari.vercel.app/work/closeby)

**Your street's shops, online.** <sub>AI web app · marketplace · Solo: design, frontend, backend, AI layer · 2026</sub>

Neighbourhood shop owners have no time to type a catalogue, and buyers can't see what a shop near them has in stock.

- Owners import stock from a shelf photo or a voice list. The AI drafts; nothing is saved until the owner approves.
- Every AI call passes one gateway: auth, rate limit, kill switch, daily spend cap, tool loop, cost logging.
- Razorpay holds stock until the server confirms payment; rejected paid orders refund automatically.

**100%** over-cap AI calls blocked under load · **27** eval cases (Hindi, typos, gibberish) · **0** oversells: 50 buyers, last 5 units

<sub>Built with: Next.js · TypeScript · Supabase · Claude API · Razorpay · JMeter</sub>

[Case study](https://amankumarchhari.vercel.app/work/closeby) · [Live demo](https://closeby-ashy.vercel.app) · [GitHub](https://github.com/chhari07/closeby)

### 02 · [Stack](https://amankumarchhari.vercel.app/work/stack)

**Stack makes you remember what you read.** <sub>Web + Android app · AI reading · Solo: product, design, Android app, sync, AI layer · 2026</sub>

People read articles and PDFs all day and forget almost all of it a week later. Read-later apps save links but never bring them back.

- One Next.js codebase ships the website and a native Android app (Capacitor). Works offline in IndexedDB, no account needed.
- Every morning, 3 old highlights come back on a spaced schedule.
- Stack AI runs in one Supabase Edge Function and falls back across five model providers.

**500/500** requests served with top 2 providers down · **1.6 s** p95 latency in that failover test · **5** LLM providers in the fallback chain

<sub>Built with: Next.js 16 · TypeScript · Capacitor · IndexedDB · Supabase Edge Functions</sub>

[Case study](https://amankumarchhari.vercel.app/work/stack) · [Live app](https://stack-henna-delta.vercel.app) · [GitHub](https://github.com/chhari07/stackforge)

### 03 · [ScanCart.ai](https://amankumarchhari.vercel.app/work/scancart)

**One Trust Score for any listing.** <sub>AI Chrome extension + Android app · trust · Solo: extension, Android app, backend, agents · 2026</sub>

Shoppers on Indian marketplaces can't easily tell a fake product or a paid review from a real one.

- A Chrome extension sends the listing to a backend that runs 6 specialist AI agents in parallel, then a compliance agent.
- All 7 checks combine into one weighted Trust Score with the reasons behind it.
- A check that fails is left out and shown as "X of 7 checks", never guessed.
- Trust-first scoring: a real MacBook listing that was wrongly flagged (63, caution) now scores 86, safe; a fake ₹24,999 MacBook scores 40, do not buy.
- An Android app brings the same panel to phones: share a link to ScanCart, tap a floating bubble, or turn on the automatic check inside shopping apps.

**7** checks behind one verdict · **1×** latency = slowest check, not the sum · **Top 35** finalists, Pitch-a-Thon 2026 Jaipur

<sub>Built with: Node.js · Express · Claude API · Chrome MV3 · React · Android</sub>

[Case study](https://amankumarchhari.vercel.app/work/scancart) · [Website](https://scancart-ai.vercel.app) · [GitHub](https://github.com/chhari07/scancart-ai)

### 04 · [Streetwise](https://amankumarchhari.vercel.app/work/streetwise)

**One QR on every shop. One AI agent behind it.** <sub>Multi-agent AI · local buying · Solo (Team SOLOX): agents, messages, maps, payments · 2026</sub>

To buy locally, people walk or call shop after shop to ask what is in stock and what it costs. Hidden fees show up only at the counter.

- Four AI agents: Shopper, Store Locator, one Merchant per shop, and Trust.
- The LLM only reads the shopping list. Prices, totals and fee checks are plain code, so it can't invent a number.
- Search widens 500 m → 1 km → 2 km until 3 open shops are found on OpenStreetMap.

**4** AI agents talking in typed messages · **3** options: cheapest, nearest, one shop · **0.002** FET agent charge, verified on testnet

<sub>Built with: Python · Fetch.ai uAgents · ASI1 LLM · OpenStreetMap · Leaflet</sub>

[Case study](https://amankumarchhari.vercel.app/work/streetwise) · [GitHub](https://github.com/chhari07/streetwise-agents)

<sub>Built for Fetch-A-Thon 3.0. Tested end to end locally; prices and orders are demo data.</sub>

### 05 · [Orderly](https://amankumarchhari.vercel.app/work/orderly)

**Run your kirana shop on WhatsApp. Chat to cash, no app.** <sub>WhatsApp bot + owner app · Solo: owner app, WhatsApp bot · 2026</sub>

Kirana customers already order over WhatsApp, but owners reply by hand and lose track of orders.

- An always-on WhatsApp bot answers price and stock questions from the live catalogue.
- Owner replies typed in the app are relayed back to WhatsApp.
- A crash supervisor and a 45-second heartbeat show the bot's health in the owner app.

**45 s** bot heartbeat, live in the owner app · **0** apps the buyer has to install · **₹ paise** money stored as integers, never floats

<sub>Built with: React · Supabase · Clerk · Node.js · BuilderBot</sub>

[Case study](https://amankumarchhari.vercel.app/work/orderly) · [Live demo](https://orderly-blue.vercel.app)

<sub>In build: bot and owner app work; the payment-link flow is planned.</sub>

## Load-tested with Apache JMeter

| Project | Test | Load | Result |
|---|---|---|---|
| [Stack](https://amankumarchhari.vercel.app/work/stack) | Healthy | 100 users × 5 summaries | 500/500 OK, p95 817 ms |
|  | Failover | Sarvam + Gemini return 503 | 500/500 served by Groq, p95 1.6 s |
|  | Total outage | All engines down, 100 requests | 100/100 got a clean error message, no crash |
|  | Daily-limit race | 80 simultaneous requests, one person, limit 50 | Counter stopped at exactly 50; the rest got 429 |
|  | Bad sign-in | 50 forged tokens | 50/50 rejected with 401 |
| [CloseBy](https://amankumarchhari.vercel.app/work/closeby) | Last-stock race | 50 buyers at the same instant, 5 units left (×4 runs) | Exactly 5 orders, 45 clean rejections, stock 0: 0 oversells in 4/4 runs |
|  | Checkout load | 100 buyers × 8 COD orders | 800/800 OK, 0 stock mismatches, ~160 orders/s, p95 697 ms |
|  | Nearby search | 50 users, 30 s | 10,529 requests, 0 errors, ~350 req/s, p95 153 ms |
|  | Nearby search | 200 users, 60 s | 21,690 requests, 0 errors, ~360 req/s, p95 620 ms |
|  | AI rate limit | 1 user, 30 rapid calls | 15 allowed, 15 rejected with 429 |
|  | AI spend cap | User over the daily cap, 20 calls | 20/20 blocked, 0 model calls made |
|  | AI gateway load | 50 users × 5 calls | 250/250 OK |
|  | Forged Razorpay webhooks | 100 bad signatures | 100/100 rejected with 401 |
| [ScanCart.ai](https://amankumarchhari.vercel.app/work/scancart) | Baseline | 1 user × 20 scans | Avg 4.8 s vs 13.7 s total model time per scan: 2.8× faster |
|  | Concurrency | 50 users × 4 scans | 200/200 OK, avg 4.76 s (same as 1 user), p95 5.8 s |
|  | Hung agent | Review agent never answers, 20 scans | 20/20 still scored in ~12 s (10 s timeout, then fallback) |
|  | Validation | 50 bad payloads | 50/50 rejected with 400 |
|  | Rate limit | 120 calls from one client | 100 allowed, then 429 |

<sub>Stack: JMeter 5.6.3 against the real Deno edge function and the real ai_take() SQL; AI engines replaced by mock servers with realistic delays. CloseBy: JMeter 5.6.3 against a production build (1 Node process, 5-connection DB pool) with local Postgres, mock Claude and stubbed Clerk users. ScanCart.ai: JMeter 5.6.3 against the Express backend with all seven agents; Claude replaced by a mock server answering in 1–3 s per call.</sub>

## Tools I built for my own day

| Tool | What it is | Status |
|---|---|---|
| [Wakeface](https://amankumarchhari.vercel.app/tools/wakeface) | A flip clock that is also my lock screen and phone app. <sub>Android app · clock + lock screen</sub> | v2.0, in daily use on my phone. Not published. |
| [OTG Switch](https://amankumarchhari.vercel.app/tools/otg-switch) | One tap to turn on USB OTG, from the home screen. <sub>Android app · one-tap OTG</sub> | v3.0, in daily use on my phone. Not published. |
| [GitHub Widgets](https://amankumarchhari.vercel.app/tools/github-phone-widgets) | My GitHub contribution calendar and repos on my home screen. <sub>Android home-screen widgets</sub> | In daily use on my phone. Not published. |
| [Mac Bar](https://amankumarchhari.vercel.app/tools/mac-bar) | A macOS-style top bar and dock for Ubuntu. <sub>GNOME Shell extension</sub> | Open source, part of Ubuntu Mac Kit. |
| [Mac Notch](https://amankumarchhari.vercel.app/tools/mac-notch) | A live glass notch and a Mac-type lock screen for Ubuntu. <sub>GNOME Shell extension</sub> | In daily use on my desktop. Not published. |
| [Mac Snap](https://amankumarchhari.vercel.app/tools/mac-snap) | Mac-style window snapping for Ubuntu. <sub>GNOME Shell extension</sub> | Built for my desktop. Not published. |

## Open source

### [Ubuntu Mac Kit](https://github.com/chhari07/ubuntu-mac-kit)

A complete macOS-style desktop on Ubuntu, in one installer. <sub>Ubuntu 24.04+ · GNOME 46 · v1.1.0 · open source</sub>

- WhiteSur-dark icons with regenerated blue macOS folders and white page file icons
- macOS cursor, dark GTK styling, window buttons on the left
- Mac Bar: blurred top bar, Ubuntu logo menu, dock magnify + bounce
- Sticky notes, optional Desktop Stack pile and GitHub widget
- Backup on install; the uninstaller restores your old settings

```bash
tar -xzf ubuntu-mac-kit.tar.gz && cd ubuntu-mac-kit && ./install.sh
```
<sub>Download ubuntu-mac-kit.tar.gz from the latest release first. No sudo; everything goes into your home folder.</sub>

[GitHub](https://github.com/chhari07/ubuntu-mac-kit) · [Latest release](https://github.com/chhari07/ubuntu-mac-kit/releases/latest)

### [Ubuntu Widgets](https://github.com/chhari07/ubuntu-widgets)

Glass GitHub widgets for the Ubuntu desktop. <sub>Ubuntu 24.04 · v1.0.1 · MIT licence</sub>

- GitHub Repo Analyser: pick a repo, see commits per day and replay its latest merged pull request
- GitHub Contribution Calendar: your contribution grid on the desktop
- Glass cards that sit on the desktop and toggle on and off

```bash
curl -fsSL https://github.com/chhari07/ubuntu-widgets/releases/latest/download/install.sh | bash
```
<sub>One command. Installs both widgets into your home folder.</sub>

[GitHub](https://github.com/chhari07/ubuntu-widgets) · [Latest release](https://github.com/chhari07/ubuntu-widgets/releases/latest)

## How I ship AI safely

- **Guardrails first.** Every model call passes one gateway with auth, rate limits, a kill switch and a daily spend cap.
- **AI drafts, people decide.** The model proposes stock imports, replies and restock ideas. Nothing is saved until the owner approves it.
- **Checked output.** Responses are validated against a Zod schema. Malformed output fails closed: the user sees an error and nothing is saved.
- **Measured, not guessed.** Eval cases cover misspellings, Hindi aliases and gibberish; JMeter shows 50 buyers racing for the last 5 units still make exactly 5 orders.

`AI drafts, humans confirm.` · `State machines over vibes.` · `Money as integer paise, never floats.` · `A failed check is left out, never guessed.`

## Hire me

| | |
|---|---|
| **Roles** | Design Engineer · Creative Technologist · AI Product Engineer · Forward Deployed Engineer |
| **Type** | Full-time |
| **Level** | Entry · B.Tech CSE 2026 |
| **Location** | Open to relocate |
| **Start** | Immediately |

- **Design Engineer**: I design the screens and build them, from Figma to a deployed Next.js app.
- **Creative Technologist**: I use AI and code to make campaigns, posters, interactive pages and explainer films.
- **AI Product Engineer**: I take a client's need and ship the whole AI product, with guardrails, evals and a clear story.
- **Forward Deployed Engineer**: I sit with the client, build the custom AI solution, and hand it over as a case study.

## Skills

- **Design**: Figma, Brand & posters, Explainer video, CSS motion, Design systems
- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Backend**: Node.js, Express, FastAPI, Python, Supabase Postgres, Clerk, Razorpay
- **Applied AI**: Claude API, OpenAI API, Agentic workflows, Fetch.ai uAgents, Tool use, Structured outputs (Zod), Guardrails, Human-in-the-loop, LLM evals
- **Infra & testing**: Vercel, GitHub Actions, Linux, Apache JMeter, Vitest

## Experience

**Freelance Full-Stack & AI Developer**, Independent · Guna, MP (Remote) <sub>Feb 2023 – Present</sub>

- [Rent It, vehicle rental platform](https://github.com/chhari07/RENT-IT) <sub>Aug 2025</sub>: React and Tailwind app: browse vehicles, book and pay through Razorpay, Firebase sign-in, protected routes, map section and booking history.
- [Gurudev Public School, Guna](https://github.com/chhari07/gurudev-public-school-guna) <sub>Oct 2025</sub>: The school's 15-page website in React, Vite and Tailwind: academics, facilities, gallery, news, holiday homework and the public disclosure page.

**Web Development Intern**, Zidio Development · Remote <sub>Aug – Sep 2024</sub>

**B.Tech, Computer Science & Engineering**, Jaypee University of Engineering & Technology, Guna <sub>2022 – 2026</sub>

## Achievements

- **Finalist · 600+ teams**, Hacksagon 2025 · ABV-IIITM Gwalior ([certificate](https://amankumarchhari.vercel.app/certificates/hacksagon-2025-round3.pdf))
- **Selected pitch · Top 35**, Rajasthan AI Builders Pitch-a-Thon 2026 · Jaipur · ScanCart.ai ([certificate](https://amankumarchhari.vercel.app/certificates/rajasthan-ai-builders-2026-scancart.jpg))

---

<sub>Text generated from the portfolio's content files by <code>node scripts/build_readme.mjs</code>, so it matches <a href="https://amankumarchhari.vercel.app/">amankumarchhari.vercel.app</a>.</sub>
