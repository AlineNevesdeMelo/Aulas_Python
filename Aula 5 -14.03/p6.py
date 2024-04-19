#Cálculo da diagonal de um triangulo
# diagonal=√largura²+comprimento²

import math
largura=float(input('Insira o valor da largura do triângulo: '))
comprimento=float(input('Insira o comprimento do triângulo: '))
diagonal=math.sqrt((largura**2)+(comprimento**2))
print('O resultado da diagonal=√largura²+comprimento²= ',round(diagonal,1))