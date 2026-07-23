from __future__ import annotations

from echo.llm import (
    ChatMessage,
    LLMProvider,
    Role,
)


class Summarizer:
    """
    Generates conversation summaries using an LLM.
    """

    def __init__(
        self,
        provider: LLMProvider,
    ) -> None:
        self._provider = provider

    def summarize(
            self,
            previous_summary: str,
            messages: list[ChatMessage],
    ) -> str:
        """
        Generate a new summary from the previous summary
        and recent conversation.
        """

        prompt = self._build_prompt(
            previous_summary,
            messages,
        )

        response = self._provider.chat(
            [
                ChatMessage(
                    role=Role.SYSTEM,
                    content="You are a conversation summarizer.",
                ),
                ChatMessage(
                    role=Role.USER,
                    content=prompt,
                ),
            ]
        )

        return response.text

    def _build_prompt(
        self,
        summary: str,
        messages: list[ChatMessage],
    ) -> str:
        """
        Build the summarization prompt.
        """

        conversation = "\n".join(
            f"{message.role.value}: {message.content}"
            for message in messages
        )

        return f"""
Previous Summary:

{summary}

Recent Conversation:

{conversation}

You are updating the long-term conversation memory.

Requirements:

- Keep only important facts.
- Remove duplicated information.
- Preserve user preferences.
- Preserve long-term goals.
- Discard casual small talk.
- Keep the summary concise.
""".strip()