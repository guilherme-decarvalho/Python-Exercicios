'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador.'''
lista = list()
aproveitamento = dict()
partidas = list()
while True:
    aproveitamento['Jogador'] = input('Nome do jogador: ')
    jogos = int(input('Quantos jogos {} jogou? '.format(aproveitamento["Jogador"])))
    partidas.clear()
    for c in range(0, jogos):
        partidas.append(int(input('     Quantos gols {} fez na partida {}? '.format(aproveitamento['Jogador'], c + 1))))
    aproveitamento['Gols'] = partidas[:]
    aproveitamento['Total'] = sum(partidas)
    lista.append(aproveitamento.copy())
    aproveitamento.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(' cod ', end='')
for i in aproveitamento.keys():
    print('{:<15}'.format(i), end='')
print()
print('-' * 40)
for k, v in enumerate(lista):
    print('{:>3} '.format(k), end='')
    for d in v.values():
        print('{:<15}'.format(str(d)), end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print('ERRO! Não existe jogador com código {}.'.format(busca))
    else:
        print(' -- LEVANTAMENTO DO JOGADOR {}:'.format(lista[busca]["Jogador"]))
        for i, g in enumerate(lista[busca]['Gols']):
            print('     No jogo {} fez {} gols.'.format(i+1, g))
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