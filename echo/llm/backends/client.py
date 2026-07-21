from __future__ import annotations

from abc import ABC, abstractmethod

import httpx


from echo.llm.exceptions import (
    LLMAuthenticationError,
    LLMConnectionError,
    LLMProviderError,
    LLMRateLimitError,
    LLMResponseError,
)
class OpenAIClient(ABC):
    """
    Abstract client for OpenAI-compatible APIs.
    """

    @abstractmethod
    def chat(
        self,
        *,
        model: str,
        messages: list[ChatMessage],
    ) -> str:
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        """Release underlying resources."""
        raise NotImplementedError


class HttpOpenAIClient(OpenAIClient):
    """
    HTTP implementation of OpenAI-compatible API.
    """

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str,
        timeout: float = 60.0,
    ) -> None:

        self._client = httpx.Client(
            base_url=base_url.rstrip("/"),
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )

    def chat(
        self,
        *,
        model: str,
        messages: list[ChatMessage],
    ) -> str:

        payload = {
            "model": model,
            "messages": [
                {
                    "role": message.role.value,
                    "content": message.content,
                }
                for message in messages
            ],
        }

        try:
            response = self._client.post(
                "/chat/completions",
                json=payload,
            )

        except httpx.ConnectError as exc:
            raise LLMConnectionError(
                "Unable to connect to the LLM service."
            ) from exc

        except httpx.HTTPError as exc:
            raise LLMProviderError(str(exc)) from exc

        if response.status_code == 401:
            raise LLMAuthenticationError(
                "Authentication failed."
            )

        if response.status_code == 429:
            raise LLMRateLimitError(
                "Rate limit exceeded."
            )

        try:
            data = response.json()

            return data["choices"][0]["message"]["content"]

        except (KeyError, IndexError, TypeError) as exc:
            raise LLMResponseError(
                "Invalid response format."
            ) from exc



    def close(self) -> None:
        self._client.close()