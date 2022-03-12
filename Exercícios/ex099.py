from time import sleep


def maior(*numeros):
    print('-=' * 17 + '-')
    sleep(0.5)
    print('Analisando os valores inseridos', end='')
    for c in '...':
        sleep(0.5)
        print(c, end='')
    sleep(0.5)

    print(f'\n  -> ', end='')
    print(*numeros, sep=' - ')
    sleep(1)

    if len(numeros) == 1:
        print(f'• Foi informado apenas {len(numeros)} número.')
    else:
        print(f'• Foram informados {len(numeros)} números.')
    sleep(0.5)
    print(f'• O maior número é o {max(numeros)}')

