#Faça um algoritmo que leia o salário de um fucionário e mostre seu novo
#salário com 15% de aumento.
s = float(input('Digite seu salário atual: '))
sa = s + s * 15/100
print('Seu salário com 15% de aumento será de R${:.2f}.'.format(sa))

#Soluções alternativas:
#s * (1 + 15 / 100)
#s * (115 / 100)
#s * 115 / 100
#s * 23 / 20
