import pytest

from p12_save_primes import find_n_primes


parameters = [
    (0, []),
    (1, [2]),
    (2, [2, 3]),
    (3, [2, 3, 5]),
    (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
]


@pytest.mark.parametrize(
    "n, result",
    parameters
)
def test_find_n_primes(n, result):
    assert find_n_primes(n) == result
