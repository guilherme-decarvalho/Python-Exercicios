'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.'''
#Var
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = '' #Por não haver ainda um nome, recebe espaço vazio
totmulher20 = 0
for p in range(1, 5): #Pessoas de 1 a 4
    print('------ {}ª PESSOA ------'.format(p)) #Conta as pessoas ordinalmente
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade #Soma todas as idades lidas
    if p == 1 and sexo in 'Mm': #Se a primeira pessoa for um homem, maioridade será a idade desse homem e nomevelho será o nome desse homem
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: #Se tiver um homem com idade maior, maioridade será a idade desse homem e nomevelho será o nome desse homem
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20: #Se for do sexo feminino e menor de 20 anos, contador contará +1
        totmulher20 += 1
mediaidade = somaidade / 4 #Média das idades
print('A média de idade do grupo é de {} ano(s).'.format(mediaidade))
print('O homem mais velho tem {} ano(s) e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo, são {} mulher(es) com menos de 20 anos.'.format(totmulher20))




