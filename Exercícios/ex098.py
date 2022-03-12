# Fazer um contador

# Funcionalidades necessárias:
#   > Mostrar uma contagem de 1 até 10 de 1 em 1
#   > Mostrar uma contagem de 10 até 0 de 2 em 2
#   > Mostrar uma contagem personalizada, escolhida pelo usuário
#       • Funções necessárias:
#            > Funcionar de trás para frente (90 até 40, de 10 em 10)
#            > Se o passo for zero, deve ser considerado com 1
#            > Se o passo for negativo, deve ser considerado como positivo

def contador(inicio, fim, passo):
    if fim > inicio:
        fim += 1
    elif inicio > fim:
        passo *= -1
        fim -= 1
        print(passo)

    for c in range(inicio, fim, passo):
        print(f'{c} → ', end='')
    print('')


contador(1, 10, 1)
contador(10, 0, 2)
