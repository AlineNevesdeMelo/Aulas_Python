# 1) Teste e explique o programa
cidades = [] #Criar a lista de cidades

for i in range(5): # Vai perguntar o nome das cidade na quant. solicitada e incluir na lista já criada.
    cidade = input(f"Digite o nome da cidade {i+1}: ")
    cidades.append(cidade) 

cidades.sort() #a função sort() modifica a lista em que é chamada, reorganizando os elementos com base em critérios específicos. 

print("Cidades em ordem alfabética:") #Vai mostrar uma lista com os nomes das cidades em ordem alfabética.
for cidade in cidades:
    print(cidade)


# 2) Altere o programa para trabalhar com 2 vetores. Além do vetor de cidade, adicione o vetor de populacao.
cidades = []
populacoes = []

for i in range(5): 
    cidade = input(f"Digite o nome da cidade {i+1}: ")
    cidades.append(cidade)
    populacao = float(input(f'Insira a população da cidade {i+1}: '))
    populacoes.append(populacao)

cidades.sort()
populacoes.sort()

print("Cidades em ordem alfabética:") 
for cidade in cidades :
    print(cidade)

print('Populações em ordem numérica:')
for populacao in populacoes:
    print(populacao)