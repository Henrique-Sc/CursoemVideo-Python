def moeda(n):
    n_format = f'R${n:.2f}'
    return n_format


def aumentar(n, x, formatar=False):
    new_n = n + (n / 100 * x)

    if formatar:
        new_n = moeda(new_n)
    return new_n


def diminuir(n, x, formatar=False):
    new_n = n - (n / 100 * x)

    if formatar:
        new_n = moeda(new_n)
    return new_n


def dobro(n, formatar=False):
    new_n = n * 2

    if formatar:
        new_n = moeda(new_n)
    return new_n


def metade(n, formatar=False):
    new_n = n / 2

    if formatar:
        new_n = moeda(new_n)
    return new_n
