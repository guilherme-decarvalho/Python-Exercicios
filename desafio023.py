'''Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados.

Ex.: Digite um número: 1834

unidade: 4
Dezena: 3
Centena: 8
Unidade de milhar: 1'''

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Unidade de milhar: {}'.format(um))
