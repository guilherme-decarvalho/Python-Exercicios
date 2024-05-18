'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''

'''
Digite um valor: 3
Quer continuar? [S/N] s
Digite um valor: 9
Quer continuar? [S/N] s
Digite um valor: 2
Quer continuar? [S/N] s
Digite um valor: 5
Quer continuar? [S/N] s
Digite um valor: 0
Quer continuar? [S/N] n
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Você digitou 5 elementos.
Os valores em ordem decrescente são [9, 5, 3, 2, 0]
O valor 5 faz parte da lista.
'''

'''
Digite um valor: 3
Quer continuar? [S/N] s
Digite um valor: 7
Quer continuar? [S/N] s
Digite um valor: 2
Quer continuar? [S/N] n
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Você digitou 3 elementos.
Os valores em ordem decrescente são [7, 3, 2]
O valor 5 não foi encontrado na lista.
'''
valor = []
cont = 0
while True:
    valor.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN': # força a digitar 'SN'
        resposta = str(input('Não entendi. Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if resposta in 'N':
        break
print('-=' * 30)
print('Você digitou {} elementos.'.format(cont)) #ou print('Você digitou {} elementos.'.format(len(valores)))
valor.sort(reverse=True)
print('Os valores em ordem decrescente são {}'.format(valor))
if 5 in valor:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
print('FIM')
