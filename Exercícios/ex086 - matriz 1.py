print('--= Matriz em Python =--')
print('')

# from random import randint
# Declarando a lista que vai ser utilizada para armazenar os dados da matriz
matriz = [[], [], []]

# Laço para digitar e salvar os números na matriz
for row in range(0, 3):
    for item in range(0, 3):
        matriz[row].append(int(input(f'Digite um número para a posição [{row}, {item}]: ')))
        # matriz[row].append(randint(1, 999))

print()
print('=-' * 22)

# Exibindo os dados
print('\nMatriz:')
for row in matriz:
    for item in row:
        print(f'\t[{item:^5}]', end=' ')
    print()


# linha1 = [1, 2, 3]
# linha2 = [4, 5, 6]
# linha3 = [7, 8, 9]
# matriz = [linha1, linha2, linha3]
# for i, linha in enumerate(matriz):
#     for index, item in enumerate(linha):
#         linha[index] = int(input(f'Digite um número para a posição [{index + 1}, {i + 1}]: '))
# print('\n', '---' * 13)
# print(f'''\nMatriz:
# \t{linha1}
# \t{linha2}
# \t{linha3}''')
