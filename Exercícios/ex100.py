from random import randint
from time import sleep


def sorteio(nums, tot_sort=5):
    print(f'Sorteando {tot_sort} números: ', end='')

    for c in range(tot_sort):
        r = randint(1, 10)
        nums.append(r)
        print(r, end=' ', sep=f'{sleep(0.5)}')
    print('PRONTO!')


def somarPar(nums):
    tot_par = list()
    for num in nums:
        if num % 2 == 0:
            tot_par.append(num)
    print(f'A soma numeros PARES é: ', end=''), sleep(0.5)
    print(sum(tot_par))


numeros = list()
sorteio(numeros)
somarPar(numeros)
