'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai
ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incuindo o total de gols
feitos durante o campeonato.'''
aproveitamento = dict()
partidas = list()
aproveitamento['Jogador'] = input('Nome do jogador: ')
jogos = int(input('Quantos jogos {} jogou? '.format(aproveitamento["Jogador"])))
for c in range(0, jogos):
    partidas.append(int(input('Quantos gols {} fez na partida {}? '.format(aproveitamento['Jogador'], c + 1))))
aproveitamento['Gols'] = partidas[:]
aproveitamento['Total'] = sum(partidas)
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)
for k, v in aproveitamento.items():
    print('O campo {} tem o valor {}.'.format(k, v))
print('-=' * 30)
print('O jogador {} jogou {} partidas.'.format(aproveitamento["Jogador"], len(aproveitamento["Gols"])))
for i, v in enumerate(aproveitamento['Gols']):
    print('   => Na partida {} fez {} gols.'.format(i+1, v))
print('Foi um total de {} gols.'.format(aproveitamento["Total"]))
