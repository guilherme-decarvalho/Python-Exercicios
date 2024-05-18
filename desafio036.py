'''Escreva um programa para aprovar um empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, ela não pode exceder 30% do salário
ou então o empréstimo será negado'''

print('='* 20 + ' \033[4mEMPRÉSTIMO BANCÁRIO\033[m ' + '='* 20)
v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o seu salário? R$'))
a = int(input('Em quantos anos você vai pagar? '))
m = 12 * a #conversão de ano para mês
p = v / m #valor da prestação
# o valor da prestação não pode exceder 30% do salário
if p <= s * 30 / 100:
    print('O valor da prestação será de R${:.2f}.'.format(p))
elif p > s * 30 / 100:
    print('O valor da prestação será de R${:.2f}. Desculpe, não será permitido o empréstimo.'.format(p))


# end = '' para continuar dois print na mesma linha
