from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PromptContext:
    """
    Runtime context used to build prompts.

    New fields will be added over time, for example:

        - memory
        - persona
        - environment
        - tools
    """