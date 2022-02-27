jogador = {
    'nome': str(input('Nome do jogador: ')).strip().title(),
    'gols': list()
}
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantos gols na {c + 1}º partida? ')))
jogador['total_gols'] = sum(jogador['gols'])

print('\n=--=--=--=--=--=--=--=--=--=--=--=--=--=\n')

print(f'Relatório de todas as partidas de {jogador["nome"]}:')
for c, v in enumerate(jogador['gols']):
    print(f'\t-> {c + 1}º partida: {v} gols.')
print(f'\n\tTotal de gols: {jogador["total_gols"]}')
