from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(slots=True, frozen=True)
class Event:
    """
    Base class for all events.
    """

    event_id: UUID
    created_at: datetime

    @classmethod
    def create(cls) -> "Event":
        return cls(
            event_id=uuid4(),
            created_at=datetime.now(),
        )