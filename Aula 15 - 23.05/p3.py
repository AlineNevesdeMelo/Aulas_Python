# 1)Faça um programa que pergunte o valor de N para o usuário.
# 2)Em seguida,  leia um vetor de N números inteiros
inteiros=[]
N=int(input('Insira a quantidade de valores da lista: '))

for i in range(N):
    inteiro=int(input('Insira o valor: '))
    inteiros.append(inteiro)

# 3)Depois, conte quantos números são iguais a zero, quantos números são maiores que zero e quantos números são menores que zero.
maiorquezero=0
igualazero=0
menorquezero=0

for i in inteiros:
    if i == 0:
        igualazero += 1
    elif i <= 0:
        menorquezero += 1
    elif i >= 0:
        maiorquezero += 1

print('Quantidade de números igual a zero: ',igualazero)
print('Quantidade de números menor que zero: ',menorquezero)
print('Quantidade de números maior que zero: ',maiorquezero)