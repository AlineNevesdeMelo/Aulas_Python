# Questão 7: Faça um Programa que leia em um vetor a nota de N alunos (pergunte o valor de N ao usuário), calcule a média.
vetor=[]
N=int(input('Insira a quant. de alunos: '))

for i in range(N):
    notas=float(input('Insira a nota: '))
    vetor.append(notas)

if len(vetor)>0: #Para verificar se o vetor está vazio ou não
    soma=sum(vetor) #Calcular a soma das notas inseridas no vetor
    qt_notas=len(vetor) #Indicar a quantidade de notas inseridas no vetor
    media=soma/qt_notas
    print('A média das notas é:',media)
else:
    print('O vetor está vazio, não é possível realizar a média.')