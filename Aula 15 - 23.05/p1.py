# 1) Utilize o programa abaixo que lê um vetor de 10 números inteiros e imprima apenas os números ímpares para separadamente mostrar também os PARES

# Criar um vetor para armazenar os números
vetor = []

# Ler os números do usuário
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    vetor.append(num)

# Imprimir os números ímpares
print("Números ímpares:")
for num in vetor:
    if num % 2 != 0:
        print(num)

# agora, imprimir os pares...
print("Números pares:")
for num in vetor:
    if num % 2 == 0:
        print(num)