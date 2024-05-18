'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''

'''
============================
    CADASTRE UMA PESSOA
============================
Idade: 33
Sexo: [M/F] M
============================
Quer continuar? [S/N] S
============================
    CADASTRE UMA PESSOA
============================
Idade: 12
Sexo: [M/F]: F
============================
Quer continuar? [S/N] 25
Quer continuar? [S/N] s
============================
    CADASTRE UMA PESSOA
============================
Idade: 25
Sexo: [M/F]: g
Sexo: [M/F]: y
Sexo: [M/F]:F
============================
Quer continuar? [S/N] w
Quer continuar? [S/N] s
============================
    CADASTRE UMA PESSOA
============================
Idade: 8
Sexo: [M/F]: M
============================
Quer continuar? [S/N] N
-------FIM DO PROGRAMA-------
Total de pessoas com mais de 18 anos: 2
Ao todo temos 2 homem(ns) cadastrado(s).
E temos 1 mulher(es) com menos de 20 anos.
'''
maioridade = conth = contm = 0
while True:
    print('=' * 60)
    print('{:^60}'.format('CADASTRE UMA PESSOA'))
    print('=' * 60)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': # força a escolher M ou F
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('=' * 60)
print('{:=^60}'.format(' FIM DO PROGRAMA '))
print('Total de pessoas com mais de 18 anos: {}'.format(maioridade))
print('Ao todo temos {} homem(ns) cadastrado(s).'.format(conth))
print('E temos {} mulher(es) com menos de 20 anos.'.format(contm))



