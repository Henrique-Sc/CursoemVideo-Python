reset = '\033[m'
IRed = '\033[38;5;9m'
red = '\033[31m'
blue = '\033[34m'

numeros = list()
numeros_pares = list()
numeros_impares = list()

numeros.append(float(input('Digite algum número: ').strip()))
while True:
    esc = str(input(f'\nDeseja continuar? [{blue}Sim{reset} / {red}Não{reset}] ').strip().upper()[0])
    while esc not in 'SN':
        esc = str(input(f'\n{IRed}Valor inválido!{reset} Digite novamente: [{blue}Sim{reset} / {red}Não{reset}] ').strip().upper()[0])
    if esc == 'N':
        break
    print('')
    numeros.append(float(input('Digite outro número: ').strip()))
print('\n' + '---' * 11, '\n')

# ordenar o números
numeros.sort()

# números pares e ímpares
for valor in numeros:
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

print(f'''
Números digitados: {numeros}
Numeros PARES digitados: {numeros_pares}
Números ÍMPARES digitados: {numeros_impares}''')
