'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

'''
Digite um valor: 7
Adicionado ao final da lista...
Digite um valor: 2
Adicionado na posição 0 da lista...
Digite um valor: 5
Adicionado na posição 1 da lista...
Digite um valor: 9
Adicionado ao final da lista...
Digite um valor: 3
Adicionado na posição 1 da lista...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Os valores digitados em ordem foram [2, 3, 5, 7, 9]
'''
num = []
# adicionando os valores
for c in range(0, 5):
    n = int(input('Digite um valor: '))
# adicionando os valores na última posição se for o primeiro valor digitado ou um número maior que o maior valor já existente
    if c == 0 or n > num[-1]: 
        num.append(n)
        print('Adicionado ao final da lista...')
# ordenando os valores
    else:
        pos = 0 # cria variável de posição
        while pos < len(num): # verifica os valores até o final da lista
            if n <= num[pos]: # verifica se o número adicionando é menor ou igual a cada posição da lista
                num.insert(pos, n) # adiciona o número na lista na posição que o número é menor ou igual
                print('Adicionado na posição {} da lista...'.format(pos))
                break # depois de adicionando, pausa o comando
            pos += 1
print('-=' * 40)
print('Os valores digitados em ordem foram {}.'.format(num))