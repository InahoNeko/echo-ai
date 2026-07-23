from __future__ import annotations

from collections.abc import Iterator

from echo.llm import (
    ChatMessage,
    ChatResponse,
    LLMProvider,
    Role,
)
from echo.memory import MemoryManager
from echo.prompt import PromptService
from echo.memory import Summarizer
class ChatSession:
    """
    Represents a single conversation session.

    A ChatSession owns the conversation history and delegates
    response generation to an LLMProvider.
    """

    def __init__(
            self,
            provider: LLMProvider,
            prompt_service: PromptService,
            memory_manager: MemoryManager,
            summarizer: Summarizer,
    ) -> None:
        self._provider = provider
        self._prompt_service = prompt_service
        self._messages: list[ChatMessage] = []
        self._memory = memory_manager
        self._summarizer = summarizer

    def _ensure_system_prompt(self) -> None:
        """
        Ensure the conversation starts with a system prompt.
        """

        if self._messages:
            return

        prompt = self._prompt_service.build_system_prompt()

        self._messages.append(
            ChatMessage(
                role=Role.SYSTEM,
                content=prompt,
            )
        )

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

        self._ensure_system_prompt()

        user = ChatMessage(
            role=Role.USER,
            content=text,
        )

        self._messages.append(user)

        messages = self._memory.build_messages(
            self._messages,
        )

        response = self._provider.chat(
            messages,
        )

        assistant = ChatMessage(
            role=Role.ASSISTANT,
            content=response.text,
        )

        self._messages.append(
            assistant,
        )

        self._refresh_summary()

        return response

    def stream(
            self,
            text: str,
    ) -> Iterator[str]:
        """
        Stream one assistant response.
        """

        self._ensure_system_prompt()

        user = ChatMessage(
            role=Role.USER,
            content=text,
        )

        self._messages.append(user)

        messages = self._memory.build_messages(
            self._messages,
        )

        chunks: list[str] = []

        for chunk in self._provider.stream_chat(
                messages,
        ):
            chunks.append(chunk)
            yield chunk

        assistant = ChatMessage(
            role=Role.ASSISTANT,
            content="".join(chunks),
        )

        self._messages.append(assistant)

        self._refresh_summary()

    def _should_refresh_summary(self) -> bool:
        """
        Decide whether the conversation summary
        should be refreshed.
        """
        return False

    def _refresh_summary(self) -> None:
        """
        Refresh conversation summary.
        """

        if not self._should_refresh_summary():
            return