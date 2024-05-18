'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquele que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

s = 0
cont = 0
for c in range(1,7):
    i = int(input('Digite o {}º número: '.format(c)))
    if i % 2 == 0:
        s += i
        cont += 1 #soma a contagem a cada aparecimento de número par        
print('Você informou {} número(s) par(es) e a soma dos pares é igual a {}.'.format(cont, s))

