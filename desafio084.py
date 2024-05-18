'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.'''

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
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso)))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print('Ao todo, você cadastrou {} pessoas.'.format(len(princ)))
print('O maior peso foi de {}Kg. Peso de '.format(mai), end='')
for p in princ:
    if p[1] == mai:
        print('{}'.format(p[0]), end= ' ')
print()
print('O menor peso foi de {}Kg. Peso de '.format(men), end='')
for p in princ:
    if p[1] == men:
        print('{}'.format(p[0]), end= ' ')
print()
'''