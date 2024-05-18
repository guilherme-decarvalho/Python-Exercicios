'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

altura = float(input('Qual é a sua altura em metros? '))
massa = float(input('Qual é a sua massa em quilos? '))
IMC = massa / altura ** 2
pesoideal1 = 18.5 * (altura ** 2)
pesoideal2 = 25 * (altura ** 2)
print('Seu IMC é {:.2f}. Seu peso ideal está entre {:.3f} e {:.3f}. '.format(IMC, pesoideal1, pesoideal2), end = '')
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif IMC >= 18.5 and IMC < 25: # 18.5 <= IMC < 25
    print('Você está no peso ideal.')
elif IMC >= 25 and IMC <= 30:
    print('Você está com sobrepeso.')
elif IMC > 30 and IMC <= 40:
    print('Você está obeso.')
elif IMC > 40:
    print('Você está com obesidade mórbida.')



