#Crie um programa que leia as variáveis A, B, C e calcule:
#resultado=math.sqrt(A)+math.sqrt(B)+math.sqrt(C)

import math
A=float(input('Digite o valor A: '))
B=float(input('Digite o valor B: '))
C=float(input('Digite o valor C: '))
resultado=math.sqrt(A)+math.sqrt(B)+math.sqrt(C)
print('O resultado de √A + √B + √C = ',round(resultado,2))