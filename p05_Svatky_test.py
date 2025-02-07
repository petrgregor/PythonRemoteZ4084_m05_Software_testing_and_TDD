from unittest.mock import MagicMock, patch

from p05_Svatky import NameDays


def test_get_name():
    # bez Mock
    name_days = NameDays("https://svatky.adresa.info/")
    assert name_days.get_name("2002") == "Oldřich"


def test_get_name_mock():
    fake_api = MagicMock()
    fake_api.get_name.return_value = "Zikmund"

    with patch("p05_Svatky.NameDays.get_name", fake_api):
        name_days = NameDays("https://svatky.adresa.info/")
        assert name_days.get_name("0205")
