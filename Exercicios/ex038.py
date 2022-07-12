from time import sleep
import color
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

sleep(0.5)
print('\nPROCESSANDO...')
sleep(0.5)

if num1 > num2:
    print(f'\nO primeiro valor \033[1m({num1:.1f})\033[m, é o {color.blue("MAIOR VALOR DIGITADO!")}')
elif num2 > num1:
    print(f'\nO segundo valor \033[1m({num2:.1f})\033[m, é o {color.blue("MAIOR VALOR DIGITADO!")}')
else:
    print(f'\nO primeiro e o segundo valor \033[1m({num1:.1f} e  {num2:.1f})\033[m {color.blue("SÃO IGUAIS!")}')
