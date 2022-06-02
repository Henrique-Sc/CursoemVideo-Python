# Importar o módulo moeda.py
import moeda

# Usar as funções aumentar, diminuir, dobro e metade
p = float(input('Digite o preço: R$'))

print()
print('-' * 30)
print()

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formatar=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formatar=True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, formatar=True)}')
print(f'Diminuindo em 13, temos {moeda.diminuir(p, 13, formatar=True)}')
