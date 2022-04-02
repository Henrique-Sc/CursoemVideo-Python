def jogador(nome='<desconhecido>', totgols=0):
    print(f'O jogador {nome} fez {totgols} gol(s)')


n = input('Nome do jogador: ').strip().title()
gols = input('Número de gols: ').strip()
print()
if gols.isnumeric():
    int(gols)
else:
    gols = 0

if n != '':
    jogador(n, gols)
else:
    jogador(totgols=gols)
