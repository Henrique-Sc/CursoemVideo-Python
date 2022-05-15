def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)')


n = str(input('Digite o nome do jogador: ')).strip().title()
g = input('Total de gols: ')

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    jogador(gols=g)
else:
    jogador(nome=n, gols=g)