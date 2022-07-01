# Tente...
try:
    a = int(input('Digite um número: ').strip())
    b = int(input('Digite outro número: ').strip())
    r = a / b

# Análise de exceções
# 1 - TypeError e ValueError
except (TypeError, ValueError):
    print(f'Tivemos um problema com o tipo de dado que você inseriu.')

# 2 - KeyboardInterrupt
except KeyboardInterrupt:
    print('O usuário preferiu não digitar nada :(')

# 3 = ZeroDivisionError
except ZeroDivisionError:
    print('Não é possível dividir um número por 0!')

# 4 - Outras exceções
except Exception as erro:
    print(f'O erro encontrado foi: {erro}')

# Se não der erro
else:
    print(f'Resultado: {a} / {b} = {r}')

# Se der erro ou não, executa essa parte ↓
finally:
    print('\nVolte sempre :)')
