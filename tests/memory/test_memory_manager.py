from echo.llm import ChatMessage, Role
from echo.memory import (
    MemoryManager,
    MessageWindow,
    SummaryMemory,
    ProfileMemory,
)


def test_build_messages_uses_window() -> None:
    """
    MemoryManager should delegate message selection
    to MessageWindow.
    """

    manager = MemoryManager(
        window=MessageWindow(
            max_messages=2,
        ),
        summary=SummaryMemory(),
        profile=ProfileMemory(),
    )

    messages = [
        ChatMessage(
            role=Role.USER,
            content=f"message {i}",
        )
        for i in range(5)
    ]

    result = manager.build_messages(messages)

    assert len(result) == 2
    assert result[0].content == "message 3"
    assert result[1].content == "message 4"


def test_build_messages_with_summary() -> None:
    """
    Summary should be inserted after the system prompt.
    """

    summary = SummaryMemory()
    summary.update("User likes Linux.")

    manager = MemoryManager(
        window=MessageWindow(
            max_messages=20,
        ),
        summary=summary,
        profile=ProfileMemory(),
    )

    messages = [
        ChatMessage(
            role=Role.SYSTEM,
            content="System Prompt",
        ),
        ChatMessage(
            role=Role.USER,
            content="Hello",
        ),
    ]

    result = manager.build_messages(messages)

    assert len(result) == 3

    assert result[0].role == Role.SYSTEM
    assert result[0].content == "System Prompt"

    assert result[1].role == Role.SYSTEM
    assert "Conversation Summary" in result[1].content
    assert "User likes Linux." in result[1].content

    assert result[2].role == Role.USER
    assert result[2].content == "Hello"


def test_profile_is_available() -> None:
    """
    MemoryManager should expose ProfileMemory.
    """

    manager = MemoryManager(
        window=MessageWindow(
            max_messages=20,
        ),
        summary=SummaryMemory(),
        profile=ProfileMemory(),
    )

    assert manager.profile is not None
    assert manager.profile.name is None
    assert manager.profile.preferences == []
    assert manager.profile.projects == []
    assert manager.profile.facts == []