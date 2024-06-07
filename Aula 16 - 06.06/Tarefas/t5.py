#Questão 5: Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
# Lista para armazenar os caracteres
caracteres = []

# Conjunto de vogais para verificação
vogais_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# Lista para armazenar as vogais lidas
consoantes_lidas = []
vogais_lidas=[]

# Lendo 10 caracteres do usuário
print("Digite 10 caracteres:")
for i in range(10):
    caractere = input("Caractere: ")
    caracteres.append(caractere)
    
    if caractere in vogais_set: # Verificando se o caractere é uma vogal
        vogais_lidas.append(caractere)
    else: # Verificando se o caractere é uma CONSOANTE
        consoantes_lidas.append(caractere)

# Contando o número de consoantes
num_consoantes = len(consoantes_lidas)

# Mostrando o número de consoantes e as consoantes lidas
print("Número de consoantes lidas: ",num_consoantes)
print("Consoantes lidas:", consoantes_lidas)