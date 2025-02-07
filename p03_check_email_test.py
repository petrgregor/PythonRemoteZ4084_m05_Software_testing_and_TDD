import pytest
from p03_check_email import check_email_format


@pytest.fixture()
def provide_email():
    print("\nPříprava emailového účtu")
    yield "badmail.com"
    print("Úklid po testování")


def test_email_exception(provide_email):
    with pytest.raises(Exception):
        email = provide_email
        print(f"\nTest email: {email}")
        assert check_email_format(email)


"""
def test_email_exception():
    with pytest.raises(Exception):
        assert check_email_format("badmail.com")
"""

