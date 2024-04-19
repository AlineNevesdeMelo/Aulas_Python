total=float(input('Insira o total: '))
série=input('Insira a série da nota fiscal: ')
if série=='E1':
    if total>180:
        imposto=total*0.17
    else:
        imposto=total*0.14
else:
    if total>199:
        imposto=total*0.18
    else:
        imposto=total*0.16
print('O imposto da nota fiscal é de R$',str(imposto))