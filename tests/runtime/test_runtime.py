"""Tests for EchoRuntime."""

from __future__ import annotations

from echo.runtime.lifecycle import LifecycleState
from echo.runtime.module import EchoModule
from echo.runtime.runtime import EchoRuntime


class DummyModule(EchoModule):
    """A simple module used for testing."""

    def __init__(self) -> None:
        self.events: list[str] = []

    @property
    def name(self) -> str:
        return "dummy"

    def initialize(self) -> None:
        self.events.append("initialize")

    def start(self) -> None:
        self.events.append("start")

    def stop(self) -> None:
        self.events.append("stop")


def test_register_module() -> None:
    runtime = EchoRuntime()
    runtime.register(DummyModule())

    assert len(runtime._modules) == 1
    
@property
def modules(self) -> tuple[EchoModule, ...]:
    return tuple(self._modules.values())


def test_duplicate_module_registration() -> None:
    runtime = EchoRuntime()

    runtime.register(DummyModule())

    try:
        runtime.register(DummyModule())
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_runtime_start() -> None:
    runtime = EchoRuntime()

    module = DummyModule()

    runtime.register(module)

    runtime.start()

    assert runtime.state is LifecycleState.RUNNING
    assert module.events == [
        "initialize",
        "start",
    ]


def test_runtime_stop() -> None:
    runtime = EchoRuntime()

    module = DummyModule()

    runtime.register(module)

    runtime.start()
    runtime.stop()

    assert runtime.state is LifecycleState.STOPPED

    assert module.events == [
        "initialize",
        "start",
        "stop",
    ]