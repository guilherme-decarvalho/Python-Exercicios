'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.'''

'''
Na palavra APRENDER temos a e e
Na palavra PROGRAMAR temos o a a
...
'''

palavra = ('nota', 'música', 'chinelo', 'fone',
           'guitarra', 'amplificador', 'programar',
           'aprender', 'pedal', 'cabo', 'ponte')
for p in palavra:
    print('\nNa palavra {} temos '.format(p.upper()), end='')
    for letra in p:
        if letra.lower() in 'aáâãàeéêiíoóôõuú':
            print(letra, end=' ')