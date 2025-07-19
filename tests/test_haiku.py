from haiku_bot.haiku import is_haiku_size, to_haiku


HAIKU = "An old silent pond a frog jumps into the pond splash silence again"


def test_is_haiku_size_true():
    assert is_haiku_size(HAIKU)


def test_is_haiku_size_false():
    assert not is_haiku_size("short")


def test_to_haiku():
    lines = to_haiku(HAIKU)
    assert lines == [
        "An old silent pond",
        "a frog jumps into the pond",
        "splash silence again",
    ]
