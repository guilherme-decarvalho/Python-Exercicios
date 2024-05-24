'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor numério

Ex.:
n = leiaInt('Digite um n')
print(f'Você acabou de digitar o número {n}')

------------------------------------------
Digite um número: w
ERRO: Digite um número inteiro válido
Digite um número:         .
ERRO: Digite um número inteiro válido
Digite um número: 
ERRO: Digite um número inteiro válido
Digite um número: 8
Você acabou de digitar o número 8.
'''
# Função
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO: Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor
    

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')