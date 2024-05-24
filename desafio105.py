'''
Faça um programa que tenha uma função chamada notas() que pode receber
várias notas de aluno e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também docstring da função

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
{'total': 4, 'maior': 10, 'menor': 5.5, 'média' 7.875, 'situação': 'BOA'}

resp = notas(3.5, 10, 6.5, sit=True)
print(resp)
{'total': 3, 'maior': 10, 'menor': 3.5, 'média' 6.666, 'situação': 'RAZOÁVEL'}

resp = notas(2.5, 2, 6.5, sit=True)
print(resp)
{'total': 3, 'maior': 6.5, 'menor': 2, 'média' 4.0, 'situação': 'RUIM'}

help(notas)
notas(*n, sit=False)
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adiciona a situação
    :return: dicionário com várias informações sobre a situação da turma.
'''
# Função
def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adiciona a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'REGULAR'
        else:
            r['situação'] = 'RUIM'

    return r

# Programa Principal
resp = notas(5.5, 6.5, sit=True)
print(resp)
help(notas)