from functions import conectarSite

red = '\033[31m'
blue = '\033[34m'
reset = '\033[m'

url = 'https://' + str(input('Digite a url de um site: https://')).strip()
print('')

nomeSite = url.replace('https://', '').replace('www.', '')
if conectarSite(url):
    print(f'{blue}O site \'{nomeSite}\' está acessível no momento.{reset}')
else:
    print(f'{red}O site \'{nomeSite}\' não está acessível no momento.{reset}')
