#Exercício 20 de estudo para P1
codigo = int(input("Informe o código do produto: "))
quantidade = int(input("Informe a qunatidade: "))
if codigo == 1001:
    valor = 5.32
elif codigo == 1324:
    valor = 6.45
elif codigo == 6548:
    valor = 2.37
elif codigo == 0987:
    valor = 5.32
elif codigo == 7623:
    valor = 6.45
total = valor * quantidade
print("O total a pagar é de R$" + str(total))

