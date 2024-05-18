#Faça um programa que leia um número inteiro qualquer e mostre na tela
#a sua tabuada.
'''n = int(input('Digite um número: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print('Sua tabuada é: \n{0} x 1 = {1} \n{0} x 2 = {2} \n{0} x 3 = {3} \n{0} x 4 = {4} \n{0} x 5 = {5} \n{0} x 6 = {6} \n{0} x 7 = {7} \n{0} x 8 = {8} \n{0} x 9 = {9} \n{0} x 10 = {10}'.format(n, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10))

#Solução alternativa 1:

#n = int(input('Digite um número para ver a sua tabuada: '))
#n1 = n
#n2 = n * 2
#n3 = n * 3
#n4 = n * 4
#n5 = n * 5
#n6 = n * 6
#n7 = n * 7
#n8 = n * 8
#n9 = n * 9
#n10 = n * 10
#print('{0} x 1 = {1} \n{0} x 2 = {2} \n{0} x 3 = {3} \n{0} x 4 = {4} \n{0} x 5 = {5} \n{0} x 6 = {6} \n{0} x 7 = {7} \n{0} x 8 = {8} \n{0} x 9 = {9} \n{0} x 10 = {10}'.format(n, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10))'''

#Solução alternativa 2:

n = int(input('Digite um número para ver a sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))
print('-' * 12)
