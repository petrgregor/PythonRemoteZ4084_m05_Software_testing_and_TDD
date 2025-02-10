import pytest
from p06_factorial import fact, fact_r


def test_factorial():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6
    assert fact(6) == 720

    with pytest.raises(ValueError):
        assert fact(-5) == 1

    with pytest.raises(ValueError):
        assert fact(3.8) == 1

    with pytest.raises(ValueError):
        assert fact("pět") == 120


def test_factorial_r():
    assert fact_r(0) == 1
    assert fact_r(1) == 1
    assert fact_r(2) == 2
    assert fact_r(3) == 6
    assert fact_r(6) == 720

    with pytest.raises(ValueError):
        assert fact_r(-5) == 1

    with pytest.raises(ValueError):
        assert fact_r(3.8) == 1

    with pytest.raises(ValueError):
        assert fact_r("pět") == 120
