# Criar um programa que leia um número N do usuário.
# Declare um vetor de tamanho N de números inteiros.
# Utilize um FOR SEM UTILIZAR append para ler N números inteiros do usuário.
# Utilize outro for para encontrar o maior valor presente no vetor. (dica: considere que o primeiro elemento do vetor, na posição 0, seja o maior e depois compare com os demais).

N=int(input('Informe a quant. de valores: '))
vetor=[0]*N

for i in range(N):
    vetor[i]=int(input('Insira um valor: '))

maior = vetor[0]
for i in vetor:
    if i>maior:
        maior=i
print(f'O maior número é {maior}')