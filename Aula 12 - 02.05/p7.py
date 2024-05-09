N=int(input('Insira a quantidade de compras realizadas: '))
soma1=0
soma2=0
for i in range(N):
    valor_compra=float(input('Insira o valor da compra: '))
    forma_pagamento=input('Pagamento em CARTÃO ou DINHEIRO? ')
    if forma_pagamento=='DINHEIRO':
        soma1+=valor_compra
    else:
        soma2+=valor_compra
print('Soma do dinheiro: ',soma1)
print('Soma dos cartões: ',soma2)