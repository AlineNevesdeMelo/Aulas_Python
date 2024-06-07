#Crie um vetor com 5 elementos inteiros e conte quantos elementos são pares.
vetor = [3, 8, 11, 20, 7]
contador_pares = 0
for elemento in vetor:
    if elemento % 2 == 0:
        contador_pares += 1
print("Quantidade de elementos pares:", contador_pares)
