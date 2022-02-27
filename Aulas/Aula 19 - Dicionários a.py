from time import sleep

# Determinar um dicionário

# dados = dict()
dados = {'nome': 'Pedro', 'idade': 17, 'sexo': 'M'}


# Mostrar os dados de um dicionário

# print(f'''O dicionário 'dados' contém os seguintes elementos:
# 'nome'  = {dados['nome']}
# 'idade' = {dados['idade']}''')


# Adicionar mais elementos no dicionário

# print(f'''
# \nCom o novo item 'sexo' inserido, agora o dicionário armazena mais um valor:
# 'nome'  = {dados['nome']}
# 'idade' = {dados['idade']}
# 'sexo'  =  {dados['sexo']}''')


# Eliminando um item

del dados['idade']


# Declarando um novo dicionário chamado 'filme'
filme = {
    'título': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

# print('\n')
""" 'values' são os valores, 'keys' as chaves e 'items' são ambos. Ao usar o método correspondente, exibi a mesma"""
# print(filme.values())
# print(filme.keys())
# print(filme.items())
# print()


# Exibindo com os itens com o for:

# for k, v in filme.items():  # Funcionamento parecido com o Enumerate, onde a primeira variável é o índice (nesse caso, as chaves), e a segunda é o valor
#     print(f'O {k} é {v}')

filmes = [{'título': 'Star Wars',
           'ano': 1977,
           'diretor': 'George Lucas'},

          {'título': 'Avengers',
           'ano': 2012,
           'diretor': 'joss Whendon'},

          {'título': 'Matrix',
           'ano': 1999,
           'diretor': 'Wachowski'}
          ]

print()
sleep(0.5)
print('==== Locadora 2000 ====')
sleep(0.5)

print()
print('-' * 32)

sleep(1)

for filme in filmes:
    print(f'''
Nome do filme: {filme["título"]}
Ano: {filme["ano"]}
Diretor: {filme["diretor"]}

--------------------------------''')
    sleep(0.8)
