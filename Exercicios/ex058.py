from random import randint
from time import sleep

# Aqui o programa vai análisar se o player vai querer jogar ou não
game = str(input('Olá! Vamos jogar um jogo de adivinhação? [S/N] ')).strip().upper()[0]
if game == 'S':
    print('\nOkay, vamos começar!')
else:
    while game not in 'S':
        print('\nOkay, quando quiser basta escrever "Sim"')
        game = str(input('Escreva aqui: ')).strip().upper()[0]
sleep(1)

print('''\nComo irá funcionar?
Eu vou escolher um número de 0 à 10 e você vai ter que adivinhar que número eu escolhi!''')
sleep(4)

# Aqui é a parte em que o programa escolhe um número e o player tenta adivinhar
print('\nPronto, já escolhi o número! Agora tente adivinhar.')

pc = 9
escolhas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cont = 0
escolha = int(input('Digite um valor entre 0 à 10: '))
cont += 1

print('')
while escolha != pc:
    if escolha > pc:
        escolha = int(input('\033[31mMenos... Tente adivinhar novamente: \033[m'))
    elif escolha < pc:
        escolha = int(input('\033[31mMais... Tente adivinhar novamente:  \033[m'))
    cont += 1

if escolha == pc:
    print(f'''\n\033[34mVocê acertou!\033[m
Você teve que dar {cont} palpites para adivinhar esse número.

(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Mais sorte na próxima vez! ✧ﾟ･: *ヽ(◕ヮ◕ヽ)''')
