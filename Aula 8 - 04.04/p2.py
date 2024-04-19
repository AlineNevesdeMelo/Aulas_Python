saldo=float(input('Insira o valor do saldo: '))
dias=int(input('Insira a quantidade de dias: '))
if saldo<0:
    if dias<30:
        saldo=saldo*1.04
    else:
        saldo=saldo+(0.8)**dias
else:
    if dias<30:
        saldo=saldo*1.08
    else:
        saldo=saldo+(0.7)**dias
print('Seu saldo será de R$',str(saldo))