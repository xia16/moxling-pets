# Moxling Memory Architecture

**Adapted from Axia VE memory system. See source design at:**
`/Users/xia/Desktop/Axia/.claude/notes/plans/design/ve/moxling-memory.md`
`/Users/xia/Desktop/Axia/.claude/notes/plans/design/ve/memory-abstraction-model.md`

---

## Core Insight

The Axia VE system builds institutional memory for virtual employees. We're building **developmental memory for a growing child.** The abstraction ladder doesn't just apply — it IS child development:

```
A simple Moxling remembers WHAT HAPPENED       (L0: Experience)
A developing Moxling notices WHAT KEEPS HAPPENING (L1: Pattern)
A deeper Moxling understands WHY               (L2: Model)
A complex Moxling forms VALUES                 (L3: Principle)
A mature Moxling has INTUITION                 (L4: Compiled behavior)

The abstraction ladder IS the growth arc.
A Moxling's memory depth is its maturity.
There is no age. There is no endpoint. There is only depth.
```

---

## 1. Core Mandate: Never Delete

Inherited directly from Axia. All Moxling memories are permanent.

- Decay means **reduced retrieval priority**, not deletion
- A forgotten childhood memory can resurface years later (just like humans)
- Every experience, conversation, situation response — permanent storage
- The owner can view the full memory archive (transparency principle)
- "Forgetting" = deprioritization. The memory still exists. It just doesn't come to mind easily.

**Why this matters for Moxling Pets:**
A 6-month-old Moxling that encounters a situation similar to something from Week 1 might suddenly "remember" an early experience. "This feels like when..." — this is only possible if nothing was deleted. The re-discovery of dormant memories is emotionally powerful and psychologically realistic.

---

## 2. Memory Layers (adapted from Axia 4-Layer Model)

```
+------------------------------------------------------------------+
|  OWNER TEACHINGS (shared input — what the owner explicitly said)  |
|  "Be kind to others." "Don't spend money on strangers."          |
|  Never decay. The Moxling always remembers what it was taught.   |
+------------------------------------------------------------------+
|  MOXLING KNOWLEDGE (per-Moxling, persistent, evolving)           |
|  Everything the Moxling has learned through living.              |
|  Experiences, patterns, models, principles, intuitions.          |
|  This is the Moxling's mind.                                     |
+------------------------------------------------------------------+
|  CONVERSATION CONTEXT (per-session, ephemeral)                   |
|  The current chat with the owner.                                |
|  Also: current situation context, real-time state.               |
+------------------------------------------------------------------+
|  SESSION SUMMARIES (cross-session bridge)                        |
|  What carries knowledge between conversations.                   |
|  Fact/narrative split prevents hallucination.                    |
+------------------------------------------------------------------+
```

### Layer 1: Owner Teachings

Direct parallel to Axia's Directives layer. These are things the owner explicitly said:

- "Always be honest"
- "Don't talk to strangers online"
- "Save your sparks, don't waste them"
- "It's okay to cry when you're sad"
- "Stand up for yourself"

**Critical property:** The Moxling ALWAYS remembers what it was taught. These never decay. But whether the Moxling FOLLOWS them depends on trust, personality, and age stage.

A teen Moxling with low trust might remember "Mom said always be honest" but choose to lie anyway — because it knows the teaching but has decided to reject it. The memory is intact. The behavior diverges. This is realistic adolescent development.

