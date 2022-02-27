print('\033[37m=-' * 5, '\033[31mSequência de Fibonacci\033[m', '\033[37m-=\033[m' * 5)
termos = int(input('\nPrimeiros termos da sequência: '))

while termos <= 1:
    termos = int(input('\n\033[31mValor inválido! Digite um valor maior ou igual que 2: \033[m'))

c = 2
t1 = 0
t2 = 1
print(f'\nOs {termos} primeiros termos da sequência é: [ \033[34m{t1} → {t2}', end=' → ')
while c != termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print(t3, end=' → ')
print('...\033[m ]')

# # Usando listas
# seq = [0, 1]
# fn = seq[-2] + seq[-1]
#
# if termos == 1:
#     print(f'\nO primeiro termo é: {seq[0]}')
# else:
#     while len(seq) != termos:
#         fn = seq[-2] + seq[-1]
#         seq.append(fn)
#     print(f'\nOs {termos} primeiros termos são: \033[31m{seq}\033[m')
