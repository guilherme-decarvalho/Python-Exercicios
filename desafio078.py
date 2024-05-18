'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na
lista.'''

'''
Digite um valor para a Posição 0: 1
Digite um valor para a Posição 1: 2
Digite um valor para a Posição 2: 1
Digite um valor para a Posição 3: 5
Digite um valor para a Posição 4: 5
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Você digitou os [1, 2, 1, 5, 5]
O maior valor digitado foi 5 nas posições 3... 4...
O menor valor digitado foi 1 nas posições 0... 2...
'''

num = []
maior = 0
menor = 0
# adicionando valores à lista
for c in range(0, 5):
    num.append(int(input('Digite um valor para a Posição {}: '.format(c))))
    if c == 0: # define o primeiro valor como maior e menor
        maior = menor = num[c]
    else: # analisa os valores como maiores e menores
        if num[c] > maior:
                maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('-=' * 30)
print('Você digitou os valores {}'.format(num))
print('O maior valor digitado foi {} na(s) posição(ões) '.format(maior), end='')
for i, v in enumerate(num):
    if v == maior:
        print('{}... '.format(i), end='')
print()
print('O menor valor digitado foi {} na(s) posição(ões) '.format(menor), end='')
for i, v in enumerate(num):
    if v == menor:
        print('{}... '.format(i), end='')
print()

