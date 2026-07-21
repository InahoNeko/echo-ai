"""Runtime service registry."""

from __future__ import annotations

from typing import Any


class ServiceRegistry:
    """
    Registry for runtime services.

    Runtime owns the registry, but knows nothing about
    concrete service implementations.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}


    def add(self, name: str, service: Any) -> None:
        if name in self._services:
            raise ValueError(
                f"Service '{name}' already exists."
            )

        self._services[name] = service

    def get(self, name: str) -> Any:
        try:
            return self._services[name]
        except KeyError as exc:
            raise KeyError(
                f"Service '{name}' is not registered."
            ) from exc

    def contains(self, name: str) -> bool:
        return name in self._services