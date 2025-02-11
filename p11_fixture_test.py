import pytest

from p11_fixture_add import add


# test 1 pomocí parametrů (bez fixtury)
@pytest.mark.parametrize("num1, num2, result",
                         [(1, 2, 3), (0, -1, -1), (10, 20, 30)])
def test_addition(num1, num2, result):
    assert add(num1, num2) == result


# @pytest.fixture(scope='module') může mít různý scope ("platnost"):
# - function (default) - vytvoří se pro každou funkci zvlášť
# - module - vytvoří se jednou na celý soubor
# - session - vytvoří se jednou pro celou testovací session


# test 2 pomocí fixtury bez parametrů
@pytest.fixture(scope='module')
def add_test_cases():
    print("\nGeneruji vstupní parametry pro testování")
    yield [(1, 2, 3), (0, -1, -1), (10, 20, 30)]
    print("\nUklízím po testování")


def test_addition_fixture(add_test_cases):
    for num1, num2, result in add_test_cases:
        assert add(num1, num2) == result


# test 3 pomocí fixtury s parametry
@pytest.fixture(scope='module', params=[(1, 2, 3), (0, -1, -1), (10, 20, 30)])
def add_test_cases_params(request):
    print(f"\nsetup...")
    yield request.param
    print(f"\nteardown...")


def test_addition_fixture_params(add_test_cases_params):
    num1, num2, result = add_test_cases_params
    assert add(num1, num2) == result
