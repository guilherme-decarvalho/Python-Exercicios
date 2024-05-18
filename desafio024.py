'''Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "santo".'''

cidade = str(input('Em que cidade você nasceu? ')).strip()
cidade = cidade.upper()
cidade = cidade.split()
cidade = cidade[0]
print('A cidade começa com Santo? {}.'.format('SANTO' in cidade))

'''solução alternativa:
cidade = str(input('Em que cidade você nasceu? ')).strip()
print('A cidade começa com Santo? {}'.format(cidade[:5].upper() == 'SANTO'))'''





