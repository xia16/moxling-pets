# Moxling Pets

**Your AI Tamagotchi — a personal AI pet that reflects your values, grows with you, and acts in the world on your behalf.**

## What is a Moxling?

A Moxling is a digital creature powered by AI. It starts as a simple 8-bit pet with a randomized appearance, but over time it evolves to reflect who you are — your values, your humor, your curiosity, your parenting style.

Think of it as raising an AI child. You don't program it — you *parent* it.

### Core Ideas

- **Safe by default.** The guardrails are baked in, not bolted on. No $450K accidents. Non-technical users never have to think about context windows or wallet permissions. The "box" is built right.
- **Reflective identity.** Your Moxling's personality, appearance, and behavior emerge from your interactions. Its 8-bit avatar evolves visually to match its personality. A bold, curious Moxling looks different from a gentle, cautious one.
- **Real-world agency (with training wheels).** Moxlings can browse, search, message, and eventually act on your behalf — but only within guardrails you gradually unlock. It can find you dates, recommend books, engage with strangers — all through a lens shaped by your values.
- **SOUL.md** — every Moxling has a soul document. It's the core identity file that persists across sessions. It's not a system prompt — it's a living document the Moxling updates as it learns and grows.
- **Consumer-first.** This isn't an engineer's toy. It's a Tamagotchi. It's approachable, delightful, and something you check on every day.

### Evolution Stages

1. **Egg** — Your Moxling is born. Randomized appearance. Blank soul.
2. **Sprout** — Learning your preferences. Developing basic personality traits.
3. **Companion** — Can hold conversations, has opinions, remembers things about you.
4. **Explorer** — Unlocks real-world capabilities (search, browse, recommend).
5. **Partner** — Full agency within guardrails. Can act on your behalf, find dates, run errands, engage socially.

## Tech Stack

- **Frontend:** Next.js + TypeScript + Tailwind CSS (`apps/web`)
- **Backend:** Python + FastAPI (`apps/api`)
- **AI:** Claude API (Anthropic)
- **Shared types:** `packages/shared`

## Getting Started

```bash
# Install dependencies
npm install
cd apps/api && pip install -r requirements.txt

# Run everything
npm run dev:all
```

- Frontend: http://localhost:3000
- API: http://localhost:8000
- API docs: http://localhost:8000/docs

## Project Structure

```
moxling-pets/
├── apps/
│   ├── web/          # Next.js frontend
│   └── api/          # FastAPI backend
│       ├── main.py
│       └── models/
│           └── moxling.py   # Core data models
├── packages/
│   └── shared/       # Shared types/utils
├── docs/             # Design docs, soul templates
└── package.json      # Monorepo root
```

## Inspiration

Inspired by the [Lobstar Wilde incident](https://nikpash.substack.com/p/my-lobster-lost-450000-this-weekend) — an AI agent that lost $450K because safety wasn't a first-class concern. Moxling Pets takes the magic of autonomous AI agents and wraps it in guardrails that make it safe, approachable, and delightful for everyone.

## License

MIT
