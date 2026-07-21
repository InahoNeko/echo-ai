from __future__ import annotations
from echo.llm.backends import OpenAIConfig

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

        llm = runtime_data["llm"]

        self.llm = OpenAIConfig(
            base_url=llm["base_url"],
            api_key=llm["api_key"],
            model=llm["model"],
            timeout=llm.get("timeout", 60.0),
        )