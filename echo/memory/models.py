from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SummaryMemoryModel:
    """
    Stores the current conversation summary.
    """

    content: str = ""


@dataclass(slots=True)
class UserProfile:
    """
    Stores long-term user information.
    """

    name: str | None = None

    preferences: list[str] = field(default_factory=list)

    facts: list[str] = field(default_factory=list)

    projects: list[str] = field(default_factory=list)