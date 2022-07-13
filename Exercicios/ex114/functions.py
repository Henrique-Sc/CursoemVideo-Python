# from selenium import webdriver
from urllib import request

red = '\033[31m'
blue = '\033[34m'
reset = '\033[m'


def conectarSite(site):

    # Minha solução:
    # navegador = webdriver.Chrome()
    # try:
    #     navegador.get(site)
    # except:
    #     return False
    # else:
    #     return True

    # Solução do Guanabara:
    try:
        request.urlopen(site)
    except:
        # print(f'{red}O site não está acessível no momento. {reset}')
        return False
    else:
        # print(f'{blue}O site está acessível no momento. {reset}')
        return True
