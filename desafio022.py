'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1- O nome com todas as letras maiúsculas
2- O nome com todas minúsculas
3- Quantas letras ao todo (sem considerar os espaços
4- Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome somente em letras maiúsculas fica {}.'.format(nome.upper()))
print('O seu nome somente em letras minúsculas fica {}.'.format(nome.lower()))
nome1 = nome.split()
nome2 = ''.join(nome1)
print('O seu nome completo tem {} letras.'.format(len(nome2)))
nome3 = nome1[0]
print('O seu primeiro nome tem {} letras.'.format(len(nome3)))

'''Solução alternativa:
nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome somente em letras maiúsculas fica {}.'.format(nome.upper()))
print('O seu nome somente em letras minúsculas fica {}.'.format(nome.lower()))
print('O seu nome completo tem {} letras.'.format(len(nome2)- nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))'''





