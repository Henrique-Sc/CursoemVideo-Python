from time import sleep


def maior(*numeros):
    # Linha bonita :)
    print('-=' * 17 + '-')

    sleep(0.5)

    # Print com pontinhos sendo exibidos a cada 0.5 segundos
    print('Analisando os valores inseridos', end='')
    for p in '...':
        sleep(0.5)
        print(p, end='')
    sleep(0.5)

    # Mostrar os números inseridos
    print(f'\n  -> ', end='')
    print(*numeros, sep=' - ')
    sleep(1)
    print('')

    # Análise dos dados
    if len(numeros) == 1:
        print(f'• Foi informado apenas {len(numeros)} número.')
    else:
        print(f'• Foram informados {len(numeros)} números.')
    sleep(0.5)
    print(f'• O maior número é o {max(numeros)}')
    sleep(0.5)

    # Linha bonita :)
    print('-=' * 17 + '-')
    sleep(0.5)



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
maior(*lista)

print('<- Fim da execução :) ->')