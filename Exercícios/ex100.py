from random import randint


def sorteia():
    numeros = []
    for c in range(5):
        numeros.append(randint(1, 10))
    print(f'Os valores')
    return numeros


def somarPar(numeros):
    tot_par = 0
    for num in numeros:
        if num % 2 == 0:
            tot_par += num
    print(tot_par)


