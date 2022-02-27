from random import randint

print('--= Matriz em Python =--')
print('')

# Declarando a lista que vai ser utilizada para armazenar os dados da matriz
matriz = [[], [], []]

# Laço para digitar e salvar os números na matriz

for row in range(0, 3):
    for item in range(0, 3):
        matriz[row].append(int(input(f'Digite um número para a posição [{row}, {item}]: ')))
        # matriz[row].append(randint(1, 10))

print()
print('=-' * 22)
column = 0

# Exibindo e analizando a matriz
tot_par = sum_third_column = max_second_row = 0
print('\nMatriz: ')
for row in matriz:
    for item in row:
        print(f'\t[{item:^5}]', end=' ')

        # Somas de todos os valores pares digitados
        if item % 2 == 0:
            tot_par += item

        # Maior valor da segunda linha
        max_second_row = max(matriz[1])

    # Soma dos valores da terceira coluna
    sum_third_column += row[2]
    print()
print()
print('=-' * 22)

# Exibição da análise da matriz
print(f'''\nAnálise da Matriz:
    1. A soma de todos os valores pares digitados: {tot_par}
    2. A soma dos valores da terceira coluna: {sum_third_column}
    3. O maior valor da segunda linha: {max_second_row}''')


# linha1 = [1, 2, 3]
# linha2 = [4, 5, 6]
# linha3 = [7, 8, 9]
# matriz = [linha1, linha2, linha3]
#
# for i, linha in enumerate(matriz):
#     for index, item in enumerate(linha):
#         linha[index] = int(input(f'Digite um número para a posição [{i + 1}, {index + 1}]: '))
#
# print('\n', '---' * 13)
# print(f'''\nMatriz:
# \t{linha1}
# \t{linha2}
# \t{linha3}''')
#
# print('\n', '---' * 13)
# print('')
#
# # Analizando a matriz
# tot_pares = 0
# colun3 = 0
#
# for linha in matriz:
#     # Soma dos valores da terceira coluna
#     colun3 += linha[2]
#
#     for item in linha:
#         # Soma dos números pares
#         if item % 2 == 0:
#             tot_pares += item
#
# # Maior valor da segunda linha
# maior_linha2 = max(matriz[1])
#
# print(f'A soma dos valores pares é {tot_pares}')
# print(f'A soma dos valores da terceira coluna é {colun3}')
# print(f'Maior valor da segunda linha: {maior_linha2}')
