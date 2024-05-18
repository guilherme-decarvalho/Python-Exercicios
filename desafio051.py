'''Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros
termos dessa progressão.'''

print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA '))
i = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
d = i + (10 - 1) * r # fórmula da PA para o décimo termo
for c in range(i, d + 1, r):
    print('{}'.format(c), end=' ')



