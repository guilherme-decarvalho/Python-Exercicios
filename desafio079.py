'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados em ordem crescente.'''

'''
Digite um valor: 5
Valor adicionado com sucesso...
Quer continuar? [S/N] s
Digite um valor: 9
Valor adicionado com sucesso...
Quer continuar? [S/N] s
Digite um valor: 3
Valor adicionado com sucesso...
Quer continuar? [S/N] s
Digite um valor: 9
Valor duplicado! Não vou adicionar...
Quer continuar? [S/N] s
Digite um valor: 3
Valor duplicado! Não vou adicionar...
Quer continuar? [S/N] s
Digite um valor: 7
Valor adicionado com sucesso...
Quer continuar? [S/N] n
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Você digitou os valores [3, 5, 7, 9]
'''
num = []
# adicionando valores à lista
while True:
    n = int(input('Digite um valor: '))
    if n not in num: # adiciona valores que não estão na lista
        num.append(n)
        print('Valor adicionado com sucesso...')
    else: # não adiciona valores já existentes
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN': # força a digitar 'SN'
        resp= str(input('Não entendi. Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N': # pausa o while
        break
print('-=' * 40)
num.sort() # ordena os valores
print('Você digitou os valores {}.'.format(num))