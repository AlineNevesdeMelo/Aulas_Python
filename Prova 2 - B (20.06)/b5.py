# Mover zeros para o final
# Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e mova todos os elementos negativos para o final do vetor, preservando a ordem dos demais elementos não-negativos.

N=int(input('Informe o valor de N: '))
vetor=[0]*N
vetor_positivo=[]
vetor_negativo=[]

for i in range(N):
    vetor[i]=float(input('Insira um número: '))

for i in vetor:
    if i<0:
        vetor_negativo.append(i)
    else:
        vetor_positivo.append(i)
        
print(f'Vetor = {vetor_positivo+vetor_negativo}')