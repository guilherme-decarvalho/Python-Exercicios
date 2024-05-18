'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.'''

'''
Digite um número entre 0 e 20: 90
Tente novamente. Digite um número entre 0 e 20: -15
Tente novamente. Digite um número entre 0 e 20: 16
Você digitou o número dezesseis.
'''

'''
Digite um número entre 0 e 20: 0
Você digitou o número zero.
'''

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze',
        'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print('Você digitou o número {}.'.format(cont[num]))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')

