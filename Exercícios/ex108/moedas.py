def moeda(n):
    n_format = f'R${n:,.2f}'.replace('.', ',')
    return n_format


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
