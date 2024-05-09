N=int(input('Quantas idades você irá calcular?: '))
soma=0
for i in range(N):
    idade=int(input('Insira a idade: '))
    soma += idade
print(soma)