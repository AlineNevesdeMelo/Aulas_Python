a=float(input('Valor de A: '))
b=float(input('Valor de B: '))
c=float(input('Valor de C: '))
if (a+b)>c or (a+c)>b or (c+b)>a:
    if a>0 and b>0 and c>0:
        if a==b and a==c:
            print('É possível formar um triângulo equilátero')
        else:
            if a==b and a!=c or a==c and a!=b or b==c and b!=a:
                print('É possível formar um triângulo isósceles')
            else:
                print('É possível formar um triângulo escaleno')
    else:
        print('Não é possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')