# pessoas = {'nome': 'Henrique',
#            'sexo': 'M',
#            'idade': 16}
#
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos\n')
# pessoas['nome'] = 'Maiara'
# pessoas['sexo'] = 'F'
# pessoas['peso'] = 56.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf'])
