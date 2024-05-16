#Altere o programa a seguir para mostrar a média das notas dos alunos..

tamanho = int(input("Digite a quantidade de alunos: "))
notas = [0] * tamanho
soma=0

for i in range(tamanho):
    elemento = input(f"Digite a nota do aluno {i+1}: ")
    notas[i] = elemento
    soma += float(elemento)
    media=soma/tamanho

print("Vetor:", notas)
print("Média: ",media)