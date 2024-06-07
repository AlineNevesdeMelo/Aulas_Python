# Criar um programa que leia um número N do usuário.
# Declare um vetor de tamanho N de caracteres.
# Utilize um FOR SEM UTILIZAR append para ler N nomes do usuário.
# Peça para o usuário informar uma letra L.
# Utilize outro for para contar quantos nomes começam com a letra L que o usuário informou.

N=int(input('Informe a quant.: '))
vetor=[""]*N
contador=0

for i in range(N):
    vetor[i]=input('Informe um nome: ')

L=input('Informe a inicial de um nome: ').lower()

for i in vetor:
    if i.lower().startswith(L):
        contador+=1
print(f'{contador} nomes começam com a letra informada.')
