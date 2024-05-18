#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians
a = float(input('Digite o ângulo em graus: '))
print('O valor de {0} GRAUS em RADIANOS é {1:.2f}. \nO SENO de {0} graus é {2:.2f}. \nO COSSENO de {0} graus é {3:.2f}. \nA TANGENTE de {0} graus é {4:.2f}.'.format(a, radians(a), sin(radians(a)), cos(radians(a)), tan(radians(a))))



