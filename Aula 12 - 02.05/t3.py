nome = input("Digite seu nome: ")
numero_vezes = int(input("Digite quantas vezes deseja imprimir o nome: "))

for i in range(1, numero_vezes + 1):
  print(f"{i} - {nome}")