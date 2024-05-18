'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues.

OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

'''
============================================
                BANCO CEV
============================================
Que valor você quer sacar? R$ 1234
Total de 24 cédula(s) de R$50
Total de 1 cédula(s) de R$20
Total de 1 cédula(s) de R$10
Total de 4 cédula(s) de R$1
============================================
Volte sempre ao BANCO CEV! Tenha um bom dia!
'''
'''
print('=' * 60)
print('{:^60}'.format(' BANCO CEV '))
print('=' * 60)
valor = int(input('Que valor você quer sacar? R$'))
cédula50 = cédula20 = cédula10 = cédula1 = 0
while True:
    cédula50 = valor // 50
    valor = valor % 50
    cédula20 = valor // 20
    valor = valor % 20
    cédula10 = valor // 10
    valor = valor % 10
    cédula1 = valor // 1
    valor = valor % 1
    if valor == 0:
        break
print('Total de {} cédula(s) de R$50.'.format(cédula50))
print('Total de {} cédula(s) de R$20.'.format(cédula20))
print('Total de {} cédula(s) de R$10.'.format(cédula10))
print('Total de {} cédula(s) de R$1.'.format(cédula1))
print('=' * 60)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''

'''Solução Alternativa:'''

print('=' * 60)
print('{:^60}'.format(' BANCO CEV '))
print('=' * 60)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print('Total de {} cédulas de R${}'.format(totcéd, céd))
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 60)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
