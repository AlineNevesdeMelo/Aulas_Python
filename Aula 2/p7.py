#Faça um programa que leia uma distância em metros e mostre:
#-Em centimetros;
#-Em milimetros.

Distância=float(input('Insira a distância em metros: '))
centímetros=Distância*100
milímetros=Distância*1000
print('Em cm: '+str(centímetros))
print('Em mm: '+str(milímetros))
