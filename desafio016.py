#Crie um programa que leia um número real qualquer pelo teclado e mostre
#na tela a sua porção inteira
from math import trunc
n = float(input('Digite um número real: '))
print('Sua porção inteira é igual a {}.'.format(trunc(n)))

#Soluções alternativas:
#from math import floor
#n = float(input('Digite um número real: '))
#print('Sua porção inteira é igual a {}.'.format(floor(n)))

#import math
#n = float(input('Digite um número real: '))
#print('Sua porção inteira é igual a {}.'.format(math.trunc(n)))

#n = float(input('Digite um número real: '))
#print('Sua porção inteira é igual a {}.'.format(int(n)))