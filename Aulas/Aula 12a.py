nome = str(input('Qual o seu nome? ')).title()
if 'Henrique' in nome:
    print('Uau  que nome lindo! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧')

elif 'Pedro' in nome or 'Paulo' in nome or 'Maria' in nome:
    print('Seu nome é bem popular no Brasil!')

elif 'May' in nome or 'Mai' in nome:
    print('Seu nome é muito lindo! ')

else:
    print('Hmm seu nome é bem normal ;-;')
print(f'Tenha um bom dia {nome}!')