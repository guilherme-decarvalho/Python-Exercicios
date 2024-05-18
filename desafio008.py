#Escreva um programa que leia um valor em metros e o exiba convertido
#em centímetros e milímetros.
m = float(input('Diga a medida em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('Sua medida pode ser convertida em {}cm e em {}mm. \nSendo convertido em decímetro, temos {}dm. Em decâmetro, temos {}dam. \nEm hectômetro, temos {}hm e em quilômetro, temos {}km.'.format(cm, mm, dm, dam, hm, km))

#Solução alternativa (caso não utilize as variáveis "cm" e "mm")
#m = float(input('Diga a medida em metros: '))
#print('Sua medida em centímetros é {}cm e sua medida em milímetros é {}mm.'.format((m * 100), (m * 1000), )(m * 10), (m / 10), (m / 100), (m / 1000)))
