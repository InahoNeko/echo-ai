from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ChatResponse:
    """Unified response from any LLM backend."""

    text: str