#Exercício 10 de estudo para P1

a=float(input('Valor de A: '))
b=float(input('Valor de B: '))
c=float(input('Valor de C: '))
if a>=b:
    if a>c:
        print('maior: a')
    else:
        print('maior: c')
else:
    print('maior: b')
    