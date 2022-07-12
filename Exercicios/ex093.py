# Declarando a lista
jogador = dict()

# Inserindo os dados
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['gols'] = list()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# Inserir a quantidade de gols em cada partida
if jogador['partidas'] != 0: print()
for c in range(jogador['partidas']):
    jogador['gols'].append(int(input(f'  - Quantos gols na {c + 1}º partida? ')))

jogador['total_gols'] = sum(jogador['gols'])

# Linha para decoração
print('\n=--=--=--=--=--=--=--=--=--=--=--=--=--=\n')

# Relatório dos dados
print(f'Relatório de todas as partidas de {jogador["nome"]}:')

for c, v in enumerate(jogador['gols']):
    print(f'  -> {c + 1}º partida: {v} gols.')
    
print(f'\nTotal de gols: {jogador["total_gols"]}')
