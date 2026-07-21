"""LLM exceptions."""

from __future__ import annotations


class LLMError(Exception):
    """Base exception for all LLM related errors."""


class LLMConnectionError(LLMError):
    """Unable to connect to the LLM service."""


class LLMAuthenticationError(LLMError):
    """Authentication failed."""


class LLMRateLimitError(LLMError):
    """Rate limit exceeded."""


class LLMResponseError(LLMError):
    """Invalid response returned by the LLM."""


class LLMProviderError(LLMError):
    """Unexpected provider error."""