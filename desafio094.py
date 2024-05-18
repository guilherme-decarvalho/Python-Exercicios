'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

a) quantas pessoas foram cadastradas.
b) a média de idade do grupo.
c) uma lista com todas as mulheres.
d) uma lista com todas as pessoas com idade acima da média.'''
lista = list()
pessoas = dict()
cont = somaidade = média = 0
while True:
    pessoas['Nome'] = input('Nome: ')
    while True:
        pessoas['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoas['Idade'] = int(input('Idade: '))
    cont += 1
    somaidade += pessoas['Idade']
    média = somaidade / cont
    lista.append(pessoas.copy())
    pessoas.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(lista)
print('-=' * 30)
if cont == 1:
    print('Foi cadastrada 1 pessoa.')
else:
    print('Foram cadastradas {} pessoas.'.format(cont))
print('A média de idade é {:5.2f}.'.format(média))
print('As mulheres cadastradas foram ', end='')
for p in lista:
    if p['Sexo'] in 'F':
        print('{} '.format(p["Nome"]), end='')
print()
print('Lista de pessoas com idade acima da média: ')
for p in lista:
    if p['Idade'] >= média:
        print('     ')
        for k, v in p.items():
            print('{} = {}; '.format(k, v), end='')
        print()
print('<< ENCERRADO >>')



