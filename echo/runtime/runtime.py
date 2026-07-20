"""Core runtime implementation."""

from __future__ import annotations

from .lifecycle import LifecycleState
from .module import EchoModule


class EchoRuntime:
    """Core runtime of the ECHO system.

    Responsibilities:
        - Manage runtime lifecycle
        - Register modules
        - Initialize modules
        - Start modules
        - Stop modules
    """

    def __init__(self) -> None:
        self._state = LifecycleState.CREATED
        self._modules: dict[str, EchoModule] = {}

    @property
    def state(self) -> LifecycleState:
        """Return current runtime state."""
        return self._state

    def register(self, module: EchoModule) -> None:
        """Register a runtime module.

        Raises:
            ValueError:
                If a module with the same name has already
                been registered.
        """

        if self._state is not LifecycleState.CREATED:
            raise RuntimeError(
                "Modules can only be registered before the runtime starts."
            )

        if module.name in self._modules:
            raise ValueError(
                f"Module '{module.name}' is already registered."
            )

        self._modules[module.name] = module

    def start(self) -> None:
        """Start runtime."""

        if self._state is LifecycleState.RUNNING:
            return

        self._state = LifecycleState.INITIALIZING

        for module in self._modules.values():
            module.initialize()

        for module in self._modules.values():
            module.start()

        self._state = LifecycleState.RUNNING

    def stop(self) -> None:
        """Stop runtime."""

        if self._state is LifecycleState.STOPPED:
            return

        self._state = LifecycleState.STOPPING

        for module in reversed(list(self._modules.values())):
            module.stop()

        self._state = LifecycleState.STOPPED