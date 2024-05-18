'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
vencer.'''

'''from random import randint
from time import sleep
computador = randint(0, 10)
jogador = 11
tentativas = 0
while jogador != computador:
    jogador = int(input('Em que número pensei? '))
    print('PROCESSANDO...')
    sleep(1.5)
    tentativas += 1
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer na {}ª tentativa!'.format(tentativas))

Solução alternativa:'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))



