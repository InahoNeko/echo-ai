from echo.llm import ChatMessage, ChatResponse, Role


def test_chat_message() -> None:
    msg = ChatMessage(
        role=Role.USER,
        content="你好",
    )

    assert msg.role is Role.USER
    assert msg.content == "你好"


def test_chat_response() -> None:
    response = ChatResponse(
        text="你好，我是景愿。"
    )

    assert response.text == "你好，我是景愿。"