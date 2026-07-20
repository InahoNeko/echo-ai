from pathlib import Path

from echo.config.reader import load_yaml


def test_load_runtime_config() -> None:
    data = load_yaml(Path("configs/runtime.yaml"))

    assert "runtime" in data