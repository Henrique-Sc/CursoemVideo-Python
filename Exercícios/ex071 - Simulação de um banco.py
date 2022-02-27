reset = '\033[m'
red = '\033[31m'
TRed = '\033[38;5;9m'

print(f'{TRed}=-={reset}' * 10)
print(f'{TRed}={reset}' f'{"Banco do Bradesco":^28}' f'{TRed}={reset}')
print(f'{TRed}=-={reset}' * 10)

print(f'\n{red}~Obs: apenas valores inteiros{reset}')
valor_saque = int(input('Digite o valor a ser sacado: R$'))

print('')
print('-=' * 16 + '-')

cedulas_200 = cedulas_100 = cedulas_50 = cedulas_20 = cedulas_10 = cedulas_5 = cedulas_1 = 0

while True:
    if valor_saque >= 200:
        cedulas_200 = valor_saque // 200
        valor_saque %= 200
        print(f'Total de {cedulas_200} cédulas de R$200')
    elif valor_saque >= 100:
        cedulas_100 = valor_saque // 100
        valor_saque %= 100
        print(f'Total de {cedulas_100} cédulas de R$100')
    elif valor_saque >= 50:
        cedulas_50 = valor_saque // 50
        valor_saque %= 50
        print(f'Total de {cedulas_50} cédulas de R$50')
    elif valor_saque >= 20:
        cedulas_20 = valor_saque // 20
        valor_saque %= 20
        print(f'Total de {cedulas_20} cédulas de R$20')
    elif valor_saque >= 10:
        cedulas_10 = valor_saque // 10
        valor_saque %= 10
        print(f'Total de {cedulas_10} cédulas de R$10')
    elif valor_saque >= 5:
        cedulas_5 = valor_saque // 5
        valor_saque %= 5
        print(f'Total de {cedulas_5} cédulas de R$5')
    elif valor_saque >= 1:
        cedulas_1 = valor_saque // 1
        valor_saque %= 1
        print(f'Total de {cedulas_1} cédulas de R$1')
    else:
        break
print('-=' * 16 + '-')
