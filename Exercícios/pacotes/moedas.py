from builtins import print


def aumentar(n, x):
    new_n = n / 100 * x
    return n + new_n


def diminuir(n, x):
    new_n = n / 100 * x
    return n - new_n


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


print(aumentar(100, 10))
print(diminuir(100, 10))
print(dobro(10))
print(metade(50))