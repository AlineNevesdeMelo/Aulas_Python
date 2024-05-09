N=int(input('Insira a quantidade de notas: '))
soma=0
for i in range(N):
    nota=int(input('Insira a nota: '))
    soma+=nota
média=soma/N
print('Média: ',média)
if média>7:
    print('Aprovado')
else:
    print('Reprovado')