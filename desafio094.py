'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

a) quantas pessoas foram cadastradas.
b) a média de idade do grupo.
c) uma lista com todas as mulheres.
d) uma lista com todas as pessoas com idade acima da média.'''
# criando variáveis
lista = list()
pessoas = dict()
cont = somaidade = media = 0

# laço
while True:
    # coletando dados
    pessoas['Nome'] = input('Nome: ')
    while True:
        pessoas['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoas['Idade'] = int(input('Idade: '))
    cont += 1 # quantidade de pessoas
    somaidade += pessoas['Idade'] # soma as idades
    media = somaidade / cont
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

# imprimindo total de cadastrados
if cont == 1:
    print('Foi cadastrada 1 pessoa.')
else:
    print(f'Foram cadastradas {cont} pessoas.')
print()

# imprimindo média de idades
print(f'A média de idade é {media:5.2f}.')
print()

# imprimindo total de mulheres cadastradas
print('Lista de mulheres cadastradas: ')
print()
for p in lista:
    if p['Sexo'] in 'F':
        print(f'    - {p["Nome"]}')
print()

# imprimindo pessoas com idade acima da média
print('Lista de pessoas com idade acima da média: ')
for p in lista:
    if p['Idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('<< ENCERRADO >>')



