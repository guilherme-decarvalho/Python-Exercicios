'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre ele (desconsiderando o flag).'''
'''n = cont = soma = 0
print('Para sair do programa, digite 999.')
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))'''


n = cont = soma = 0
print('Para sair do programa, digite 999.')
n = int(input('Digite um número: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))