b = 'DESAFIO 011'
print(f'{b:=^35}')
l = float(input('\nComprimento da parede: '))
a = float(input('Altura da parede: '))
print(f'\nÁrea da parede é de {l*a:.2f}m²\nIrá precisar de {l*a/2:.2f} litros de tinta')
