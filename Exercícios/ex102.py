# Funções
def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: Número que deseja-se saber o seu fatorial
    :param show: Exibe ou não a conta (opcional)
    :return: Retorna o Fatorial
    """

    f = 1
    for c in range(1, n + 1):
        f *= c

        if show:  # show == True
            print(c, end='')
            if c < n:
                print(' x ', end='')
            else:
                print(' = ', end='')
            if c == n:
                print(f)

    return f


# Programa principal
print('-' * 25)
num = int(input('Digite um número: ').strip())
while True:
    esc = input('Deseja visualizar a conta? [Sim / Não]: ').strip().upper()[0]
    if esc not in 'SN':
        print('\nErro! Digite "S" ou "N"')
    else:
        break

if esc == 'S':
    esc = True
else:
    esc = False

print(fatorial(num, esc))
