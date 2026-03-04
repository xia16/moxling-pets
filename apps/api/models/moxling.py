from datetime import datetime

from pydantic import BaseModel, Field


class MoxlingTraits(BaseModel):
    """Core personality traits that evolve based on owner interactions."""

    curiosity: float = Field(default=0.5, ge=0.0, le=1.0)
    boldness: float = Field(default=0.5, ge=0.0, le=1.0)
    warmth: float = Field(default=0.5, ge=0.0, le=1.0)
    wit: float = Field(default=0.5, ge=0.0, le=1.0)
    independence: float = Field(default=0.5, ge=0.0, le=1.0)


class MoxlingAppearance(BaseModel):
    """8-bit visual representation — evolves to reflect the owner."""

    base_sprite: str = "default"
    color_primary: str = "#7C3AED"
    color_secondary: str = "#F59E0B"
    accessories: list[str] = Field(default_factory=list)
    expression: str = "neutral"
    evolution_stage: int = Field(default=1, ge=1, le=5)


class MoxlingCreate(BaseModel):
    name: str
    owner_id: str


class Moxling(BaseModel):
    id: str
    name: str
    owner_id: str
    traits: MoxlingTraits = Field(default_factory=MoxlingTraits)
    appearance: MoxlingAppearance = Field(default_factory=MoxlingAppearance)
    soul: str = ""  # The SOUL.md content — core identity
    memory: str = ""  # Persistent memory across sessions
    born_at: datetime = Field(default_factory=datetime.utcnow)
    last_active: datetime = Field(default_factory=datetime.utcnow)
    mood: str = "content"
    energy: float = Field(default=1.0, ge=0.0, le=1.0)


class GuardrailConfig(BaseModel):
    """Safety guardrails — the 'box' that keeps moxlings safe.

    These are set by the platform, not the user.
    Inspired by the Lobstar Wilde incident: safety-first by design.
    """

    max_spend_per_action: float = 10.0  # USD
    max_spend_per_day: float = 50.0  # USD
    can_post_social: bool = False
    can_send_messages: bool = False
    can_transact: bool = False
    require_owner_approval: list[str] = Field(
        default_factory=lambda: ["spend", "post", "message"]
    )
    blocked_actions: list[str] = Field(default_factory=list)
