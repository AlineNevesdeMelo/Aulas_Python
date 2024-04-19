qtitens=int(input('Quantidade de itens: '))
total=float(input('Valor total da compra: '))
if qtitens>10 and total>100:
    desconto=total*0.15
else:
    desconto=total*0.06
print('Seu desconto será de R$',str(desconto))