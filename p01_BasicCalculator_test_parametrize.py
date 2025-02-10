import pytest
from p01_BasicCalculator import BasicCalculator


@pytest.mark.parametrize(
    "num1, num2, result",
    [(3, 5, 8), (-6, -4, -10), (-3, 4, 1), (5, -6, -1), (5, 0, 5)]
)
def test_addition(num1, num2, result):
    assert BasicCalculator().add(num1, num2) == result


parameters = [
    (3, 5, -2),
    (-6, -4, -2),
    (-3, 4, -7),
    (5, -6, 11),
    (5, 0, 5)
]

@pytest.mark.parametrize(
    "num1, num2, result",
    parameters
)
def test_subtraction(num1, num2, result):
    assert BasicCalculator().subtract(num1, num2) == result


parameters = [
    (2.1, 3.2, -1.1),
    (10, 5.3, 4.7)
]

@pytest.mark.parametrize(
    "num1, num2, result",
    parameters
)
def test_subtraction_float(num1, num2, result):
    assert BasicCalculator().subtract(num1, num2) == result
