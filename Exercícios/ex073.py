classificados = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atlético-GO', 'Ceará SC', 'Athletico-PR', 'Internacional',
                 'Santos', 'São Paulo', 'Juventude', 'Cuiabá', 'Bahia', 'Fluminense', 'Grêmio', 'Sport Recife', 'América-MG', 'Chapecoense')

print('\033[1;3mClassificados - Campeonato Brasileiro de Futebol 2021\033[m')

print(f'\nOs cinco primeiros colocados: ', end='')
for top5 in range(0, 5):
    print(classificados[top5], end=', ' if top5 < 4 else '')

print('\n')
print('=-' * 45)

print('\nOs quatro ultimos classificados: ', end='')
for c in range(-4, 0):
    print(classificados[c], end=', ' if c < -1 else '')

print('\n')
print('=-' * 45)

print('\nLista dos classificados em ordem alfabética: ')

for ordem, lista in enumerate(sorted(classificados)):
    print(f'{ordem + 1}. {lista}')

print()
print('=-' * 20)

print(f'\nO Chapecoense ficou na {classificados.index("Chapecoense") + 1}ª posição')
