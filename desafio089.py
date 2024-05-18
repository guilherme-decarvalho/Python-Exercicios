'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente'''
lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print('{}'.format('Nº'), '{:>5}'.format('NOME'), '{:>10}'.format('MÉDIA'))
print('-' * 30)
for i, a in enumerate(lista):
    print('{}'.format(i), '{:>5}'.format(a[0]), '{:>10}'.format(a[2]))
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print('Notas de {} são {}'.format(lista[opc][0], lista[opc][1]))
print('<<< VOLTE SEMPRE!!! >>>')