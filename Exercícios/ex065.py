from time import sleep
reset = '\033[m'
red = '\033[31m'
IRed = '\033[38;5;9m'
blue = '\033[34m'
IYellow = '\033[38;5;11m'
IBlue = '\033[38;5;12m'

print(f'{red}-={reset}' * 4, 'Maiores e menores valores ', f'{red}=-{reset}' * 4)

num = [float(input('\nDigite um número: ').strip())]
num += [float(input('Digite outro número: '))]

escolha = str(input(f'\nDeseja continuar? [{blue}S{reset}/{red}N{reset}] ')).strip().upper()[0]
while escolha == 'S':
    num += [float(input('Digite outro número: '))]
    escolha = str(input(f'\nDeseja continuar? [{blue}S{reset}/{red}N{reset}] ')).strip().upper()[0]

print(f'\n{IYellow}Analizando os dados', end='')
sleep(0.8)
for c in f'...':  # Contagem dos pontos um por um
    print(c, end='', flush=True)
    sleep(0.8)

print(f'''\n\n{reset}Total de números analizados: {len(num)}
Maior número {max(num)}
Menor número: {min(num)}

{IBlue}Média dos valores: {sum(num) / len(num):.1f}''')
