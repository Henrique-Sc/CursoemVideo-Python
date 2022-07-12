lista = (int(input('Digite um número: ').strip()),
         int(input('Digite outro número: ').strip()),
         int(input('Digite mais um número: ').strip()),
         int(input('Digite o último número: ').strip()))

print(f'\nVocê digitou os números: ', end='')
for cont, num in enumerate(lista):
    print(num, end=' ')

# contagem do número 9
cont9 = lista.count(9)
print(f'\n\nO número 9 apareceu ', end='')
if cont9 > 0:
    print(f'{cont9}', 'vezes' if cont9 > 1 else 'vez')
else:
    print('nenhuma vez')

# Mostrando o índice do número 3
if 3 in lista:
    print(f'O primeiro número 3 apareceu na {lista.index(3) + 1}ª posição')
else:
    print('Não foi digitado o valor 3')

# Mostrando os números pares digitados
print(f'Números pares digitados: ', end='')
c = 0
for cont, num in enumerate(lista):
    if lista[cont] % 2 == 0:
        print(lista[cont], end=' ')
        c += 1
if c == 0:
    print('{}Não foi digitado nenhum número par{}'.format('\033[3m', '\033[m'))
