# Questão 10: Faça um Programa que peça a idade e a altura de N pessoas (peça o valor de N para o usuário), armazene cada informação no vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idade=[]
altura=[]
N=int(input('Insira a quantidade de pessoas: '))

for i in range(N):
    h=float(input('Informe a altura: '))
    altura.append(h)
    age=int(input('Informe a idade: '))
    idade.append(age)

print('Vetor idade = ',idade)
print('Vetor altura = ',altura)

alt_reverse=altura[::-1] #Fatiamento de listas (Slicing)
idade_reverse=idade[::-1] #Fatiamento de listas (Slicing)
print('Vetor idade inversa = ',idade_reverse)
print('Vetor altura inversa = ',alt_reverse)