from random import randint

sort = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Números sorteados: ', end='')
for c in sort:
    print(c, end=' ')
print(f'\nMenor valor sorteado: {min(sort)}')
print(f'Maior valor sorteado: {max(sort)}')
