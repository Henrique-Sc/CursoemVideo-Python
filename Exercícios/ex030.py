num = int(input('Digite um número qualquer: '))
n = num / 2 % 1
if n == 0:
    print(f'\nO número {num} é par!')
else:
    print(f'O número {num} é impar!')
