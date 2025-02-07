from unittest.mock import MagicMock, patch

from p04_get_only_numbers import get_only_numbers


def test_read_only_numbers():
    #bez mock - pracujeme přímo se souborem "aa"
    #assert get_only_numbers() == '15|2|8|6|5|12|25|215|19563|5|8|12|7'

    test_data = ["Hello World",
                 "15,2,8",
                 "Hi,9",
                 '5,12,25,215,19563,"101"',
                 "5",
                 "Ahoj",
                 "8",
                 "12",
                 '"18"',
                 "7"]
    expected = '15|2|8|9|5|12|25|215|19563|5|8|12|7'

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data  # nahradí návratovou honotu metody get_data ve třídě API
    #fake_api.get_file.return_value = 'aa'  # toto nic nedělá
    with patch("p04_get_only_numbers.API", fake_api):
        assert get_only_numbers() == expected
