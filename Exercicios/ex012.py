b1 = 'DESAFIO 012'
print(f'{b1:=^35}')
print('='*12, 'Descontos', '='*12)
p = float(input('\nValor do produto: R$ '))
d = float(input('Valor do desconto: '))
print(f'\nO preço do produto é de: R$ {p - (p/100*d):.2f}')
