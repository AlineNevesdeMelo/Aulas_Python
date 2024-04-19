#Exercício 31 de estudo para P1
def calcular_e(numero_termos):

  e = 1
  fatorial = 1

  for i in range(1, numero_termos + 1):
    fatorial *= i
    e += 1 / fatorial

  return e

# Exemplo de uso
for numero_termos in (3, 4, 5):
  valor_e = calcular_e(numero_termos)
  print(f"E com {numero_termos} termos: {valor_e}")
