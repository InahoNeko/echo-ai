from __future__ import annotations

from .models import SummaryMemoryModel


class SummaryMemory:
    """
    Stores the conversation summary.
    """

    def __init__(self) -> None:
        self._model = SummaryMemoryModel()

    @property
    def content(self) -> str:
        """
        Current summary text.
        """
        return self._model.content

    def update(
        self,
        content: str,
    ) -> None:
        """
        Replace the current summary.
        """
        self._model.content = content

    def clear(self) -> None:
        """
        Clear the summary.
        """
        self._model.content = ""

    @property
    def model(self) -> SummaryMemoryModel:
        """
        Underlying summary model.
        """
        return self._model