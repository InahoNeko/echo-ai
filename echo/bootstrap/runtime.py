"""ECHO Runtime lifecycle management.

This module provides the core runtime controller
for starting and stopping the ECHO system.
"""

from __future__ import annotations

from enum import Enum


class RuntimeStatus(Enum):
    """Runtime running states."""

    STOPPED = "STOPPED"
    RUNNING = "RUNNING"


class Runtime:
    """Main lifecycle controller of ECHO.

    Runtime is responsible only for:
    - starting the system
    - stopping the system
    - exposing current status

    It does not handle:
    - AI models
    - memory
    - user interaction
    - business logic
    """

    VERSION = "0.1.0-alpha"

    def __init__(self) -> None:
        self._status = RuntimeStatus.STOPPED

    def start(self) -> None:
        """Start ECHO runtime."""

        if self._status == RuntimeStatus.RUNNING:
            return

        self._status = RuntimeStatus.RUNNING

    def stop(self) -> None:
        """Stop ECHO runtime."""

        if self._status == RuntimeStatus.STOPPED:
            return

        self._status = RuntimeStatus.STOPPED

    @property
    def status(self) -> RuntimeStatus:
        """Get current runtime status."""

        return self._status

    @property
    def version(self) -> str:
        """Get runtime version."""

        return self.VERSION