vel = int(input('Qual a velocidade do seu veículo? '))
if vel <= 80:
    print('\nvocê não atingiu o limite de velocidade!')
else:
    print('\nVocê ultrapassou o limite de 80km/h!')
    print(f'Você tomou uma multa de R${(vel - 80) * 7}!')
