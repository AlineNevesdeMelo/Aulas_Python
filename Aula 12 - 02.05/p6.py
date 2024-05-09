N=int(input('Insira a quantidade de vendas: '))
soma=0
for i in range(N):
    venda=float(input('Insira o valor da venda: '))
    soma+=venda
if soma>500:
    imposto=soma*0.15
else:
    imposto=soma*0.11
print(imposto)