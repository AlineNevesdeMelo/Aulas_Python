#Exercício 8 de estudo para P1

a=float(input('Coeficiente a: '))
b=float(input('Coeficiente b: '))
c=float(input('Coeficiente c: '))
d=float(input('Coeficiente d: '))
e=float(input('Coeficiente e: '))
f=float(input('Coeficiente f: '))
x=((c*e-b*f)/(a*e-b*d))
y=((a*f-c*d)/(a*e-b*d))
print('Valor de x: ',str(round(x,2)))
print('Valor de y: ',str(round(y,2)))