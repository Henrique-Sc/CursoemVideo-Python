from time import sleep

# Determinando a função

def contador(inicio, fim, passo):
    # Verificação dos dados, para trata-lo corretamente
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    # Exibição dos dados
    # Linha bonita :)
    print('-' * 50)
    sleep(0.3)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
    sleep(0.3)

    # Verificação dos dados, para trata-lo corretamente
    if fim > inicio:
        fim += 1
    elif inicio > fim:
        passo *= -1
        fim -= 1

    print('   -> ', end='')
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
        sleep(0.21)
    print('FIM!')
    sleep(0.3)
    # Linha bonita :)
    print('-' * 50)
    sleep(0.3)


contador(1, 10, 1)
contador(10, 0, 2)

print('\n' + '-' * 50)
print('Agora é a sua vez de fazer uma contagem personalizada :)')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
