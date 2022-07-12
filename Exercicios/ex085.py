num_par = []
num_impar = []
numeros = [num_par[:], num_impar[:]]

# Perguntar ao usuário quantos números ele deseja digitar
digit_num = int(input('Quer digitar quantos números? ').strip())

# Verificando se digitou um número menor que 0 para não dar conflito com o FOR abaixo.
if digit_num <= 0: print('')
while digit_num <= 0:
    digit_num = int(input('Valor inválido! Digite um número maior que 1: '))
print()

# Um loop para digitar os números desejados
for c in range(1, digit_num + 1):
    num = int(input(f'Digite o {c}º número: ').strip())

    # Verificando se o número digitador é par ou ímpar, e colocando na lista adequada
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

# colocar os números digitados em ordem numérica
numeros[0].sort()
numeros[1].sort()

# Verificando se existe dados nas listas
if len(numeros[0]) == 0:
    numeros[0].append('Não foi digitado nenhum número PAR')
if  len(numeros[1]) == 0:
    numeros[1].append('Não foi digitado nenhum número ÍMPAR')

# Exibindo os valores
print(f'''\n{'-=' * 14}\n
Números pares: {numeros[0]}
Números ímpares: {numeros[1]}''')
