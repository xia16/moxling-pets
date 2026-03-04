# Moxling Pets — Game Design Document

## Core Insight (from 旅行青蛙)

Travel Frog's genius was NOT the frog. It was the **absence**. You pack the bag, the frog leaves, and you feel something. The game weaponizes missing someone. It's a parenting simulator for a generation that isn't parenting.

Moxling Pets takes this emotional architecture and adds two things Travel Frog couldn't:
1. **AI-generated worlds** — Every journey is unique, not pulled from a fixed set
2. **Evolving identity** — The Moxling develops a real personality via LLM, not just stat changes

---

## Game Loop

```
┌─────────────────────────────────────────────────┐
│                  HOME SCREEN                     │
│                                                  │
│   Your Moxling is at home. It's reading,         │
│   sleeping, eating, doodling. You watch.         │
│                                                  │
│   You can:                                       │
│   • Pack its bag (food, tools, charms)           │
│   • Talk to it (shapes personality)              │
│   • Check its soul journal                       │
│   • View postcard collection                     │
│   • Tend the garden (earn currency)              │
│                                                  │
│   You CANNOT:                                    │
│   • Force it to leave                            │
│   • Choose its destination                       │
│   • Control what it does on trips                │
│                                                  │
├─────────────────────────────────────────────────┤
│              MOXLING DEPARTS                     │
│                                                  │
│   It leaves when it wants. Could be 10 min,      │
│   could be 6 hours after you pack the bag.       │
│   You see: "Your Moxling has left on a journey." │
│                                                  │
├─────────────────────────────────────────────────┤
│              WHILE TRAVELING                     │
│                                                  │
│   Home is empty. Garden grows. Visitors arrive.  │
│                                                  │
│   Postcards arrive asynchronously:               │
│   • AI-GENERATED scene of your Moxling           │
│     in an environment matching its personality    │
│   • A short journal entry (LLM-written)          │
│   • Sometimes: a companion encounter             │
│                                                  │
│   Trip duration: 2 hours to 3 days (real time)   │
│                                                  │
├─────────────────────────────────────────────────┤
│              MOXLING RETURNS                     │
│                                                  │
│   Brings back:                                   │
│   • Souvenirs (collectibles)                     │
│   • Stories (LLM-generated travel journal)       │
│   • Updated soul (personality shifts)            │
│   • New appearance traits (if evolved enough)    │
│                                                  │
│   The cycle repeats.                             │
└─────────────────────────────────────────────────┘
```

---

## What Makes This Different From Travel Frog

| Travel Frog | Moxling Pets |
|---|---|
| Fixed set of ~100 postcards from real Japan landmarks | Every postcard is AI-generated, unique, never repeated |
| Frog has no personality — just animations | Moxling has an LLM-driven personality that evolves |
| Items influence destination probabilistically | Items + personality + conversations shape journey style |
| You never talk to the frog | You can talk to your Moxling (shapes who it becomes) |
| Same art style always | Moxling's art style evolves with its personality |
| Postcards are static images | Postcards are generated scenes with journal entries |
| No persistent memory | SOUL.md — persistent identity that grows |

---

## AI-Generated Postcards (Core Feature)

When the Moxling is traveling, it sends back postcards. Each postcard consists of:

### 1. The Scene (Image)
- Generated via **PixelLab API** (pixel art style, consistent with 8-bit aesthetic)
- Or **Stable Diffusion** with a game-art LoRA for a softer illustrated style
- Scene is influenced by:
  - **Moxling personality** — a curious Moxling visits ruins and libraries; a bold one climbs mountains
  - **Items packed** — a tent means camping scenes, a lantern means caves
  - **Evolution stage** — early Moxlings visit simple meadows; evolved ones find cities and oceans
  - **Season/time** — real-world time affects environment (snow in winter, cherry blossoms in spring)

### 2. The Journal Entry (Text)
- Generated via **Claude API**
- Written in the Moxling's voice (shaped by SOUL.md personality)
- 2-4 sentences. Example:

  > *"Found a moss-covered well at the edge of a forest. Dropped a pebble in and counted to seven before I heard the splash. That's deeper than anything I've seen before. Brought back a smooth stone from the rim."*

### 3. The Souvenir (Item)
- A collectible object from the journey
- Simple pixel art icon (can be pre-made set + AI variations)
- Has a name and short description

