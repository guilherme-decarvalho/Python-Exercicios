'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex.: 5! = 5x4x3x2x1=120'''

n = int(input('Digite um número: '))
#fatorial = num * (num - 1) * (n -2) * ... * 2 * 1
c = n
f = 1
print('Calculando {}! ='.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='') # se c > 1, imprime ' x ', se c == 1, imprime ' = '
    if c > 1:
        print (' x ', end='')
    else:
        print(' = ', end='')
    f *= c # multiplica f por c
    c -= 1 # retira 1 de c
print('{}.'.format(f))

'''Solução alternativa:

utilizar from math import factorial'''







