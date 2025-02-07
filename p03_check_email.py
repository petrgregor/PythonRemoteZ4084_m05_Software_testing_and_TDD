import re


def check_email_format(email):
    """oveření jestli je formát zadaného emailu správný"""
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Nevalidní formát emailu")
    return "Email je v pořádku"


if __name__ == '__main__':
    print(check_email_format("petr@gregor.cz"))
    #print(check_email_format("petr@cz"))
