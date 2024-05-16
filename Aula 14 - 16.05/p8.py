#Explique o append, o sum e o len

notas = []

for i in range(5):
    nota = float(input(f"Digite a nota da disciplina {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média aritmética das notas é: {media:.2f}")

# Foi criado um vetor chamado "notas", cujo os espaços estavam vazios.
# O laço "for", vai perguntar e inserir 5 notas dentro do vetor.
# O "append" significa acrescentar, só que vai acrescentar na última casa disponível dentro vetor.
# O "sum" soma as notas inseridas pelo usuário.
# O "len" conta quantos valores foram inseridos.