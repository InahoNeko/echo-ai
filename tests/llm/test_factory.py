from echo.llm.backends import (
    OpenAIConfig,
    OpenAIProvider,
    create_openai_provider,
)


def test_create_openai_provider() -> None:
    config = OpenAIConfig(
        base_url="http://localhost:11434/v1",
        api_key="ollama",
        model="qwen3:8b",
    )

    provider = create_openai_provider(config)

    assert isinstance(provider, OpenAIProvider)

    assert provider.model == "qwen3:8b"