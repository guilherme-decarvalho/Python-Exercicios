'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja
errado, peça a digitação novamente até ter um valor correto'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('OPÇÃO INVÁLIDA!')
print('Obrigado pela resposta!')

'''Solução alternativa:


sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] #fatiamento pra pegar só a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip.upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))'''



