#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2m²
h = float(input('Qual a altura da parede? '))
b = float(input('Qual a largura da parede? '))
a = h * b
l = a/15.5
print('Sua parede tem {0}m X {1}m. A área da parede é igual a {2:.2f}m² e será necessário {3:.3f} litros de tinta.'.format(h, b, a, l))


