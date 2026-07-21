from __future__ import annotations

from .client import HttpOpenAIClient
from .config import OpenAIConfig
from .openai import OpenAIProvider


def create_openai_provider(
    config: OpenAIConfig,
) -> OpenAIProvider:
    """
    Create an OpenAI-compatible provider.

    This is the single entry point for constructing the provider
    and its underlying HTTP client.
    """

    client = HttpOpenAIClient(
        base_url=config.base_url,
        api_key=config.api_key,
        timeout=config.timeout,
    )

    return OpenAIProvider(
        config=config,
        client=client,
    )