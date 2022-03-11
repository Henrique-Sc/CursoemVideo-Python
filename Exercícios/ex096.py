def area(larg, comp):
    calc_area = larg * comp
    print(f'A área desse terreno é de {calc_area:.1f}m²')


# Título
print('--- Controle de Terrenos ---')

# Inserção dos dados
larg = float(input('\nLargura (m): '))
comp = float(input('Comprimento (m): '))
print()

area(larg, comp)
