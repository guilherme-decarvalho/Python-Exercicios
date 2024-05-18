'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo
que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
jogos = {'Jogador1' : randint(1, 6),
         'Jogador2' : randint(1, 6),
         'Jogador3' : randint(1, 6),
         'Jogador4' : randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogos.items():
    print('{} tirou {} no dado.'.format(k, v))
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print('  {}º lugar: {} com {}.'.format(i+1, v[0], v[1]))
    sleep(1)