from color import red, blue, yellow
from random import randint
from time import sleep
from emoji import emojize

print(yellow('-=' * 15))
print(f'\033[31m{"PEDRA, PAPEL, TESOURA":^29}\033[m')
print(yellow('-=' * 15))

pedra = emojize(':fist:', use_aliases=True)
papel = emojize(':hand:', use_aliases=True)
tessoura = emojize(':v:', use_aliases=True)

player = float(input(f"""\n{'Escolha uma das opções abaixo: '}

{red(f'1 - para {pedra}')}
{blue(f'2 - para {papel}')}
{yellow(f'3 - para {tessoura}')}

{'Qual foi a opção escolhida?'} """))

if player < 1 or player > 3:
    print(red('\nOPÇÃO INVÁLIDA! Insira uma opção entre 1 e 3!'))
else:
    print('\nJO', end=''), sleep(0.6), print('KEN', end=''), sleep(0.6), print('PO!!!\n')

    pc = randint(1, 3)

    print('-=' * 8)
    if player == 1 and pc == 1:
        print(f'{"Você escolheu"} {pedra}')
        print(f'{"E a máquina escolheu"} {pedra}')
        print('-=' * 8)
        print(f'\n{yellow("EMPATE!")}')

    elif player == 1 and pc == 2:
        print(f'{"Você escolheu"} {pedra}')
        print(f'{"E a máquina escolheu"} {papel}')
        print('-=' * 8)
        print(f'\n{red("VOCÊ PERDEU!")}')

    elif player == 1 and pc == 3:
        print(f'{"Você escolheu"} {pedra}')
        print(f'{"E a máquina escolheu"} {tessoura}')
        print('-=' * 8)
        print(f'\n{blue("VOCÊ GANHOU!")}')

    elif player == 2 and pc == 1:
        print(f'{"Você escolheu"} {papel}')
        print(f'{"E a máquina escolheu"} {pedra}')
        print('-=' * 8)
        print(f'\n{blue("VOCÊ GANHOU!")}')

    elif player == 2 and pc == 2:
        print(f'{"Você escolheu"} {papel}')
        print(f'{"E a máquina escolheu"} {papel}')
        print('-=' * 8)
        print(f'\n{yellow("EMPATE!")}')

    elif player == 2 and pc == 3:
        print(f'{"Você escolheu"} {papel}')
        print(f'{"E a máquina escolheu"} {tessoura}')
        print('-=' * 8)
        print(f'\n{red("VOCÊ PERDEU!")}')

    elif player == 3 and pc == 1:
        print(f'{"Você escolheu"} {tessoura}')
        print(f'{"E a máquina escolheu"} {pedra}')
        print('-=' * 8)
        print(f'\n{red("VOCÊ PERDEU!")}')

    elif player == 3 and pc == 2:
        print(f'{"Você escolheu"} {tessoura}')
        print(f'{"E a máquina escolheu"} {papel}')
        print('-=' * 8)
        print(f'\n{blue("VOCÊ GANHOU!")}')

    elif player == 3 and pc == 3:
        print(f'{"Você escolheu"} {tessoura}')
        print(f'{"E a máquina escolheu"} {tessoura}')
        print('-=' * 8)
        print(f'\n{yellow("EMPATE!")}')

