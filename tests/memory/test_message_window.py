from echo.llm import ChatMessage, Role
from echo.memory import MessageWindow


def test_returns_all_messages_when_under_limit() -> None:
    """
    Should return all messages when history
    is smaller than the window size.
    """

    window = MessageWindow(
        max_messages=10,
    )

    messages = [
        ChatMessage(
            role=Role.USER,
            content=f"message {i}",
        )
        for i in range(5)
    ]

    result = window.build(messages)

    assert result == messages