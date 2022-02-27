reset = '\033[m'
IRed = '\033[38;5;9m'
red = '\033[31m'
blue = '\033[34m'

numeros = list()
numeros.append(int(input('Digite algum número: ').strip()))
while True:
    esc = str(input(f'Deseja continuar? [{blue}Sim{reset} / {red}Não{reset}] ').strip().upper()[0])
    while esc not in 'SN':
        esc = str(input(f'\n{IRed}Valor inválido!{reset} Digite novamente: [{blue}Sim{reset} / {red}Não{reset}] ').strip().upper()[0])
    if esc == 'N':
        break

    numeros.append(int(input('Digite outro número: ').strip()))

print('\n' + '---' * 11, '\n')

# Quantidade de elementos
print(f'Foram digitados {len(numeros)} números')

# Ordem decrescente
numeros.sort(reverse=True)
print(f'Números digitados em ordem decrescente: {numeros}')

# Se o valor 5 está ou não na lista
print('O valor 5', end=' ')
if 5 in numeros:
    print('foi encontrado na lista')
else:
    print('não foi encontrado na lista')
