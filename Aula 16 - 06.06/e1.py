# Crie um programa que leia N do usuário.
# Depois, faça um FOR para ler N números inteiros do usuário
# Em seguida, faça um outro FOR para mostrar os números e as respectivas posições, somente daqueles que estão em posições pares.

N=int(input('Informe a quant. de vezes: '))
vetor = []

for i in range(N):
    num=int(input('Informe um número: '))
    vetor.append(num)

for i in range(len(vetor)):
    if i%2==0:
        print(f'Posição {i}, número {vetor[i]}')
        
