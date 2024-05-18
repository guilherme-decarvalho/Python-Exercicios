#Crie um algoritmo que leia um número e mostre o seu dobro,
#triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {}. \nSeu triplo é {}. \nA sua raiz quadrada é {:.2f}.'.format(n, d, t, r))

#Solução alternativa (caso não precise das variáveis "d", "t" e "r")
#n = int(input('Digite um número: '))
#print('O dobro de {} é {}. \nSeu triplo é {}. \nA sua raiz quadrada é {:.2f}.'.format(n, (n * 2), (n * 3), (n ** (1/2))))

#raiz quadrada também pode ser --> pow(n,(1/2)

