# teste = list()
# teste.append('Henrique')
# teste.append(15)
#
# galera = list()
# galera.append(teste[:])
#
# teste[0] = 'Maria'
# teste[1] = 22
#
# galera.append(teste[:])
# print(galera)


galera = [['João', 19], ['Alana', 16], ['Maria', 33], ['Pedro', 25]]
for p in galera:
    print(f'Nome: {p[0]} \nIdade: {p[1]}')
    print('')