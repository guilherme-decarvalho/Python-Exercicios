'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
na ordem correta.'''

'''
Digite a expressão: ((a+b)*c)
Sua expressão está válida
'''

'''
Digite a expressão: ((a+b)*c))
Sua expressão está errada
'''

'''
Digite a expressão: ((a+b)*c
Sua expressão está errada
'''
# armazenando a expressão
expr = str(input('Digite a expressão: '))
pilha = [] # lista para armazenanar os símbolos da expressão
for símb in expr: # cria variável para colher fatiamento na expressão
    if símb == '(': # se ( está na expressão, adiciona à lista pilha
        pilha.append('(')
    elif símb == ')': # se ) está na expressão
        if len(pilha) > 0: # retira ( se tiver
            pilha.pop()
        else:
            pilha.append(')') # adiciona ) se não tiver (
            break # valida a retirada só se tiver (
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
print(len(pilha))