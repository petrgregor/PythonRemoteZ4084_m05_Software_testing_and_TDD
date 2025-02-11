import pytest

from p14_Exercise_word_count import word_count


params = [
    ("", 0),
    ("Ahoj", 1),
    ("Ahoj, jak se máš?", 4),
    ("Hello      this    is    a    test   ", 5),
    (123, 1)
]


@pytest.mark.parametrize("s, result", params)
def test_word_count(s, result):
    assert word_count(s) == result
