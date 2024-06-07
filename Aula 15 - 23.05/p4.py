#Crie um programa que leia dois vetores VETA e VETB de 4 números inteiros cada.
#Depois, calcule a soma dos elementos correspondentes na mesma posição no VETC.
#Por exemplo:
#VETA= [1,4,6,4]
#VETB = [6,3,1,0]
#resultado VETC = [7, 7, 7, 4] 
#dica: VETC[i] = VETA[i] + VETB[i]

vetorA=[]
vetorB=[]
vetorC=[]

print('Insira os valores do vetor A')
for i in range(4):
    valor=int(input('Insira o valor: '))
    vetorA.append(valor)

print('Insira os valores do vetor B')
for i in range(4):
    valor=int(input('Insira o valor: '))
    vetorB.append(valor)

for i in range(4):
    soma=vetorA[i]+vetorB[i]
    vetorC.append(soma)
print('O resultado é ', vetorC)