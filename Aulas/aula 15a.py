s = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s += num
print('A soma dos números digitados é {s}')
