#Faça um programa que leia x1, x2, y1, y2 e calcule a distância euclidiana entre os pontos A(x1,x2) e B(y1,y2)
#distância=√(x2-x1)²+(y2-y1)²

import math
x1=float(input('Insira o valor x1: '))
x2=float(input('Insira o valor x2: '))
y1=float(input('Insira o valor y1: '))
y2=float(input('Insira o valor y2: '))
distância=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print('O resultado de distância=√(x2-x1)²+(y2-y1)²= ',round(distância,2))