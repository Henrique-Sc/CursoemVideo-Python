num = list()

for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
print('')

# analizando o maior valor
print(f'O maior valor digitado foi {max(num)}', end=' ')
if num.count(max(num)) == 1:
    print(f'na posição {num.index(max(num))}.')
else:
    print(f'nas posições', end=' ')

    for i, v in enumerate(num):
        if v == max(num):
            print(f'{i}...', end=' ')
    print('')

    # for c in range(0, len(num)):
    #     if num[c] == max(num):
    #         print(f'{num.index(max(num), c)}...', end=' ')
    # print('')

# analizando o menor valor
print(f'O menor valor digitado foi {min(num)}', end=' ')
if num.count(min(num)) == 1:
    print(f'na posição {num.index(min(num))}.')
else:
    print(f'nas posições', end=' ')

    for i, v in enumerate(num):
        if v == min(num):
            print(f'{i}...', end=' ')

    # for c in range(0, len(num)):
    #     if num[c] == min(num):
    #         print(f'{num.index(min(num), c)}...', end=' ')
