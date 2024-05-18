#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
#escolhido.
from random import choice
nome1 = input('Digite o nome do(a) primeiro(a) aluno(a): ')
nome2 = input('Digite o nome do(a) segundo(a) aluno(a): ')
nome3 = input('Digite o nome do(a) terceiro(a) aluno(a): ')
nome4 = input('Digite o nome do(a) quarto(a) aluno(a): ')
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O aluno escolhido(a) foi {}.'.format(escolhido))

