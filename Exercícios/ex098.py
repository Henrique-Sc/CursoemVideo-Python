from time import sleep


# Determinando a função
def contador(inicio, fim, passo, timer=0.3):
    # Verificação dos dados, para trata-lo corretamente
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    # Exibição dos dados
    # Linha bonita :)
    print('-' * 50)
    sleep(timer)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
    sleep(timer)

    # Verificação dos dados, para trata-lo corretamente
    if fim > inicio:
        fim += 1
    elif inicio > fim:
        passo *= -1
        fim -= 1

    print('   -> ', end='')
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
        sleep(timer)
    print('FIM!')
    sleep(timer)
    # Linha bonita :)
    print('-' * 50)
    sleep(timer)


contador(1, 10, 1)
contador(10, 0, 2)

print('\nAgora é a sua vez de fazer uma contagem personalizada :)')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
