def moeda(n):
    n_format = f'R$ {n:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')
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


def resumo(n, aum, red):
    linha = '=' * 32

    print(linha)
    print(f'{"RESUMO DO VALOR":^32}')
    print(linha)
    print(f' {"Preço analisado"} \t{moeda(n)}')
    print(f' {"Dobro do valor"} \t{dobro(n, formatar=True)}')
    print(f' {"Metade do valor"} \t{metade(n, formatar=True)}')
    print(f' {aum}% de aumento \t{aumentar(n, aum, formatar=True)}')
    print(f' {red}% de redução \t{diminuir(n, red, formatar=True)}')
    print(linha)
