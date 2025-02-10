import pytest
from p07_prime import is_prime


def test_is_prime():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(997) is True

    assert is_prime(-2) is False

    with pytest.raises(TypeError):
        assert is_prime("2") is True
        assert is_prime(5) is False  # tento řádek je nedostupný, předchozí řádek vyvolá výjimku

    with pytest.raises(TypeError):
        assert is_prime(2.2) is True

