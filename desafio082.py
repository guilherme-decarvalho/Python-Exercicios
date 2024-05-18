'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas valores pares e os valores ímpares
digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

'''
Digite um valor: 6
Quer continuar? [S/N] s
Digite um valor: 2
Quer continuar? [S/N] s
Digite um valor: 7
Quer continuar? [S/N] s
Digite um valor: 8
Quer continuar? [S/N] s
Digite um valor: 3
Quer continuar? [S/N] s
Digite um valor: 9
Quer continuar? [S/N] n
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
A lista completa é [6, 2, 7, 8, 3, 9]
A lista de pares é [6, 2, 8]
A lista de ímpares é [7, 3, 9]
'''
valor = []
pares = []
impares = []
# criando lista Valor
while True:
    valor.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Não entendi. Quer continuar? [S/N] '))
    if resposta in 'N':
        break
# separando pares e ímpares
for i, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 40)
print('A lista completa é {}.'.format(valor))
print('A lista de pares é {}.'.format(pares))
print('A lista de ímpares é {}.'.format(impares))