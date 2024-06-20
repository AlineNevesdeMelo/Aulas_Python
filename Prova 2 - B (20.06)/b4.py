#Encontrar a sequência.
#Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e encontre uma sequência crescente contígua de mais de 3 números dentro do vetor. O programa deve imprimir o tamanho dessa sequência e os elementos que a compõem.

n = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(n):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    vetor.append(elemento)

tamanho_max = 0
inicio_sequencia = 0
tamanho_atual = 1
inicio_atual = 0

for i in range(1, n):
    if vetor[i] > vetor[i - 1]:
        tamanho_atual += 1
    else:
        if tamanho_atual > tamanho_max:
            tamanho_max = tamanho_atual
            inicio_sequencia = inicio_atual
        tamanho_atual = 1
        inicio_atual = i

if tamanho_atual > tamanho_max:
    tamanho_max = tamanho_atual
    inicio_sequencia = inicio_atual

if tamanho_max > 3:
    sequencia = vetor[inicio_sequencia:inicio_sequencia + tamanho_max]
    print(f"Maior sequência crescente contígua com mais de 3 números: {sequencia}")
    print(f"Tamanho da sequência: {tamanho_max}")
else:
    print("Não foi encontrada nenhuma sequência crescente contígua com mais de 3 números.")
