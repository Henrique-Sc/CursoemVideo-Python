# Importar o módulo moeda.py
import moedas

# Usar as funções aumentar, diminuir, dobro e metade
p = float(input('Digite o preço: R$'))

print()
print('-' * 30)
print()

print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, formatar=True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, formatar=True)}')
print(f'Aumentando em 10%, temos {moedas.aumentar(p, 10, formatar=True)}')
print(f'Diminuindo em 13, temos {moedas.diminuir(p, 13, formatar=True)}')
