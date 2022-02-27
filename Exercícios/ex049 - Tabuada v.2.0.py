reset = '\033[m'
red = '\033[31m'

# Introdução
print(f'{red}-={reset}' * 3, 'Tabuada', f'{red}=-{reset}' * 3)

# Salvando o número que será usado
num = int(input('\nDigite algum número para ver a sua tabuada: '))

print('\n-=-=-=-=-=-=-=-')
for c in range(1, 11):  # For para mostrar a tabuada
    print(f'{num} x {c} = {num * c}')
print('-=-=-=-=-=-=-=-=-')
