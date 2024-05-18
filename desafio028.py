'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
print('---QUE NÚMERO EU PENSEI?---')
from random import randint
n1 = randint(0, 5)
n2 = int(input('Digite um número de 0 a 5: '))
if n2 == n1:
    print('Parabéns, você ganhou! O número que você digitou é {} e o que pensei também é {}.'.format(n2, n1))
else:
    print('Você perdeu! Tente de novo! O número que você digitou é {} e o que pensei foi {}.'.format(n2, n1))

'''Solução alternativa:
from random import randint
from time import sleep
computador = randint(0, 5)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))'''

