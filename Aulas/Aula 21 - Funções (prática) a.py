def fatorial(num=1):
    """
    Retorna o fatorial do valor informado
    :param num: Número que se deseja saber o fatorial
    :return: Retorna o fatorial
    """
    f = 1
    for c in range(1, num + 1):
        f *= c
    return f


print(fatorial(5))
