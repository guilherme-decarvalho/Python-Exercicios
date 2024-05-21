'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.'''
from datetime import date
trab = {}
trab['Nome'] = input('Nome: ')
trab['Idade'] = int(input('Ano de nascimento: '))
trab['Idade'] = date.today().year - trab['Idade']
trab['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if trab['CTPS'] != 0:
    trab['Ano de Contratação'] = int(input('Ano de contratação: '))
    trab['Salário'] = float(input('Salário: R$'))
    trab['Aposentadoria'] = trab['Idade'] + 35 - (date.today().year - trab['Ano de Contratação'])
print('-=' * 30)
for k, v in trab.items():
    print(f'{k}: {v}', end='')
    print()
