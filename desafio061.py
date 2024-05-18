'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.'''

'''print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA '))
i = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = -1
while c < 9:
    c += 1
    if c == 0:
        print('{}'.format(i), end=' ')
    else:
        i = i + r
        print('{}'.format(i), end=' ')'''

'''Solução alternativa:'''

print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA '))
i = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
#termo = i
cont = 1
while cont <=10:
#    print('{}'.format(termo), end=' ')
    print('{}'.format(i), end=' ')
#    termo += r
    i += r
    cont += 1


