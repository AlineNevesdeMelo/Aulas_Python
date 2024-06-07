# Criar um programa que leia um número N do usuário.
# Declare um vetor de tamanho N de números inteiros.
# Utilize um FOR SEM UTILIZAR append para ler N números do usuário.
# Utilize outro for para calcular o produtório (multiplicação) dos números presentes nas posições ímpares do vetor.
# dica: inicializar a variável produtorio=1

N=int(input('Informe a quant.: '))
vetor=[0]*N
produto=1

for i in range(N):
    vetor[i]=int(input('Informe um número: '))

for i in range(len(vetor)):
    if i%2!=0:
        produto*=vetor[i]
print(f'Produtório = {produto}')