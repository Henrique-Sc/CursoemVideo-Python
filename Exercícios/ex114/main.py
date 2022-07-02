from functions import conectarSite

nomeSite = 'https://' + str(input('Digite a url de um site: https://')).strip()
print('')
conectarSite(nomeSite)
