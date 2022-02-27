from math import sin, tan, cos, radians
ang = float(input('digite um ângulo qualquer: '))
seno = sin(radians(ang))
print(f'\nO seno do ângulo {ang} é {seno:.2f}')
cosseno = cos(radians(ang))
print(f'O cosseno do ângulo {ang} é {cosseno:.2f}')
tangente = tan(radians(ang))
print(f'A tangente do ângulo {ang} é {tangente:.2f}')