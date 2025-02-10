import pytest
from p06_factorial import fact, fact_r


@pytest.mark.parametrize(
    "number, result",  # definujeme názvy proměnných v tupple
    [(0, 1), (1, 1), (2, 2), (3, 6), (5, 120), (6, 720), (10, 3628800)]  # seznam hodnot, které se budou vkládat do assert
)
def test_fact(number, result):
    assert fact(number) == result
