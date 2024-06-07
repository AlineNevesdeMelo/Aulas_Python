# Questão 3: Faça um Programa que leia 4 notas em um vetor e depois calcule e mostre a média.
vetor=[]
for i in range(4):
    notas=float(input('Insira a nota: '))
    vetor.append(notas)

if len(vetor)>0: #Para verificar se o vetor está vazio ou não
    soma=sum(vetor) #Calcular a soma das notas inseridas no vetor
    qt_notas=len(vetor) #Indicar a quantidade de notas inseridas no vetor
    media=soma/qt_notas
    print('A média das notas é:',media)
else:
    print('O vetor está vazio, não é possível realizar a média.')