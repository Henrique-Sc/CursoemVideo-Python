print('\033[34m-=\033[m' * 14)
print('\033[31mANALIZADOR DE NÚMEROS PRIMOS')
print('\033[34m-=\033[m' * 14)
num = int(input('\nDigite um número qualquer: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi dividido {cont} vezes')
if cont == 2:
    print(f'\n\033[34mÉ um número PRIMO!\033[m')
else:
    print('\n\033[31mNÃO é um número PRIMO\033[m')

# for c in range(1, num + 1):
#     if num % c == 0:
#         cont = cont + 1
# if cont == 2:
#     print(f'\nO número \033[4m{num}\033[m é \033[34mPRIMO!\033[m')
# else:
#     print(f'\nO número \033[4m{num}\033[m \033[31mNÃO É PRIMO!\033[m')
