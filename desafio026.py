'''Faça um programa que leia uma frase pelo teclado e mostre

1- Quantas vezes aparece a letra "A".
2- Em que posição ela aparece a primeira vez.
3- Em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantas vezes aparece a letra "A"? {}'.format(frase.count('A')))
print('Em que posição ela aparece a primeira vez? {}'.format(frase.find('A')+1))
print('Em que posição ela aparece a última vez? {}'.format(frase.rfind('A')+1))





