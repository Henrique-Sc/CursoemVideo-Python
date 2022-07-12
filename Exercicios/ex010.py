b = 'DESAFIO 010'
print(f'{b:=^35}')
b1 = 'Conversor de real para dolar'
print(f'{b1:^36}')
r = float(input('\nQuando dinheiro você tem em sua carteira: R$ '))
dolar = r/3.27
print(f'Você pode comprar ${dolar:.2f}')
