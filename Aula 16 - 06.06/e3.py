# Crie um programa que leia o valor de N do usuário
# Declare um vetor de N posições de Strings: vetor = [""] * N
# Faça um FOR SEM append para o usuário informar N nomes no vetor: vetor[i]=nome
# Faça outro FOR para mostrar os nomes que tem mais de 5 letras

N=int(input('Informe a quant. de valores: '))
vetor=['']*N

for i in range(N):
    vetor[i]=input('Informe um nome: ')

for i in range(len(vetor)):
    if len(vetor[i])>5:
        print(f'Nome: {vetor[i]}')
