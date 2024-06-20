# Crie um vetor com as temperaturas máximas dos 7 dias da semana: [28.5, 30.2, 26.8, 29.3, 31.1, 27.9, 29.7].
#Peça ao usuário que índice do dia ele deseja consultar (0 a 6) e mostre a temperatura daquele dia.

# Criação do vetor com as temperaturas máximas dos 7 dias da semana
temperaturas = [28.5, 30.2, 26.8, 29.3, 31.1, 27.9, 29.7]

# Solicitação do índice do dia ao usuário
indice = int(input("Digite o índice do dia que você deseja consultar (0 a 6): "))

# Verificação se o índice está dentro do intervalo válido

if 0 <= indice <= 6:
   print(f"A temperatura máxima do dia {indice} é: {temperaturas[indice]}°C")
else:
   print("Índice inválido! Por favor, digite um número entre 0 e 6.")
