from __future__ import annotations

from dataclasses import dataclass

from .enums import Role


@dataclass(slots=True, frozen=True)
class ChatMessage:
    """A single chat message."""

    role: Role
    content: str