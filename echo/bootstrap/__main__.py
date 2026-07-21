"""ECHO runtime entry point."""

from __future__ import annotations

from pathlib import Path

from echo.application.chat.session import ChatSession
from echo.config.manager import ConfigurationManager
from echo.llm.backends import create_openai_provider
from echo.presentation.cli import run_console
from echo.runtime.runtime import EchoRuntime


def main() -> None:
    """Start ECHO runtime."""

    # Runtime
    runtime = EchoRuntime()

    # Configuration
    config = ConfigurationManager(
        Path("configs"),
    )

    # LLM
    provider = create_openai_provider(
        config.llm,
    )

    # Register services
    runtime.services.add(
        "llm",
        provider,
    )

    # Chat
    session = ChatSession(provider)

    print("=" * 32)
    print(f"  {config.runtime.name}")
    print("=" * 32)
    print(f"Version : {config.runtime.version}")

    runtime.start()

    print("Status  : RUNNING")
    print()

    try:
        run_console(session)
    finally:
        provider.close()
        runtime.stop()

        print()
        print("ECHO Runtime stopped.")


if __name__ == "__main__":
    main()