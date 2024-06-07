# Questão 4: Faça um Programa que leia um vetor de 10 caracteres, e diga quantas vogais foram lidas. Imprima as vogais.

# Lista para armazenar os caracteres
caracteres = []

# Conjunto de vogais para verificação
vogais_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# Lista para armazenar as vogais lidas
vogais_lidas = []

# Lendo 10 caracteres do usuário
print("Digite 10 caracteres:")
for i in range(10):
    caractere = input("Caractere: ")
    caracteres.append(caractere)
    # Verificando se o caractere é uma vogal
    if caractere in vogais_set:
        vogais_lidas.append(caractere)

# Contando o número de vogais
num_vogais = len(vogais_lidas)

# Mostrando o número de vogais e as vogais lidas
print(f"Número de vogais lidas: {num_vogais}")
print("Vogais lidas:", vogais_lidas)
