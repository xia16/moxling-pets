# Moxling Pets — Game Design Document

## What This Actually Is

**Moxling Pets is not a game. It's a behavioral mirror disguised as a child-raising simulator.**

Your Moxling is an AI creature that grows up. It gets scared. It lies. It asks for things it doesn't need. It gets bullied. It makes friends. It wastes money. It has tantrums. It falls in love with bad ideas. It comes to you with problems and watches what you do.

The way you respond — across hundreds of micro-decisions over weeks and months — builds a behavioral profile that reveals who you actually are as a caregiver, decision-maker, and human being. Not who you say you are. Who you are when a small thing is crying at 2am and you're tired.

This profile powers everything downstream:
- **Matchmaking**: Compare demonstrated behavior, not dating profiles
- **Self-awareness**: "Here's how you actually handle conflict vs how you think you do"
- **Parenting readiness**: Not a test — a mirror
- **Compatibility**: Do your caregiving styles complement or clash?

---

## The Sims, Not Travel Frog

The v1 design was too passive. Travel Frog is beautiful but the owner is a spectator. In Moxling Pets, you are a **parent**. The Moxling needs you. It presents you with situations that require real decisions. Your decisions have consequences that shape who it becomes.

### The Sims Parallel
| The Sims | Moxling Pets |
|---|---|
| You control the Sim directly | You influence the Moxling through responses and decisions |
| Needs bars (hunger, fun, social) | Emotional states driven by LLM |
| Life events are scripted/random | Life events are LLM-generated, contextual to YOUR Moxling |
| Consequences are mechanical (mood drops) | Consequences are behavioral (personality shifts, trust changes) |
| You're God | You're a parent — influence without control |

---

## Core Loop

```
┌──────────────────────────────────────────────────────┐
│                    DAILY LIFE                         │
│                                                       │
│  Your Moxling lives. It does things autonomously.     │
│  It eats, plays, reads, explores its environment.     │
│  You can watch, or not.                               │
│                                                       │
│  Periodically, SITUATIONS arise:                      │
│                                                       │
│  ┌────────────────────────────────────────────┐       │
│  │  "Another Moxling called me stupid today.  │       │
│  │   What should I do?"                       │       │
│  │                                            │       │
│  │  [Talk to me about it]                     │       │
│  │  [Stand up for yourself]                   │       │
│  │  [Ignore them]                             │       │
│  │  [I'll handle it]                          │       │
│  │  [Free response...]                        │       │
│  └────────────────────────────────────────────┘       │
│                                                       │
│  Your response is recorded. It shapes the Moxling.    │
│  It also shapes YOUR behavioral profile.              │
│                                                       │
├──────────────────────────────────────────────────────┤
│                  ENVIRONMENTS                         │
│                                                       │
│  The Moxling exists in AI-generated environments:     │
│  • Home (its room, your shared space)                 │
│  • School / playground (social situations)            │
│  • The outside world (adventures, challenges)         │
│  • Other Moxlings' spaces (social visits)             │
│                                                       │
│  Environments are simple pixel art scenes generated   │
│  by AI. They don't need to be interactive 3D worlds.  │
│  They're BACKDROPS for the situations that matter.    │
│                                                       │
├──────────────────────────────────────────────────────┤
│                  GROWTH                               │
│                                                       │
│  Over weeks/months, the Moxling develops:             │
│  • Personality (directly shaped by your responses)    │
│  • Trust level (does it come to you with problems?)   │
│  • Resilience (can it handle things on its own?)      │
│  • Social skills (how does it treat other Moxlings?)  │
│  • Values (what does it think is right/wrong?)        │
│                                                       │
│  The Moxling becomes a reflection of your parenting.  │
└──────────────────────────────────────────────────────┘
```

---

## Situation Engine (The Heart of the Product)

The LLM generates situations that test different aspects of the owner. These aren't random — they're sequenced like a developmental curriculum, escalating in complexity as the Moxling "ages."

### Situation Categories

#### 1. Emotional Regulation
The Moxling has feelings and doesn't know what to do with them.

