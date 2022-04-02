def fatorial(num=1):
    f = 1
    for c in range(1, num + 1):
        f *= c
        print(c, f)


fatorial(5)