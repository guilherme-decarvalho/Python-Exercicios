'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
multado.
A multa vai custar R$7,00 por cada km acima do limite.'''

v = float(input('Velocidade: '))
if v > 80:
    val = v - 80
    m = 7 * val
    print('VOCÊ FOI MULTADO! \nA multa é de R$7.00 por cada Km/h acima do limite. \nVocê passou a {}Km/h, isso é {}Km/h acima do limite. \nSua multa será de R${:.2f}.'.format(v, val, m))
