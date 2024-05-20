'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente'''
lista = []
while True:
    # armazenando nomes e notas
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    # adicionando os dados à lista
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN' or resp in '':
        resp = str(input('Não entendi. Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)

# mostrando o nome e a média
print(f'{'Nº':<4}', f'{'NOME':<10}', f'{'MÉDIA':>8}')
print('-' * 40)
for i, a in enumerate(lista):
    print(f'{i:<4}', f'{a[0]:<10}', f'{a[2]:>8.1f}')

# mostrando as notas
while True:
    print('-' * 40)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print('Notas de {} são {}'.format(lista[opc][0], lista[opc][1]))
print('<<< VOLTE SEMPRE!!! >>>')