# Faktoriál: https://cs.wikipedia.org/wiki/Faktori%C3%A1l
# n! = n * (n-1) * (n-2) * ... * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 1 * 2 * 3 * 4 * 5 = 120
# 0! = 1


def fact(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# pomocí rekurze
# n! = n * (n-1)!
# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!  STOP
# 0! = 0 * (-1)!  TOTO UŽ NEDÁVÁ SMYSL
def fact_r(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError
    if n == 0:
        return 1
    return n * fact_r(n-1)


if __name__ == '__main__':
    for n in range(1, 11):
        print(f"{n}! = {fact(n)}")
    print('-'*80)
    print(f"5! = {fact_r(5)}")
