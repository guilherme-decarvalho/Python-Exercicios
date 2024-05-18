'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJAS GUANABARA '))
preçonormal = float(input('Qual é o valor do produto? R$'))
formapagamento = int(input('''Digite a forma de pagamento
1 = À VISTA NO DINHEIRO OU CHEQUE
2 = À VISTA NO CARTÃO
3 = 2x NO CARTÃO
4 = 3x OU MAIS NO CARTÃO
Qual opção? '''))
if formapagamento == 1:
    preço = preçonormal * 90 / 100
    print('O valor a ser pago será de R${:.2f}.'.format(preço))
elif formapagamento == 2:
    preço = preçonormal * 95 / 100
    print('O valor a ser pago será de R${:.2f}.'.format(preço))
elif formapagamento == 3:
    preço = preçonormal
    print('O valor a ser pago será de R${:.2f}. O valor das parcelas será R${:.2f}.'.format(preço, preço / 2))
elif formapagamento == 4:
    preço = preçonormal * 120 / 100
    parcelas = int(input('Em quantas parcelas será pago? '))
    print('O valor a ser pago será de R${:.2f}. O valor das parcelas será R${:.2f}.'.format(preço, preço / parcelas))
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')

