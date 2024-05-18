'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

Ex.: Ana Maria de Souza
Primeiro: Ana
Último: Souza'''

nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))


