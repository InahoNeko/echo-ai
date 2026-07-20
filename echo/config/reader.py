"""YAML configuration reader."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file.

    Args:
        path:
            Path to the YAML file.

    Returns:
        Parsed YAML data.

    Raises:
        FileNotFoundError:
            If the configuration file does not exist.

        ValueError:
            If the YAML root node is not a mapping.
    """

    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {path}"
        )

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if data is None:
        return {}

    if not isinstance(data, dict):
        raise ValueError(
            "Configuration root must be a mapping."
        )

    return data