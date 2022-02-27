from random import randint
from time import sleep

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'{"JOGOS DA MEGA SENA":^26}')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('')

quant_jogos = int(input('Quando jogos você quer que seja sorteado? ').strip())
print('')

print(f'-=-=-= Sorteando {quant_jogos} jogo(s) =-=-=-\n')

for c in range(1, quant_jogos + 1):
    jogo = list()
    cont = 0
    while cont != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    sleep(0.8)
print('')

print('-=-=-=-= < Boa sorte! > =-=-=-=-')

