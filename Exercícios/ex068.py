from random import randint
from time import sleep

reset = '\033[m'
red = '\033[31m'
IRed = '\033[38;5;9m'
IBlue = '\033[38;5;12m'

print(f'{red}-={reset}' * 4, 'Par ou ímpar', f'{red}=-{reset}' * 4)

cont = 0
while True:
    esc1 = int(input('\nDigite um valor: '))
    esc2 = (str(input('Par ou ímpar? [P/I] ')).strip().upper()[0])
    while esc2 not in 'PIÍ':
        esc2 = str(input('Valor incorreto! Digite novamente: ')).strip().upper()[0]
    pc = randint(0, 10)
    resultado = (pc + esc1)
    print('')
    print(f'-=-' * 18)
    print(f'Você jogou {esc1} e o computador escolheu {pc}, a soma é {resultado}.')
    if esc2 == 'P':
        if resultado % 2 == 0:
            print(f'{IBlue}{"Você ganhou! Parabéns (づ｡◕‿‿◕｡)づ":^54}{reset}')
        else:
            print(f'{IRed}{"Você perdeu! Mais sorte na próxima vez.":^54}{reset}')
            print(f'-=-' * 18)
            break
    else:
        if resultado % 2 == 0:
            print(f'{IRed}{"Você perdeu! Mais sorte na próxima vez.":^54}{reset}')
            print(f'-=-' * 18)
            break
        else:
            print(f'{IBlue}{"Você ganhou! Parabéns (づ｡◕‿‿◕｡)づ":^54}{reset}')
    print(f'-=-' * 18)
    cont += 1
    sleep(0.5)
sleep(0.8)
print('')
print('-=' * 5, f'GAMER OVER. Vitórias seguidas: {cont}', '=-' * 5)
