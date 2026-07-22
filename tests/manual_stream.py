from echo.llm.backends import (
    OpenAIConfig,
    create_openai_provider,
)

from echo.llm import (
    ChatMessage,
    Role,
)

config = OpenAIConfig(
    base_url="http://127.0.0.1:11434/v1",
    api_key="ollama",
    model="qwen3:8b",
)

provider = create_openai_provider(config)

messages = [
    ChatMessage(
        role=Role.USER,
        content="你好",
    )
]

for chunk in provider._client.stream_chat(
    model=config.model,
    messages=messages,
):
    print(chunk, end="", flush=True)

print()