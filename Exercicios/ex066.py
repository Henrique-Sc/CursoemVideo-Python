from time import sleep

reset = '\033[m'
red = '\033[31m'
IYellow = '\033[38;5;11m'

print(f'{red}~Obs: Digite 999 para parar{reset}')

# num = [float(input('\nDigite um número: ').strip())]
# while True:
#     num.append(float(input('Digite outro número: ').strip()))
#     if 999 in num:
#         num.remove(999)
#         break
cont = 1
total = float(input('\nDigite um número: ').strip())
while True:
    num = float(input('Digite outro número: ').strip())
    if num == 999:
        break
    total += num
    cont += 1

print(f'\n{IYellow}Analizando os dados digitados', end='')
sleep(0.5)
for c in '...':
    print(c, end='', flush=True)
    sleep(0.8)

# print(f'''\n\n{reset}Quantidades de números digitados: {len(num)}
# Soma dos números digitados: {sum(num)}''')
print(f'''\n\n{reset}Números digitados: {cont}
Soma total desses números: {total}''')
