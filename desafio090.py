'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela. (>= 7: aprovado, <7: reprovado)'''
aluno = {}
aluno['Nome'] = input('Nome: ') # lendo o nome do aluno
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: ')) # lendo a média do aluno
# verificando se o aluno está aprovado, reprovado ou de recuperação
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
# print('-=' * 30)
# print(aluno)
print('-=' * 30)
for chave, valor in aluno.items():
    print(f'{chave} = {valor}.', end=' ')
    print()
