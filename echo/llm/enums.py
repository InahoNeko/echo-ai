from __future__ import annotations

from enum import StrEnum


class Role(StrEnum):
    """Chat message roles."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"