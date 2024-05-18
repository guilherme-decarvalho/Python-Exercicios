'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalos de 1 até 500.'''

soma = 0
cont = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        cont += 1
print('O somatório de todos os {} números ímpares múltiplos de 3 de 1 a 500 é {}'.format(cont, soma))

'''s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print('O somatório dos números ímpares múltiplos de 3 de 1 a 500 é {}'.format(s))'''

'''s = 0
for c in range(3, 501, 6):
    s += c
print('O somatório dos números ímpares múltiplos de 3 de 1 a 500 é {}'.format(s))'''