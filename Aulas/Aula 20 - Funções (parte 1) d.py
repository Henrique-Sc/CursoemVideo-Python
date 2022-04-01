def dobro(lista):
    for i, n in enumerate(lista):
        lista[i] *= 2


num = [4, 5, 6, 9]
dobro(num)
print(num)
