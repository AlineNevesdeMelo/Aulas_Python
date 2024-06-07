# 1) Teste e explique o programa
alturas = [] #Cria um vetor (lista).

for i in range(5): # Vai perguntar e armazenar os valores de altura informados pelo usuária na quant. indicada.
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    alturas.append(altura) #Vai inserir os valores na lista criada.

contador = 0
for altura in alturas: #Vai verificar os elementos na lista
    if altura > 1.80: # Se o valor do elemento da lista for maior que 1.80
        contador += 1 # Vai adicionar 1 unidade à variável contador.

print(f"{contador} pessoas têm altura superior a 1.80 metro.") #Mostra ao usuário quantas pessoas tem mais de 1.8m de altura

# 2) Altere para contar também as pessoas com menos de 1,50
alturas = []

for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    alturas.append(altura)

contador1 = 0
contador2 = 0
for altura in alturas:
    if altura > 1.80:
        contador1 += 1
    if altura < 1.50:
        contador2 += 1

print(f"{contador1} pessoas têm altura superior a 1.80 metro.")
print(f"{contador2} pessoas têm altura inferior a 1.50 metro.")

