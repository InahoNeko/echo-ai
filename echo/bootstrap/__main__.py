"""ECHO runtime entry point."""

from __future__ import annotations

from echo.memory import Summarizer
from echo.memory import (
    MemoryManager,
    MessageWindow,
    SummaryMemory,
    ProfileMemory,
)

from echo.application.chat.session import ChatSession
from echo.config.manager import ConfigurationManager
from echo.llm.backends import create_openai_provider
from echo.presentation.cli import run_console
from echo.runtime.runtime import EchoRuntime

from pathlib import Path

from echo.prompt import (
    PromptBuilder,
    PromptLoader,
    PromptService,
)


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

    loader = PromptLoader(
        Path("echo/prompt"),
    )

    builder = PromptBuilder()

    summarizer = Summarizer(
        provider,
    )

    prompt_service = PromptService(
        loader=loader,
        builder=builder,
    )

    memory_manager = MemoryManager(
        window=MessageWindow(
            max_messages=20,
        ),
        summary=SummaryMemory(),
        profile=ProfileMemory(),
    )




    session = ChatSession(
        provider=provider,
        prompt_service=prompt_service,
        memory_manager=memory_manager,
        summarizer=summarizer,
    )
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