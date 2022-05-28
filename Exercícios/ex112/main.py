# Importar o módulo moeda
from utilidadesCeV import moeda
from utilidadesCeV import dado


# Usar as funções aumentar, diminuir, dobro e metade
p = dado.leiaDinheiro('15')
moeda.resumo(p, 80, 35)
