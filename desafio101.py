'''
Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.

------------------------------------
Em que ano você nasceu? 2000
Com 18 anos: VOTO OBRIGATÓRIO. 

------------------------------------
Em que ano você nasceu? 2010
Com 8 anos: NÃO VOTA

------------------------------------
Em que ano você nasceu? 1970
Com 48 anos: VOTO OBRIGATÓRIO

------------------------------------
Em que ano você nasceu? 1910
Com 108 anos: VOTO OPCIONAL
'''
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 70 > idade >=18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade >= 70 or 18 > idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))


'''def voto():
    from datetime import date
    atual = date.today().year
    ano = int(input('Em que ano você nasceu? '))
    idade = atual - ano
    if 70 > idade >=18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 70 or 18 > idade >= 16:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: NÃO VOTA')


# Programa Principal
voto()'''