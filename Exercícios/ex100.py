from random import randint
from time import sleep


def sorteio(lista, tot_sort=5, timer=0.5):
    print(f'Sorteando {tot_sort} números: ', end='')

    for c in range(tot_sort):
        r = randint(1, 10)
        lista.append(r)
        print(r, end=' ', sep=f'{sleep(timer)}')
    sleep(timer), print('PRONTO!'), sleep(timer)


def somarPar(lista):
    tot_par = list()
    for num in lista:
        if num % 2 == 0:
            tot_par.append(num)
    print(f'A soma dos numeros PARES de {lista} é: {sum(tot_par)}')


numeros = list()
sorteio(numeros, tot_sort=5, timer=0.22)
somarPar(numeros)
