'''Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.'''
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA-SENA'))
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quant: # se menor que 1, pula o laço
    cont = 0 # contador de números adicionados à lista
    # sorteando os números
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append((num)) # adiciona número à lista se for um número ainda não adicionado
            cont += 1 
        if cont >= 6:
            break
    lista.sort() # ordena os números
    jogos.append(lista[:]) # copia a lista para jogos
    lista.clear() # limpa a lista
    total += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, ' BOA SORTE!!! ', '-=' * 5)
