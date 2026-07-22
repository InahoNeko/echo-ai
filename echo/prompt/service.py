from __future__ import annotations

from .builder import PromptBuilder
from .context import PromptContext
from .loader import PromptLoader


class PromptService:
    """
    High-level prompt service.
    """

    def __init__(
        self,
        loader: PromptLoader,
        builder: PromptBuilder,
    ) -> None:
        self._loader = loader
        self._builder = builder

    def build_system_prompt(self) -> str:
        template = self._loader.load("system")

        return self._builder.build(
            template=template,
            context=PromptContext(),
        )