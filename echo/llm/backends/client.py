from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator

import httpx

from echo.llm import ChatMessage
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
        """
        Generate a complete response.
        """
        raise NotImplementedError

    @abstractmethod
    def stream_chat(
        self,
        *,
        model: str,
        messages: list[ChatMessage],
    ) -> Iterator[str]:
        """
        Stream response chunks.
        """
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        """
        Release underlying resources.
        """
        raise NotImplementedError


class HttpOpenAIClient(OpenAIClient):
    """
    HTTP implementation of an OpenAI-compatible API.
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

    def _build_payload(
        self,
        *,
        model: str,
        messages: list[ChatMessage],
        stream: bool,
    ) -> dict:
        """
        Build request payload.
        """

        return {
            "model": model,
            "stream": stream,
            "messages": [
                {
                    "role": message.role.value,
                    "content": message.content,
                }
                for message in messages
            ],
        }

    def chat(
        self,
        *,
        model: str,
        messages: list[ChatMessage],
    ) -> str:
        """
        Send a non-streaming chat request.
        """

        payload = self._build_payload(
            model=model,
            messages=messages,
            stream=False,
        )

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
            raise LLMProviderError(
                str(exc)
            ) from exc

        if response.status_code == 401:
            raise LLMAuthenticationError(
                "Authentication failed."
            )

        if response.status_code == 429:
            raise LLMRateLimitError(
                "Rate limit exceeded."
            )

        response.raise_for_status()

        try:
            data = response.json()

            content = data["choices"][0]["message"]["content"]

        except (KeyError, IndexError, TypeError) as exc:
            raise LLMResponseError(
                "Invalid response format."
            ) from exc

        if not isinstance(content, str):
            raise LLMResponseError(
                "Invalid response content."
            )

        return content

    def stream_chat(
            self,
            *,
            model: str,
            messages: list[ChatMessage],
    ) -> Iterator[str]:
        """
        Send a streaming chat request.
        """

        payload = self._build_payload(
            model=model,
            messages=messages,
            stream=True,
        )

        try:
            with self._client.stream(
                    "POST",
                    "/chat/completions",
                    json=payload,
            ) as response:

                if response.status_code == 401:
                    raise LLMAuthenticationError(
                        "Authentication failed."
                    )

                if response.status_code == 429:
                    raise LLMRateLimitError(
                        "Rate limit exceeded."
                    )

                response.raise_for_status()

                for line in response.iter_lines():

                    if not line:
                        continue

                    if not line.startswith("data: "):
                        continue

                    data = line[6:]

                    if data == "[DONE]":
                        break

                    try:
                        import json

                        chunk = json.loads(data)

                        delta = (
                            chunk["choices"][0]
                            .get("delta", {})
                            .get("content")
                        )

                        if delta:
                            yield delta

                    except (
                            json.JSONDecodeError,
                            KeyError,
                            IndexError,
                            TypeError,
                    ):
                        continue

        except httpx.ConnectError as exc:
            raise LLMConnectionError(
                "Unable to connect to the LLM service."
            ) from exc

        except httpx.HTTPError as exc:
            raise LLMProviderError(
                str(exc)
            ) from exc

    def close(self) -> None:
        """
        Close the HTTP client.
        """

        self._client.close()