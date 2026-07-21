from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class OpenAIConfig:
    """
    Configuration for an OpenAI-compatible provider.
    """

    base_url: str
    api_key: str
    model: str
    timeout: float = 60.0