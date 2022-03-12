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


lista = list()
lista.append(float(input('Digite o primeiro número: ').strip()))
while True:
    esc = str(input('Deseja continuar? [Sim / Não] ')).strip().upper()[0]
    c = 0
    print()
    while esc not in 'SN':
        esc = str(input(f'Valor inválido! Digite "Sim" ou "Não": ')).strip().upper()[0]
        c += 1
    if c != 0:
        print()

    if esc == 'N':
        break
    else:
        pass
    lista.append(float(input('Digite outro número: ').strip()))
