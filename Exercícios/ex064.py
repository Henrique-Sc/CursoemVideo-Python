print('''\033[37mDigite números aleatórios quaisquer.
Obs: Digite "999" para parar.\033[m''')
print('')
# num = []
# while 999 not in num:
#     num.append(float(input('Digite algum valor: ')))
# if 999 in num:
#     num.remove(999)
# print(f'\nNo total teve {len(num)} números digitados, e soma de todos eles é {sum(num)}')

num = cont = total = 0
while num != 999:
    num = float(input('Digite algum valor: '))
    if num != 999:
        cont += 1
        total += num
print(f'\nNo total teve {cont} números digitados, e soma de todos eles é {total}')
