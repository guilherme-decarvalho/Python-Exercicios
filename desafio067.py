'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

c = p = 0
while True:
    print('-=' * 20)
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
        break
    print('-=' * 20)
    for c in range(1,11):
        p = n * c
        print('{} x {} = {}'.format(n, c, p))
    '''while c > 11:
        p = n * c
        c += 1
        if c == 11:
            break
    print('{} x {} = {}'.format(n, c, p))'''
print('Fim do programa. Volte sempre!')

