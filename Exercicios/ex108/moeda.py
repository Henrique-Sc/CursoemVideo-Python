def moeda(n, moeda='R$'):
    n_format = f'{moeda} {n:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')
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
