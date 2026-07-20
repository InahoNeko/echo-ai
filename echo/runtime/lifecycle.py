"""Runtime lifecycle definitions."""

from __future__ import annotations

from enum import Enum


class LifecycleState(Enum):
    """Lifecycle states of the ECHO runtime."""

    CREATED = "created"
    INITIALIZING = "initializing"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"