from echo.logger import get_logger


def test_logger_singleton() -> None:
    logger1 = get_logger("runtime")
    logger2 = get_logger("runtime")

    assert logger1 is logger2