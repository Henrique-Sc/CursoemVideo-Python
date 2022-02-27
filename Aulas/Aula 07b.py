x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
s = x + y
m = x * y
d = x / y
di = x // y
p = x ** y
print(f'A soma é {s}, o produto é {m}, a divisão {d:.3f}', end=' ')
print(f'a divisão inteira é {di} e a é potência {p}')
print(f'A soma é {s} \nO produto é {m}\nA divisão é {d:.3f}\nA divisão inteira é {di}\nA potência é {p}')
