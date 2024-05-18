'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disse que quer mostrar 0 termos.'''
'''
print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA '))
i = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
cont = 1
j = 0
while cont <= 10:
    print('{}'.format(i), end=' - ')
    i += r
    cont += 1
    if cont > 10:
        j = int(input('\nDeseja mostrar mais quantos termos? '))
        j = 10 + j
        while j != 10 and cont <= j:
            i += r
            cont += 1
            print('{}'.format(i), end=' - ')
        else:
            print('Fim')

'''
print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA '))
i = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10 # para forçar começar com os 10 primeiros termos
while mais != 0:
    total += mais # para iniciar com os 10 primeiros termos
    while cont <= total:
        print('{}'.format(i), end=' ')
        i += r
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão com total de {} termos.'.format(total))