print('\033[37m-=\033[m' * 5, '\033[31mFatoração de números inteiros\033[m', '\033[37m=-\033[m' * 5)
num = int(input('\nDigite algum número: ').strip())

if num <= 1:
    print('\n\033[31mDigite um número maior ou igual a 1\033[m')
else:
    f = 1
    # # Usando o For
    # for c in range(1, num + 1):
    #     f *= c
    # print(f'\nO resultado de {num}! é {f}')
    # print('Fórmula: ', end='')
    # for c in range(num, 0, -1):
    #     print(c, end='')
    #     print(' x ' if c > 1 else ' = ', end='')
    # print(f)

    # Usando o While
    c = num
    while c > 0:
        f *= c
        c -= 1
    print(f'\nO resultado de {num}! é {f}')
    print('Fórmula: ', end='')
    while num > 0:
        print(num, end='')
        print(' x ' if num > 1 else ' = ', end='')
        num = num - 1
    print(f)
