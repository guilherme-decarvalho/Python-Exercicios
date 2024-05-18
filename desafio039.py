'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do
prazo.'''
from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - nascimento
print('Quem nasceu em {} tem {} anos de idade em {}.'.format(nascimento, idade, date.today().year))
if idade < 18:
    print('Falta {} ano(s) para você se alistar.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(date.today().year + (18 - idade)))
elif idade == 18:
    print('Está na hora de se alistar.')
elif idade > 18: # Poderia ser usado "else:"
    print('Você deveria ter se alistado há {} ano(s).'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(date.today().year - (idade - 18)))







