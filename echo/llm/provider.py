from __future__ import annotations

from abc import ABC, abstractmethod

from .message import ChatMessage
from .response import ChatResponse


class LLMProvider(ABC):
    """Abstract interface for all LLM providers."""

    @abstractmethod
    def chat(
        self,
        messages: list[ChatMessage],
    ) -> ChatResponse:
        """Generate a response."""
        raise NotImplementedError