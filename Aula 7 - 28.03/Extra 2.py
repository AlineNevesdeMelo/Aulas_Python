import math
a=float(input('Valor de a: '))
b=float(input('Valor de b: '))
c=float(input('Valor de c: '))
delta=(b**2)-4*a*c
if delta>=0:
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    print('x1=',x1,' e x2=',x2)
else:
    print('Não existe solução no ℝ')
