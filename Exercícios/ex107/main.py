# Importar o módulo moeda.py
import moedas

# Usar as funções aumentar, diminuir, dobro e metade
p = float(input('Digite o preço: R$'))

print()
print('-' * 30)
print()
print(f'A metade de R${p:.2f} é R${moedas.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moedas.dobro(p):.2f}')
print(f'Aumentando em 10%, temos R${moedas.aumentar(p, 10):.2f}')
print(f'Diminuindo em 13, temos R${moedas.diminuir(p, 13):.2f}')