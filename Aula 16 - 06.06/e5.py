# Criar um programa que leia o valor de N do usuário, leia N nomes (sem append).
# Em seguida, mostre os nomes que estão em posições pares (mostre também a posição).
# Depois, mostre os outros nomes que estão em posições impares (a posicão também).

N=int(input('Informe a quant. de valores: '))
vetor=[""]*N

for i in range(N):
    vetor[i]=input('Insira um nome: ')

print('Nomes na posição par da lista/vetor')
for i in range(len(vetor)):
    if i%2==0:
        print(f'Nome: {vetor[i]} \n Posição: {i}')

print('Nomes na posição impar')
for i in range(len(vetor)):
    if i%2!=0:
        print(f'Nome: {vetor[i]} \n Posição: {i}')