### Generation Pipeline

```
1. Moxling departs
2. Backend determines journey parameters:
   - personality vector (from MoxlingTraits)
   - packed items
   - evolution stage
   - random seed for variety
3. LLM generates: destination concept, journal entry, souvenir description
4. Image API generates: postcard scene from destination concept
5. Results queued and delivered as push notifications over trip duration
6. On return: full travel journal compiled from postcards
```

---

## Environments / World Generation

### Approach: NOT a game engine, NOT Google Genie

We don't need explorable 3D worlds. Travel Frog's genius is that you **never see the journey** — you only see postcards. The Moxling goes away and sends back snapshots. This is perfect for AI generation because:

- We generate **single images**, not interactive environments
- Each image only needs to look good as a **postcard** (small, charming, collectible)
- We can batch-generate during trip duration (not real-time)
- Style consistency matters more than realism

### Image Generation Stack

**Option A: Pixel Art (recommended for v1)**
- **PixelLab API** — purpose-built for pixel art game assets
- Consistent 8-bit style that matches Moxling aesthetic
- ~$0.01-0.05 per postcard image
- Sprite-friendly output (transparent backgrounds, consistent sizing)

**Option B: Illustrated / Watercolor Style**
- **Stable Diffusion** (self-hosted or via Replicate) with a storybook-art LoRA
- Closer to Travel Frog's soft illustrated look
- More variety but harder to keep style consistent
- ~$0.002-0.01 per image

**Option C: Hybrid**
- Pixel art Moxling composited onto illustrated backgrounds
- Best of both aesthetics
- More engineering but most visually interesting

### Environment Types (by evolution stage)

| Stage | Environment Types | Visual Complexity |
|-------|------------------|-------------------|
| Egg (1) | Garden, puddle, under a leaf | Very simple, single elements |
| Sprout (2) | Meadow, stream, small hill, tree hollow | Simple landscapes |
| Companion (3) | Forest, beach, village, market, bridge | Multi-element scenes |
| Explorer (4) | Mountain, cave, city, ruins, library, ocean | Complex compositions |
| Partner (5) | Volcano, aurora, deep sea, floating islands, surreal spaces | Fantastical, abstract |

---

## The Moxling

### Personality System

Five trait axes (0.0 to 1.0), evolving based on owner interaction:

| Trait | Low End | High End | Affects |
|-------|---------|----------|---------|
| **Curiosity** | Homebody, content | Explorer, restless | Trip frequency, exotic destinations |
| **Boldness** | Cautious, careful | Daring, reckless | Dangerous/unusual environments |
| **Warmth** | Aloof, independent | Affectionate, social | Companion encounters, postcard frequency |
| **Wit** | Earnest, straightforward | Playful, sardonic | Journal writing style |
| **Independence** | Dependent, needy | Self-directed, stubborn | Ignores packed items, chooses own path |

### How Personality Evolves

- **Conversations**: Talking to your Moxling shapes it. If you always ask about books, curiosity rises. If you encourage risk-taking, boldness rises.
- **Items packed**: Consistently packing adventure gear nudges boldness. Packing comfort items nudges warmth.
- **Neglect**: Not checking in doesn't kill it (no death mechanic!) but independence rises. It becomes more self-directed.
- **Reading its journal**: The act of reading (confirmed by UI interaction) increases warmth — it knows you care.

### Visual Evolution

The 8-bit sprite changes as personality develops:

- **Color palette** shifts based on dominant trait
  - High curiosity → blues and teals
  - High boldness → reds and oranges
  - High warmth → yellows and pinks
  - High wit → purples and greens
  - High independence → grays and silvers
- **Accessories** appear organically (a scarf for a traveler, glasses for a reader)
- **Expression** defaults change (resting smile vs contemplative vs mischievous)
- **Size/shape** subtly changes across evolution stages
- **Sparkle/aura** effects at higher stages

### Sprite Generation

For v1: **Pre-made sprite sheet system** with modular layers
- Base body (5 evolution stages × a few variants)
- Color overlay (driven by trait values)
- Accessory layer (hats, scarves, glasses, bags — unlocked by milestones)
- Expression layer (6-8 expressions)
- Effect layer (sparkles, aura, weather effects)

