sexo_aceito = ['F', 'M', 'O']
sexo = str(input('''Qual o seu sexo? 

[F] Feminino
[M] Masculino
[O] Outros...

Digite aqui: ''')).upper().strip()[0]

while sexo not in sexo_aceito:
    sexo = str(input('\n\033[31mDados incorretos!\033[m Insira um valor válido: [F/M/O] ')).upper().strip()[0]
print('\n\033[34mDados coletados com sucesso!\033[m')
