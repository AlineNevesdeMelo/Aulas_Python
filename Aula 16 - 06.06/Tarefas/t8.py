# Questão 8: Faça um Programa que leia em um vetor a nota de N alunos (pergunte o valor de N ao usuário), depois, mostre o índice do vetor das notas maiores ou iguais que 6 e em seguida, mostre o índice do vetor das notas menores que 6.
vetor=[]
notas_maior=[]
notas_menor=[]

N=int(input('Insira a quant. de alunos: '))

for i in range(N):
    notas=float(input('Insira a nota: '))
    vetor.append(notas)

for notas in vetor:
    if notas>=6:
        notas_maior.append(notas)
    else:
        notas_menor.append(notas)

print('Maiores notas = ',notas_maior)
print('Menores notas = ',notas_menor)