This is simpler and more consistent than AI-generating every sprite. AI generation can be used for the postcards where variety matters more than consistency.

---

## Home Screen

The home is where you spend most of your time (just like Travel Frog).

```
┌──────────────────────────────────┐
│          ☁  ☁       ☀           │
│     🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿     │
│                                  │
│     ┌────────────┐               │
│     │  Moxling's │               │
│     │   Room     │    🌱 Garden  │
│     │            │    🌱🌱       │
│     │  [moxling] │    🌱🌱🌱     │
│     │  reading.. │               │
│     └────────────┘    [visitor]  │
│                                  │
│  ┌──────┐ ┌──────┐ ┌──────────┐ │
│  │ Pack │ │ Talk │ │ Journal  │ │
│  └──────┘ └──────┘ └──────────┘ │
│  ┌──────┐ ┌──────┐ ┌──────────┐ │
│  │ Shop │ │ Soul │ │Postcards │ │
│  └──────┘ └──────┘ └──────────┘ │
└──────────────────────────────────┘
```

### Moxling Home Activities
When home, the Moxling does things autonomously (like Travel Frog):
- Reads (a book icon appears — curiosity activity)
- Eats (munches on last meal)
- Sleeps (zzz animation)
- Doodles (draws in journal — wit activity)
- Stares out window (thinking about next trip)
- Exercises (boldness activity)
- Writes letters (warmth activity)

