from haiku_bot.haiku import is_haiku_size, to_haiku


def test_is_haiku_size_true():
    assert is_haiku_size("abcdefg hijklmn opq")


def test_is_haiku_size_false():
    assert not is_haiku_size("short")


def test_to_haiku():
    message = "a" * 17
    lines = to_haiku(message)
    assert lines == ["aaaaa", "aaaaaaa", "aaaaa"]
