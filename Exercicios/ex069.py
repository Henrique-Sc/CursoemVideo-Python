from time import sleep
reset = '\033[m'
red = '\033[31m'
IBlue = '\033[38;5;12m'
IYellow = '\033[38;5;11m'

analise_idade = 0
quant_m = 0
quant_f = 0
cont = 1
while True:
    print(f'{IBlue}=-={reset}' * 10, f'\n{f"CADASTRO DA {cont}º PESSOA":^30}\n', end='' f'{IBlue}=-={reset}' * 10)
    print('\n')
    idade = int(input('Sua idade: ').strip())
    sexo = str(input('Seu sexo: (Masculino, Feminino ou outros) ')).strip().upper()[0]
    while sexo not in 'MFO':
        sexo = str(input(f'{red}Valores inválidos! Digite um valor válido: {reset}')).strip().upper()[0]

    if idade >= 18:
        analise_idade += 1
    if sexo == 'M':
        quant_m += 1
    if sexo == 'F' and idade < 20:
        quant_f += 1
    cont += 1

    print('')
    print(f'{IBlue}=-={reset}' * 10)
    print('')

    esc = str(input('Deseja continuar? (Sim / Não) ')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input(f'{red}Valores inválido! Digite um valor válido: (Sim / Não) {reset}')).strip().upper()[0]
    print('')
    if esc == 'N':
        break

print(f'{IYellow}Analizando os dados', end='')
sleep(0.5)
for c in '...':
    print(c, end='', flush=True)
    sleep(0.8)

print(f'''\n\n{reset}Quantidades de pessoas com mais de 18 anos: {analise_idade}
Quantidade de homens cadastrados: {quant_m}
Quantidades de mulheres com menos de 20 anos: {quant_f}''')
