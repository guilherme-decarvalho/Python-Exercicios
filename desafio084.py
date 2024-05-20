'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.'''

pessoas = list() # lista que armazenará o nome e o peso das pessoas
nomepeso = list() # nome e peso
maior = menor = 0

while True:
    # armazenando os dados nome e peso
    nomepeso.append(str(input('Digite o nome: ')))
    nomepeso.append(float(input('Digite o peso em kg: ')))
    # definindo o menor e o maior peso
    if len(pessoas) == 0:
        maior = menor = nomepeso[1]
    else:
        if nomepeso[1] > maior:
            maior = nomepeso[1]
        if nomepeso[1] < menor:
            menor = nomepeso[1]
    pessoas.append(nomepeso[:]) # armazenando uma cópia de nomepeso em pessoas
    nomepeso.clear() # limpando a lista nomepeso
    # perguntando ao usuário se ele quer continuar
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = (str(input('Não entendi. Quer continuar? [S/N] '))).strip().upper()[0]
    if continua in 'N':
        break
print('-=' * 30)
print(pessoas)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}kg. Este é o peso de', end=' ')
for pessoa in pessoas: # verifica cada pessoa em na lista de pessoas e procura o maior peso
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}kg. Este é o peso de', end=' ')
for pessoa in pessoas: # verifica cada pessoa em na lista de pessoas e procura o menor peso
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')

'''
pessoas = list()
nomepeso = list()
pessoasleves = list()
pessoaspesadas = list()
resposta = ''
cont = maior = menor = contmaior = contmenor = 0
# adicionando pessoas
while True: # primeiro adicionar à lista nomepeso pra depois adicionar à lista pessoas
    nomepeso.append(str(input('Nome: ')))
    nomepeso.append(float(input('Peso: ')))
    pessoas.append(nomepeso[:])
    if cont == 0: # igualando a 1ª pessoa a menor e maior peso
        menor = maior = nomepeso[1]
        contmenor = contmaior = 1
        pessoaspesadas.append(nomepeso[0]) # adicionando a pesadas
        pessoasleves.append(nomepeso[0]) # adicionando a leves
    else:
        if nomepeso[1] == maior == menor:
            contmaior += 1
            contmenor += 1
            pessoaspesadas.append(nomepeso[0])
            pessoasleves.append(nomepeso[0])
        elif nomepeso[1] == maior and nomepeso[1] > menor:
            contmaior += 1
            pessoaspesadas.append(nomepeso[0])
        elif nomepeso[1] > maior:
            pessoaspesadas.clear()
            maior = nomepeso[1]
            contmaior = 1
            pessoaspesadas.append(nomepeso[0])
        elif nomepeso[1] == menor and nomepeso[1] < maior:
            contmenor += 1
            pessoasleves.append(nomepeso[0])
        elif nomepeso[1] < menor:
            pessoasleves.clear()
            menor = nomepeso[1]
            contmenor = 1
            pessoasleves.append(nomepeso[0])
    cont += 1
    nomepeso.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Não entendi. Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print('-=' * 30)
print('Foram cadasradas {} pessoas.'.format(cont)) #ou format(len(pessoas))
print('O maior peso foi {}kg. {} pessoa(s) foi(foram) registrada(s) com esse peso: {}.'.format(maior, contmaior, pessoaspesadas))
print('O menor peso foi {}kg. {} pessoa(s) foi(foram) registrada(s) com esse peso: {}.'.format(menor, contmenor, pessoasleves))
'''