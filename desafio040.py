'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Sua média é {:.1f}.'.format(m))
if m < 5:
    print('Você está \033[1;31mREPROVADO\033[m.')
elif m >= 5 and m < 7: # poderia ser "7 > m >= 5"
    print('Você está em \033[1;33mRECUPERAÇÃO\033[m. Estude!')
elif m >= 7: # poderia ser "else"
    print('Parabéns, você está \033[1;34mAPROVADO\033[m.')
