#Faça um algoritmo que leia o preço de um produto e mostre seu novo
#preço com 5% de desconto.
p = float(input("Digite o preço do produto: R$"))
pd = p - p * 5/100
print('O preço do produto com 5% de desconto é igual a R${:.2f}.'.format(pd))

#Soluções alternativas:
#p * (1 - 5/100)
#p * (95/100)
#p * 95 / 100
#p * 19 / 20