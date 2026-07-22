from __future__ import annotations

from .context import PromptContext


class PromptBuilder:
    """
    Build the final prompt from a template
    and runtime context.
    """

    def build(
        self,
        *,
        template: str,
        context: PromptContext,
    ) -> str:
        return template