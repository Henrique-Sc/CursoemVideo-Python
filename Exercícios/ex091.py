from time import sleep
from random import randint
from operator import itemgetter

sort = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

print(f'-=-=-= Jogo de dados =-=-=-')
print(f'\nValores que serão sorteados:')
sleep(0.8)
for k, v in sort.items():
    print(f'  - {k} tirou {v} no dado.')
    sleep(0.8)

# função sorted: coloca dados em ordem (tuplas e listas, podendo ter números ou letras)
# Se for ordenar um dicionário, tem que usar o "itemgetter". Comando: key:itemgetter(x) -
# Dentro do itemgetter, no lugar do X, coloca 0 para as chaves ou 1 para os valores
ranking = sorted(sort.items(), key=itemgetter(1), reverse=True)

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print(f'\nRanking dos jogadores: ')
sleep(0.8)
for i, jogador in enumerate(ranking):
    print(f'  > {i + 1}º Lugar: {jogador[0]} com {jogador[1]}.')
    sleep(0.8)
