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
        except UnicodeDecodeError:
            print("\n[Input Error] Failed to decode terminal input.")
            continue

        if not text:
            continue

        if text.lower() in {"exit", "quit"}:
            break

        try:

            print()
            print("景愿 > ", end="", flush=True)

            for chunk in session.stream(text):
                print(chunk, end="", flush=True)

            print("\n")

        except LLMError as exc:
            print(f"\n[LLM ERROR] {exc}\n")
            continue