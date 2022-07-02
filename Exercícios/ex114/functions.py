from selenium import webdriver

red = '\033[31m'
yellow = '\033[33m'
reset = '\033[34m'


def conectarSite(site):
    navegador = webdriver.Chrome()
    try:
        navegador.get(site)
    except:
        print(f'{red}Não consegui conectar no site \'{site}\'!{reset}')
    else:
        print(f'{yellow}Eu consegui conectar no site \'{site}\'!{reset}')
