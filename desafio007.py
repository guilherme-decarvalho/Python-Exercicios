#Desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A média é {:.1f}.'.format(m))

#Solução alternativa (caso não necessite da variável "m"
#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#print('A média é {:.1f}.'.format((n1 + n2)/2))
