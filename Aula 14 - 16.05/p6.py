#TESTE E EXPLIQUE

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho    #<---- o que é isso?

for i in range(tamanho):
    elemento = input(f"Digite o elemento {i+1}: ")
    vetor[i] = elemento

print("Vetor:", vetor)
#Comentário 1: "vetor = [0] * tamanho"
# Está pegando o zero dentro do vetor e multiplicando pelo o tamanho que o usuário indica.
#Comentário 2: o "for" está alterando o valor zero por 1, fazendo com que o valor inserido pelo usuário
#seja mostrado e indique quantas casas o vetor terá.