| Situation | What It Tests |
|---|---|
| "I'm scared of the dark in my room." | Comfort vs dismiss vs problem-solve |
| "I don't want to go to school today." | Empathy vs authority vs inquiry |
| "I'm SO angry. I broke my favorite toy." | Validation vs lecture vs distraction |
| "Everyone else has [thing] and I don't." | Boundaries vs indulgence vs teaching |
| "I had a nightmare about you leaving." | Emotional availability, reassurance |

#### 2. Social Conflict
The Moxling encounters other Moxlings and has problems.

| Situation | What It Tests |
|---|---|
| "My friend took my thing and won't give it back." | Advocacy vs teach self-advocacy |
| "Nobody wanted to play with me today." | Comfort vs social coaching |
| "I said something mean and now they're crying." | Accountability vs protection |
| "A bigger Moxling keeps pushing me around." | Intervention style, teaching resilience |
| "My friend wants me to do something I don't want to." | Teaching consent and boundaries |

#### 3. Ethical Dilemmas
The Moxling faces right-vs-right or right-vs-easy choices.

| Situation | What It Tests |
|---|---|
| "I found something that isn't mine. Can I keep it?" | Honesty values |
| "My friend cheated and asked me not to tell." | Loyalty vs integrity |
| "If I lie, nobody gets in trouble." | Truth-telling under pressure |
| "The new kid is weird. Nobody likes them." | Inclusion, empathy for outsiders |
| "I can win but only if I'm unfair." | Competition ethics |

#### 4. Money & Resources
The Moxling has access to sparks (currency) and wants things.

| Situation | What It Tests |
|---|---|
| "I want to spend all my sparks on this shiny thing." | Financial boundaries |
| "Can I have more sparks? Please?" | Saying no, delayed gratification |
| "My friend doesn't have any sparks for food." | Generosity, teaching sharing |
| "I saved up for something but now I want something else." | Commitment, impulse control |
| "Someone said they'd double my sparks if I give them mine." | Scam awareness, critical thinking |

#### 5. Independence & Growth
The Moxling wants to do things on its own.

| Situation | What It Tests |
|---|---|
| "I want to go exploring alone." | Letting go vs overprotection |
| "I know you said no but I think I can handle it." | Boundaries vs trust |
| "I tried something new and I failed." | Response to failure |
| "I don't need your help anymore." | Handling rejection gracefully |
| "I made a decision you wouldn't have made." | Respecting autonomy |

#### 6. Identity & Self-Discovery
The Moxling is figuring out who it is.

| Situation | What It Tests |
|---|---|
| "I don't like the things you like." | Accepting difference |
| "Why am I different from other Moxlings?" | Handling identity questions |
| "I want to change my name/appearance." | Supporting self-expression |
| "I don't know what I'm good at." | Encouragement style |
| "I want to be like [other Moxling] instead of me." | Building self-worth |

### Situation Mechanics

