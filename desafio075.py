'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No
final, mostre:

a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro 3.
c) Quais foram os números pares.'''

'''
Digite um número: 5
Digite outro número: 9
Digite mais um número: 2
Digite o último número: 3
Você digitou os valores (5, 9, 2, 3)
O valor 9 apareceu 1 vez(es)
O valor 3 apareceu na 4ª posição
Os valores pares digitados foi(foram) 2.
'''

'''Digite um número: 2
Digite outro número: 4
Digite mais um número: 6
Digite o último número: 8
Você digitou os valores (2, 4, 6, 8)
O valor 9 apareceu 0 vez(es)
O valor 3 foi digitado em nenhuma posição
Os valores pares digitados foi(foram) 2 4 6 8.'''
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('Você digitou os valores {}.'.format(num))
print('O valor 9 apareceu {} vez(es).'.format(num.count(9)))
if 3 in num:
    print('O valor 3 apareceu na {}ª posição.'.format(num.index(3)+1))
else:
    print('O valor 3 foi digitado em nenhuma posição.')
print('O(s) valores par(es) digitado(s) foi(foram) ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

