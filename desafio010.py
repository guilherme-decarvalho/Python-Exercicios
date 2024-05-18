#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27
r = float(input('Quantos reais você tem na carteira? R$'))
d = r / 5.23
e = r / 6.1
i = r / 0.05
print('Você pode comprar US${:.2f}, ou €{:.2f}, ou ¥{:.2f}.'.format(d, e, i))