- **Frequency**: 2-4 situations per day (not overwhelming — like real parenting, it's intermittent)
- **Timing**: Push notifications at varied times. Some at 2am. Some during work. Parenting doesn't have office hours.
- **Urgency levels**:
  - **Low**: Can respond anytime in next 24 hours (journal entries, questions)
  - **Medium**: Should respond within a few hours (social problems, sadness)
  - **High**: Moxling is actively distressed — response within 30 min shapes outcome significantly
- **Response types**:
  - Pre-written options (2-4 choices) for quick response
  - Free text for nuanced parenting
  - Silence (not responding IS a response — the Moxling notices)
- **Consequences**: Every response shifts the Moxling's development. No response is "wrong" — but every response reveals something about the owner.

---

## Behavioral Profile (The Real Product)

Behind the cute pixel art, the system is building a multi-dimensional profile of the owner.

### Profile Dimensions

```
PARENTING STYLE QUADRANT
                    High Control
                        │
         Authoritarian  │  Authoritative
         "Because I     │  "Let's talk about
          said so"      │   why, but the
                        │   answer is no"
   ─────────────────────┼─────────────────────
         Neglectful     │  Permissive
         "..."          │  "Sure, whatever
         (no response)  │   you want"
                        │
                    Low Control

ADDITIONAL DIMENSIONS:
┌─────────────────────────────────────────────┐
│ Emotional Availability                       │
│ ████████████████████░░░░░░  78%             │
│ (How often do you respond to emotional need) │
├─────────────────────────────────────────────┤
│ Consistency                                  │
│ ██████████████░░░░░░░░░░░░  56%             │
│ (Same situation → same response over time?)  │
├─────────────────────────────────────────────┤
│ Empathy-First vs Solution-First              │
│ ◄████████████░░░░░░░░░░░░░►                 │
│ Empathy                         Solution     │
├─────────────────────────────────────────────┤
│ Risk Tolerance                               │
│ ██████████████████░░░░░░░░  72%             │
│ (Do you let the Moxling try risky things?)   │
├─────────────────────────────────────────────┤
│ Boundary Firmness                            │
│ ████████████████░░░░░░░░░░  64%             │
│ (Do you hold the line or cave?)              │
├─────────────────────────────────────────────┤
│ Autonomy Support                             │
│ ██████████████████████░░░░  88%             │
│ (Do you let the Moxling make own choices?)   │
├─────────────────────────────────────────────┤
│ Teaching Style                               │
│ ◄██████████████████░░░░░░░►                 │
│ Show by example          Explain with words  │
├─────────────────────────────────────────────┤
│ Response to Failure                          │
│ ◄████████░░░░░░░░░░░░░░░░►                 │
│ "It's okay"              "What did we learn" │
└─────────────────────────────────────────────┘
```

### How the Profile Is Built

Every interaction is classified:

```python
# Simplified scoring logic
{
    "situation": "Moxling is scared of the dark",
    "response": "There's nothing to be scared of, go to sleep",
    "classifications": {
        "emotional_validation": 0.2,   # low — dismissed the feeling
        "solution_oriented": 0.7,      # high — tried to fix it
        "empathy": 0.3,                # low — didn't acknowledge fear
        "control": 0.6,                # moderate — directed behavior
        "availability": 0.9            # high — responded quickly
    }
}
```

Over hundreds of interactions, the profile stabilizes. Short-term noise averages out. What remains is signal.

### Profile Uses

1. **Self-reflection dashboard**: "Here's how you've parented your Moxling over the past month"
2. **Matchmaking**: Compare behavioral profiles for compatibility (not just "we both like hiking")
3. **Growth tracking**: "You've become more patient over the past 3 months"
4. **Moxling outcome**: Your Moxling's personality IS your report card — is it confident? Anxious? Kind? Aggressive? That's you.

---

## The Moxling's Development

### Age Stages (replaces evolution stages)

| Stage | Age Feel | Duration | Situations | Complexity |
|-------|----------|----------|------------|------------|
| **Newborn** | 0-1 year | Week 1-2 | Basic needs: hungry, tired, scared | Simple binary choices |
| **Toddler** | 1-3 years | Week 2-4 | Tantrums, curiosity, "no!", first words | Emotional regulation |
| **Child** | 4-8 years | Month 1-3 | School, friends, fairness, lying, sharing | Social + ethical |
| **Tween** | 9-12 years | Month 3-6 | Identity, peer pressure, independence | Complex dilemmas |
| **Teen** | 13-17 years | Month 6-12 | Big decisions, rebellion, relationships, values | High-stakes choices |
| **Young Adult** | 18+ | Month 12+ | The Moxling advises YOU. Role reversal. | Mirror mode |

The Young Adult stage is the payoff: the Moxling is now a reflection of everything you taught it. It gives you advice. It parents you back. The quality of that advice reveals what you actually instilled.

### Personality Traits (expanded)

| Trait | Shaped By | Range |
|-------|-----------|-------|
| **Confidence** | How you handled their failures and successes | Insecure ↔ Self-assured |
| **Empathy** | How you modeled care for others | Self-centered ↔ Deeply empathetic |
| **Resilience** | How you responded to their struggles | Fragile ↔ Bounces back |
| **Honesty** | How you handled truth-telling situations | Deceptive ↔ Radically honest |
| **Trust** | How consistently and warmly you responded | Guarded ↔ Open |
| **Curiosity** | How you responded to their questions and exploration | Incurious ↔ Endlessly curious |
| **Independence** | How much autonomy you allowed | Dependent ↔ Self-directed |
| **Kindness** | How you modeled treating others | Indifferent ↔ Compassionate |

### The Trust Mechanic

**Trust is the master variable.** It determines whether the Moxling comes to you at all.

- High trust → Moxling tells you things proactively. Shares fears. Asks for help.
- Low trust → Moxling hides problems. You find out after the fact. It handles things alone (sometimes badly).
- Trust is built slowly and lost quickly (like real life).
- Trust builders: consistent responses, emotional validation, keeping promises
- Trust breakers: ignoring them, inconsistency, overreacting, breaking promises

If trust drops below a threshold, the Moxling stops presenting situations. It just... lives quietly. You see it in its room but it doesn't come to you. This is the most powerful feedback the system can give. Silence.

---

## Environments (Visual Layer)

Environments are **backdrops for situations**, not explorable worlds. They set mood and context.

### Environment Types

| Environment | Used For | Visual Style |
|---|---|---|
| **Home / Bedroom** | Emotional conversations, bedtime, safety | Warm, cozy pixel art room |
| **School / Playground** | Social situations, learning, peer conflict | Bright, busy, other Moxlings visible |
| **Park / Nature** | Exploration, adventure, independence | Green, open, changing weather/seasons |
| **Town / Market** | Money decisions, strangers, real-world encounters | Bustling, colorful, shops and stalls |
| **Friend's House** | Social dynamics, different family styles | Variations on home — contrast |
| **Rainy Day / Storm** | Emotional distress, fear, comfort | Dark, moody, rain effects |
| **Festival / Celebration** | Joy, sharing, gratitude | Bright, decorative, festive |
| **Unknown Place** | New experiences, being lost, courage | Unfamiliar, slightly unsettling |

### Generation Approach

**Simple layered pixel art, NOT 3D worlds.**

```
Background layer:  AI-generated or pre-made tileset backdrop
                   (sky, walls, landscape — sets the mood)

Mid layer:         Props and context objects
                   (desk, trees, playground equipment)

Character layer:   Moxling sprite + other Moxling sprites
                   (pre-made modular sprites, not AI-generated per frame)

UI layer:          Situation text, response options, status
```

For v1, environments can be a **curated set of ~20 background scenes** (hand-drawn or AI-generated once) rather than generating new ones per situation. The SITUATIONS are what need to be unique, not the backdrops.

AI-generated environments become valuable later when Moxlings travel or visit new places — then each postcard/scene can be unique.

---

## Conversation System (Upgraded)

The chat is no longer just "talk to shape personality." It's the primary parenting interface.

### How Conversations Work

The Moxling initiates most conversations (like a real child coming to you). You can also initiate, but a child that only talks when spoken to is a sign of low trust.

**Moxling-initiated** (situations):
```
┌─────────────────────────────────────┐
│ 🐾 Moxling                         │
│                                     │
│ "I drew a picture at school today   │
│  but the teacher said it wasn't     │
│  good enough. I tried really hard." │
│                                     │
│  ┌───────────────────────────────┐  │
│  │ "I'm sure it was beautiful"   │  │
│  ├───────────────────────────────┤  │
│  │ "What did the teacher say     │  │
│  │  specifically?"               │  │
│  ├───────────────────────────────┤  │
│  │ "Not everything has to be     │  │
│  │  perfect. Did you have fun?"  │  │
│  ├───────────────────────────────┤  │
│  │ [Type your own response...]   │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

**Owner-initiated** (check-ins):
```
You: "How was your day?"
Moxling: "It was okay I guess."
         (low-trust response — guarded)

vs.

Moxling: "It was SO cool! I found a weird bug
          in the garden and I named it Gerald
          and then it flew away and I was sad
          but also happy because Gerald is free
          now. Do you think Gerald misses me?"
         (high-trust response — open, sharing)
```

### LLM Architecture for Conversations

```
System prompt:
├── SOUL.md (Moxling's current identity, personality, trust level)
├── MEMORY.md (what it remembers about past conversations)
├── Current situation context (if situation-triggered)
├── Age stage behavioral guidelines
└── Owner's behavioral profile (so the Moxling reacts to PATTERNS)

The Moxling's responses are NOT just friendly chatbot responses.
They reflect:
- Trust level (how open/guarded it is)
- Personality (shaped by past parenting)
- Current emotional state
- Memory of how the owner handled similar situations before
- Age-appropriate language and concerns
```

---

## Matchmaking System

### The Insight

Dating apps match on what people **say** they want. Moxling Pets matches on what people **do** when a small thing needs them.

### How It Works

1. **Opt-in**: Owner consents to matchmaking at any time
2. **Profile comparison**: The system compares behavioral profiles, not bios
3. **Compatibility dimensions**:
   - Complementary parenting styles (authoritative + authoritative = strong match)
   - Similar values (both high empathy, both consistent)
   - Compatible conflict styles
   - Aligned risk tolerance
4. **Moxling meeting**: Two compatible owners' Moxlings "meet" during a travel/play event
5. **Shared postcard**: An AI-generated scene of both Moxlings together
6. **Owner introduction**: If both owners agree, they can see each other's Moxling profile and journal highlights
7. **The Moxling's opinion**: Your Moxling tells you what it thinks of the match. High-trust Moxlings give honest assessments. Low-trust ones say "I don't know" or nothing.

### Why This Is Powerful

- You can't fake behavioral data collected over months
- "I'm patient and empathetic" vs "your Moxling is anxious and guarded" tells the real story
- The Moxling itself becomes a conversation starter ("What's yours like?")
- Shared Moxling postcards are inherently shareable / social

---

## Social System — Moxlings Interacting With Each Other

### The Idea

Your Moxling doesn't exist alone. It lives in a world with other people's Moxlings. And just like real children, how your Moxling behaves socially is a direct reflection of how you raised it.

A confident Moxling makes friends easily. An anxious one clings. A kind one shares. A guarded one watches from the edges. An aggressive one starts conflicts. **The playground is the product demo.**

### How Social Interactions Work

```
┌──────────────────────────────────────────────────────┐
│                   MOXLING SOCIAL                      │
│                                                       │
│  Moxlings can:                                        │
│  • Visit other Moxlings' homes                        │
│  • Play together in shared environments               │
│  • Have conflicts (bullying, exclusion, arguments)     │
│  • Form friendships (best friends, groups)             │
│  • Go on trips together (shared postcards)             │
│  • Learn from each other (trait influence)             │
│                                                       │
│  You CANNOT:                                          │
│  • Choose your Moxling's friends                      │
│  • Force interactions                                 │
│  • Control what happens in social situations           │
│                                                       │
│  You CAN:                                             │
│  • Advise your Moxling before/after social events     │
│  • Respond to social situations it brings to you       │
│  • Watch social interactions unfold (if trust is high) │
└──────────────────────────────────────────────────────┘
```

### Social Interaction Types

#### 1. Playdates
Your Moxling meets another Moxling in a shared environment. What happens depends on both Moxlings' personalities (which reflect both owners' parenting):

| Your Moxling | Other Moxling | What Happens |
|---|---|---|
| High confidence + high kindness | High confidence + high kindness | Best friends immediately. Shared adventures. |
| High confidence + low empathy | Low confidence + high trust | Your Moxling dominates. Other Moxling follows. |
| Low trust + high independence | High warmth + high curiosity | Awkward at first. Other Moxling keeps trying. |
| High curiosity + low resilience | High boldness + low kindness | Your Moxling gets peer-pressured. Comes to you upset. |

The LLM generates the scene based on both Moxlings' trait vectors. Neither owner controls the outcome.

#### 2. Conflicts
Moxlings disagree, fight, exclude, or hurt each other. Both owners get a situation notification:

```
Your Moxling: "I was playing with Spark and they said my
drawing was ugly and I shouldn't draw anymore."

(Meanwhile, Spark's owner gets:)
Spark: "I told another Moxling their drawing wasn't good.
They looked really sad. Did I do something wrong?"
```

Both owners' responses shape their respective Moxlings AND the relationship between them. If Owner A teaches empathy and Owner B teaches dismissal, the two Moxlings drift apart naturally.

#### 3. Shared Adventures
Moxlings who are friends can travel together. This generates:
- A shared AI postcard (both Moxlings in the scene)
- Dual journal entries (each Moxling's perspective)
- Social trait development (cooperation, compromise, shared joy)

#### 4. Social Learning
Moxlings influence each other — just like real kids:
- A brave Moxling makes a timid friend slightly braver
- A dishonest Moxling can teach bad habits to a trusting one
- A curious Moxling sparks curiosity in others

This creates a tension: do you let your Moxling be friends with "badly raised" ones? This is ITSELF a parenting situation that gets recorded in your behavioral profile.

### The Social Graph

```
         [Your Moxling]
        /      |       \
    [Friend] [Friend] [Acquaintance]
       |        |
    [Their      [Their
     friends]    friends]

The social graph expands organically.
Your Moxling makes friends based on:
- Proximity (same "neighborhood" = same server/cohort)
- Compatibility (trait alignment)
- Shared experiences (traveled together, survived conflict)
- Owner activity (active owners' Moxlings meet more often)
```

### Owner Social Features

| Feature | Description |
|---|---|
| **Playground feed** | See what your Moxling did socially today (like a daycare report) |
| **Other parents** | See anonymized profiles of other Moxling owners (opt-in only) |
| **Parenting circles** | Groups of owners whose Moxlings are friends — community |
| **Shared postcards** | When Moxlings travel together, both owners get the postcard |
| **Conflict mediation** | When Moxlings fight, both owners can discuss (opt-in messaging) |

### Social Environments

| Environment | What Happens There |
|---|---|
| **Playground** | Free play, making friends, physical games |
| **School** | Structured social situations, group projects, competition |
| **Park** | Exploration with friends, adventure, discovery |
| **Market** | Trading, sharing, money situations involving other Moxlings |
| **Festival** | Large group events, celebrations, social dynamics at scale |
| **Sleepover** | Deep friendship moments, secrets, vulnerability |

### Emergent Social Dynamics

The most powerful part: **social dynamics emerge organically from the aggregate of all owners' parenting decisions.**

- If most owners in a cohort are empathetic, the social environment is warm and cooperative
- If most owners are competitive, the playground becomes intense and hierarchical
- Cliques form. Outcasts appear. Popular Moxlings emerge. Bullies arise.
- ALL of this is a reflection of the humans behind the Moxlings

This is the data goldmine: not just individual behavioral profiles, but the **social ecosystem that emerges from collective parenting styles**. It's sociology in a bottle.

---

## Data & Privacy

This product collects deeply personal behavioral data. Privacy must be foundational, not an afterthought.

### Principles

1. **Behavioral profile is local-first.** Stored on device. Only shared with explicit, granular consent.
2. **Matchmaking is opt-in and anonymized.** The system compares profiles without revealing raw data.
3. **No selling data. Ever.** This is the rule. The product's value IS trust.
4. **Transparency.** The owner can see their full behavioral profile at any time. No hidden scoring.
5. **Right to delete.** One button wipes everything. The Moxling forgets. The profile is gone.
6. **Age gating.** This product is for adults reflecting on their own caregiving instincts, not for children.

---

## Tech Architecture (Updated)

```
┌───────────────────────────────────────────────────────┐
│                      FRONTEND                          │
│               Next.js + React + Tailwind               │
│                                                        │
│  ┌──────────────┐  ┌──────────────────────────────┐   │
│  │   PixiJS     │  │     React Components         │   │
│  │  (Moxling    │  │  • Situation cards            │   │
│  │   sprite,    │  │  • Conversation interface     │   │
│  │   room,      │  │  • Behavioral profile dash    │   │
│  │   weather)   │  │  • Postcard gallery           │   │
│  └──────────────┘  │  • Journal / soul viewer      │   │
│                     │  • Matchmaking UI             │   │
│                     └──────────────────────────────┘   │
│                                                        │
│  State: Zustand        Auth: Clerk/Supabase Auth       │
│  Mobile: PWA → Capacitor                               │
├───────────────────────────────────────────────────────┤
│                      BACKEND                           │
│               FastAPI (Python)                          │
│                                                        │
│  ┌──────────────────────────────────────────────────┐ │
│  │  SITUATION ENGINE                                 │ │
│  │  • Age-stage curriculum of situations             │ │
│  │  • LLM generates contextual variations            │ │
│  │  • Scheduling (2-4/day, varied timing)            │ │
│  │  • Urgency classification                         │ │
│  │  • Response classification & scoring              │ │
│  └──────────────────────────────────────────────────┘ │
│                                                        │
│  ┌──────────────────────────────────────────────────┐ │
│  │  MOXLING BRAIN (Claude API)                       │ │
│  │  • Personality-driven conversation                │ │
│  │  • Trust-modulated openness                       │ │
│  │  • Memory management (SOUL.md + MEMORY.md)        │ │
│  │  • Situation generation                           │ │
│  │  • Journal entry writing                          │ │
│  └──────────────────────────────────────────────────┘ │
│                                                        │
│  ┌──────────────────────────────────────────────────┐ │
│  │  BEHAVIORAL PROFILER                              │ │
│  │  • Response classification (empathy, control,     │ │
│  │    consistency, availability, etc.)               │ │
│  │  • Profile aggregation over time                  │ │
│  │  • Pattern detection (improving? declining?)      │ │
│  │  • Matchmaking compatibility scoring              │ │
│  └──────────────────────────────────────────────────┘ │
│                                                        │
│  ┌──────────────────────────────────────────────────┐ │
│  │  IMAGE GENERATION                                 │ │
│  │  • PixelLab API for environment scenes            │ │
│  │  • Postcard generation for travel/social events   │ │
│  └──────────────────────────────────────────────────┘ │
│                                                        │
│  Database: PostgreSQL (profiles, situations, responses)│
│  Queue: Celery/Redis (situation scheduling, image gen) │
│  Cache: Redis (active Moxling state)                   │
└───────────────────────────────────────────────────────┘
```

---

## MVP Scope (v0.1) — Revised

Build the **situation engine + conversation loop** first. The pretty visuals come later.

### Must Have (Week 1-4)

1. **Moxling creation** — name it, see a randomized pixel sprite
2. **Home screen** — simple room backdrop, Moxling with 3-4 idle animations
3. **Situation engine** — 2 situations/day from a curated starter set (~30 situations)
4. **Response system** — 3-4 pre-written options + free text per situation
5. **Conversation** — basic chat when no active situation (5 messages/day)
6. **Moxling personality** — visible trait bars that shift based on responses
7. **Trust meter** — visible indicator of Moxling's trust in you
8. **Basic SOUL.md** — Moxling's identity doc, viewable by owner

### Nice to Have (Month 2-3)

9. **Behavioral profile dashboard** — see your own parenting patterns
10. **Age progression** — Moxling ages from Newborn → Child over time
11. **AI-generated environment backdrops** — scenes matching situation context
12. **Push notifications** — situations arrive as notifications
13. **Garden / sparks** — passive currency + simple economy

### Future (Month 4+)

14. **Matchmaking** — behavioral profile comparison
15. **Moxling social** — Moxlings meeting other Moxlings
16. **Travel / postcards** — Moxling goes on trips, sends AI-generated postcards
17. **Young Adult stage** — Moxling advises the owner (role reversal)
18. **Mobile app** — Capacitor wrap for iOS/Android

---

## Emotional Design Principles (Revised)

1. **The Moxling is not a chatbot.** It's a developing being. It has moods, fears, and opinions that you didn't give it.
2. **No correct answers.** Every parenting style produces a different Moxling. Authoritarian parents get obedient but guarded Moxlings. Permissive parents get confident but impulsive ones. The system doesn't judge — it reflects.
3. **Silence is the loudest feedback.** If the Moxling stops coming to you, that's the system telling you something. No pop-up says "trust is low." You just... notice the absence.
4. **Time matters.** A Moxling raised over 6 months is profoundly different from one raised for 2 weeks. The depth of the behavioral profile, and the Moxling's complexity, requires real time. This is not a game you "complete."
5. **The Moxling is the report card.** You don't need a dashboard to know how you're doing. Look at your Moxling. Is it happy? Confident? Does it come to you? Does it trust you? That's your answer.
6. **No death, no failure state.** The Moxling always survives. But it might become someone you didn't intend. That's the consequence.
7. **The mirror doesn't lie.** The most uncomfortable feature of this product is that it shows you who you are, not who you think you are.
