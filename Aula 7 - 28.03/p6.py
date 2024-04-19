compra=float(input('Insira o valor da compra: '))
estado=input('Insira o estado em que mora: ')
if compra>1500:
    if estado=='sp' or estado=='São Paulo':
        imposto=compra*1.12
        print('Imposto de 12% e sua compra terá o valor final de R$',imposto)
    else:
        imposto=compra*1.08
        print('Imposto de 8% e sua compra terá o valor final de R$',imposto)
else:
    imposto=compra*1.16
    print('Imposto de 16% e sua compra terá o valor final de R$',imposto)