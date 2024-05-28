'''
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
'''
import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'O site Pudim não está acessível no momento.')
else:
    print(f'Consegui acessar o site Pudim com sucesso.')
    print(site.read())