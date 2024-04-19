#Exercício 13 de estudo para P1

num1=int(input('Valor 1: '))
num2=int(input('Valor 2: '))
num3=int(input('Valor 3: '))
if num1>=num2:
    if num1>num3:
        print('Maior: ',str(num1))
    else:
        print('Maior: ',str(num3))
else:
    if num2>num3:
        print('Maior: ',str(num2))
    else:
        print('Maior: ',str(num3))
