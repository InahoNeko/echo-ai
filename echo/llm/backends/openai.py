from __future__ import annotations

from echo.llm import (
    ChatMessage,
    ChatResponse,
    LLMProvider,
)

from .client import OpenAIClient
from .config import OpenAIConfig


class OpenAIProvider(LLMProvider):
    """
    OpenAI-compatible LLM provider.

    This provider is responsible for translating domain models
    (ChatMessage / ChatResponse) to and from the underlying client.

    It does not perform HTTP requests directly.
    """

    def __init__(
        self,
        config: OpenAIConfig,
        client: OpenAIClient,
    ) -> None:
        self._config = config
        self._client = client

    @property
    def model(self) -> str:
        """Current model name."""
        return self._config.model

    def chat(
        self,
        messages: list[ChatMessage],
    ) -> ChatResponse:
        """
        Generate a chat response.

        Parameters
        ----------
        messages:
            Conversation history.

        Returns
        -------
        ChatResponse
        """

        text = self._client.chat(
            model=self._config.model,
            messages=messages,
        )

        return ChatResponse(
            text=text,
        )

    def close(self) -> None:
        """Release provider resources."""

        self._client.close()

