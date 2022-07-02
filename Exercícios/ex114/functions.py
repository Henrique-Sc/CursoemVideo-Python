from selenium import webdriver

red = '\033[31m'
blue = '\033[34m'
reset = '\033[34m'


def conectarSite(site):
    navegador = webdriver.Chrome()
    try:
        navegador.get(site)
    except:
        title = navegador.title
        print(f'{red}O site {title} não está acessível no momento.{reset}')
    else:
        title = navegador.title
        print(f'{blue}O site {title} está acessível no momento.{reset}')
