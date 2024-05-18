'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
uma Sequência de Fibonacci.

Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''

n = int(input('Quantos termos da Sequência de Fibonacci deseja ver? '))
t1 = 1
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n: # enquanto o contador for menor que o número digitado
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2 # o primeiro termo recebe o próximo e assim por diante
    t2 = t3 # o segundo termo recebe o próximo e assim por diante
    cont += 1

'''while cont <= n:
    if cont == 0:
        t = 0
        print('0', end=' ')
    elif cont == 1:
        t = 2 * cont - 1
        print('{}'.format(t), end=' ')
    else:
        t = (cont - 2) - (cont + 1)
    cont += 1'''