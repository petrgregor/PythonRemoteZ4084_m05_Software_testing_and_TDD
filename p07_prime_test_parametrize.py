import pytest
from p07_prime import is_prime


parameters = [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (100, False),
    (101, True),
    (997, True),
    (1000, False),
    (-2, False)
]


@pytest.mark.parametrize(
    "n, result",
    parameters
)
def test_is_prime(n, result):
    assert is_prime(n) is result


parameters = [
    ("2",), ("Hi",), (2.2,), ([5],)
]


@pytest.mark.parametrize("n", parameters)
def test_is_prime_exception(n):
    with pytest.raises(TypeError):
        is_prime(n)
