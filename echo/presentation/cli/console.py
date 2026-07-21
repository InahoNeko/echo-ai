from __future__ import annotations

from echo.application.chat.session import ChatSession
from echo.llm import LLMError


def run_console(session: ChatSession) -> None:
    """
    Run the interactive console.
    """

    print()
    print("Type 'exit' or 'quit' to stop.")
    print()

    while True:

        try:
            text = input("You > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not text:
            continue

        if text.lower() in {"exit", "quit"}:
            break

        try:
            response = session.send(text)

        except LLMError as exc:
            print(f"\n[LLM ERROR] {exc}\n")
            continue

        print(f"\n景愿 > {response.text}\n")