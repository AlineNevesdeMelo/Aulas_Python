#Faça um programa que que leia A,B,C e calcule:
#Resultado=math.sqrt(a**2+b**2+c**2)

import math
a=float(input('Insira o valor de a: '))
b=float(input('Insira o valor de b: '))
c=float(input('Insira o valor de c: '))
Resultado=math.sqrt(a**2+b**2+c**2)
print('O resultado do cálculo é: ',round(Resultado))