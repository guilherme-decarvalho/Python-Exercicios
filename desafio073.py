'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados
b) Os últimos 4 colocados na tabela
c) Uma lista em ordem alfabética
d) Em que posição na tabela está o time da Chapecoense'''

'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Lista de times do Brasileirão: ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', '...')
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Os 5 primeiros são ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro')
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Os 4 últimos são ('Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Times em ordem alfabética: ['Atlético', 'Atlético-GO', 'Atlético-PR', 'Avaí', '...']
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
O Chapecoense está na 8ª posição
'''
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 60)
#print('Lista de times do Brasileirão: {}.'.format(times))
# Mostrando a lista de times
print('Lista de times do Brasileirão:', end=' ')
for t in times:
    if t != times[-1]:
        print(f'{t}', end=', ')
    else:
        print(f'{t}.')
print('-=' * 60)
# Mostrando os 5 primeiros times
print('Os 5 primeiros são', end=' ')
for t in times[0:5]:
    if t != times[4]:
        print(f'{t}', end=', ')
    else:
        print(f'{t}.')
print('-=' * 60)
# Mostrando os 4 últimos times
print('Os 4 últimos são', end=' ')
for t in times[-4:]:
    if t != times[-1]:
        print(f'{t}', end=', ')
    else:
        print(f'{t}.')
print('-=' * 60)
# Mostrando os times em ordem alfabética
print('Times em ordem alfabética: {}.'.format(sorted(times)))
print('-=' * 60)
print('O Chapecoense está na {}ª posição.'.format(times.index("Chapecoense")+1))

