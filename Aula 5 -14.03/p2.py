#Leia do usuário A e B e calcule:
#Resultado=math.sqrt(sin(A)+sin(B))

import math
A=int(input('Insira o valor de A: '))
B=int(input('Insira o valor de B: '))
Resultado=math.sqrt(math.sin(A) + math.sin(B))
print('O resultado do calculo é: ',round(Resultado,2))
