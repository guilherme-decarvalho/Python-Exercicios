'''Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o
maior.'''
# bibliotecas
from time import sleep


# função
def maior(* num):
    cont = maior = 0
    # valores informados
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.5)
        # analisando o maior
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    

# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()