'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.'''
'''continua = ''
soma = 0
cont = 0
maior = 0
menor = 0
while continua != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()
media = soma / cont
print('A soma dos números digitados é {}.'.format(soma))
print('A média entre esses números é {}.'.format(media))
print('O maior número digitado foi {}.'.format(maior))
print('O menor número digitado foi {}.'.format(menor))

'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N)')).upper().strip()[0] #Para considerar só a 1ª letra
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))

