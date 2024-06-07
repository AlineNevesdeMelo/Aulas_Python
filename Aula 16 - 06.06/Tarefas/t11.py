# Questão 11: Faça um Programa que leia um vetor A com N números inteiros (pergunte o valor de N ao usuário), calcule e mostre a somatória dos quadrados dos elementos do vetor.

N = int(input("Digite o número de elementos do vetor: "))
A = []

for i in range(N):
    numero = int(input("Digite o elemento do vetor: "))
    A.append(numero)

# Calcula a somatória dos quadrados dos elementos do vetor A
somatoria_quadrados = sum(x**2 for x in A)

print("A somatória dos quadrados dos elementos do vetor é: ",somatoria_quadrados)