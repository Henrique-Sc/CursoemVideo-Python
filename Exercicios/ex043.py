reset = '\033[m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
cyan = '\033[36m'
IWhite = '\033[38;5;15m'

print(f'{yellow}-={reset}' * 15)
print(f'{red}{"CALCULADORA DE IMC":^30}{reset}')
print(f'{yellow}-={reset}' * 15)

print(f'\n{IWhite}OBS: para escrever números com vírgula, troca-se a "," pelo "."{reset}')

peso = float(input('\nDigite o seu peso (kg): '))
altura = float(input('Digite a sua altura (cm): '))
imc = peso / (altura / 100) ** 2

print(f'\nO seu IMC é {yellow}{imc:.1f}{reset}, você está', end=" ")
if imc < 18.5:
    print(f'{red}ABAIXO DO PESO{reset}!')
    
elif 18.5 <= imc < 25:
    print(f'no {blue}PESO IDEAL{reset}!')
    
elif 25 <= imc < 30:
    print(f'{cyan}ACIMA DO PESO{reset}!')
    
elif 30 <= imc < 40:
    print(f'com {green}OBESIDADE{reset}!')
    
else:
    print(f'com {red}OBESIDADE MÓRBIDA{reset}!')
