#Exercício 7 de estudo para P1

custo_fábrica=float(input('Insira o custo de fábrica do carro: '))
percentual_distribuidor=custo_fábrica*0.28
valor_imposto=custo_fábrica*0.45
custo_consumidor= custo_fábrica + percentual_distribuidor + valor_imposto
print('Custo ao consumidor: R$ ',str(custo_consumidor))