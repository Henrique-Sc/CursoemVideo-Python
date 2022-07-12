from functions import leiaInt, leiaFloat

bold = '\033[1m'
reset = '\033[m'

a = leiaInt(f'Digite um número {bold}INTEIRO{reset}: ')
b = leiaFloat(f'Digite um número {bold}REAL{reset}: ')

print(f'\nVocê digitou o números {bold}{a}{reset} e {bold}{b}{reset}!')
