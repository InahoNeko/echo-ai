from __future__ import annotations

from pathlib import Path

from echo.config.reader import load_yaml
from echo.config.schema import RuntimeConfig


class ConfigurationManager:
    """Configuration manager."""

    def __init__(self, config_dir: Path) -> None:
        runtime_data = load_yaml(config_dir / "runtime.yaml")

        runtime = runtime_data["runtime"]

        self.runtime = RuntimeConfig(
            name=runtime["name"],
            version=runtime["version"],
        )