'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1): # todos os números de 1 até o número digitado
    if num % c == 0: #divide por todos os números no range e resto zero
        print('\033[34m', end='') #mostra o número em azul
        tot += 1 # conta a cada aparecimento de resto 0
    else:
        print('\033[m', end='') #mostra na cor padrão
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividido {} vez(es)'.format(num, tot), end=' ')
if tot == 2:
    print('e, por isso, ele É PRIMO!')
else:
    print('e, por isso, ele NÃO É PRIMO!')



