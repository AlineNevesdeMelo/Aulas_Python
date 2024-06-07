# Criar um programa que leia o valor de N do usuário
# Declare um vetor de tamanho N de números decinais (float)
# Utilize um FOR SEM UTILIZAR append para ler N números do usuário
# Utilize outro for para calcular a somatória dos número que estão em posições PARES

N=int(input('Informe a quant. de valores: '))
vetor=[0.0]*N
soma=0

for i in range(N):
    vetor[i]=float(input('Insira um número: '))

for i in range(len(vetor)):
    if i%2==0:
        soma+=vetor[i]
print(f'A soma é: {soma}')