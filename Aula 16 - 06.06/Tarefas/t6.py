# Questão 6: Faça um Programa que leia N números inteiros (pergunte para o usuário o valor de N) e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor impar. Imprima os três vetores.
vetor=[]
vetor_par=[]
vetor_impar=[]
N=int(input('Insira a quant. de valores no vetor: '))

for i in range(N):
    num=int(input('Insira os valores: '))
    vetor.append(num)

for num in vetor:
    if num%2 != 0:
        vetor_impar.append(num)
    else:
        vetor_par.append(num)

print('Vetor impar = ',vetor_impar)
print('Vetor par = ',vetor_par)