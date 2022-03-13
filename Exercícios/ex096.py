def area(larg, comp):
    calc_area = larg * comp
    print(f'A área desse terreno é de {calc_area:.1f}m²')

# Título
print('--- Controle de Terrenos ---')

# Inserção dos dados
largura = float(input('\nLargura (m): '))
comprimento = float(input('Comprimento (m): '))
print()
area(largura, comprimento)
