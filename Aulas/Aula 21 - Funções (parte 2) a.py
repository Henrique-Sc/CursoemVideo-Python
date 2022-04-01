# Interactive Help no Python
print(input.__doc__)
help(input)


def contador1(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.

    :param i: Início da contagem
    :param f: Final da contagem
    :param p: Passo da contagem
    :return: sem retorno
    """

    for c in range(i, f + 1, p):
        print(c, end=' → ')
    print('FIM')


contador1(1, 10, 1)
print(contador1.__doc__)
