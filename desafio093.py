'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai
ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incuindo o total de gols
feitos durante o campeonato.'''
aproveitamento = dict()
partidas = list()

# lendo dados
aproveitamento['Jogador'] = input('Nome do jogador: ')
jogos = int(input(f'Quantos jogos {aproveitamento["Jogador"]} jogou? '))

# lendo gols por partidas
for c in range(0, jogos):
    partidas.append(int(input(f'Quantos gols {aproveitamento['Jogador']} fez na partida {c + 1}? ')))
aproveitamento['Gols'] = partidas[:] # copia partidas em Gols
aproveitamento['Total'] = sum(partidas) # soma dos gols
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)

# imprimindo na tela
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

# imprimindo na tela
print(f'O jogador {aproveitamento["Jogador"]} jogou {len(aproveitamento["Gols"])} partidas.')
for i, v in enumerate(aproveitamento['Gols']):
    print('   => Na partida {} fez {} gols.'.format(i+1, v))
print(f'Foi um total de {aproveitamento["Total"]} gols.')
