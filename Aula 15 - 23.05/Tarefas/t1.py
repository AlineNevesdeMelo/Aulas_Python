#1) teste e explique esse programa
idades = []

for i in range(5): # For vai repetir a pergunta a quantidade de vezes solicitado
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade) # .append significa adicionar elementos numa lista

idade_mais_alta = max(idades) # max: retorna o número mais alto ou a data mais recente numa sequencia ou lista de elementos
idade_mais_baixa = min(idades) # min: o menor valor em uma sequência de elementos

print(f"A idade mais alta é: {idade_mais_alta}")
print(f"A idade mais baixa é: {idade_mais_baixa}")

#2) Altere o programa anterior para trabalhar com o vetor de nomes de alunos junto com o vetor de notas de alunos

idades = []
notas = []

for i in range(5): 
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)
    nota = float(input('Insira a nota do aluno: '))
    notas.append(nota)

idade_mais_alta = max(idades) 
idade_mais_baixa = min(idades)
nota_mais_alta = max(notas)
nota_mais_baixa = min(notas)

print(f"A idade mais alta é: {idade_mais_alta}")
print(f"A idade mais baixa é: {idade_mais_baixa}")
print('A nota mais alta é: ',nota_mais_alta)
print('A nota mais baixa é: ',nota_mais_baixa)