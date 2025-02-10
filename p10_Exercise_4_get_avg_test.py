""" Cvičení 4
Funkce get_avg bere ze souboru how_much čísla a počítá jejich průměr.
Otestuj funkci get_avg s vědomím, že očekává pouze čísla v souboru a nemůžeš
použít soubor k testování.
"""
from unittest.mock import MagicMock, patch

import pytest

from p10_Exercise_4_get_avg import *


def test_get_avg():
    # používáme původní _get_data funkci:
    #assert get_avg(3) == 2
    #assert get_avg(5) == 3

    fake_get_data = MagicMock(return_value="1")
    with patch("p10_Exercise_4_get_avg._get_data", fake_get_data):
        assert get_avg(1) == 1

    fake_get_data = MagicMock(return_value="12")
    with patch("p10_Exercise_4_get_avg._get_data", fake_get_data):
        assert get_avg(2) == 1.5

    fake_get_data = MagicMock(return_value="123")
    with patch("p10_Exercise_4_get_avg._get_data", fake_get_data):
        assert get_avg(3) == 2


parameters = [
    (1, 1),
    (2, 1.5),
    (3, 2),
    (4, 2.5),
    (5, 3),
    (6, 3.5),
    (7, 4),
    (8, 4.5),
    (9, 5)
]


@pytest.mark.parametrize("how_much, result", parameters)
def test_get_avg_param(how_much, result):
    r = ''
    for i in range(1, how_much + 1):
        r += str(i)
    fake_get_data = MagicMock(return_value=r)
    #fake_get_data = MagicMock(return_value=''.join(str(i) for i in range(1, how_much+1)))
    with patch("p10_Exercise_4_get_avg._get_data", fake_get_data):
        assert get_avg(how_much) == result
