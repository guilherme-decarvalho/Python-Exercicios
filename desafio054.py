'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
totmaior = 0
totmenor = 0
for pessoas in range(1, 8): #Da 1ª a 7ª pessoa
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas))) #Conta as pessoas ordinalmente
    idade = date.today().year - nasc
    if idade >= 21:
        totmaior += 1 #A cada ocorrência, contar
    else:
        totmenor += 1 #A cada ocorrência, contar
print('Ao todo, há {} pessoas maiores de idade'.format(totmaior), end=' ')
print('e há {} pessoas menores de idade.'.format(totmenor))

