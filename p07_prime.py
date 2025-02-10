# https://cs.wikipedia.org/wiki/Prvo%C4%8D%C3%ADslo
# Definujte funkci is_prime(n), která vrací True, pokud je zadané číslo prvočíslo.
# Prvočíslo je číslo, které má přesně dva dělitele a to jedničku a samu sebe.
# 5 je prvočíslo, protože je dělitelné beze zbytku pouze čísly 1 a 5.
# 2 je prvočíslo, protože je dělitelná beze zbytku pouze čísly 1 a 2.
# 4 není prvočíslo, protože je dělitelná beze zbytku čísly 1, 2 a 4.
# 1 není prvočíslo, protože je beze zbytku dělitelná pouze jedním číslem 1.


def is_prime(n):
    # TODO: použitý algoritmus není optimální, zkuste ho vylepšit
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(20):
        if is_prime(i):
            print(f"{i} je prvočíslo")
        else:
            print(f"{i} není prvočíslo")
