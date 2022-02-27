# valores = list()
# print('Obs: digite -1 para parar. ')
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     if -1 in valores:
#         valores.remove(-1)
#         break
# print(f'\nLista: {valores}')
# for cont, valor in enumerate(valores):
#     print(f'Encontrei na posição {cont} o valor {valor}!')
# print('Cheguei no final da lista.')

a = [1, 2, 3]
" interligação entre uma lista e outra"
# b = a
# b[2] = 5

" Copia uma lista em outra "
b = a[:]
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')
