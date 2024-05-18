'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência. No final, mostre uma listagem de preços organizando os dados em forma
tabular.'''

'''
listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90)
'''

'''
==========================================
            LISTAGEM DE PREÇOS
------------------------------------------
Lápis............................R$   1.75
Borracha.........................R$   2.00
Caderno..........................R$  15.90
Estojo...........................R$  25.00
Transferidor.....................R$   4.20
Compasso.........................R$   9.99
Mochila..........................R$ 120.32
Canetas..........................R$  22.30
Livro............................R$  34.90
------------------------------------------
'''
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('=' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end='')
    else:
        print('R${:>8.2f}'.format(listagem[pos]))
print('-' * 40)