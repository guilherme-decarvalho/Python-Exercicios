'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois
disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão
na tupla.'''

'''
Os valores sorteados foram: 5 7 5 4 6
O maior valor sorteado foi: 7
O menor valor sorteado foi: 4
'''
from random import randint
num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores sorteados foram: ', end='')
for n in num:
    print('{} '.format(n), end='')
print ('\nO maior valor sorteado foi {}.'.format(max(num)))
print ('O menor valor sorteado foi {}.'.format(min(num)))

