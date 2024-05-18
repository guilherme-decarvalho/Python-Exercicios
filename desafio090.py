'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela. (>= 7: aprovado, <7: reprovado)'''
aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input('Média de {}: '.format(aluno["Nome"])))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-=' * 30)
print(aluno)
print('-=' * 30)
for k, v in aluno.items():
    print('{} = {}'.format(k, v), end=' ')
    print()
