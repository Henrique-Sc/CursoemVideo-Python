from time import sleep

print('\033[37m-=\033[m' * 5, '\033[31mCalculadora\033[m', '\033[37m=-\033[m' * 5)
num1 = int(input('\nDigite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

escolha = 0
escolhas = [1, 2, 3, 4, 5]

print('\n' + '=-=' * 10)

while escolha != 5:
    # fazendo o usuário digitar alguma escolha

    escolha = int(input('''
O que deseja fazer com esses números?

    \033[34m[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR\033[m

>->-> Escolha: '''))
    # corrigindo erros de digitação
    while escolha not in escolhas:
        print('\n' + '=-=' * 10)
        escolha = int(input('''
\033[31mVALOR INCORRETO! Digite novamente\033[m

    \033[34m[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR \033[m

>->-> Sua escolha: '''))

    # Tratando as escolhas do usuário

    if escolha == 1 or escolha == 2 or escolha == 3:
        if escolha == 1:
            print(f'\nA operação inserida é {num1} + {num2} = {num1 + num2}')
        elif escolha == 2:
            print(f'\nA operação inserida é {num1} * {num2} = {num1 * num2}')
        elif escolha == 3:
            if num1 > num2:
                maior = num1
                print(f'\nO maior número digitado é o {maior}')
            elif num2 > num1:
                maior = num2
                print(f'\nO maior número digitado é o {maior}')
            elif num1 == num2:
                print('\nOs dois números são iguais')
        sleep(2)
    elif escolha == 4:
        print('\nDigites novos números')
        print('')
        num1 = int(input('  Primeiro valor: '))
        num2 = int(input('  Segundo valor: '))
    print('\n' + '=-=' * 10)
    sleep(1)
print('\nSaindo do programa...')
sleep(1)
