def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)')


name = str(input('Digite o nome do jogador: ')).strip().title()
g = input('Total de gols: ')

if g.isnumeric():
    int(g)

# if name == '':

