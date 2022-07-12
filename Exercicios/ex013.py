b1 = 'DESAFIO 013'
print(f'{b1:=^35}')
s = float(input('\nValor do seu salário: R$'))
a = float(input('Valor do aumento: %'))
print(f'\nSeu novo salário será de {s + (s/100*a):.2f}')
