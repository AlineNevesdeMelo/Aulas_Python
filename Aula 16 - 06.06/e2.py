# Crie um programa que leia N do usuário.
# Utilize um FOR para ler N nomes SEM utilizar o comando append
# Faça outro FOR para mostrar os nomes e as respectivas posições se a posição for ÍMPAR

N=int(input('Informe a quant. de valores: '))
vetor=[0]*N

for i in range(N):
    nomes=input('Informe um nome: ')
    vetor[i]=nomes

for i in range(len(vetor)):
    if i%2!=0:
        print(f'Posição {i}, {vetor[i]}')