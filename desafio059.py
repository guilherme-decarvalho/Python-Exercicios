'''Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
s = 4
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
opção = 0
while opção != 5:
    print('''O que deseja fazer?
[1] Somar os números
[2] Multiplicar os números
[3] Verificar qual dos números é maior
[4] Novos números
[5] Sair do programa''')
    opção = int(input('Digite sua escolha: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é {}.'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            print('{] é maior que {}.'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}.'.format(n2, n1))
        else:
            print('{} é igual a {}.'.format(n1, n2))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa! Volte Sempre!')







