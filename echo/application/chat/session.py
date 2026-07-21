from __future__ import annotations

from echo.llm import ChatMessage, ChatResponse, LLMProvider, Role


class ChatSession:
    """
    Represents a single conversation session.

    A ChatSession owns the conversation history and delegates
    response generation to an LLMProvider.
    """

    def __init__(self, provider: LLMProvider) -> None:
        self._provider = provider
        self._messages: list[ChatMessage] = []

    @property
    def messages(self) -> tuple[ChatMessage, ...]:
        """Read-only conversation history."""
        return tuple(self._messages)

    def clear(self) -> None:
        """Clear the current conversation."""
        self._messages.clear()

    def send(self, text: str) -> ChatResponse:
        """
        Send one user message.

        Steps:
            1. append user message
            2. call provider
            3. append assistant reply
            4. return response
        """

        user = ChatMessage(
            role=Role.USER,
            content=text,
        )

        self._messages.append(user)

        response = self._provider.chat(self._messages)

        assistant = ChatMessage(
            role=Role.ASSISTANT,
            content=response.text,
        )

        self._messages.append(assistant)

        return response