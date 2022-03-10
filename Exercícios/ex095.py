from time import sleep

# Cores
r = '\033[m'
IR = '\033[38;5;9m'
IB = '\033[38;5;12m'

# Declaração das variáveis, e inserção dos dados
jogadores = []
cont = 0
while True:
    print('-' * 38)  # Linha para Design
    jogadores.append({'nome': str(input('Nome do(a) jogador(a): ')).strip().title(), 'gols': list()})
    
    # noinspection PyTypeChecker
    jogadores[cont]['partidas'] = int(input(f'Quantas partidas {jogadores[cont]["nome"]} jogou? '))
    if jogadores[cont]['partidas'] == 0:
        jogadores[cont]['gols'].append(0)
    print()
    
    # noinspection PyTypeChecker
    for c in range(jogadores[cont]['partidas']):
        jogadores[cont]['gols'].append(int(input(f'Quantos gols na {c + 1}ª partida? ')))

    cont += 1
    print('-' * 38)  # Linha para design
    
    # Perguntar se o usuário quer inserir mais dados
    esc = str(input(f'\nDeseja continuar? [{IB}S{r}im / {IR}N{r}ão] ')).strip().upper()[0]
    # Tratanto as opções
    if esc not in 'NS':
        print()
        while esc not in 'NS':
            esc = str(input(f'{IR}Valor incorreto!{r} Deseja continuar? [{IB}S{r}im / {IR}N{r}ão] ')).strip().upper()[0]
    print()
    if esc == 'N':
        break
        
# Bloco apenas para design, e deixar a visualização melhor
for c, jogador in enumerate(jogadores):
    if c == 0:
        n = len(jogador['nome'])
    elif len(jogador['nome']) > n:
        n = len(jogador['nome'])
n += 1
title = len(str(f'{"Cod":<4} {"nome":<{n+1}} {"total de gols"}'))

sleep(0.5)
# Linha para design
print('\n' + '=' * title)
sleep(0.5)

# Título da tabela
print(f'{"Cod":<4} {"Nome":<{n+1}} {"Total de gols"}')
sleep(0.5)

# Mostrando os dados em forma de tabela
for c, jogador in enumerate(jogadores):
    print(f' {c:<4} {jogador["nome"]:<{n+1}} {sum(jogador["gols"])}')
    sleep(0.5)
    
# linha para design
print('\n' + '=' * title)
sleep(0.5)

# Dados mais detalhados
print('\n~Digite o código do jogador')
# While para a inserção dos dados

while True:
    levant = int(input('\nMostrar dados de qual jogador(a)? (999 para parar) ').strip())

    # Verificando o valor inserido, para trata-lo corretamente
    if levant == 999:
        break
    
    elif levant >= len(jogadores) or levant < 0:
        print('')
        while True:
            levant = int(input(f'{IR}Valor incorreto!{r} Digite corretamente o número do(a) jogador(a): ').strip())
            if 0 <= levant < (len(jogadores)):
                break
    
    # Bloco para design no terminal
    title = len(str(f'\n-- Levantamento do(a) jogador(a) {jogadores[levant]["nome"]} --'))
    print(f'\n-- Levantamento do(a) jogador(a) {jogadores[levant]["nome"]} --')
    
    # Mostrando o levantamento
    if jogadores[levant]['partidas'] != 0:
        for i, gols in enumerate(jogadores[levant]['gols']): 
            if gols == 0:
                print(f'\t> Não fez nenhum gol na {i + 1}ª partida')
            elif gols == 1:
                print(f'\t> Fez {gols} gol na {i + 1}ª partida')
            elif gols > 1:
                print(f'\t> Fez {gols} gols na {i + 1}ª partida')
    else:
        print('\t> Não jogou nenhuma partida')
        
print(f'\n{IB}<- Programa finalizado ->{r}')
