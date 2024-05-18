'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso
lidos.'''

maior = 0
menor = 0
for p in range(1, 6): #Da 1ª a 5ª pessoa
    peso = float(input(('Peso da {}ª pessoa: '.format(p)))) #Conta as pessoas ordinalmente
    if p == 1: #Primeira pessoa será o maior e menor peso
        maior = peso
        menor = peso
    else:
        if peso > maior: #Se o peso da 2ª pessoa em diante for maior que o da anterior, esse será o peso maior
            maior = peso
        if peso < menor: #Se o peso da 2ª pessoa em diante for menor que o da anterior, esse será o peso menor
            menor = peso
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi de {}Kg.'.format(menor))
