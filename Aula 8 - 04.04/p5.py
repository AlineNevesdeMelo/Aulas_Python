aluguel=float(input('Insira o valor do aluguel: '))
área=float(input('Insira a área do imóvel: '))
total=float(input('Insira o valor total do imóvel: '))
if área>50:
    if total>350000:
        if aluguel>1800:
            preço=aluguel*12+total
        else:
            preço=aluguel*6+total
    else:
        preço=aluguel+total
else:
    preço=total*1.12
print('O preço de venda é de R$',str(preço))
