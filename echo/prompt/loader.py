from __future__ import annotations

from pathlib import Path


class PromptLoader:
    """
    Load prompt templates from disk.
    """

    def __init__(self, root: Path) -> None:
        self._root = root

    def load(self, name: str) -> str:
        path = self._root / f"{name}.md"

        return path.read_text(
            encoding="utf-8",
        )