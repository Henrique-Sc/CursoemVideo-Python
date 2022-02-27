from time import sleep

reset = '\033[m'
IRed = '\033[38;5;9m'
IBlue = '\033[38;5;12m'
red = '\033[31m'
gray = '\033[37m'

print(f'{gray}-=-={reset}', f'{red}Análise de 5 números', f'{gray}=-=-{reset}')
sleep(1)

numeros = list()
maior = int()

for a in range(1, 6):
    num = int(input(f'\nDigite o {a}º número: '))
    if a == 1:
        numeros.append(num)
    else:
        maior = 0
        for c in range(0, len(numeros)):
            if num >= numeros[c]:
                maior += 1
        numeros.insert(maior, num)

    if maior + 1 == len(numeros):
        print(f'Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {maior} da lista...')

print(f'\nNúmeros digitados: {numeros}')
