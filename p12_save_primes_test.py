import pytest

from p12_save_primes import find_n_primes, save_primes


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


# tmp_path je zabudovaná fixtura pro vytvoření dočasné složky
@pytest.fixture
def add_test_cases(tmp_path):
    """fixtura pro vytvoření dočasného souboru"""
    file_name = tmp_path / "test_primes.txt"  # setup - vytvoříme soubor
    print(f"Setup: dočasný soubor se jmenuje {file_name}")
    yield file_name
    print(f"Soubor {file_name} existuje: {file_name.exists()}")
    print(f"Smažeme dočasný soubor {file_name}")
    if file_name.exists():  # teardown
        file_name.unlink()  # smažeme soubor
    print(f"Soubor {file_name} existuje: {file_name.exists()}")


def test_save_primes(add_test_cases):
    """Testujeme uložení prvočísel do souboru"""
    n = 5
    save_primes(n, add_test_cases)

    # ověříme, že soubor existuje
    assert add_test_cases.exists()

    # otestujeme obsah souboru
    expected_primes = ["2\n", "3\n", "5\n", "7\n", "11\n"]
    with open(add_test_cases, 'r') as f:
        lines = f.readlines()

    assert lines == expected_primes
