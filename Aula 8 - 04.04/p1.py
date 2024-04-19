altura=float(input('Insira sua altura: '))
idade=int(input('Insira sua idade: '))
if idade>17:
    if altura>160:
        bolsa=1120
    else:
        bolsa=1410
else:
    bolsa=1439
print('Você receberá uma bolsa de R$',str(bolsa))
