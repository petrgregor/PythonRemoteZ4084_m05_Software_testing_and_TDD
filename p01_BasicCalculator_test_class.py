import pytest
from p01_BasicCalculator import BasicCalculator


class Test:
    def setup_method(self):
        print("setup_method: Tato metoda se spustí jednou na začátku každého testu "
              "a slouží k nastavení prostředí pro test.")

    def teardown_method(self):
        print("teardown_method: Tato metoda se spustí na konci každého testu "
              "a slouží k vyčištění testovacího prostředí.")

    def test_addition(self):
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

    def test_subtraction(self):
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

    def test_multiply(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.multiply(3, 5)
        assert result == 15
        assert basic_calculator.multiply(-6, -4) == 24
        assert basic_calculator.multiply(-3, 4) == -12
        assert basic_calculator.multiply(5, -6) == -30
        assert basic_calculator.multiply(5, 0) == 0
        assert round(basic_calculator.multiply(2.1, 3.2), 5) == 6.72
        assert round(basic_calculator.multiply(10, 5.3), 5) == 53
        assert basic_calculator.multiply("3", "5") is None
        assert basic_calculator.multiply("Hello", "World") is None
        assert basic_calculator.multiply(3, "5") is None
        assert basic_calculator.multiply([3], 5) is None

    @pytest.mark.skip("Test dělení chci přeskočit.")
    def test_divide(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.divide(6, 3)
        assert result == 2
        assert basic_calculator.divide(-6, -2) == 3
        assert basic_calculator.divide(-3, 3) == -1
        assert basic_calculator.divide(6, -6) == -1
        assert round(basic_calculator.divide(2.1, 3.2), 5) == 0.65625
        assert round(basic_calculator.divide(11.25, 2.25), 5) == 5
        assert basic_calculator.divide("3", "5") is None
        assert basic_calculator.divide("Hello", "World") is None
        assert basic_calculator.divide(3, "5") is None
        assert basic_calculator.divide([3], 5) is None

        # assert basic_calculator.divide(5, 0) == 5
        # testování výjimky
        with pytest.raises(ZeroDivisionError):
            assert basic_calculator.divide(5, 0)
