'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''
from datetime import date
a = int(input('Qual é o ano? Coloque 0 para o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(a))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(a))

'''SOLUÇÕES ALTERNATIVAS
a = int(input('Qual é o ano? '))
if a % 4 == 0:
    print('O ano {} é BISSEXTO.'.format(a))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(a))
'''

