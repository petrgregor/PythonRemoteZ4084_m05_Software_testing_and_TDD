"""
Napište funkci, která má dva parametry:
- n - počet nalezených prvočísel
- file_name - název souboru, do kterého se uloží výsledek

Funkce nalezne prvních n prvočísel a uloží je do souboru s názvem 'file_name'.
"""
from p07_prime import is_prime


def find_n_primes(n):
    """Najde prvních n prvočísel"""
    primes = []
    num = 0
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def save_primes(n, file_name):
    """Uloží nalezených n prvočísel do souboru"""
    primes = find_n_primes(n)
    with open(file_name, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")


if __name__ == '__main__':
    print(find_n_primes(10))
    save_primes(20, 'primes20.txt')
