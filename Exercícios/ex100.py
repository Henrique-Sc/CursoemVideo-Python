from random import randint


def sorteia():
    numeros = list()
    for c in range(5):
        numeros.append(randint(1, 10))
    print(numeros)


sorteia()