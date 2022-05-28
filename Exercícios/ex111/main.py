# Importar o módulo moeda
from utilidadesCeV import moeda

# Usar as funções aumentar, diminuir, dobro e metade
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)
