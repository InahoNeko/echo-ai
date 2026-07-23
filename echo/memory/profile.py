from __future__ import annotations

from .models import UserProfile


class ProfileMemory:
    """
    Stores long-term user profile information.
    """

    def __init__(self) -> None:
        self._model = UserProfile()

    @property
    def model(self) -> UserProfile:
        """
        Return the underlying profile model.
        """
        return self._model

    @property
    def name(self) -> str | None:
        return self._model.name

    @property
    def preferences(self) -> list[str]:
        return self._model.preferences

    @property
    def facts(self) -> list[str]:
        return self._model.facts

    @property
    def projects(self) -> list[str]:
        return self._model.projects

    def clear(self) -> None:
        """
        Reset the profile.
        """
        self._model = UserProfile()