def funcao():
    global n1, n2
    n1 = 4
    n2 = 10
    print(f'N1 dentro vale {n1}')
    print(f'N2 dentro vale {n2}')


n1 = 2
n2 = 8
funcao()
print(f'N1 no global vale {n1}')
print(f'N2 no global vale {n2}')
