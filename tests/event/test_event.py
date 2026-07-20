from echo.event import Event


def test_create_event() -> None:
    event = Event.create()

    assert event.event_id is not None
    assert event.created_at is not None