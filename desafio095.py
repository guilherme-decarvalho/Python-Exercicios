'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador.'''
lista = list()
aproveitamento = dict()
partidas = list()
while True:
    # lendo dados
    aproveitamento.clear() # limpando o dicionário
    aproveitamento['Jogador'] = input('Nome do jogador: ')
    jogos = int(input(f'Quantos jogos {aproveitamento["Jogador"]} jogou? '))
    partidas.clear()

    # lendo gols por partidas
    for c in range(0, jogos):
        partidas.append(int(input(f'     Quantos gols {aproveitamento["Jogador"]} fez na partida {c + 1}? ')))
    aproveitamento['Gols'] = partidas[:]
    aproveitamento['Total'] = sum(partidas)
    lista.append(aproveitamento.copy()) # copiando o dicionário à lista
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(' cod ', end='')

# tabela dos jogadores
for i in aproveitamento.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

# escolhendo o jogador para apresentar os dados
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[busca]["Jogador"]}:')
        for i, g in enumerate(lista[busca]['Gols']):
            print(f'     No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')



'''print('-=' * 30)
for k, v in aproveitamento.items():
    print('O campo {} tem o valor {}.'.format(k, v))
print('-=' * 30)
print('O jogador {} jogou {} partidas.'.format(aproveitamento["Jogador"], len(aproveitamento["Gols"])))
for i, v in enumerate(aproveitamento['Gols']):
    print('   => Na partida {} fez {} gols.'.format(i+1, v))
print('Foi um total de {} gols.'.format(aproveitamento["Total"]))'''