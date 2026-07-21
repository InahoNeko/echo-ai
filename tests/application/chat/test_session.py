from echo.application.chat.session import ChatSession
from echo.llm import (
    ChatMessage,
    ChatResponse,
    LLMProvider,
)


class FakeProvider(LLMProvider):

    def chat(
        self,
        messages: list[ChatMessage],
    ) -> ChatResponse:

        return ChatResponse(
            text="你好，我是景愿。"
        )


def test_send_message() -> None:

    session = ChatSession(
        provider=FakeProvider()
    )

    response = session.send("你好")

    assert response.text == "你好，我是景愿。"

    assert len(session.messages) == 2

    assert session.messages[0].content == "你好"

    assert session.messages[1].content == "你好，我是景愿。"


def test_clear_history() -> None:

    session = ChatSession(
        provider=FakeProvider()
    )

    session.send("hello")

    assert len(session.messages) == 2

    session.clear()

    assert len(session.messages) == 0