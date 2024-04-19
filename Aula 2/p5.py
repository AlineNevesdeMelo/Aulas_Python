#Faça um programa que leia:
#-Peso;
#-Altura
#Calcule o IMC=peso/altura**2
#Mostre o IMC

peso=float(input('Insera seu peso em quilogramas: '))
altura=float(input('Insira sua altura em metros: '))
IMC=peso/(altura**2)
print('Resultado do IMC: '+str(round(IMC,2)))