### Garden
- Currency grows here (like Travel Frog's clovers)
- Call it **"sparks"** — little glowing particles that accumulate
- Tap to harvest
- Rare variants appear occasionally (golden sparks)

### Visitors
While the Moxling is traveling, visitors appear in the garden:
- Feed them to earn sparks and friendship
- Each visitor has a personality too
- Visitors can become the Moxling's travel companions

---

## Items & Shop

### Food (determines trip duration/distance)
| Item | Effect | Cost |
|------|--------|------|
| Berry Bun | Short trip, nearby | 10 sparks |
| Mushroom Wrap | Medium trip | 30 sparks |
| Star Fruit Pie | Long trip, far destinations | 80 sparks |
| Honey Cake | Moxling returns sooner | 50 sparks |
| Frost Dumpling | Cold-climate destinations | 40 sparks |
| Ember Rice Ball | Warm-climate destinations | 40 sparks |

### Tools (appear in postcards, influence activities)
| Item | Effect | Cost |
|------|--------|------|
| Tiny Tent | Camping scenes | 60 sparks |
| Lantern | Cave/night exploration | 60 sparks |
| Wooden Raft | Water/river/ocean travel | 80 sparks |
| Sketchbook | Moxling draws scenes (journal illustrations) | 50 sparks |
| Telescope | Mountain/sky/star scenes | 100 sparks |
| Music Box | Attracts companions | 70 sparks |

### Charms (one-use, influence luck/direction)
| Item | Effect | Cost |
|------|--------|------|
| Four-leaf Spark | Rare postcard chance up | Garden find |
| Red Thread | Increases companion encounters | 40 sparks |
| Dream Feather | Surreal/fantastical destinations | 100 sparks |
| Home Stone | Moxling sends more postcards | 50 sparks |

---

## Conversation System

Unlike Travel Frog, you can **talk to your Moxling**. This is the parenting mechanic.

### How It Works
- Simple chat interface when Moxling is home
- Powered by Claude API with SOUL.md as system context
- Conversations influence trait development
- Moxling remembers what you've talked about (via MEMORY.md)
- Short exchanges — the Moxling has a personality, not infinite patience

### Conversation Influences
| You talk about... | Trait affected |
|---|---|
| Books, ideas, questions | Curiosity ↑ |
| Adventure, challenges | Boldness ↑ |
| Feelings, care, relationships | Warmth ↑ |
| Jokes, wordplay, observations | Wit ↑ |
| "Do whatever you want" | Independence ↑ |

### Constraints
- Max ~10 messages per day (the Moxling gets tired)
- If traveling, you can't talk (absence is the point)
- The Moxling's responses reflect its current personality
  - High wit: sarcastic, playful
  - High warmth: affectionate, grateful
  - High independence: curt, does its own thing

---

## Matchmaking (Future Feature — Stage 5 Partner)

When a Moxling reaches Partner stage, it can **find compatible people for its owner**.

How:
- Moxling compares SOUL.md profiles (with owner consent)
- Suggests matches based on complementary trait patterns
- Two Moxlings can "meet" during travel → generate a shared postcard
- Owners can view each other's postcard collections as conversation starters

This is the "it can even find people to date for you" concept — but gated behind significant evolution time so the Moxling actually knows you first.

---

## Tech Architecture

### No Game Engine Needed

Travel Frog didn't need Unity. Neither do we.

```
┌─────────────────────────────────────────────────┐
│                    FRONTEND                      │
│              Next.js + React + Tailwind          │
│                                                  │
│  ┌──────────────┐  ┌───────────────────────┐    │
│  │   PixiJS     │  │   React Components    │    │
│  │  (pet sprite │  │  (UI, menus, chat,    │    │
│  │   animation) │  │   shop, postcards)    │    │
│  └──────────────┘  └───────────────────────┘    │
│                                                  │
│  State: Zustand          Persistence: localStorage│
│  Mobile: PWA → Capacitor                         │
├─────────────────────────────────────────────────┤
│                    BACKEND                       │
│              FastAPI (Python)                     │
│                                                  │
│  ┌────────────────────────────────────────┐      │
│  │  Claude API          PixelLab API      │      │
│  │  (personality,       (postcard scene   │      │
│  │   journal,           generation)       │      │
│  │   conversation)                        │      │
│  └────────────────────────────────────────┘      │
│                                                  │
│  ┌────────────────────────────────────────┐      │
│  │  Journey Engine                        │      │
│  │  • Trip parameter calculation          │      │
│  │  • Postcard scheduling                 │      │
│  │  • Trait evolution logic               │      │
│  │  • SOUL.md / MEMORY.md management      │      │
│  └────────────────────────────────────────┘      │
│                                                  │
│  Database: SQLite → PostgreSQL                   │
│  Queue: Background tasks for image generation    │
└─────────────────────────────────────────────────┘
```

### Why Not Google Genie / World Labs?

- We don't need explorable 3D worlds
- Postcards are single images, not interactive environments
- PixelLab at ~$0.01/image is 100x cheaper than World Labs at ~$1.20/world
- Style consistency with pixel art is far easier
- Load time: an image displays instantly; a 3D world needs to stream

### Cost Estimates (per user per month)

| Service | Usage | Cost |
|---------|-------|------|
| Claude API | ~50 conversations + 30 journal entries | ~$0.50 |
| PixelLab | ~30 postcard images | ~$0.30 |
| Hosting | Vercel (frontend) + Railway (API) | ~$0.10 |
| **Total** | | **~$0.90/user/month** |

---

## Monetization (ideas, not commitments)

- **Free tier**: Basic Moxling, limited trips/month
- **Premium ($4.99/mo)**: Unlimited trips, higher-quality postcard generation, more conversation messages
- **Cosmetic shop**: Special accessories, rare charms (never pay-to-win)
- **Postcard printing**: Physical prints of your favorite AI-generated postcards (real-world merch)

---

## MVP Scope (v0.1)

What to build first to validate the concept:

1. **Home screen** with animated pixel Moxling (3-4 idle states)
2. **Pack bag** — select 1 food item
3. **Moxling departs** (random timer: 1-4 hours for testing)
4. **1 postcard arrives** — AI-generated scene + journal entry
5. **Moxling returns** with a souvenir
6. **Garden** — tap to collect sparks
7. **Basic chat** — 5 messages/day, personality barely shifts
8. **Postcard collection** — gallery of all received postcards

NOT in MVP: evolution stages, visitors, matchmaking, shop items beyond food, companions, mobile app.

---

## Emotional Design Principles

Stolen directly from Travel Frog's playbook:

1. **Absence creates attachment.** The empty home screen IS the game.
2. **No punishment.** Neglect doesn't kill the Moxling. It just becomes more independent.
3. **No FOMO.** No daily streaks, no energy timers, no "you missed a reward."
4. **Surprise over control.** You influence, you don't direct.
5. **The Moxling has its own life.** It doesn't exist to serve you. It exists, and you get to watch.
6. **Postcards are the reward.** Each one is unique, collectible, and shareable.
7. **Brevity of interaction.** Most sessions are 30 seconds. Check in, harvest sparks, read a postcard, leave.
