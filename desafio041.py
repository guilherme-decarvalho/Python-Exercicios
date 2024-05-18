'''A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a
idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''
from datetime import date
nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - nascimento
print('O atleta tem {} anos de idade.'.format(idade))
cores = {'limpa': '\033[m',
        'mirim': '\033[1;33m',
        'infantil': '\033[1;34m',
        'júnior': '\033[1;35m',
        'sênior': '\033[1;36m',
        'master': '\033[1;32m'}
if idade <= 9:
    print('Atleta {}MIRIM{}.'.format(cores['mirim'], cores['limpa']))
elif idade > 9 and idade <= 14: # somente <= 14
    print('Atleta {}INFANTIL{}.'.format(cores['infantil'], cores['limpa']))
elif idade > 14 and idade <= 19: # somente <= 19
    print('Atleta {}JÚNIOR{}.'.format(cores['júnior'], cores['limpa']))
elif idade > 19 and idade <= 25: # somente <= 25
    print('Atleta {}SÊNIOR{}.'.format(cores['sênior'], cores['limpa']))
elif idade > 25: # poderia ser "else"
    print('Atleta {}MASTER{}.'.format(cores['master'], cores['limpa']))


