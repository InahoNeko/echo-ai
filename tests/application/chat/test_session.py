from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

from echo.application.chat.session import (
    ChatSession,
    Summarizer,
)

from echo.llm import (
    ChatMessage,
    ChatResponse,
    LLMProvider,
)

from echo.memory import (
    MemoryManager,
    MessageWindow,
    ProfileMemory,
    SummaryMemory,
)

from echo.prompt import (
    PromptBuilder,
    PromptLoader,
    PromptService,
)


class FakeProvider(LLMProvider):
    def chat(
        self,
        messages: list[ChatMessage],
    ) -> ChatResponse:
        return ChatResponse(
            text="你好，我是景愿。",
        )

    def stream_chat(
        self,
        messages: list[ChatMessage],
    ) -> Iterator[str]:
        yield "你好，我是景愿。"


def create_session() -> ChatSession:
    """
    Create a ChatSession for testing.
    """

    prompt_service = PromptService(
        loader=PromptLoader(
            Path("echo/prompt"),
        ),
        builder=PromptBuilder(),
    )

    memory_manager = MemoryManager(
        window=MessageWindow(
            max_messages=20,
        ),
        summary=SummaryMemory(),
        profile=ProfileMemory(),
    )

    provider = FakeProvider()

    return ChatSession(
        provider=provider,
        prompt_service=prompt_service,
        memory_manager=memory_manager,
        summarizer=Summarizer(
            provider=provider,
        ),
    )


def test_send_message() -> None:
    session = create_session()

    response = session.send("你好")

    assert response.text == "你好，我是景愿。"

    # System + User + Assistant
    assert len(session.messages) == 3

    assert session.messages[0].role.value == "system"
    assert session.messages[1].content == "你好"
    assert session.messages[2].content == "你好，我是景愿。"


def test_clear_history() -> None:
    session = create_session()

    session.send("hello")

    assert len(session.messages) == 3

    session.clear()

    assert len(session.messages) == 0