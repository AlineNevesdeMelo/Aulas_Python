#Contar ocorrências de um elemento sem utilizar funções prontas do Python
#Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e um valor para a variável X.
#O programa deve contar quantas vezes o valor da variável X aparece no vetor e imprimir essa contagem.

N=int(input('Insira o valor de N: '))
vetor=[0]*N
x=2
contador=0

for i in range(N):
    vetor[i]=int(input('Informe um número: '))
    if vetor[i]==x:
        contador+=1
print(f'A variável x aparece {contador} vezes.')
