# Criar um programa que leia um número N do usuário.
# Declare um vetor de tamanho N de números inteiros.
# Utilize um FOR SEM UTILIZAR append para ler N números do usuário.
# Utilize outro for para contar quantos números pares estão presentes em posições impares do vetor.

N=int(input('Informe a quant.: '))
vetor=[0]*N
contador=0

for i in range(N):
    vetor[i]=int(input('Informe um número: '))

for i in range(N):
    if i%2!=0:
        if vetor[i]%2==0:
            contador += 1
print(f'{contador} elementos são nº pares em posições impares.')