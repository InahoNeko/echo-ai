from echo.llm.exceptions import (
    LLMAuthenticationError,
    LLMConnectionError,
    LLMError,
    LLMProviderError,
    LLMRateLimitError,
    LLMResponseError,
    LLMTimeoutError,
)


def test_exception_inheritance() -> None:
    assert issubclass(LLMConnectionError, LLMError)
    assert issubclass(LLMTimeoutError, LLMError)
    assert issubclass(LLMAuthenticationError, LLMError)
    assert issubclass(LLMRateLimitError, LLMError)
    assert issubclass(LLMResponseError, LLMError)
    assert issubclass(LLMProviderError, LLMError)