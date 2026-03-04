from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class AgeStage(str, Enum):
    NEWBORN = "newborn"      # Week 1-2: basic needs
    TODDLER = "toddler"      # Week 2-4: tantrums, "no!", first words
    CHILD = "child"          # Month 1-3: school, friends, fairness
    TWEEN = "tween"          # Month 3-6: identity, peer pressure
    TEEN = "teen"            # Month 6-12: big decisions, rebellion
    YOUNG_ADULT = "young_adult"  # Month 12+: role reversal, advises owner


class MoxlingTraits(BaseModel):
    """Personality traits shaped by owner's parenting responses."""

    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    empathy: float = Field(default=0.5, ge=0.0, le=1.0)
    resilience: float = Field(default=0.5, ge=0.0, le=1.0)
    honesty: float = Field(default=0.5, ge=0.0, le=1.0)
    trust: float = Field(default=0.7, ge=0.0, le=1.0)  # starts high — yours to lose
    curiosity: float = Field(default=0.5, ge=0.0, le=1.0)
    independence: float = Field(default=0.3, ge=0.0, le=1.0)
    kindness: float = Field(default=0.5, ge=0.0, le=1.0)


class MoxlingAppearance(BaseModel):
    """8-bit visual representation — evolves to reflect personality."""

    base_sprite: str = "default"
    color_primary: str = "#7C3AED"
    color_secondary: str = "#F59E0B"
    accessories: list[str] = Field(default_factory=list)
    expression: str = "neutral"


class MoxlingCreate(BaseModel):
    name: str
    owner_id: str


class Moxling(BaseModel):
    id: str
    name: str
    owner_id: str
    age_stage: AgeStage = AgeStage.NEWBORN
    traits: MoxlingTraits = Field(default_factory=MoxlingTraits)
    appearance: MoxlingAppearance = Field(default_factory=MoxlingAppearance)
    soul: str = ""  # SOUL.md — core identity, updated by the Moxling itself
    memory: str = ""  # MEMORY.md — facts and history
    born_at: datetime = Field(default_factory=datetime.utcnow)
    last_active: datetime = Field(default_factory=datetime.utcnow)
    mood: str = "content"
    energy: float = Field(default=1.0, ge=0.0, le=1.0)
    friends: list[str] = Field(default_factory=list)  # IDs of other Moxlings


# --- Situation Engine ---


class SituationCategory(str, Enum):
    EMOTIONAL = "emotional"        # fear, anger, sadness, joy
    SOCIAL = "social"              # conflict, friendship, bullying, peer pressure
    ETHICAL = "ethical"            # lying, cheating, fairness, inclusion
    FINANCIAL = "financial"        # spending, saving, sharing, scams
    INDEPENDENCE = "independence"  # risk, autonomy, failure, growth
    IDENTITY = "identity"          # self-discovery, difference, self-worth


class SituationUrgency(str, Enum):
    LOW = "low"        # respond within 24h
    MEDIUM = "medium"  # respond within a few hours
    HIGH = "high"      # respond within 30 min — outcome changes significantly


class Situation(BaseModel):
    """A life event that tests the owner's caregiving instincts."""

    id: str
    moxling_id: str
    category: SituationCategory
    urgency: SituationUrgency
    description: str  # what the Moxling says/shows
    context: str  # background for LLM (not shown to user)
    options: list[str] = Field(default_factory=list)  # pre-written response choices
    allows_free_text: bool = True
    environment: str = "home"  # backdrop scene
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime | None = None
    resolved: bool = False


class SituationResponse(BaseModel):
    """How the owner responded to a situation."""

    id: str
    situation_id: str
    owner_id: str
    response_text: str
    response_option_index: int | None = None  # which pre-written option, if any
    responded_at: datetime = Field(default_factory=datetime.utcnow)
    response_time_seconds: int = 0  # how long they took to respond

    # LLM-classified behavioral scores (filled by backend after response)
    emotional_validation: float | None = None
    solution_orientation: float | None = None
    empathy_score: float | None = None
    control_level: float | None = None
    consistency_score: float | None = None  # vs past similar situations


# --- Behavioral Profile (the real product) ---


class ParentingStyle(str, Enum):
    AUTHORITATIVE = "authoritative"    # high warmth + high structure
    AUTHORITARIAN = "authoritarian"    # low warmth + high structure
    PERMISSIVE = "permissive"          # high warmth + low structure
    NEGLECTFUL = "neglectful"          # low warmth + low structure


class BehavioralProfile(BaseModel):
    """The owner's behavioral profile, built from hundreds of micro-decisions."""

    owner_id: str
    parenting_style: ParentingStyle | None = None  # emerges over time

    # Core dimensions (0.0 to 1.0)
    emotional_availability: float = Field(default=0.5, ge=0.0, le=1.0)
    consistency: float = Field(default=0.5, ge=0.0, le=1.0)
    empathy_vs_solution: float = Field(default=0.5, ge=0.0, le=1.0)  # 0=empathy-first, 1=solution-first
    risk_tolerance: float = Field(default=0.5, ge=0.0, le=1.0)
    boundary_firmness: float = Field(default=0.5, ge=0.0, le=1.0)
    autonomy_support: float = Field(default=0.5, ge=0.0, le=1.0)
    teaching_style: float = Field(default=0.5, ge=0.0, le=1.0)  # 0=by example, 1=verbal explanation
    failure_response: float = Field(default=0.5, ge=0.0, le=1.0)  # 0=comfort, 1=lesson

    total_situations_responded: int = 0
    total_situations_ignored: int = 0
    avg_response_time_seconds: float = 0.0

    updated_at: datetime = Field(default_factory=datetime.utcnow)


# --- Social System ---


class SocialInteraction(BaseModel):
    """When two Moxlings interact — shaped by both owners' parenting."""

    id: str
    moxling_a_id: str
    moxling_b_id: str
    interaction_type: str  # "play", "conflict", "share", "visit"
    description: str  # LLM-generated scene
    environment: str  # backdrop
    outcome: str = ""  # what happened
    postcard_image_url: str | None = None  # AI-generated scene of both Moxlings
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MatchmakingProfile(BaseModel):
    """Anonymized behavioral profile used for owner matchmaking."""

    owner_id: str
    behavioral_profile: BehavioralProfile
    moxling_summary: str  # LLM-generated summary of the Moxling's personality
    opt_in: bool = False
    compatible_with: list[str] = Field(default_factory=list)  # owner IDs
