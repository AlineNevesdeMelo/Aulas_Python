#Exercício 16 de estudo para P1

código=int(input('Digite o código do pedido: '))
quant=int(input('Informe a quantidade do lanche: '))
if código==100 or código==103:
    preço=1.2
elif código==101 or código==104:
    preço=1.3
elif código==102:
    vpreço=1.5
elif código==105:
    preço=1
valor_total=preço*quant
print('Valor total = ',str(round(valor_total,2)))