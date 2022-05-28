def moeda(n):
    """
    -> Formata o valor recebido como monetário

    :param n:  Número a ser analisado
    :return:   Retorna o valor formatado
    """

    n_format = f'R$ {n:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')
    return n_format


def aumentar(n, x, formatar=False):
    """
    -> Calcula o aumento de um número (em porcentagem)

    :param n:         número a ser aumentado
    :param x:         valor do aumento (%)
    :param formatar:  parâmetro opcional, se True ele retorna o valor formatado como monetário
    :return:          retorna o valor
    """

    new_n = n + (n / 100 * x)

    if formatar:
        new_n = moeda(new_n)
    return new_n


def diminuir(n, x, formatar=False):
    """
    -> Calcula a redução de um número (em porcentagem)

    :param n:         número a ser reduzido
    :param x:         valor da redução (%)
    :param formatar:  parâmetro opcional, se True ele retorna o valor formatado como monetário
    :return:          retorna o valor
    """

    new_n = n - (n / 100 * x)

    if formatar:
        new_n = moeda(new_n)
    return new_n


def dobro(n, formatar=False):
    """
    -> Retorna o dobro do valor inserido

    :param n:         número a ser calculado o dobro
    :param formatar:  parâmetro opcional. Se True, retorna o valor formatado como monetário
    :return:          retorna o dobro do valor inserido
    """

    new_n = n * 2

    if formatar:
        new_n = moeda(new_n)
    return new_n


def metade(n, formatar=False):
    """
    -> Retorna a metade do valor inserido

    :param n:         número a ser calculado a metade
    :param formatar:  parâmetro opcional. Se True, retorna o valor formatado como monetário
    :return:          retorna a metade do valor inserido
    """

    new_n = n / 2

    if formatar:
        new_n = moeda(new_n)
    return new_n


def resumo(n, aum, red):
    """
    -> Mostra para o usuário uma tabulação, com todos os cálculos do módulo. Dobro, metade, aumento e redução.

    :param n:    preço do produto a ser analisado
    :param aum:  porcentagem do aumento
    :param red:  porcentagem da redução
    :return:     sem retorno.
    """

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
