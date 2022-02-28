# from random import randint

# Código de cores
reset = '\033[m'
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
IWhite = '\033[38;5;15m'

# Título e introdução
print(f'{IWhite}=-=- Contador de números pares -=-={reset}\n')
print('↓ Digite seis números inteiros nos campos abaixo ↓\n')

# Salvando os dados inseridos em uma lista, se eles forem PAR
nums = list()
for c in range(6):
    # ---- Testes ----
    # num = randint(1, 10)
    # print(f'{yellow}{c + 1}º{reset} número: {num}')
    
    num = int(input(f'{yellow}{c + 1}º{reset} número: ').strip())
    
    if num % 2 == 0:
        nums.append(num)

# Print voltado para desing no terminal
print('\n=-=-=-=-=-=-=-=-=-=\n')

# Resultado
if len(nums) == 0:
    print('Nenhum número PAR digitado, não é possível realizar os cálculos...')
    
elif len(nums) == 1:
    print(f'Apenas um valor PAR digitado {nums}, não é possível realizar os cálculos...')
    
else:
    print(f'Foram digitados {len(nums)} números PARES {nums}. A soma entre eles é {sum(nums)}!')
    
# ---- CÓDIGO ANTIGO ----

# soma = 0
# cont = 0
# for c in range(1, 7):
#     num = int(input(f'{c}° Número: '))
#     if num % 2 == 0:
#         soma += num
#         cont = cont + 1
# if cont == 1 or cont == 0:
#     if cont == 1:
#         print("\033[31m\nComo tem apenas um valor PAR, não é possivel efetuar uma soma\033[m")
#     else:
#         print("\033[31m\nNão foi digitado nenhum valor que seja PAR")
# else:
#     print(f'\033[34m\nA soma de todos os valores pares ({cont}) é {soma}\033[m')
