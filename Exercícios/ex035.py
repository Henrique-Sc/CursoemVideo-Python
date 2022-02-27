print('\033[33m-=\033[m' * 15)
print(f'\033[34m{"Verificador de triângulos":^30}\033[m')
print('\033[33m-=\033[m' * 15)

print('\n\033[30mDigite os seguimentos desse triângulo, para anarlizarmos ele: \033[m')
a = float(input('\nValor da primeira reta: '))
b = float(input('Valor da segunda reta: '))
c = float(input('Valor da terceira reta: '))

if a+b > c and b+c > a and c+a > b:
    print('\nUtilizando esses valores, \033[34mÉ POSSÍVEL\033[m formar um \033[33mtriângulo!\033[m')
else:
    print('\nUtilizando esses valores, \033[31mNÃO É POSSÍVEL\033[m formar um \033[33mTriângulo!\033[m')