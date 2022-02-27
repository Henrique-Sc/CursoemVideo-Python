pesos = []
menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    pesos += [peso]
    # if c == 1:
    #     maior = peso
    #     menor = peso
    # else:
    #     if peso > maior:
    #         maior = peso
    #     if peso < menor:
    #         menor = peso
print(f'\nMaior peso digitado: {min(pesos):.1f}Kg')
print(f'Menor peso digitado: {max(pesos):.1f}Kg')
