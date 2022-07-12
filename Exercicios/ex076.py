lista = ('Mouse', 80.00,
         'Mousepad', 15.99,
         'Teclado mecânico', 120.45,
         'Headset', 110.90,
         'Monitor', 350.49,
         'Cadeira gamer', 400.00,
         'Notebook', 2500)

print('=' * 37)
print('=' + '-=' * 4, 'Listagem de preço', '=-' * 4 + '=')
print('=' * 37)
print()
print('-' * 37)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<27}', end='')
    elif c % 2 == 1:
        print(f'R${lista[c]:>8.2f}')
print('-' * 37)
