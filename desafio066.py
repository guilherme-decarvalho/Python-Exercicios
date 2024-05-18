'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digiter o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag).'''

cont = soma = 0
while True:
    n = int(input('Digite um número (digite 999 para sair do programa): '))
    if n == 999:
        break
    cont += 1
    soma += n
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
