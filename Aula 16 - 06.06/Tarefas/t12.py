# Questão 12: Faça um Programa que leia dois vetores com N elementos cada (pergunte o valor de N para o usuário). Gere um terceiro vetor de 2*N elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

N = int(input("Digite o número de elementos de cada vetor: "))
A = []
B = []

# Solicita ao usuário para inserir os elementos do vetor A
print("Digite os elementos do vetor A")
for i in range(N):
    numero = int(input('Elemento de A: '))
    A.append(numero)

# Solicita ao usuário para inserir os elementos do vetor B
print("Digite os elementos do vetor B")
for i in range(N):
    numero = int(input('Elemento de B: '))
    B.append(numero)

# Inicializa o vetor C
C = []

# Intercala os elementos dos vetores A e B no vetor C
for i in range(N):
    C.append(A[i])
    C.append(B[i])

# Mostra o vetor C
print("O vetor C intercalado é: ", C)
