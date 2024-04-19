#Faça um programa que leia A,B,C,D e calcule:
#x=A²-√B²
#y=C²+√D²
#r=√(x+y)²

import math
A=float(input('Insira o valor A: '))
B=float(input('Insira o valor B: '))
C=float(input('Insira o valor C: '))
D=float(input('Insira o valor D: '))
x=(A**2)-(math.sqrt(B**2))
y=((C**2)+math.sqrt(D**2))
r=math.sqrt((x+y)**2)
print('O resultado de x=A²-√B²= ',x)
print('O resultado de y=C²+√D²= ',y)
print('O resultado de r=√(x+y)²= ',r)