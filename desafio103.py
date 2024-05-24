'''
Faça um programa que tenha uma função chamada ficha(), que receba dois
parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
tenha sido informado corretamente.

------------------------------------------
Nome do Jogador: Romário
Total de Gols: 33
O jogador Romário fez 33 gol(s) no campeonato.

------------------------------------------
Nome do Jogador: 
Total de Gols: 2
O jogador <desconhecido> fez 2 gol(s) no campeonato.

------------------------------------------
Nome do Jogador: 
Total de Gols: 
O jogador <desconhecido> fez 0 gol(s) no campeonato.
'''
# Função
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

# Programa Principal
j = (str(input('Nome do Jogador: ')))
g = (str(input('Total de Gols: ')))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)