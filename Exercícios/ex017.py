from math import sqrt
print('-' * 8, 'Desafio 017', '-' * 8)
a = float(input('\nValor do cateto oposto: '))
b = float(input('Valor do cateto adjacente: '))
c = sqrt((a ** 2) + (b ** 2))
print(f'A hipotenusa é {c:.2f}')