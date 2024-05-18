'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
pares e ímpares em ordem crescente.'''
num = []
pares = []
impares = []
for n in range(0, 7):
       num.append(int(input('Digite o {}º valor: '.format(n+1))))
for n, v in enumerate(num):
       if v % 2 == 0:
              pares.append(v)
       else:
              impares.append(v)
print('Os números digitados foram {}.'.format(num))
print('Os números pares são {}.'.format((sorted(pares))))
print('Os números ímpares são {}.'.format(sorted(impares)))

'''
num = [[], []]
valor = 0
for c in range(1, 8)
       valor = int(input('Digite o {}º valor: '.format(c)))
       if valor % 2 == 0:
              num[0].append(valor)
       else:
              num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print('Os valores pares digitados foram: {}'.format(num[0]))
print('Os valores ímpares digitados foram: {}'.format(num[1]))
'''