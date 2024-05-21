'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo
que o vencedor tirou o maior número no dado.'''
from random import randint # números aleatórios
from time import sleep # tempo para imprimir os resultados
from operator import itemgetter # para ordenar

# sorteando no dicionário jogos
jogos = {'Jogador1' : randint(1, 6),
         'Jogador2' : randint(1, 6),
         'Jogador3' : randint(1, 6),
         'Jogador4' : randint(1, 6)
         }

# criando a lista ranking
ranking = list()

# imprimindo os valores sorteados
print('Valores sorteados:') 
for k, v in jogos.items():
    print('{} tirou {} no dado.'.format(k, v))
    sleep(1)

# ordenando o ranking
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
