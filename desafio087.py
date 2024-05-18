'''Aprimore o desafio anterior, mostrando no final:

a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = coluna3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor para [{}, {}]: '.format(l, c)))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print('[{:^5}]'.format(matriz[l][c]), end= '')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()
print('-=' * 30)
print('A soma de todos os valores pares digitados é {}.'.format(somapares))
for l in range(0, 3):
    coluna3 += matriz[l][2]
print('A soma dos valores da terceira coluna é {}.'.format(coluna3))
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print('O maior valor da segunda linha é {}.'.format(maior))


