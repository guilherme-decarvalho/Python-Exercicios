'''Faça um programa que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre a
área do terreno.'''

def área(larg, comp):
    a = larg * comp
    print('As dimensões do terreno são {:.2f}m e {:.2f}m. A área desse terreno é de {:.2f}m².'.format(larg, comp, a))


print(' Controle de Terrenos')
print('-' * 20)
l = float(input(' LARGURA (m): '))
c = float(input(' COMPRIMENTO (m): '))
área(l, c)