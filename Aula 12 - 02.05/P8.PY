X=int(input('Insira a quantidade de provas: '))
soma1=0
soma2=0
for i in range(X):
    nota_prova=int(input('Insira a nota da prova: '))
    soma1+=nota_prova
média_prova=soma1/X

Y=int(input('Insira a quantidade de trabalhos: '))
for i in range(Y):
    nota_trabalho=int(input('Insira a nota do trabalho: '))
    soma2+=nota_trabalho
média_trabalho=soma2/Y
média_bimestral=(0.3*média_trabalho) + (0.7*média_prova)
print('Média bimestral: ',média_bimestral)