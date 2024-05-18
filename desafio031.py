'''Desenvolva um programa que pergunte a distância de uma viagem
em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens
de até 200km e R$0,45 para viagens mais longas.'''

d = float(input('Qual a distância da viagem em Km? '))
if d <= 200:
    v = 0.5 * d
    print('O preço da passagem é {}.'.format(v))
else:
    v = 0.45 * d
    print ('O preço da passagem é {}.'.format(v))

'''Soluções alternativas
d = float(input('Qual a distância da viagem em Km? '))
if d <= 200:
    v = 0.5 * d
else:
    v = 0.45 * d
print ('O preço da passagem é {}.'.format(v))

========================== OU ==========================

d = float(input('Qual a distância da viagem em Km? '))
v = 0.5 * d if d <= 200 else d * 0.45
print ('O preço da passagem é {}.'.format(v))'''