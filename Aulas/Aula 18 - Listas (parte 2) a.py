# dados1 = ['Pedro', 25]
# dados2 = ['Maria', 19]
# dados3 = ['João', 35]
#
# pessoas = [dados1, dados2, dados3]
#
# print(f'Lista "pessoas": {pessoas}')
# print(f'\nPessoas [0][0]: {pessoas[0][0]}')
# print(f'Pessoas [1][1]: {pessoas[1][1]}')
# print(f'Pessoas [2][0]: {pessoas[2][0]}')

galera = list()

for c in range(1, 6):
    dados = list()
    print(f'-=-= {c}ª PESSOA =-=-')
    dados.append(str(input('Primeiro nome: ')).strip().title())
    dados.append(int(input('Idade: ').strip()))
    print(dados)

    dados = tuple(dados)
    galera.append(dados)

    print('')
    print('=-' * 12, '\n')
print(f'Dados coletados: {galera}')
