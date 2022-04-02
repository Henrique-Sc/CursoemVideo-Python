def somar(*a):
    s = sum(a)
    # print(f'A soma vale {s}')
    return s


r1 = somar(1, 2, 3)
r2 = somar(10, 5)
r3 = somar(4)

print(f'Os resultados foram {r1}, {r2} e {r3}')
