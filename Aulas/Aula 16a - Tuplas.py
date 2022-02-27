lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim', 'Coxinha', 'Batata frita')

# Formas de mostrar um índice formatado em uma tupla
for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

