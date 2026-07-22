from __future__ import annotations

from abc import ABC, abstractmethod

from .message import ChatMessage
from .response import ChatResponse
from collections.abc import Iterator


class LLMProvider(ABC):
    """Abstract interface for all LLM providers."""

    @abstractmethod
    def chat(
        self,
        messages: list[ChatMessage],
    ) -> ChatResponse:
        """Generate a response."""
        raise NotImplementedError

    @abstractmethod
    def stream_chat(
            self,
            messages: list[ChatMessage],
    ) -> Iterator[str]:
        """
        Stream chat response.

        Yields
        ------
        str
            One text chunk at a time.
        """
        raise NotImplementedError