"""ECHO runtime entry point."""

from .runtime import Runtime


def main() -> None:
    """Start ECHO runtime."""

    runtime = Runtime()

    print("=" * 32)
    print("         ECHO Runtime")
    print("=" * 32)

    print(f"Version : {runtime.version}")
    print(f"Status  : {runtime.status.value}")

    runtime.start()

    print()
    print(f"Status  : {runtime.status.value}")
    print("ECHO Runtime started.")


if __name__ == "__main__":
    main()