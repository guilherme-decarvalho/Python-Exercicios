'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço "for".'''

print('{:=^40}'.format(' TABUADA '))
n = int(input('Qual tabuada você quer? '))
for c in range(1, 11): # c é a variável de contador do intervalo
    p = n * c # resultado da tabuada do número escolhido
    #print('{} x '.format(n), c, ' = {}'.format(p))
    print('{} x {:2} = {}'.format(n, c, p))


