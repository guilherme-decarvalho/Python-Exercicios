'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.'''

'''
=======================================
         LOJA SUPER BARATÃO
=======================================
Nome do Produto: Mouse
Preço: R$ 50
Quer continuar? [S/N] s
Nome do Produto: Caneta
Preço: R$ 3
Quer continuar? [S/N] s
Nome do Produto: Notebook
Preço: R$ 2550
Quer continuar? [S/N] s
Nome do Produto: Impressora
Preço: R$ 900
Quer continuar? [S/N] s
Nome do Produto: Monitor
Preço: R$1250
Quer continuar? [S/N] n
--------- FIM DO PROGRAMA ---------
O total da compra foi de R$ 4653.00
Temos 2 produtos custando mais de R$1000
O produto mais barato foi Caneta que custa R$ 3.00.
'''

print('=' * 60)
print('{:^60}'.format('LOJA SUPER BARATÃO'))
print('=' * 60)
total = maisdemil = barato = cont = 0
produtomaisbarato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().lower()
    while produto == '':
        produto = str(input('Nome do Produto: ')).strip().lower()
    preço = float(input('Preço: R$'))
    while preço == '':
        preço = float(input('Preço: R$'))
    continua = ' '
    total += preço
    if preço > 1000:
        maisdemil += 1
    cont += 1
    if cont == 1 or preço < barato:
        produtomaisbarato = produto
        barato = preço
    while continua not in 'SN': # and continua == '':
        continua = str(input(('Quer continuar? [S/N] '))).strip().upper()[0]
    if continua == 'N':
        break
print('{:=^60}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi de R${:.2f}.'.format(total))
print('Temos {} produto(s) custando mais de R$1000.'.format(maisdemil))
print('O produto mais barato foi {} que custa R${:.2f}.'.format(produtomaisbarato, barato))


