#Remover nomes duplicados
#Escreva um programa que leia um vetor de nomes de tamanho N (informado pelo usuário) e remova todos os nomes duplicados do vetor. 
#O programa deve imprimir o vetor resultante. 
#Por exemplo, se o vetor original for ['Edgar', 'Emilio', 'Cleiton', 'Edgar' ], o programa deve imprimir ['Edgar', 'Emilio', 'Cleiton'].
N=int(input('Insira o valor de N: '))
vetor=[0]*N
for i in range(N):
    vetor[i]=(input('Informe um número: '))

print(list(set(vetor)))