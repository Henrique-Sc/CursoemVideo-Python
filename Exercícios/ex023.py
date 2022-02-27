num = input('Digite um número entre 0 a 9999: ')
tamanho = 4 - len(num)
novo_num = tamanho * '0' + num

print(f"""\nOs digitos separados desse número é:
Unidade: {novo_num[3]}
Dezena:  {novo_num[2]}
Centena: {novo_num[1]}
Milhar:  {novo_num[0]}""")