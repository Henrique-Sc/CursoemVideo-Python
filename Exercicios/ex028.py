from random import randint
from time import sleep
inicio = input('Olá humano! Quer jogar um jogo comigo? (sim ou não) ').upper()
if inicio == 'SIM':
    print('\nYeeh! Vamos jogar!')
    print('Eu vou pensar em um número de 0 a 5 e você tenta adivinhar okay?')
    sleep(4)
    print('\nHmm...')
    sleep(1)
    num = randint(0,5)
    print('\nPronto! Pensei em um número, agora tenta adivinhar hehehe :)')
    escolhido = int(input('\nDigite o número que eu escolhi (0 a 5): '))
    if escolhido == num:
        print('\nAaah ,_, você ganhou de mim...')
        print('Mas parabéns! Gostei de jogar com você :3')
    else:
        print('\nHahahah você perdeu, tente novamente =^')
        print(f'O número que eu escolhi foi o {num}!')
else:
    print('\nOkay ,_, até mais...')