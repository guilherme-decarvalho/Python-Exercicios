'''Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número, que é {}, é maior que o segundo número, que é {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo número, que é {}, é maior que o primeiro número, que é {}.'.format(n2, n1))
elif n1 == n2:
    print('Não existe número maior, ambos são iguais.')

#PODERIA SER USADO "else:" para "elif n1 == n2:"

