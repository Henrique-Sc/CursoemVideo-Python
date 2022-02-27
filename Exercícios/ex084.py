reset = '\033[m'
red = '\033[31m'
blue = '\033[34m'
IRed = '\033[38;5;9m'
IYellow = '\033[38;5;11m'
IGreen = '\033[38;5;10m'
IBlue = '\033[38;5;12m'

dados_total = list()
temp = list()
maior = menor = 0
cont = 1

while True:
    print(f'{IRed}-=-={reset} {cont}ª PESSOA {IRed}=-=-{reset}')

    temp.append(str(input('Primeiro nome: ').strip().title()))
    temp.append(float(input('Digite seu peso: ').strip()))

    if cont == 1:
        maior = menor = temp[1]
    elif temp[1] > maior:
        maior = temp[1]
    elif temp[1] < menor:
        menor = temp[1]
    dados_total.append(temp[:])
    temp.clear()

    esc = input(f'\nDeseja continuar? [{blue}Sim{reset} / {red}Não{reset}] ').strip().upper()[0]
    print('')
    while esc not in 'SN':
        esc = input(f'{IRed}Valor incorreto!{reset} Digite novamente: [{blue}Sim{reset} / {red}Não{reset}] ').strip().upper()[0]
    print('')

    if esc == 'N':
        break
    cont += 1
print('=-' * 15)

# Exibindo os dados
print(f'\nAo todo, foram cadastrados {len(dados_total)} pessoas.')
print(f'''\nO {red}maior peso{reset} foi de {IBlue}{maior:.2f}Kg{reset}
Peso de: ''', end='')
for dados in dados_total:
    if dados[1] == maior:
        print(f'{IYellow}[{dados[0]}]{reset}', end=' ')

print(f'''\n\nO {IGreen}menor peso{reset} foi de {IBlue}{menor:.2f}Kg{reset}
Peso de: ''', end='')
for dados in dados_total:
    if dados[1] == menor:
        print(f'{IYellow}[{dados[0]}]{reset}', end=' ')
