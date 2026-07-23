from __future__ import annotations

from echo.llm import (
    ChatMessage,
    Role,
)

from .message_window import MessageWindow

from .summary import SummaryMemory

from .profile import ProfileMemory

class MemoryManager:
    """
    Coordinates all memory components.
    """

    def __init__(
            self,
            window: MessageWindow,
            summary: SummaryMemory,
            profile: ProfileMemory,
    ) -> None:
        self._window = window
        self._summary = summary
        self._profile = profile

    @property
    def summary(self) -> SummaryMemory:
        """
        Conversation summary.
        """
        return self._summary

    @property
    def profile(self) -> ProfileMemory:
        """
        Long-term user profile.
        """
        return self._profile
    def build_messages(
            self,
            messages: list[ChatMessage],
    ) -> list[ChatMessage]:
        """
        Build the final messages sent to the LLM.
        """

        window = self._window.build(messages)

        if not window:
            return []

        if not self._summary.content:
            return window

        summary = ChatMessage(
            role=Role.SYSTEM,
            content=(
                "Conversation Summary:\n"
                f"{self._summary.content}"
            ),
        )

        return [
            window[0],
            summary,
            *window[1:],
        ]