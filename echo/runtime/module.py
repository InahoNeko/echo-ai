"""Base abstraction for all ECHO modules."""

from __future__ import annotations

from abc import ABC, abstractmethod


class EchoModule(ABC):
    """Base class for all runtime modules.

    Every capability in ECHO (Memory, LLM, Voice, etc.)
    must inherit from this class.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique module name."""

    @abstractmethod
    def initialize(self) -> None:
        """Initialize resources before the runtime starts."""

    @abstractmethod
    def start(self) -> None:
        """Start the module."""

    @abstractmethod
    def stop(self) -> None:
        """Stop the module and release runtime resources."""