idade=int(input('Sua idade: '))
valor=float(input('Valor do plano de saúde: '))
if idade>=60:
    valor=valor*1.22
    print('Com acréscimo de 22% seu plano será de R$',valor)
else:
    valor=valor*1.06
    print('Com acréscimo de 6% seu plano será de R$',valor)