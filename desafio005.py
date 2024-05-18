#Faça um programa que leia um número inteiro e mostre
#na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('Seu sucessor é {} e seu antecessor é {}.'.format(s, a))

#Solução alternativa (usar caso não precise das variáveis "a" e "s")
#n = int(input('Digite um número: '))
#print('Seu sucessor é {} e seu antecessor é {}.'.format((n+1), (n-1)))

#Ordem de precedência:
#Parênteses
#Potênciação
#multiplicação, divisão, divisão inteira e módulo
#soma e subtração

