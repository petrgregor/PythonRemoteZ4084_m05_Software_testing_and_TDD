import pytest
from p01_BasicCalculator import BasicCalculator


def test_addition():
    basic_calculator = BasicCalculator()
    result = basic_calculator.add(3, 5)
    assert result == 8
    assert basic_calculator.add(-6, -4) == -10
    assert basic_calculator.add(-3, 4) == 1
    assert basic_calculator.add(5, -6) == -1
    assert basic_calculator.add(5, 0) == 5
    assert round(basic_calculator.add(2.1, 3.2), 5) == 5.3
    assert round(basic_calculator.add(10, 5.3), 5) == 15.3
    assert basic_calculator.add("3", "5") is None
    assert basic_calculator.add("Hello", "World") is None
    assert basic_calculator.add(3, "5") is None
    assert basic_calculator.add([3], 5) is None


def test_subtraction():
    basic_calculator = BasicCalculator()
    result = basic_calculator.subtract(3, 5)
    assert result == -2
    assert basic_calculator.subtract(-6, -4) == -2
    assert basic_calculator.subtract(-3, 4) == -7
    assert basic_calculator.subtract(5, -6) == 11
    assert basic_calculator.subtract(5, 0) == 5
    assert round(basic_calculator.subtract(2.1, 3.2), 5) == -1.1
    assert round(basic_calculator.subtract(10, 5.3), 5) == 4.7
    assert basic_calculator.subtract("3", "5") is None
    assert basic_calculator.subtract("Hello", "World") is None
    assert basic_calculator.subtract(3, "5") is None
    assert basic_calculator.subtract([3], 5) is None
