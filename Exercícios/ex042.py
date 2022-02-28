from time import sleep
from color import yellow, red, blue, cyan, magenta

print(yellow('-=' * 15))
print(red(f'{"ANALIZADOR DE TRIÂNGULOS":^30}'))
print(yellow('-=' * 15))

print(blue('\nDigite os segmentos do triângulo para analizarmos ele:'))
a = float(input('\nPrimeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

print('\n\033[1mDADOS COLETADOS!\033[m Por favor, aguarde enquanto \033[4mverificamos os dados...\033[m')
sleep(2)
if a + b > c and a + c > b and b + c > a:
    print(f'\nCom essas medidas, {blue("É POSSÍVEL")} formar um {yellow("triângulo!")}')
    if a == b and b == c and c == a:
        print(f'E como {red("todas")} as medidas do triângulo são iguais, esse triângulo é um {cyan("TRIÂNGULO EQUILÁTERO!")}')
    elif a == b or b == c or c == a:
        print(f'E como existe apenas {magenta("dois")} segmentos iguais desse triângulo, esse triângulo é um {cyan("TRIÂNGULO ISÓSCELES!")}')
    else:
        print(f'E como {red("nenhuma")} reta desse triângulo tem o mesmo comprimento que outra, esse triângulo é um {cyan("TRIÂNGULO ESCALENO!")}')
else:
    print(f'\nCom essas medidas, {red("NÃO É POSSÍVEL")} formar um {yellow("triângulo!")}')
