'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também
um função leiaFloat()com a mesma funcionalidade.
'''
# Função
def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))    
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return valor


def leiaFLoat(msg):
    while True:
        try:
            valor = float(input(msg)) 
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return valor


# Programa Principal
n = leiaInt('Digite um número inteiro: ')
m = leiaFLoat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {m}.')
