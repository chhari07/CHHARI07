<h1 align="center">Aman Kumar Chhari</h1>

<p align="center">
  <b>Full-Stack &amp; Applied AI Engineer</b> &nbsp;·&nbsp; Guna, MP &nbsp;·&nbsp; B.Tech CSE 2026
</p>

<p align="center">
  <i>AI that drafts. Humans confirm.</i>
</p>

<p align="center">
  <a href="https://amankumarchhari.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-0c0c0e?style=for-the-badge&logo=vercel&logoColor=10b981&labelColor=0c0c0e"/></a>
  <a href="https://www.linkedin.com/in/aman-chhari-9613bb235"><img src="https://img.shields.io/badge/LinkedIn-0c0c0e?style=for-the-badge&logo=linkedin&logoColor=10b981&labelColor=0c0c0e"/></a>
  <a href="mailto:amankumarchhari@gmail.com"><img src="https://img.shields.io/badge/Email-0c0c0e?style=for-the-badge&logo=gmail&logoColor=10b981&labelColor=0c0c0e"/></a>
</p>

---

I build systems where an LLM does the judgment and deterministic code does everything that touches money, stock or state. Every AI call in my products runs through one gateway: kill switch, daily spend cap, input sanitisation, tool loop, then a human confirmation step before anything is written.

My three main projects target the same problem space — kirana retail in tier-2 India, WhatsApp as the interface, Hinglish as the input. The hard part was never the model call. It was making the thing survive real use.

**Open to** Full-Stack / Applied AI / Founding Engineer roles — Gurgaon, Bengaluru or remote. Available now.

---

## Featured Projects

### CloseBy — AI-assisted local marketplace
Buyers order from real neighbourhood shops; owners manage stock and orders from a dashboard with agentic tools that cut the manual work — stock imports from shelf photos and voice lists, restock suggestions, order triage.

- Every AI output is a **draft the owner approves** before it is saved. Nothing writes to catalogue or price autonomously.
- **27 eval cases** covering Hinglish input, unit-less quantities and unmatched brand names — accuracy measured, failures published.
- Structured output with schema validation and prompt-injection guarding at the gateway.
- Razorpay flow holds stock until payment is confirmed, auto-refunds on rejected orders.
- Seven-state order machine, geohash proximity search — both deterministic, no agent involved.

`Next.js 15` `TypeScript` `Supabase Postgres` `Clerk` `Claude API` `Razorpay`

[Repository](https://github.com/chhari07/closeby)

---

### ScanCart.ai — counterfeit and fake-review detection for Indian e-commerce
Chrome extension that runs specialist LLM agents over a live product listing — review forensics, rating patterns, seller verification, price anomaly, quality scoring, alternatives and compliance — fused into one weighted Trust Score.

- Parallel fan-out keeps total latency close to the slowest agent rather than the sum.
- A failed agent is **excluded from the score, never guessed**; the verdict degrades and flags reduced confidence.
- Pitched at the Rajasthan AI Builders Pitch-a-Thon, Jaipur.

`JavaScript` `Node.js` `Express` `Claude API` `Chrome MV3` `React`

[Live demo](https://scancartdemo.netlify.app) · [Repository](https://github.com/chhari07/scancart.ai)

---

### Orderly — WhatsApp ordering for kirana shops
An owner app plus an always-on WhatsApp bot that answers price and stock questions from the shop's live catalogue. No app install for the buyer.

- Natural-language order parsing from mixed Hindi-English messages into a structured, priced cart.
- Confirmation card sent back before any charge — the agent never commits money.
- State-machine order flow; owner replies relayed through the bot.
- Crash supervisor with automatic reconnect on the WhatsApp session.

`React` `Supabase` `Clerk` `Node.js` `BuilderBot`

---

## How I Build

- **Agent where judgment is needed, code everywhere else.** Open-vocabulary parsing and unstructured extraction get an LLM. Proximity search, state transitions and money handling stay deterministic.
- **Evals before polish.** A number with a stated method beats a demo that only shows the happy path.
- **Failure modes are part of the design.** Timeouts, ambiguous input and duplicate webhooks each have a defined behaviour.
- **Integer paise, idempotent webhooks, frozen line items.** Non-negotiable anywhere payments are involved.

---

## Stack

**Frontend** React · Next.js (App Router) · TypeScript · Tailwind CSS · Framer Motion

**Backend & AI** Node.js · Express · Python · Claude API / Anthropic SDK · LangGraph · tool use & function calling · LLM evals · Zod · RAG

**Data & Infra** PostgreSQL (Supabase) · MongoDB · Firebase · Clerk · Razorpay · Vercel · GitHub Actions

---

<div align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=chhari07&show_icons=true&hide_border=true&bg_color=0c0c0e&title_color=10b981&icon_color=10b981&text_color=c9d1d9" />
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=chhari07&layout=compact&hide_border=true&bg_color=0c0c0e&title_color=10b981&text_color=c9d1d9&langs_count=8" />
</div>

---

<p align="center">
  <a href="mailto:amankumarchhari@gmail.com"><b>amankumarchhari@gmail.com</b></a>
</p>
