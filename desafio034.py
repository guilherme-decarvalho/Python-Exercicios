'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%.'''
s = float(input('Qual é o valor do salário? R$'))
if s > 1250:
    a = s * 10/100
    sn = s + a
else:
    a = s * 15/100
    sn = s + a
print('O salário atual é R${:.2f} e terá um aumento de R${:.2f}. O novo salário será de R${:.2f}.'.format(s, a, sn))

