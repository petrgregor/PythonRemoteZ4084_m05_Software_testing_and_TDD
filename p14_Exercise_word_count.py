"""Počítání slov
Implementujte funkci `word_count(s)`, která vrátí počet slov v daném řetězci.
A otestujte ji."""


def word_count(s):
    return len(str(s).split())


if __name__ == '__main__':
    s = """"Počítání slov
Implementujte funkci `word_count(s)`, která vrátí počet slov v daném řetězci. 
A otestujte ji."""
    print(word_count(s))
