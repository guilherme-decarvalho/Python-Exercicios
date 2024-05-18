#Faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triângulo retângulo, calcule e mostre o comprimento
#da hipotenusa
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('O valor da hipotenusa é igual a {}.'.format(hypot(co, ca)))

#Soluções alternativas:

'''import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('O valor da hipotenusa é igual a {}.'.format(math.hypot(co, ca)))'''

'''co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é igual a {}.'.format(h))'''

