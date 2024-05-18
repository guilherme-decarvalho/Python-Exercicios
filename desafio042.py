'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''
r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Com essas retas, É POSSÍVEL formar um triângulo.', end = '')
    if r1 == r2 and r2 == r3: # r1 == r2 == r3
        print('Esse triângulo será equilátero.')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('Esse triângulo será isósceles.')
    elif r1 != r2 and r2 != r3 and r1 != r3: # "else:" "r1 != r2 != r3 != r1"
        print('Esse triângulo será escaleno.')
else:
    print('Com essas retas, NÃO É POSSÍVEL formar um triângulo.')
