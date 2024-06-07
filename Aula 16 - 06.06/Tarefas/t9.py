# Questão 9: Faça um Programa que leia um vetor de N números inteiros (peça para o usuário informar o valor de N), mostre a soma e a multiplicação dos números do vetor.
vetor=[]
N=int(input('Insira a quant. de valores no vetor: '))

for i in range(N):
    num=int(input('Insira o valor: '))
    vetor.append(num)

soma=sum(vetor)
print('Soma = ',soma)

resultado=1
# Itera sobre cada número no vetor e multiplica pelo resultado acumulado
for num in vetor:
    resultado *= num
print('Produto = ',resultado)