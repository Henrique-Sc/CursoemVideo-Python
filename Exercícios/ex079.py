from time import sleep

reset = '\033[m'
IRed = '\033[38;5;9m'
IGreen = '\033[38;5;10m'
IYellow = '\033[38;5;11m'
red = '\033[31m'
blue = '\033[34m'

numeros = list()

while True:
    num = int(input('Digite um número: ').strip())
    sleep(0.3)
    if num in numeros:
        print(f'\n{IYellow}Número já adicionado, valor desconsiderado.{reset}')
    else:
        numeros.append(num)
        print(f'\n{IGreen}Número adicionado com sucesso!{reset}')
    sleep(0.7)

    esc = str(input(f'\nDeseja continuar? [{blue}Sim{reset} / {red}Não{reset}] ').strip().upper()[0])
    while esc not in 'SN':
        esc = str(input(f'\n{IRed}Valor inválido!{reset} Digite novamente: [{blue}Sim{reset} / {red}Não{reset}] ').strip().upper()[0])
    if esc == 'N':
        break
    print('')

    sleep(0.5)

sleep(0.5)
print('')
print('---' * 11, '\n')
sleep(0.5)

nums_crescente = numeros[:]
nums_crescente.sort()
print(f'Números digitados: {nums_crescente}')