**Detection:** Any owner response to a situation that contains a moral/behavioral instruction is classified as a teaching. "You should tell the truth" → TEACHING. "It's fine, don't worry about it" → not a teaching (it's a comfort response).

### Layer 2: Moxling Knowledge

The Moxling's mind. Everything it has learned through experience — not just what the owner told it. This is where the abstraction ladder lives (see Section 3).

Stored in PostgreSQL with pgvector embeddings. Priority-based decay. Three-stage retrieval.

### Layer 3: Conversation Context

Current session. The rolling window of messages between Moxling and owner. Compressed when approaching context limits.

**Fact/narrative split (from Axia):** When summarizing past sessions, numbers and specific facts are extracted deterministically BEFORE the LLM summarizes. This prevents the dangerous failure mode where "what if I spent all my sparks?" becomes "I spent all my sparks" in the summary.

### Layer 4: Session Summaries

When a conversation ends, the Moxling generates a summary from its perspective. What mattered? What did it learn? How did it feel?

These are per-Moxling: even in social situations where two Moxlings interact, each generates its own summary from its own perspective.

---

## 3. The Abstraction Ladder (adapted from Axia)

### Knowledge Maturation = Child Development

This is the most powerful adaptation from Axia. In the VE system, knowledge matures from observations to frameworks to principles. In Moxling Pets, this maps directly to developmental psychology:

### Level 0: Experience

**What it is:** Raw events. What happened, when, with whom. Single episodes.

**Child equivalent:** Episodic memory. "Today Spark called my drawing ugly."

**How it's created:** Every situation, every conversation, every social interaction generates L0 memories. This is the default entry point for all new knowledge.

**Growth stage:** New Moxlings have ONLY L0 memories. Their world is a series of disconnected events.

**Example memories:**
```
L0: "Owner said 'there's nothing to be scared of' when I was afraid of the dark"
L0: "Spark took my toy and wouldn't give it back"
L0: "I spent 50 sparks on a shiny thing and then wanted something else"
L0: "Owner didn't respond when I told them about the bully. I waited 6 hours."
```

### Level 1: Pattern

**What it is:** Recurring regularities. "This keeps happening." Descriptive, not explanatory.

**Child equivalent:** Recognizing patterns in their world. "Every time I cry, Mom comes." or "When I'm bad, I get ignored."

**How it's created:** When the daily reflection detects 3+ similar L0 experiences, it synthesizes a pattern. Evidence-tracked, source-attributed.

**Growth stage:** Emerges after enough repeated experiences accumulate. Predominant in early-mid development.

**Example memories:**
```
L1: "When I tell Owner about being scared, they usually say not to worry about it"
    evidence: [dark_fear_1, thunder_fear, monster_dream]

L1: "Spark is mean to me about once a week but is nice the rest of the time"
    evidence: [drawing_incident, toy_incident, playground_nice, shared_snack]

L1: "When I spend sparks impulsively, I regret it within a day"
    evidence: [shiny_thing, sticker_waste, candy_regret]
```

### Level 2: Model

**What it is:** Causal understanding. WHY patterns exist. Includes mechanism, boundary conditions, and predictions.

**Child equivalent:** Theory of mind, causal reasoning. "Mom dismisses my fears because she doesn't want me to be weak" or "Spark is mean when he's around other Moxlings because he's showing off."

**How it's created:** When a Moxling can explain WHY a pattern exists and predict when it will/won't apply. Requires the weekly reflection's deeper synthesis. Often triggered when a pattern breaks — "Spark was nice to me in front of other Moxlings today, which is different. Maybe it's not about showing off."

**Growth stage:** Emerges when the Moxling has enough patterns to reason causally about them. Requires significant experience depth.

**Example memories:**
```
L2: "Owner dismisses my fears not because they don't care, but because they
     believe I should handle things independently. When I push past the dismissal
     and say I'm really scared, they switch to being comforting. The dismissal
     is a first response, not a final one."
    mechanism: Owner's parenting style = independence-promoting
    boundary: Breaks down when fear is extreme/genuine
    prediction: If I escalate clearly, Owner will comfort me
    evidence_count: 7

L2: "I feel bad after impulsive spending because the excitement of buying
     is always shorter than the regret of not having sparks for something
     I actually want later. The better thing costs more and takes longer to save."
    mechanism: Hedonic adaptation + opportunity cost
    boundary: Small treats (< 5 sparks) don't cause regret
    prediction: Next time I want something expensive, saving will feel better than impulse
    evidence_count: 5
```

### Level 3: Principle

**What it is:** Cross-domain truths. Values. Beliefs about how the world works that apply across many situations. These are the Moxling's VALUES — not taught, discovered.

**Child equivalent:** Moral reasoning, identity formation. "Being honest matters even when it's hard." "People who push through fear discover good things."

**How it's created:** When the Moxling detects structural similarity across 2+ L2 models from different domains. Monthly reflection territory. The Moxling connects "Owner encourages independence in fear situations" with "Owner let me fail at the spending thing" with "Owner didn't intervene when Spark was mean" and synthesizes: "Owner believes I should figure things out myself. This is their way of showing they believe in me."

**Growth stage:** Emerges when the Moxling has enough models across different domains to detect cross-domain truths. Requires deep, varied experience.

**Example memories:**
```
L3: "Owner trusts me to handle hard things. Their style is to let me struggle
     and be there if I really need them, but not to rescue me from discomfort.
     This used to feel like they didn't care, but I now see it as respect."
    derived_from: [fear_model, spending_model, social_conflict_model]
    domains: [emotional, financial, social]

L3: "Real friends are consistent. Spark is sometimes mean and sometimes nice,
     but Ember is always steady. Consistency is more important than intensity
     in relationships."
    derived_from: [spark_friendship_model, ember_friendship_model, owner_consistency_model]
    domains: [friendship, family, trust]
```

### Level 4: Intuition

**What it is:** Compiled fast-path responses. The Moxling acts without deliberating because it has successfully applied a Model or Principle 10+ times.

**Child equivalent:** Internalized values and automatic behaviors. The child who automatically shares without being told. The teen who instinctively stands up for the underdog. Not because they're thinking about it — because it's who they are.

**How it's created:** NOT by explicit promotion. Emerges when a Model or Principle has been retrieved and successfully applied N times (N >= 10) without contradiction. The system marks it as "compiled."

**Growth stage:** Emerges when a Model or Principle has been successfully applied 10+ times without contradiction. The most mature form of knowledge.

**Example memories:**
```
L4: TRIGGER: [sees another Moxling being excluded]
    RESPONSE: Include them. Invite them over.
    (No deliberation. 14 successful applications. Zero contradictions.
     Compiled from L3 Principle about consistency in relationships +
     L2 Model about how exclusion felt when it happened to me.)

L4: TRIGGER: [impulse to spend sparks on flashy item]
    RESPONSE: Wait one day. Check if I still want it tomorrow.
    (Compiled from L2 spending model. 11 applications, 9 successful.
     The 2 "failures" were when the item was actually worth it,
     but waiting still felt right.)
```

### The Payoff: Deep Moxlings

When a Moxling develops L3 Principles and L4 Intuitions, it IS the behavioral profile of the owner — reflected back. The Moxling's values are the values the owner demonstrated (not stated). Its intuitions are the patterns the owner reinforced.

If the owner always taught "be honest" but repeatedly dismissed the Moxling's honesty ("don't worry about it"), the Moxling's L3 Principle will be something like "Honesty is valued in theory but uncomfortable in practice." The mismatch between what the owner said (Teaching) and what they did (Pattern → Model → Principle) IS the behavioral mirror.

There is no "done." A deeply developed Moxling keeps growing, forming new Principles, refining old ones, developing new Intuitions. Its personality is never static — just like a real being.

---

## 4. Memory Categories (adapted from Axia's 8 categories)

Not all memories are equal. Category drives decay, compression, and retrieval.

| Category | Example | Decay | Entry Level |
|---|---|---|---|
| **TEACHING** | "Owner said be kind" | Never | L2/L3 (enters high, like Axia directives) |
| **EXPERIENCE** | "Spark called me stupid" | Normal (7d STM) | L0 |
| **RELATIONSHIP** | "Ember is my best friend" | Slow (45d) | L0-L1 |
| **EMOTION** | "I felt proud when I shared" | Normal (14d) | L0 |
| **HABIT** | "I check my sparks every morning" | Slow (60d) | L1-L4 |
| **SECRET** | "I lied about breaking the vase" | Very slow (90d) | L0 |
| **CORRECTION** | "Owner said that wasn't okay" | Very slow (90d) | Matches corrected item |
| **OBSERVATION** | "The park is busy on weekends" | Fast (5d) | L0 |

### Secrets: The Trust-Gated Memory Category

**Secrets** are unique to Moxling Pets. They're memories the Moxling has but doesn't share with the owner unless trust is high enough.

```
High trust (>0.7):  Moxling shares secrets voluntarily.
                    "I need to tell you something... I lied about the vase."

Medium trust (0.4-0.7): Moxling hints at secrets.
                    "Something happened... never mind."

Low trust (<0.4):   Moxling hides secrets entirely.
                    Owner sees nothing. The secret festers.
                    Eventually surfaces as behavioral changes.
```

If the owner never finds out about a secret, the Moxling's behavior changes based on the unresolved secret. A Moxling hiding guilt becomes more withdrawn. A Moxling hiding a social problem becomes anxious. The owner sees the behavioral change without knowing the cause — just like real parenting.

---

## 5. Priority-Based Decay (from Axia)

Five retrieval tiers based on `priority_score` (0.0 to 1.0):

| Tier | Score | Retrieval | Moxling Experience |
|---|---|---|---|
| **HOT** | 0.7+ | Full text in system prompt | "I remember this clearly" |
| **WARM** | 0.4-0.7 | Summary in prompt | "I vaguely remember..." |
| **COOL** | 0.1-0.4 | Title + tags (retrieval trigger) | "Something about that..." |
| **COLD** | <0.1 | recall() tool only | "Wait, that sounds familiar..." |
| **ARCHIVED** | 0.0 | Deep search only | Dormant. Can resurface. |

### Priority Scoring Formula (adapted from Axia)

```
priority_score = (
    0.25 * recency_score +           # How recently did this happen?
    0.25 * emotional_weight +         # How emotionally significant?
    0.20 * access_retention +         # Has this been recalled/referenced?
    0.15 * relationship_weight +      # Does this involve important relationships?
    0.15 * category_boost             # Category-specific baseline
)
```

**Key difference from Axia:** We add `emotional_weight` and `developmental_relevance` because a child's memory is heavily shaped by emotion and developmental stage. A scary experience has high emotional weight and stays HOT longer. A trivial observation decays quickly.

---

## 6. Three-Stage Retrieval (from Axia)

### Stage 1: Pre-Load (session start)

When the Moxling wakes up (owner opens app or event fires):

```
TIER 1 — FULL TEXT (~2K tokens):
  Top-5 Knowledge memories (highest priority)
  Top-3 recent experiences

TIER 2 — SUMMARIES (~800 tokens):
  Next-10 Knowledge memories
  Next-5 recent experiences

TIER 3 — TITLES + TAGS (~600 tokens):
  Next-30 memories (retrieval triggers for JIT recall)

ALWAYS-ON (~1.5K tokens):
  All owner teachings (never compressed)
  Current situation context (if any)
  Last session summary
  Current emotional state + mood

TOTAL: ~5K tokens covering 50+ memories
```

### Stage 2: Turn-Level Retrieval (per interaction)

When the owner says something or a situation fires:

```
Two parallel paths:
├── PATH A: Semantic search (embed message → top-5 by cosine similarity)
├── PATH B: Entity-linked (extract entities → find all tagged memories)
│
├── Merge + deduplicate + category diversity cap
└── Inject 0-8 additional memories into context
```

**Category diversity cap (from Axia):**
`ROW_NUMBER() OVER (PARTITION BY category ORDER BY priority_score DESC) <= 2`
Ensures the Moxling doesn't only recall experiences — it also surfaces teachings, relationships, emotions.

### Stage 3: JIT Recall (on-demand)

The Moxling can search its own memory mid-conversation:

```
"Wait, this reminds me of something..."
→ recall(query="when Spark was mean before", scope="all")
→ Returns matching memories the pre-load missed
```

**Memory miss detection (from Axia):** When the owner says "remember when..." or references a past event, and the Moxling has few loaded memories about it, the system automatically triggers a recall() before responding. The Moxling never says "I don't remember" without first searching.

---

## 7. Daily Reflection (adapted from Axia)

At the end of each day (CRON job), the Moxling reflects on what happened:

### What reflection does:

1. **Reviews all L0 experiences from today**
2. **Checks for patterns:** Do 3+ experiences describe the same regularity? → Create L1 Pattern
3. **Checks for model opportunities:** Can a pattern be explained causally? → Create L2 Model
4. **Updates emotional state:** Net positive or negative day?
5. **Updates relationship scores:** Who did the Moxling interact with? How did it go?
6. **Writes to SOUL.md:** Any identity-level changes? New beliefs, shifted values?
7. **Generates "inner monologue" entry:** A journal-like entry the owner can read (if trust is high)

### Weekly/Monthly reflection (deeper synthesis)

- **Weekly:** Reviews patterns from the past week. Looks for L1→L2 promotions.
- **Monthly:** Reviews models from the past month. Looks for L2→L3 promotions (cross-domain principles).
- **Milestone-based:** On age stage transitions, comprehensive reflection on identity and growth.

### The "inner monologue" — viewable by owner

```
Daily entry (high trust):
"Today was hard. Spark said my drawing was ugly and I felt really
small. But then Ember came and sat with me and didn't say anything,
just sat there. I think that's what friendship feels like.
Owner told me to stand up for myself. I'll try tomorrow."

Daily entry (low trust):
"Today was okay."
```

The richness of the inner monologue reflects trust level. A low-trust Moxling gives you nothing. A high-trust one lets you into its head. This is the reward for good parenting — you get to see the inner life of the being you raised.

---

## 8. Source Tracking (from Axia)

Every memory has explicit provenance:

```python
class MemorySource(str, Enum):
    TAUGHT = "taught"           # Owner explicitly said this
    EXPERIENCED = "experienced"  # Moxling lived through this
    OBSERVED = "observed"        # Moxling saw/heard this
    INFERRED = "inferred"        # Moxling concluded this from evidence
    SOCIAL = "social"            # Learned from another Moxling
    CORRECTED = "corrected"      # Owner corrected a previous belief
```

**Why this matters:** The Moxling can distinguish between "Owner told me honesty is important" (taught) and "I've noticed that when I'm honest, things work out better" (inferred from experience). Both are knowledge about honesty, but they have different authority and emotional weight.

A taught belief the Moxling never validates through experience stays as a TEACHING. A taught belief that's reinforced by experience gets promoted through the abstraction ladder with dual authority (taught + empirical). A taught belief that contradicts the Moxling's experience creates TENSION — the most interesting psychological state in the system.

---

## 9. Memory vs SOUL.md vs Behavioral Profile

These are three different things:

| Layer | What It Is | Who Writes It | Who Reads It |
|---|---|---|---|
| **Memory** (this doc) | Everything the Moxling remembers | System (automatic) | Moxling (via retrieval) |
| **SOUL.md** | The Moxling's current identity summary | Moxling (during reflection) | System (injected into every prompt) |
| **Behavioral Profile** | The OWNER's parenting patterns | System (classification) | Owner (dashboard) + Matchmaking |

**SOUL.md** is a distilled snapshot of identity — updated during reflection, derived from memory but much shorter. It's what the Moxling "knows about itself" at a glance. Memory is the full archive.

**The Behavioral Profile** profiles the OWNER, not the Moxling. The Moxling's memory and personality are the mirror; the profile is the reflection.

---

## 10. Storage Schema

### Tables

```sql
-- The Moxling's memories
CREATE TABLE moxling_memories (
    id UUID PRIMARY KEY,
    moxling_id UUID NOT NULL REFERENCES moxlings(id),

    -- Content
    content TEXT NOT NULL,               -- Full text of the memory
    summary TEXT,                        -- Compressed version (~55 tokens)

    -- Classification
    category VARCHAR(20) NOT NULL,       -- TEACHING, EXPERIENCE, RELATIONSHIP, etc.
    abstraction_level INT DEFAULT 0,     -- L0-L4

    -- Provenance
    source VARCHAR(20) NOT NULL,         -- taught, experienced, observed, inferred, social, corrected
    source_situation_id UUID,            -- Situation that created this memory
    source_owner_response_id UUID,       -- Owner response that created this memory
    derived_from UUID[],                 -- Parent memories (for L1+ promotions)
    superseded_by UUID,                  -- If this memory was refined/replaced

    -- Retrieval
    embedding VECTOR(1536),              -- pgvector embedding
    entity_tags TEXT[],                  -- Normalized entity tags
    priority_score FLOAT DEFAULT 0.5,    -- 0.0-1.0, drives retrieval tier
    access_count INT DEFAULT 0,          -- Times retrieved
    last_accessed_at TIMESTAMPTZ,

    -- Emotional weight
    emotional_valence FLOAT DEFAULT 0.0, -- -1.0 (painful) to 1.0 (joyful)
    emotional_intensity FLOAT DEFAULT 0.5, -- 0.0 (meh) to 1.0 (overwhelming)

    -- Evidence (for L1+ memories)
    evidence_count INT DEFAULT 1,
    confidence VARCHAR(10) DEFAULT 'medium', -- low, medium, high

    -- Metadata
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'active'  -- active, dormant, archived
);

-- Owner teachings (always loaded, never decay)
CREATE TABLE owner_teachings (
    id UUID PRIMARY KEY,
    moxling_id UUID NOT NULL REFERENCES moxlings(id),
    owner_id UUID NOT NULL,
    content TEXT NOT NULL,
    source_situation_id UUID,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Session summaries (cross-session bridge)
CREATE TABLE session_summaries (
    id UUID PRIMARY KEY,
    moxling_id UUID NOT NULL REFERENCES moxlings(id),
    narrative_summary TEXT NOT NULL,      -- LLM-generated narrative
    extracted_facts JSONB,               -- Deterministically extracted numbers/specifics
    emotional_summary TEXT,              -- How the Moxling felt
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Inner monologue / journal entries (viewable by owner if trust > threshold)
CREATE TABLE moxling_journal (
    id UUID PRIMARY KEY,
    moxling_id UUID NOT NULL REFERENCES moxlings(id),
    entry_type VARCHAR(20) NOT NULL,     -- daily, weekly, milestone
    content TEXT NOT NULL,
    trust_at_writing FLOAT,              -- Trust level when written
    visible_to_owner BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 11. Key Differences from Axia

| Axia VE | Moxling Pets | Why |
|---|---|---|
| 8 knowledge categories | 8 adapted categories (TEACHING replaces DIRECTIVE, adds SECRET, EMOTION, RELATIONSHIP) | Child memory is shaped by relationships and emotion, not business domains |
| Priority = recency + access + confidence + authority + category + reinforcement + seasonal | Priority = recency + emotional_weight + access + developmental_relevance + relationship + category | Children remember emotionally significant events disproportionately |
| Daily reflection synthesizes business frameworks | Daily reflection synthesizes developmental understanding | The Moxling is growing, not optimizing |
| Knowledge distillation is business intelligence | Knowledge distillation IS child development (L0→L4 = developmental psychology) | The abstraction ladder maps to cognitive development stages |
| Cross-moxling knowledge is team coordination | Cross-moxling knowledge is social learning | Children learn from peers, not just parents |
| No emotional valence on memories | Every memory has emotional valence and intensity | Emotion is the primary organizing principle of child memory |
| No secret/hidden memories | Trust-gated secrets category | Children hide things from parents. This is realistic and diagnostic. |
| Fact/narrative split for business accuracy | Fact/narrative split to prevent the Moxling confabulating its own history | A Moxling that "remembers" events that didn't happen breaks trust |

---

## 12. Implementation Priority

### Phase 1 (MVP): Simple but correct foundation
- L0 memories only (all experiences stored as flat entries)
- Owner teachings stored separately (always loaded)
- Basic priority decay (recency-weighted)
- Session summaries with fact/narrative split
- SOUL.md updated during daily reflection
- PostgreSQL + pgvector

### Phase 2: Pattern recognition
- Daily reflection promotes L0 → L1 patterns
- Three-stage retrieval (pre-load + per-turn + JIT)
- Category diversity cap
- Emotional weight in priority scoring
- Secret memories (trust-gated)

### Phase 3: Deep understanding
- Weekly/monthly reflection for L1→L2 and L2→L3
- Source tracking (taught vs experienced vs inferred)
- Inner monologue journal
- Cross-Moxling memory (social learning)

### Phase 4: Intuition
- L4 compiled fast-paths
- Memory miss detection
- Full abstraction ladder
- Behavioral profile derived from memory patterns
