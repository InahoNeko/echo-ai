from __future__ import annotations

from echo.llm import ChatMessage


class MessageWindow:
    """
    Maintains a sliding window over conversation history.
    """

    def __init__(
        self,
        max_messages: int = 20,
    ) -> None:
        self._max_messages = max_messages

    @property
    def max_messages(self) -> int:
        return self._max_messages

    def build(
            self,
            messages: list[ChatMessage],
    ) -> list[ChatMessage]:
        """
        Return the most recent messages.
        """

        if len(messages) <= self._max_messages:
            return list(messages)

        return list(messages[-self._max_messages :])