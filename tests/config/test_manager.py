from echo.config import config


def test_runtime_config() -> None:
    assert config.runtime.name == "ECHO Runtime"
    assert config.runtime.version == "0.1.0-alpha"