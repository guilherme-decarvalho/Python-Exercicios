'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas no final do jogo.'''

'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
VAMOS JOGAR PAR OU ÍMPAR?
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Diga um valor: 8
Par ou Ímpar? [P/I] P
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Você jogou 8 e o computador 2. Total de 10 DEU PAR
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Você VENCEU!
Vamos jogar novamente...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Diga um valor: 3
Par ou Ímpar? [P/I] P
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Você jogou 3 e o computador 2. Total de 5 DEU ÍMPAR
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Você PERDEU!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=
GAME OVER! Você venceu 1 vez(es).
'''

from random import randint
#print('{:=^60}'.format(' VAMOS JOGAR PAR OU ÍMPAR? '))
print('=' * 60, '\n{:^60}'.format('VAMOS JOGAR PAR OU ÍMPAR?'))
vence = 0
while True:
    print('=' * 60)
    usuário = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0] # força colocar P ou I
    computador = randint(0, 10)  #jogada do computador
    soma = usuário + computador  #soma para saber se é par ou ímpar
    print('=' * 60)
    if soma % 2 == 0:
        print('Você jogou {} e o computador {}. Total de {} DEU PAR.'.format(usuário, computador, soma))
        soma = 'P'
    elif soma % 2 == 1: # ou else
        print('Você jogou {} e o computador {}. Total de {} DEU ÍMPAR.'.format(usuário, computador, soma))
        soma = 'I'
# comparando a escolha do usuário com a soma
    if soma == escolha: 
        print('=' * 60)
        print('Você VENCEU! \nVamos jogar novamente')
    if soma != escolha:
        print('Você PERDEU!')
        break
    vence += 1
print('=' * 60)
print('GAME OVER! Você venceu {} vez(es).'.format(vence))

'''Solução Alternativa:

from random import randint
#print('{:=^60}'.format(' VAMOS JOGAR PAR OU ÍMPAR? '))
print('=' * 60, '\n{:^60}'.format('VAMOS JOGAR PAR OU ÍMPAR?'))
vence = 0
while True:
    print('=' * 60)
    usuário = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)  #jogada do computador
    soma = usuário + computador  #soma para saber se é par ou ímpar
    print('=' * 60)
    print('Você jogou {} e o computador {}. Total de {}. '.format(usuário, computador), end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vence += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!)
            vence += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('=' * 60)
print('GAME OVER! Você venceu {} vez(es).'.format(vence))

'''