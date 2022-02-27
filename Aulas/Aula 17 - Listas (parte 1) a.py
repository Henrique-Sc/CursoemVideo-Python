lanche = ['Hamburgue', 'Suco', 'Pizza', 'Pudim']  # Determina a lista

print(f'Lista inicial: {lanche}')

# Adicionar elementos
""" <lista>[<index>] só funciona quando já existe o index expecíficado. Não adiciona novos itens, apenas os substituis """
lanche[3] = 'Picolé'

""" Método 'append' adiciona novos itens na lista, sempre na última opção """
lanche.append('Cookie')
lanche.append('Cookie')

""" Método 'insert' adiciona valores em uma posição específica. """
lanche.insert(0, 'Cachorro-quente')

print(f'\nLista com novos itens: {lanche}')


# Eliminar valores

" O comando 'del' pode eliminar um elemento de uma lista "
del lanche[3]

" Método 'pop' elimina o último elemento, mas também o seu index pode ser especificado "
lanche.pop(3)

""" O método 'remove' elimina um elemento especificado pelo seu valor 
    Ao ter itens com mesmo valor, ele elimina a primeira ocorrência """
lanche.remove('Cookie')

" Elimina o valor 'Pizza' se ele estiver na lista "
if 'Pizza' in lanche:
    lanche.remove('Pizza')

print(f'\nLista com itens excluidos: {lanche}')

print('\n', '--' * 50, '\n')

# Formas de declarar uma lista:

" 1 - Usando o método 'list' "
valores = list(range(4, 11))

print(f'Valores (list): {valores}')

" 2 - Usando os conchetes "
valores = [8, 2, 5, 4, 9, 3, 0]

print(f'Valores ([]): {valores}')

" O método 'sort' ordenar a lista "
valores.sort()

print(f'\nValores (crescente): {valores}')

" Podemos também usar o parâmetro 'reverse=True' para ordernar a lista em forma decrescente "
valores.sort(reverse=True)

print(f'Valores (decrescente): {valores}')

" O método 'len' retorna o número de itens na lista "

print(f'\nNúmero de itens: {(len(valores))}')